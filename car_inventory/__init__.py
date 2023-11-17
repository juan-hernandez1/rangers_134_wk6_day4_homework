from flask import Flask 
from flask_migrate import Migrate 
from flask_cors import CORS
from flask_jwt_extended import JWTManager


#internal imports 
from .blueprints.site.routes import site
from .blueprints.auth.routes import auth 
from .blueprints.api.routes import api
from config import Config 
from .models import login_manager, db
from .helpers import JSONEncoder

#instantiating our Flask app
app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)

#wrap our app in login_manager so we can use it wherever in our app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in' 
login_manager.login_message = "Your Log In Is Required!"
login_manager.login_message_category = 'warning'





app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)


#instantiating our datbase & wrapping our app
db.init_app(app)
migrate = Migrate(app, db)
app.json_encoder = JSONEncoder
cors = CORS(app)