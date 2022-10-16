#!/usr/bin/env bash
# Script that sets up the web servers for the deployment of web_static

apt-get update
apt-get install -y nginx

mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/

echo "Hello World!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu/data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.html;

    location /hbnb_static {
      alias /data/web_statuc/current;
      index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
	internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart