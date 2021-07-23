FROM python:3.8
RUN apt update && apt install -y protobuf-compiler && apt clean
ENTRYPOINT ["/bin/helloworld"]
COPY helloworld/pex_binary.pex /bin/helloworld
