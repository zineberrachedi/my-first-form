from flask import Flask , render_template, request
import sqlite3

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
  return render_template('form.html')

@app.route('/Thnks',methods=['GET', 'POST'])
def thank_you():
   
   if request.method == 'POST':
      fname=request.form.get("Fname")
      username=request.form.get("username")
      email=request.form.get("email")
      tel=request.form.get("tel")
      gender=request.form.get("gender")
      password=request.form.get("password")
      country=request.form.get("country")
      photo=request.files.get("photo")
      if not fname:
       error_message = "Name is required :)"
       return render_template('form.html',error_message=error_message,fname=fname,username=username,gender=gender,email=email,tel=tel,country=country)
      
      if not username:
       error_message = "username is required :)"
       return render_template('form.html',error_message=error_message,fname=fname,username=username,gender=gender,email=email,tel=tel,country=country)
      
      if not email:
       error_message = "Email is required :)"
       return render_template('form.html',error_message=error_message,fname=fname,username=username,gender=gender,email=email,tel=tel,country=country)
      
      if not gender:
       error_message = "choose your gender please :)"
       return render_template('form.html',error_message=error_message,fname=fname,username=username,gender=gender,email=email,tel=tel,country=country)
      
      if not password:
        error_message = "password is required :)"
        return render_template('form.html',error_message=error_message,fname=fname,username=username,gender=gender,email=email,tel=tel,country=country)

      
        # حفظ الصورة
      pfpname = "deff.png"
      if photo and photo.filename:
            pfpname = photo.filename
            photo.save(f"static/uploads/{pfpname}")

        # حفظ البيانات في قاعدة البيانات
      try:
            con = sqlite3.connect("myDataBase.db")
            cursor = con.cursor()
            cursor.execute('''
                INSERT INTO USERS (name, username, email, password, gender, tel, country, photo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (fname, username, email, password, gender, tel, country, pfpname))
            con.commit()
            message ="success"
      except Exception as e:
            con.rollback()
            message ="an error has accoured in the database"
            return render_template('form.html', message=message, fname=fname, username=username, gender=gender, email=email, tel=tel, country=country)
      finally:
            con.close()

      return render_template('thankyou.html',message=message)

   else:

    return render_template("form.html")
    
if __name__=="__main__":
    app.run(debug=True)

