#!/usr/bin/env bash
# This script sets up the web server for deployment of the web_static files.
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

if [ -L /data/web_static/current ]
then
    rm /data/web_static/current
fi

ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/

if grep -q hbnb_static /etc/nginx/sites-available/default
then
    echo ""
else
    sed -i '/:80 default_server/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

service nginx restart
