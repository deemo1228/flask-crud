# 導入相對應的套件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import config



db = SQLAlchemy()
# db.init_app(app)
# migrate = Migrate(app, db)
# seeder = FlaskSeeder()
# seeder.init_app(app, db)






def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.debug = config[config_name].DEBUG  # debug mode
    db.init_app(app)

    # from app.views import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')
    from app.views.frontend import frontend as frontend_blueprint
    app.register_blueprint(frontend_blueprint)

    return app