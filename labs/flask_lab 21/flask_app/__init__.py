import flask



def create_app():
    '''
    Function: create_app
    Summary: Создание flask приложения
    '''

    app = flask.Flask(__name__,
                      instance_relative_config=True,
                      template_folder="templates",
                      static_folder="static")

    # загружаем настройки
    app.config.from_pyfile('config.py', silent=False)
    app.config['SECRET_KEY'] = 'liza_liza'
    # Главная страница сайта
    @app.route('/')

    @app.route('/Home_Page')
    def index_page():

        return flask.render_template('index.html')

    # CV страница сайта

    @app.route('/CV')
    def about():
        return flask.render_template('about.html')

    @app.route('/CV/<mode>')
    def set_background(mode):
        flask.session['mode'] = mode
        return flask.redirect(flask.url_for('about'))

    # Background (первая звездочка)

    @app.route('/Background')
    def bg():
        return flask.render_template('bg.html')



    #Вращающийся кубик
    @app.route('/Cube')
    def cube():
        return flask.render_template('Cube.html')



    return app
