# coding: utf-8
"""Web application for recording dormice monitoring data
"""

from flask import (Flask, request, redirect, url_for, send_from_directory,
                   flash, render_template)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    """
    Access the test table on postgres and return
    """
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
