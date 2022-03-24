FROM ubuntu:18.04

RUN apt-get update && apt-get install -y cmake build-essential python3 python3-pip

COPY ./ /src
WORKDIR /src

RUN  cmake /src  && cmake --build .

RUN useradd -ms /bin/bash techproguser
USER techproguser

RUN pip3 install flask

ENTRYPOINT [ "python3",  "app.py", "--host", "0.0.0.0", "--port", "5000" ]

