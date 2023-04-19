Example helloworld flask app hosted in heroku that serves up static content as well as an api

### Structure of code:

| Foler | Description |
| :--------- | :------------- |
| ./backend | holds all the backend APIs
| ./backend/app.py | creates the app, defines the APIs
| ./backend/appfactory.py | set the static folder when creating the flask app
| ./frontend | holds the front-end code
| ./frontend/build |  the result of a build goes into here
| ./frontend/build/static | 
| ./frontend/build/static/index.html | sample static content
| ./Procfile | first cd to backend, then starts gunicorn
| ./requirements.txt | needs to be in root folder


## Commands to deploy to heroku:

``` shell
$ heroku login
$ heroku buildpacks:set heroku/python
$ heroku create
$ git push heroku main
```

## Tests after deploying

this URL:

>    https://mysterious-sea-45373.herokuapp.com/index.html

will render the frontend/build/static/index.html file, returning

**hello world**

this URL:

>    https://mysterious-sea-45373.herokuapp.com/api/data

will render the route "/api/data" defined in backend/app.py, returning 

*{ "url": "/api/data", "content": "here is some data"}*
