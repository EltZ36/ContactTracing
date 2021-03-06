#this file is usually called run.py
from project import app

'''
If you are running this on repl.it, comment out views.py and uncomment the lines below

from flask import Flask, render_template

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/question')
def questions():
    return render_template('question.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
'''
app.run(
  host='0.0.0.0', 
  port=5000,
  debug=True
)
