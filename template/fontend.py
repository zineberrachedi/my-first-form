from flask import Flask , render_template, request
app=Flask(__name__)
@app.route('/Thnks')
def index():
   return render_template('thankyou.html')
if __name__=="__main__":
    app.run(debug=True)
