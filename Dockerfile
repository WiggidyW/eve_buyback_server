FROM python:3.10-bullseye
ARG ITEM_CONFIGURATOR_TC_SERVICE_URL
ARG ITEM_CONFIGURATOR_REFRESH_TOKEN
ENV ITEM_CONFIGURATOR_TC_SERVICE_URL=$ITEM_CONFIGURATOR_TC_SERVICE_URL
ENV ITEM_CONFIGURATOR_REFRESH_TOKEN=$ITEM_CONFIGURATOR_REFRESH_TOKEN
COPY ./datagen_py /datagen_py
WORKDIR /datagen_py
RUN pip install -r requirements.txt
RUN python /datagen_py/main.py

FROM rust:1.69-bullseye
COPY ./server_rs /server_rs
COPY --from=0 /datagen_py/out/static_map.rs /server_rs/src/
WORKDIR /server_rs
RUN apt-get update && apt-get install -y protobuf-compiler
RUN cargo build --release
RUN mv /server_rs/target/release/eve_buyback_server /root/service

FROM frolvlad/alpine-glibc:alpine-3.17
COPY --from=1 /root/service service
COPY ./db.sqlite db.sqlite
RUN apk add openssl1.1-compat
RUN chmod +x service
ENV BUYBACK_TS_SERVICE_ADDRESS='0.0.0.0:8080'
CMD ["./service"]
