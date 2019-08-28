FROM	ubuntu

RUN	cd /tmp \
&&	apt-get update \
&&	apt-get install -y wget python3\
&&	wget https://raw.githubusercontent.com/erpangilinan/file-rename/master/file_rename.py \
&&	chmod +x file_rename.py \
&&	cp -r * /usr/local/bin \
&&	cd / \
&&	apt autoremove -y wget \
&&	rm -rf /tmp/* \
&&	rm -rf /var/lib/apt/list/*

LABEL	tool=filerename version=0.0.3

WORKDIR /data