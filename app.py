from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import os




app = Flask(__name__)

# Set configuration BEFORE creating SQLAlchemy instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# To create SQLAlchemy instance
db = SQLAlchemy(app)

#  User model Definition
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)
   


# Create the database and tables
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirmed = request.form['confirmed']
        
        if password != confirmed:
            return "Passwords do not match!", 400
        
        exist_user = User.query.filter_by(username = username).first()

        if exist_user:
            flash("Username already exists!")
            return render_template('register.html')
        else:
         hashed_password = generate_password_hash(password)

         # Create a new user instance
         new_user = User(username = username,password =hashed_password)
         db.session.add(new_user)
         db.session.commit()
         # Redirect to home page after successful registration
         return redirect(url_for('login'))
    redirect(url_for('login'))
    return render_template('register.html')
    


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']

        user =User.query.filter_by(username=username).first()

        # Check if user exists and password is correct
        if user and check_password_hash(user.password,password):
            flash("Login successful!")
            return redirect(url_for('home'))
        else:
           flash("Invalid username or password!")
            
    return render_template('login.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=False)