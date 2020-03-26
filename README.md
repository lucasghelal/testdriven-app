# Microservices with Docker, Flash & React

[![Build Status](https://travis-ci.org/LucasHelal/testdriven-app.svg?branch=master)](https://travis-ci.org/LucasHelal/testdriven-app)

## Configuration

Install:
- [Docker-Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker without sudo](https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-18-04-pt)
- [Anaconda/Conda](https://docs.anaconda.com/anaconda/install/)

1. Create a virtual env 
```
conda create -n testdrivenapp python
```

2. Install requirements.txt
```
pip install -r services/users/requirements.txt
```

3. Docker (Mac)
```
$ brew install docker docker-machine docker-compose
```

* If you are using ZSH
- Add docker and docker machine in .zshrc
```
plugins=(... docker docker-compose)
```

* VirtualBox
```
$ brew cask install virtualbox
```
- If fail to install Virtualbox
[VirtualBoxInstall](https://medium.com/@DMeechan/fixing-the-installation-failed-virtualbox-error-on-mac-high-sierra-7c421362b5b5)

* Create a new virtual machine
```
docker-machine create --driver virtualbox default
docker-machine env default
eval $(docker-machine env default)
```

* Check docker installation
```
$ docker run hello-world
$ docker-machine stop default
```


## Change Dev -> Production
```
$ eval $(docker-machine env testdriven-prod)
$ docker-compose -f docker-compose-prod.yml up -d --build

```