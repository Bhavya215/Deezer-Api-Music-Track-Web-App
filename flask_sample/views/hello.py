from flask import Blueprint, flash, render_template, request, redirect, url_for
hello = Blueprint('hello', __name__, url_prefix='/')


@hello.route('/')
def index():
    #name = request.args.get('name', 'World')
    return redirect(url_for("auth.login"))