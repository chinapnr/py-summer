from application.router import *

if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'], debug=app.config['DEBUG'])
