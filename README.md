Example helloworld flask app hosted in heroku that serves up static content and hosts an api

### Structure of code:

| Foler | Description |
| :--------- | :------------- |
| ./backend | Descriptoin |
| ./backend/app.py | creates the app, defines the APIs
| ./backend/appfactory.py | set the static folder
| ./frontend | 
| ./frontend/build |  
| ./frontend/build/static | 
| ./frontend/build/static/index.html | static content
| ./Procfile | cd to backend, then starts gunicorn
| ./requirements.txt | needs to be in root folder


## Commands to deploy to heroku:

``` shell
$ heroku login
$ heroku buildpacks:set heroku/python
$ heroku create
$ git push heroku main
```

## Tests

after deploying, this:

    https://mysterious-sea-45373.herokuapp.com/index.html

will render the frontend/build/static/index.html file, returning

**hello world**

this:

    https://mysterious-sea-45373.herokuapp.com/api/data

will render the route /api/data defined in backend/app.py, returning 

*{ "rul": "/api/data", "content": "here is some data"}*
