from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config.from_envvar('APP_SETTINGS')


@app.route('/')
def index():
    return render_template('index.html', fb_app_id=app.config['FB_APP_ID'])


if __name__ == '__main__':
    app.run('0.0.0.0')
