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
      email=request.form.get("email")
      tel=request.form.get("tel")
      gender=request.form.get("gender")
      text=request.form.get("text1")
      country=request.form.get("country")
      photo=request.files.get("photo")
      if not fname:
       error_message = "First name is required :)"
       return render_template('form.html',error_message=error_message,fname=fname,lname=lname,gender=gender,email=email,tel=tel,text=text,country=country)
      
      if not lname:
       error_message = "Last name is required :)"
       return render_template('form.html',error_message=error_message,fname=fname,lname=lname,gender=gender,email=email,tel=tel,text=text,country=country)
      
      if not email:
       error_message = "Email is required :)"
       return render_template('form.html',error_message=error_message,fname=fname,lname=lname,gender=gender,email=email,tel=tel,text=text,country=country)
      
      if not gender:
       error_message = "choose your gender please :)"
       return render_template('form.html',error_message=error_message,fname=fname,lname=lname,gender=gender,email=email,tel=tel,text=text,country=country)
      
      if not tel:
        error_message = "tel is required :)"
        return render_template('form.html',error_message=error_message,fname=fname,lname=lname,gender=gender,email=email,tel=tel,text=text,country=country)
      
      if not photo or photo.filename =='':
        error_message = "please uploade you photo :)"
        return render_template('form.html',error_message=error_message,fname=fname,lname=lname,gender=gender,email=email,tel=tel,text=text,country=country)

      return render_template('thankyou.html')
   else:

    return render_template("form.html")
    
if __name__=="__main__":
    app.run(debug=True)
