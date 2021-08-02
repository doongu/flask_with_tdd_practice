# application/create.py
# create.py 서버 객체를 생성하는 py파일

from flask import Flask

def create_app(mode='dev'): # 개발 모드인걸 단순히 명시 해놓은듯.
    app = Flask(__name__)
    if mode == 'dev':
        app.config['DEBUG'] = True # 디버그 모드를 활성화/비활성화 함  # 참고, https://flask-docs-kr.readthedocs.io/ko/latest/config.html
        # 이런식으로도 되고 한번에 여러개를 하려면
        # app.config.update( DEBUG = True, SECRET_KEY = '...' )
    return app # Flask 객체를 return