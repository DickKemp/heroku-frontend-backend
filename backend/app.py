from appfactory import create_app

app = create_app()

@app.route('/api')
def home():
    return '{ "url": "/api" }'

@app.route('/api/data')
def data():
    return '{ "rul": "/api/data", "content": "here is some data"}'


