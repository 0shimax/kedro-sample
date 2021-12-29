#!/bin/bash
set -e

SYS_LONG_BIT=$(getconf LONG_BIT)

PACKAGE_LIST="libre2-dev \
    autotools-dev \
	automake \
    make \
    gcc \
    g++ \
	build-essential \
	git apt-transport-https apt-utils \
	ca-certificates \
	pkg-config \
	wget \
	zlib1g \
	zlib1g-dev \
	libssl-dev \
	curl libcurl4-openssl-dev \
	autoconf \
	sudo \
	gfortran \
	python3-dev \
	language-pack-en \
	liblttng-ust0 \
	libcurl4 \
	libssl1.1 \
	libkrb5-3 \
	libicu66 \
	libtinfo-dev \
	libtool \
	openssh-server \
	aria2 \
	bzip2 \
	unzip \
	zip \
	rsync libunwind8 libpng-dev libexpat1-dev \
	python3-setuptools python3-numpy python3-wheel python python3-pip python3-pytest \
	openjdk-11-jdk \
	graphviz"

apt-get update && apt-get install -y --no-install-recommends $PACKAGE_LIST  # libre2-dev wget aria2 make gcc g++ libssl-dev zlib1g-dev python3-dev python3-pip
rm -rf /var/lib/apt/lists/*

if [ $SYS_LONG_BIT = "64" ]; then
  echo "Installing Go"
  mkdir -p /tmp/go
#   cd /tmp/go
#   wget https://dl.google.com/go/go1.12.6.linux-amd64.tar.gz
#   tar -C /usr/local -vzxf /tmp/go/go1.12.6.linux-amd64.tar.gz

#   echo "Installing CMAKE"
#   aria2c https://github.com/Kitware/CMake/releases/download/v3.18.1/cmake-3.18.1-Linux-x86_64.tar.gz
#   tar -zxf cmake-3.18.1-Linux-x86_64.tar.gz --strip=1 -C /usr
  cd /tmp/go
  wget https://dl.google.com/go/go1.17.5.linux-amd64.tar.gz
  tar -C /usr/local -vzxf /tmp/go/go1.17.5.linux-amd64.tar.gz

  echo "Installing CMAKE"
  aria2c https://github.com/Kitware/CMake/releases/download/v3.22.1/cmake-3.22.1-Linux-x86_64.tar.gz
  tar -zxf cmake-3.22.1-linux-x86_64.tar.gz --strip=1 -C /usr

  echo "Installing onnxruntime"
  aria2c https://github.com/microsoft/onnxruntime/releases/download/v1.10.0/onnxruntime-linux-x64-1.10.0.tgz
  tar -zxf onnxruntime-linux-x64-1.10.0.tgz --strip=1
  cp -r include/* /usr/include 
  cp -r lib/* /usr/lib
  ldconfig /usr/lib
fi

echo "Installing googletest from source"
cd /tmp
git clone https://github.com/google/googletest.git
cd googletest
git checkout release-1.11.0
mkdir b
cd b
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_INSTALL_SYSCONFDIR=/etc -DCMAKE_POSITION_INDEPENDENT_CODE=ON
make -j$(getconf _NPROCESSORS_ONLN)
make install
cd /tmp
rm -rf /tmp/googletest


echo "Installing protobuf from source"
git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git checkout v3.16.0
mkdir b
cd b
cmake ../cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_SYSCONFDIR=/etc -DCMAKE_POSITION_INDEPENDENT_CODE=ON -Dprotobuf_BUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug
make -j$(getconf _NPROCESSORS_ONLN)
make install
cd ..
mkdir b2
cd b2
cmake ../cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_SYSCONFDIR=/etc -DCMAKE_POSITION_INDEPENDENT_CODE=ON -Dprotobuf_BUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release
make -j$(getconf _NPROCESSORS_ONLN)
make install
cd /tmp
rm -rf /tmp/protobuf

echo "Installing grpc"
git clone -b v1.41.0 https://github.com/grpc/grpc
cd grpc
git submodule update --init
mkdir -p "third_party/cares/cares/cmake/build"
pushd "third_party/cares/cares/cmake/build"
cmake -DCMAKE_BUILD_TYPE=Release ../..
make -j$(getconf _NPROCESSORS_ONLN) install
popd
mkdir -p cmake/build
cd cmake/build
cmake ../.. -DCMAKE_BUILD_TYPE=Release -DgRPC_CARES_PROVIDER=package    \
           -DgRPC_PROTOBUF_PROVIDER=package \
           -DgRPC_SSL_PROVIDER=package      \
           -DgRPC_ZLIB_PROVIDER=package
make -j$(getconf _NPROCESSORS_ONLN)
make install
cd /tmp
rm -rf /tmp/grpc

python3 -m pip install grpcio==1.41.0 requests protobuf