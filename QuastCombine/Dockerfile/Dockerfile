FROM	ubuntu

RUN cd /tmp \
&&	apt-get update \
&&	DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends wget python3 python3-matplotlib python3-tk \
&&	wget --no-check-certificate https://raw.githubusercontent.com/erpangilinan/Akda/master/QuastCombine/QuastCombine.py \
&&	chmod +x QuastCombine.py \
&&	cp -r * /usr/local/bin \
&&	cd / \
&&	apt autoremove -y wget \
&&	rm -rf /tmp/* \
&&	rm -rf /var/lib/apt/list/*

LABEL	tool=quast_combine version=1.0.0

WORKDIR /data