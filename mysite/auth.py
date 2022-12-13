from flask import Flask, request, render_template,redirect,url_for,flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_usuario():
    return render_template('login.html')

@auth.route('/login', methods = ['POST'])
def login():
    try:
        if request.method == 'POST':
                usuario = request.form['usuario']
                senha = request.form['password']
                remember = True if request.form['remember'] else False
                acesso = login.query.filter_by(usuario=usuario,senha=sqlalchemy.func.md5(senha)).first()
                if not acesso:
                    flash('SENHA OU USUÁRIO INCORRETO')
                    return redirect(url_for('auth.login'))

                login_user(acesso, remember=remember)
                return redirect(url_for('main.principal'))

        return redirect(url_for('login_usuario'))
    except:
        return render_template('login.html', mensagem='FALHA DE CONEXÃO')

