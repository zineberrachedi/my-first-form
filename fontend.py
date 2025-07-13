from flask import Flask , render_template, request
app=Flask(__name__)



@app.route('/',methods=['GET'])
def home():
  return render_template('form.html')

@app.route('/Thnks',methods=['GET', 'POST'])
def thank_you():
   
   if request.method == 'POST':
      fname=request.form.get("Fname")
      lname=request.form.get("Lname")
      if fname=="":
       error_message = "First name is required :)"
       return render_template('form.html',error_message=error_message)
      
      if lname=="":
       error_message = "Last name is required :)"
       return render_template('form.html',error_message=error_message)

      return render_template('thankyou.html')
   else:

    return render_template("form.html")
    
if __name__=="__main__":
    app.run(debug=True)
