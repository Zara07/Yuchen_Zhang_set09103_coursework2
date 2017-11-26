from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mail import Mail, Message
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'YourSuperSecreteKey'


@app.route('/')
def root():
  return render_template('home.html')

@app.route('/products/')
def products():
  return render_template('products.html')

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 534
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'zzzara07@gmail.com'
app.config['MAIL_PASSWORD'] = 'zmly1996'

mail = Mail(app)

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
         flash('Please fill in all fields and check them')
         return redirect(url_for('contact'))
        else:
            msg = Message("Message from your visitor" + form.name.data,
                          sender='zzzara07@gmail.com',
                          recipients=['yourRecieve@mail.com', 'someOther@mail.com'])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
        return "Successfully  sent message!"
    
    return render_template('contact.html', form=form)

@app.route('/signup/')
def signup():
       
  return render_template('signup.html')


@app.route('/login/',methods=["GET","POST"])
def login():
    error=None
    if request.method == "POST":
        attempted_emailaddress = request.form['emailaddress']
        attempted_password = request.form['password']
      
        if attempted_emailaddress == "111@111" and attempted_password == "password":
            return redirect(url_for('root'))
        else:
            error = "Invalid credentials. Try Again."
         
    return render_template('login.html',error=error)


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
