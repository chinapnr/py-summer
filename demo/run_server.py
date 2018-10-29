from py_summer import app

if __name__ == '__main__':
    print('Summer server started on port %s.' % app.config['IP_PORT'])
    app.run(host=app.config['IP'], port=app.config['PORT'])

