#!/bin/bash
# running on ubuntu 18.04.6 VM
# put this in ~/install.sh and run with "cd; sh install.sh" and provide password when prompted

# versions from video tutorial
SILK_VER=3.12.0
YAF_VER=2.8.4
LIBFXBUF_VER=1.7.1

# download in ~ dir
wget http://tools.netsa.cert.org/releases/silk-${SILK_VER}.tar.gz
wget http://tools.netsa.cert.org/releases/yaf-${YAF_VER}.tar.gz
wget http://tools.netsa.cert.org/releases/libfixbuf-${LIBFXBUF_VER}.tar.gz
tar -zxvf silk-${SILK_VER}.tar.gz
tar -zxvf yaf-${YAF_VER}.tar.gz
tar -zxvf libfixbuf-${LIBFXBUF_VER}.tar.gz

# get all dependencies from video tutorial plus website
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y build-essential libglib2.0-dev libpcap-dev python-dev liblzo2-dev zlib1g-dev libgnutls28-dev python3.8-dev

sudo apt-get install -y net-tools openssh-server traceroute

# install fixbuf
cd ~/libfixbuf-${LIBFXBUF_VER}
./configure && make && sudo make install

# install yaf
cd ~/yaf-${YAF_VER}
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
./configure --applabel && make && sudo make install

sudo cp etc/init.d/yaf /etc/init.d/yaf
sudo chmod a+x /etc/init.d/yaf

sudo mkdir /data

# install silk tools
cd ~/silk-${SILK_VER}
./configure --with-libfixbuf=/usr/local/lib/pkgconfig/ --enable-ipv6 --with-python && make && sudo make install

cat <<EOF >>silk.conf
/usr/local/lib
/usr/local/lib/silk
EOF

sudo mv silk.conf /etc/ld.so.conf.d

sudo ldconfig

sudo cp site/twoway/silk.conf /data

# this didn't work with the latest package of silk tools but works on older versions
sudo cp /usr/local/share/silk/etc/init.d/rwflowpack /etc/init.d


# modify /data/sensors.conf with:


# probe S0 ipfix
# listen-on-port 18001
# protocol tcp
# listen-as-host 127.0.0.1
# end probe

# group my-network
# ipblocks 192.168.1.0/24 #local subnet
# end group

# sensor S0
# ipfix-probes S0
# internal-ipblocks @my-network
# external-ipblocks remainder
# end sensor


# modify /usr/local/etc/rwflowpack.conf with:


# ENABLED=1
# statedirectory=/data
# SENSOR_CONFIG=/data/sensors.conf
# LOG_TYPE=legacy
# LOG_DIR=/var/log


# modify /usr/local/etc/yaf.conf (default file comes from yaf unzipped/etc/yaf.conf.in) with:


# ENABLED=1
# YAF_CAP_IF=ens2 # Ensure this is correct for your machine
# YAF_IPFIX_PORT=18001 # Must match value in sensors.conf
# YAF_EXTRAFLAGS="--silk"


# modify /etc/init.d/rwflowpack


# DEFAULT_SCRIPT_CONFIG_LOCATION=/data/


# then trying to bring things up
sudo systemctl daemon-reload
sudo /etc/init.d/yaf start
sudo /etc/init.d/rwflowpack start

sudo ufw allow 18001/tcp

# check yaf log which should be running
# watch -n 1 tail /var/log/yaf.log

# or try to run yaf from cli
# sudo yaf --in=ens2 --out=127.0.0.1 --live=pcap --ipfix-port=18001 --silk