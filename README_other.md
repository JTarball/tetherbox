[![Circle CI](https://circleci.com/gh/JTarball/docker-django-polymer-starter-kit.svg?style=svg)](https://circleci.com/gh/JTarball/docker-django-polymer-starter-kit)


<a href="http://www.djangoproject.com/" ><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." style="float: right;" /></a>

<img src="https://www.polymer-project.org/images/logos/lockup.svg" />


#### Current Integrated Version/s 

-	[`v1.2.6`, `generator-polymer`](https://github.com/yeoman/generator-polymer.git)
-	[`1.8.6`, `Django`](https://www.djangoproject.com/download/)

## Django Polymer start project using Docker
## Intro
This is a quick fire starter kit for getting a Docker Web project up and running. Django web framework is used for the backend essentially making it a  REST API. Google Polymer is used for the frontend.

This project integrates **generator-polymer** project with a dockerized django app.

## Cheatsheet



### Rebuild and Upload base image 


### Useful Commands
`docker login`
  - you will need to login into docker hub (set up an account if you dont have one)
`docker build -t "<IMAGE>" .`
  - this will build the Dockerfile in the current directory and tag it with "jtarball/docker-base:latest"
`docker push "<IMAGE>"`
  - push to docker hub
`docker-compose up`
 - this command will create and start containers
`docker rm $(docker ps -a -q); docker rmi $(docker images -q);`
 - kill and remove all docker images and containers
`docker rmi $(docker images -q --filter "dangling=true")`
 - Clean up un-tagged docker images
`docker stop $(docker ps -a -q)`
 - Stop all docker processes


### Developer Notes
#### React Notes
- uses virtual "fake" dom for diff -> updates


`render: function()` - a representation of your view

#### Flux Notes


#### How to update base docker image 'docker-base'
From `docker` directory run:
```
git submodule update --remote --merge 
```

### Considerations / Future
In the future I might consider incorporating ideas from the following projects:

* https://github.com/imkevinxu/django-kevin
* https://github.com/luzfcb/cookiecutter-django-oauth
* https://github.com/pydanny/cookiecutter-django

*e.g. caching, sendGrid email support, heroku, better management*
