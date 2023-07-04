#!/usr/bin/env python3
from pathlib import Path
import pb.item_configurator_pb2_grpc as pb_client
import pb.item_configurator_pb2 as pb_proto
import grpc
import tempfile
from datetime import datetime
import argparse
import shutil
import json
import os

# OUT_PATH = Path(os.environ['BUYBACK_SERVER_OUT_PATH'])
# GIT_URL = os.environ['BUYBACK_SERVER_GIT']
OUT_PATH = Path('out')
DEBUG_OUT_PATH = Path('../server_rs/src')
ITEMCFG_TOKEN = os.environ['ITEM_CONFIGURATOR_REFRESH_TOKEN']
ITEMCFG_CLIENT = pb_client.ItemConfiguratorStub(
    grpc.insecure_channel(
        os.environ['ITEM_CONFIGURATOR_TC_SERVICE_URL']
    )
)

STATIC_MARKETS = {
    1030049082711: '1DQ1-A',
    60003760: 'Jita',
}
MARKET_KEYS = {
    '1dq1-a': 1030049082711,
    '1dq1a': 1030049082711,
    '1dq1': 1030049082711,
    '1dq': 1030049082711,
    'jita': 60003760,
}

def write_markets(f, markets):
    for k, v in markets.items():
        f.write(f'    {k}: "{v}",\n')

def parse_float(v) -> 'int | None':
    if v is None:
        return None
    elif isinstance(v, int):
        if v == 0 or v == 1:
            return v
    elif isinstance(v, float):
        if v >= 0.0 and v <= 1.0:
            return round(v * 100.0)
    raise ValueError()

def parse_efficiency(efficiency) -> 'int | None':
    try:
        return parse_float(efficiency)
    except ValueError:
        raise ValueError(f'Invalid efficiency: {efficiency}')

def parse_modifier(modifier) -> 'int | None':
    try:
        return parse_float(modifier)
    except ValueError:
        raise ValueError(f'Invalid mod: {modifier}')

def parse_order_target(order_target) -> 'int | None':
    if order_target is None:
        return None
    elif isinstance(order_target, str):
        order_target = order_target.lower()
        if order_target == 'buy' or order_target == 'maxbuy':
            return 2
        elif order_target == 'sell' or order_target == 'minsell':
            return 1
    raise ValueError(f'Invalid kind: {order_target}')

def parse_location(location) -> 'int | None':
    if location is None:
        return None
    elif isinstance(location, str):
        location = location.lower()
        if MARKET_KEYS.get(location) is not None:
            return MARKET_KEYS.get(location)
    elif isinstance(location, int):
        if location in STATIC_MARKETS:
            return location
    raise ValueError(f'Invalid market: {location}')

def parse_json(jsonStr) -> 'list[int]':
    jsonObj = {k.lower(): v for k, v in json.loads(jsonStr).items()}

    try:
        efficiency = parse_float(jsonObj.get('efficiency'))
        order_target = parse_order_target(jsonObj.get('kind'))
        modifier = parse_modifier(jsonObj.get('mod'))
        location = parse_location(jsonObj.get('location'))
    except ValueError as e:
        raise ValueError(f'{jsonStr}: {e}')
    
    row = [0, 0, 0, 0]

    if efficiency is not None:
        row[0] = efficiency

    if order_target is not None:
        if modifier is None or location is None:
            raise ValueError(f'Invalid json: {jsonObj} - has kind but missing mod or location')
        row[1] = order_target

    if modifier is not None:
        if order_target is None or location is None:
            raise ValueError(f'Invalid json: {jsonObj} - has mod but missing kind or location')
        row[2] = modifier

    if location is not None:
        if order_target is None or modifier is None:
            raise ValueError(f'Invalid json: {jsonObj} - has location but missing kind or mod')
        row[3] = location

    return row

def write_regions(f, itemcfg_client, refresh_token):
    regions: 'dict[str, list[tuple[int, list[int]]]]' = {}

    rep = itemcfg_client.List(pb_proto.ListReq(
        include_configured=pb_proto.Query.TRUE,
        include_enabled=pb_proto.Query.TRUE,
        refresh_token=refresh_token,
        include_market_group=False,
        include_category=False,
        include_group=False,
        include_name=False,
        include_json=True,
        name='buyback',
        language='',
    ))

    jsonRows = [parse_json(jsonStr) for jsonStr in rep.json]

    for item in rep.items:
        for region, idx in item.json_idx.items():
            regions.setdefault(region, []).append((item.type_id, jsonRows[idx]))

    for region, items in regions.items():
        f.write(f'    "{region}" => phf::phf_map! {{\n')
        for (type_id, jsonRow) in items:
            f.write(f'        "{type_id}" => ({jsonRow[0]}, {jsonRow[1]}, {jsonRow[2]}, {jsonRow[3]}),\n')
        f.write('    },\n')

def main(debug=False):
    tempDir = tempfile.mkdtemp()
    tempDirPath = Path(tempDir)
    if debug:
        os.makedirs('debug_out', exist_ok=True)
        parentDir = Path('debug_out')
    else:
        parentDir = tempDirPath

    ver = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create the file
    with open(parentDir / 'static_map.rs', 'w') as f:
        f.write(f'pub const PRICE_VERSION: &str = "{ver}";\n')
        f.write('\n')
        f.write('pub static MARKET_MAP: phf::Map<u64, &str> = phf::phf_map! {\n')
        write_markets(f, STATIC_MARKETS)
        f.write('};\n')
        f.write('\n')
        f.write('pub static REGION_MAP: phf::Map<&str, phf::Map<u32, (u8, u8, u8, u64)>> = phf::phf_map! {\n')
        write_regions(f, ITEMCFG_CLIENT, ITEMCFG_TOKEN)
        f.write('};\n')
    
    # Just copy it if debug, leaving the file in place
    if debug:
        shutil.copy(
            parentDir / 'static_map.rs',
            DEBUG_OUT_PATH / 'static_map.rs',
        )
    # Move it otherwise
    else:
        shutil.move(
            parentDir / 'static_map.rs',
            OUT_PATH / 'static_map.rs',
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--debug',
        help='Save output to debug_out',
        action='store_true',
        dest='debug',
        default=False,
    )
    args = parser.parse_args()
    try:
        debug = args.debug
    except AttributeError:
        debug = False
    main(debug=debug)
