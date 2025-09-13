from flask import Flask, render_template, request, redirect, url_for, flash, session
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

# User model Definition
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
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
        username = request.form.get('username')
        password = request.form.get('password')
        confirmed = request.form.get('confirmed')
        
        # Check if all fields are provided
        if not username or not password or not confirmed:
            flash("All fields are required!")
            return render_template('register.html')
        
        # Check if passwords match
        if password != confirmed:
            flash("Passwords do not match!")
            return render_template('register.html')
        
        # Check if username already exists
        exist_user = User.query.filter_by(username=username).first()
        
        if exist_user:
            flash("Username already exists!")
            return render_template('register.html')
        else:
            # Create new user
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password)
            
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("Registration successful! Please login.")
                return redirect(url_for('login'))
            except Exception as e:
                db.session.rollback()
                flash("Registration failed. Please try again.")
                return render_template('register.html')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if fields are provided
        if not username or not password:
            flash("Username and password are required!")
            return render_template('login.html')
        
        # Find user
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            # Set session
            session['username'] = username
            flash("Login successful!")
            return redirect(url_for('dashboard'))  # Redirect to dashboard instead of home
        else:
            flash("Invalid username or password!")
            return render_template('login.html')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'username' not in session:
        flash("Please login to access the dashboard.")
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()  # Clear the session
    flash("You have been logged out successfully.")
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=True)  # Set debug=True for development