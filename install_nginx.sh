#!/bin/bash
setcolor_failure="echo -en \\033[91m"
setcolor_success="echo -ne \\033[32m"
setcolor_normal="echo -e \\033[0m"

if [ $UID -ne 0 ];then
    $setcolor_failure
    echo -n "请以管理员身份运行该脚本"
    $setcolor_normal
    exit
fi

if rpm --quiet -q wget ; then
    wget -c http://nginx.org/download/nginx-1.14.0.tar.gz
else
    $setcolor_failure
    echo -n "找不到wget，请安装该软件。"
    $setcolor_normal
    exit
fi

if ！id nginx &> /dev/null; then
    adduser -s /sbin/nologin nginx
fi

if [ ! -f nginx-1.14.0.tar.gz ];then
    $setcolor_failure
    echo -n "未找到nginx源码包，请先正确下载该软件。"
    $setcolor_normal
    exit
else
    yum -y install gcc pcre-devel zlib-devel openssl-devel
    clear
    $setcolor_success
    echo -n "接下来，需要花几分钟时间编译源码安装nginx..."
    $setcolor_normal
    sleep 6
    tar -xf nginx-1.14.0.tar.gz
    cd nginx-1.14.0/
    ./configure \
    --user=nginx --group=nginx --prefix=/opt/nginx/ --with-stream \
    --with-http_ssl_module --with-http_stub_status_module \
    --without-http_autoindex_module --without-http_ssi_module 
    make && make install
fi

if [ -x /opt/nginx/sbin/nginx ]; then
    clear
    $setcolor_success
    echo -n "一键部署nginx已经完成"
    $setcolor_normal
fi

