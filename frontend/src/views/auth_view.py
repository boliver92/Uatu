from src import app, db
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import  check_password_hash, generate_password_hash


@app.route('/user')
def user_endpoint():
    return 'User endpoint!'

@app.route('/user/db')
def db_endpoint():
    return db.test_func()
