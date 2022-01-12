from flask import Flask, render_template,request
app=Flask(__name__)

print(app)

#@app.route('/')
#def index():
    #url= url("https://cdn.pixabay.com/photo/2016/12/19/18/21/snowflake-1918794_960_720.jpg");
#   name='MUMCZZ19QCY'
 # return render_template('index.html', vid=name)

#@app.errorhandler(404)
#    return( render_template('404.html'), 404)

if __name__=='__main__':
    app.run(debug=True)
