from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return render_template('success',name = user)
   else:
      user = request.args.get('nm')
      return render_template ('success',name = user)

if __name__ == '__main__':
   app.run(debug = True)