"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template


@bp.route("/dashboard") # cria uma rota para navegador http://127.0.0.1:5000/dashboard
def dashboard(): # função que gerencia rota deve ser única
    """ Painel de vendas"""
    # remova o login

    import locale
    # Define para o padrão brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    vendas: list = [
        {"mes":"Janeiro", "total":139519.19 },
        {"mes":"Fevereiro", "total":131514.99 },
        {"mes":"Março", "total":128519.31 },
        {"mes":"Abril", "total":139191.95 },
        {"mes":"Maio", "total":141611.19 },
        {"mes":"Junho", "total":142591.19 },
        {"mes":"Julho", "total":152112.19 },
        {"mes":"Agosto", "total":123451.89 },
        {"mes":"Setembro", "total":161123.29 },
        {"mes":"Outubro", "total":162349.16 },
        {"mes":"Novembro", "total":171789.90 },
        {"mes":"Dezembro", "total":169844.17 },
    ] # fim lista vendas
    
    return render_template("dashboard/index.html", vendas=vendas, locale=locale) # Renderiza um template
    
