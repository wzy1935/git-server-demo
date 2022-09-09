from flask import Flask, send_file, request
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
app.config['SECRET_KEY'] = 'example key'
auth = HTTPBasicAuth()


@auth.get_password
def password(username):  # user: user1  password: 123456
    return '123456' if username == 'user1' else None


@app.route("/<path:file_path>")
@auth.login_required
def file_hosting(file_path):
    file_path = file_path.replace('.git', '/.git', 1)
    return send_file(f'repos/{file_path}')


app.run(port=8080)