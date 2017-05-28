### Connect to the VM using SSH

### Switch to root

`sudo -s`

### Remove previous Docker installations

`sudo apt-get remove docker docker-engine`

### Install Docker

```
sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
software-properties-common
```

`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

```
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"
```

`sudo apt-get update`

`sudo apt-get install docker-ce`

### Install Docker-Compose

```curl -L https://github.com/docker/compose/releases/download/1.13.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose```

`sudo chmod +x /usr/local/bin/docker-compose`

### Clone App

`cd`

`git clone https://github.com/Radu-Raicea/docker-nginx-flask-postgres.git`

### Build App

`cd docker-nginx-flask-postgres`

`docker-compose up`

#### If you screw up and want to uninstall docker, docker-compose, all containers, images, etc.

`sudo apt-get purge docker-ce`

`sudo rm -rf /var/lib/docker`

`sudo rm /usr/local/bin/docker-compose`
