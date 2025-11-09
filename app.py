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
    name = db.Column(db.String(50), nullable=True)

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
        name = request.form.get('name')
        
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
            new_user = User(username=username, password=hashed_password, name=name)
            
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
            session['user_id'] = user.id
            session['username'] = username
            flash("Login successful!")
            return redirect(url_for('dashboard'))
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

@app.route('/profile')
def profile():
    # Check if user is logged in
    if 'user_id' not in session:
        flash("Please login to access your profile.")
        return redirect(url_for('login'))
    
    # Get current user
    user = User.query.get(session['user_id'])
    if not user:
        flash("User not found.")
        return redirect(url_for('login'))
    
    return render_template('profile.html', user=user)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    # Check if user is logged in
    if 'user_id' not in session:
        flash("Please login to edit your profile.")
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user:
        flash("User not found.")
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_username = request.form.get('username')
        
        # Validate inputs
        if not new_name or not new_username:
            flash("Name and username cannot be empty!")
            return redirect(url_for('profile'))
        
        # Check if new username is already taken by another user
        if new_username != user.username:
            existing_user = User.query.filter_by(username=new_username).first()
            if existing_user:
                flash("Username already taken by another user!")
                return redirect(url_for('profile'))
        
        # Update user information
        user.name = new_name
        user.username = new_username
        
        try:
            db.session.commit()
            session['username'] = new_username  # Update session
            flash("Profile updated successfully!")
            return redirect(url_for('profile'))
        except Exception as e:
            db.session.rollback()
            flash("Failed to update profile. Please try again.")
            return redirect(url_for('profile'))
    
    return redirect(url_for('profile'))

@app.route('/delete_account', methods=['POST'])
def delete_account():
    # Check if user is logged in
    if 'user_id' not in session:
        flash("Please login first.")
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user:
        flash("User not found.")
        return redirect(url_for('login'))
    
    try:
        db.session.delete(user)
        db.session.commit()
        session.clear()
        flash("Your account has been deleted successfully.")
        return redirect(url_for('home'))
    except Exception as e:
        db.session.rollback()
        flash("Failed to delete account. Please try again.")
        return redirect(url_for('profile'))

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out successfully.")
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=True)