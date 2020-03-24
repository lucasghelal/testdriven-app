# Workflow

## Aliases

* Add it on .bashrc ou .zshrc:

```
alias dc='docker-compose'
alias dm='docker-machine'
```

* Remove docker images:

```
$ docker rmi $(docker images -q)
```

* Acess psql on Docker:
```
$ dc exec users-db psql -U postgres

# \c users_dev
# select * from users;
```


## Deploy 

* Create EC2 Machine (São Paulo) with Docker:
```
dm create --driver amazonec2 --amazonec2-region sa-east-1 testdriven-prod
```

* Redirect client Docker to EC2:
```
$ dm env testdriven-prod
$ eval $(dm env testdriven-prod)
```
* List and remove docker machines 
```
$ dm ls
$ dm rm NamaDM
```
* Run  Container, Create DB, Add seed of datas and run tests:
```
$ dc -f docker-compose-prod.yml up -d --build

$ dc -f docker-compose-prod.yml exec users python manage.py recreate_db

$ dc -f docker-compose-prod.yml exec users python manage.py seed_db

$ dc -f docker-compose-prod.yml exec users python manage.py test
```
* See IP of EC2:

```
$ dm ip testdriven-prod
```

* Check env environment
```
$ dc -f docker-compose-prod.yml exec users env
```

* Docker to localhost
```
$ eval $(dm env -u)
```

## Tests
```
$ docker-compose exec users python manage.py test
```