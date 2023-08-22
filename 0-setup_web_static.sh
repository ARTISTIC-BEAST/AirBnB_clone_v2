#!/usr/bin/env bash
# 0. Prepare your web servers
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/shared/ 
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >/data/web_static/releases/test/index.html
ln -snf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
my_string="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"
FILE=/etc/nginx/sites-available/default
result=$(grep "$my_string" "$FILE")
if [ -z "$result" ]; then
    sed -i "48 a $my_string" "$FILE"
fi
service nginx restart
exit 0
