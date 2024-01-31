FROM quay.io/centos/centos:stream9
LABEL authors="Jose Castillo Lema <josecastillolema@gmail.com>"

RUN dnf upgrade -y \
    && dnf install -y epel-release \
    && dnf install -y --setopt=tsflags=nodocs python3-pip \
    && dnf install -y --setopt=tsflags=nodocs python3-devel \
    && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

RUN pip3 --no-cache-dir install -U pip \
    && python3 -m pip install cloudevents kubernetes flask

WORKDIR /machineset-gw

COPY ./machineset-gw/* ./

EXPOSE 8080

CMD [ "python3", "machineset-gw.py"]
