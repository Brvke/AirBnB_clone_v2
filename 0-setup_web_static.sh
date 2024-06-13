#!/usr/bin/env bash
#Bash script to setuup web servers for deployment

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Hello World!" > /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Best School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html
test -L /data/web_static/current && sudo rm /data/web_static/current

new_locatio=" \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "36i\\$new_location" /etc/nginx/sites-enabled/default
sudo service nginx restart
