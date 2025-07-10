from flask import Flask , render_template, request
app=Flask(__name__)
@app.route('/Thnks',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('thankyou.html')
    else:
        return render_template('thankyou.html')
if __name__=="__main__":
    app.run(debug=True)
