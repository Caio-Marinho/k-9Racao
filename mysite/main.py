from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

