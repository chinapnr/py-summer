from py_summer import app

if __name__ == '__main__':
    print('Summer server started on port %s.' % app.config['IP_PORT'])
    app.run(host='127.0.0.1', port=app.config['IP_PORT'])


@app.route('/hello')
def get_user():
    return 'py_summer'


if __name__ == '__main__':
    app.run('127.0.0.1')
