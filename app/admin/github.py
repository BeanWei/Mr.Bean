from flask import url_for, session, redirect, request, flash, current_app
from flask_oauthlib.client import OAuth
from app.admin import bp
import os

oauth = OAuth(current_app)

github = oauth.remote_app(
    'github',
    consumer_key = os.environ.get('Client_ID'),
    consumer_secret = os.environ.get('Client_secret'),
    request_token_params = {'scope': 'user:email'},
    base_url = 'https://api.github.com/',
    request_token_url = None,
    access_token_url = 'https://github.com/login/oauth/access_token',
    authorize_url = 'https://github.com/login/oauth/authorize'
)


@bp.route('/login')
def login():
    flash('登录成功')
    return github.authorize(callback=url_for('github.authorize', _external=True))


@bp.route('/logout')
def logout():
    session.pop('github_token', None)
    flash('已退出···')
    return redirect(url_for('main.index'))


@bp.route('/login/authorize')
def authorize():
    resp = github.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Access denied: reason=%s error=%s resp=%s' % (
            request.args['error'],
            request.args['error_description'],
            resp
        )
    session['github_token'] = (resp['access_token'], '')
    return redirect(url_for('admin.index'))


@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')