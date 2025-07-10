from flask import Flask , render_template, request
app=Flask(__name__)
@app.route('/',methods=['GET'])
def home():
  return render_template('form.html')


@app.route('/Thnks',methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        print("ok")
        return render_template('thankyou.html')
    else:
        return render_template('form.html')
if __name__=="__main__":
    app.run(debug=True)
