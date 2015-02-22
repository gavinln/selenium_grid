This VM demonstrates using docker with a ubuntu VM that supports docker and supports virtual box shared folders (vboxsf)

sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest

docker run -t -i phusion/baseimage:latest /sbin/my_init -- bash -l

cd /vagrant/fig/odbc
sudo docker build -t odbc_test .

sudo docker save -o ubuntu_docker_python.tar odbc_test

https://onedrive.live.com/download?cid=5184C6CE006B3E69&resid=5184C6CE006B3E69%21506&authkey=ANkLm7KmSwJruVA

sudo docker load -i ubuntu_docker_python.tar

To setup an nginx reverse proxy
See https://github.com/jwilder/nginx-proxy
docker run -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock jwilder/nginx-proxy

To setup Miniconda use
https://github.com/ContinuumIO/docker-images/blob/master/miniconda/Dockerfile

To create a Samba share
1. Create a directory in /srv
sudo mkdir /srv/pictures

2. Set the correct permissions
sudo chmod 777 /srv/pictures
