from flask import Flask, render_template


class Web:
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.app.add_url_rule('/',
                              'home',
                              self.home,
                              methods=['GET',
                                       'POST'
                                       ])

    def run(self):
        self.app.run(host="127.0.0.1", port=5789, debug=True)

    def home(self):
        return render_template('home.html')
