**Flask Authentication App**

A secure and user-friendly web application built with Flask that provides user registration, login, and authentication functionality. 
This app features a modern, responsive design and implements secure password hashing for user data protection.

🌟**Features**

**Secure User Registration**: Create new accounts with password confirmation

**User Authentication**: Login with username and password

**Password Security**: Passwords are hashed using Werkzeug's security functions

**Flash Messages**: User-friendly feedback for login/registration attempts

**Responsive Design**: Modern UI with custom CSS styling

**SQLite Database**: Lightweight database for user data storage

**Form Validation**: Client-side and server-side validation

🚀**Live Demo**

 https://registeration-and-login-auth.onrender.com
 
📋**Prerequisites**

**Before running this application, make sure you have:**

Python 3.7 or higher installed
pip package manager

🔧**Technologies Used**:

**Backend**: Flask (Python web framework).

**Database**: SQLite with SQLAlchemy ORM.

**Authentication**: Flask-Login, Werkzeug password hashing.

**Frontend**: HTML5, CSS3, JavaScript.

**Deployment**: Render (Platform-as-a-Service).

📱**Pages Overview**

**Home Page**

Welcome message and platform introduction.

Feature highlights (Secure Login, Personal Dashboard, Fast & Reliable)
Quick access buttons to Login and Register.

**Registration Page**

User registration form with username and password.

Password confirmation validation.

Password strength indicator.

Secure password hashing before database storage.

**Login Page**

User authentication form.

Flash message support for login feedback.

Redirect to home page on successful login.

🔐**Security Features**

**Password Hashing**: Uses Werkzeug's generate_password_hash() for secure password storage.

**Password Verification**: Implements check_password_hash() for login authentication.

**CSRF Protection**: Secret key configuration for form security.

**Input Validation**: Both client-side and server-side validation.

🚀**Deployment**

**This application is configured for deployment on Render**:

**1. Push to GitHub**: Ensure your code is in a GitHub repository

**2. Connect to Render**: Link your GitHub repo to Render

**3. Configure Build Settings**:

**Build Command**: pip install -r requirements.txt

**Start Command**: gunicorn app:app

**4. Deploy**: Render will automatically build and deploy your app

**👤Author :**
Andile NtshangaAW

**GitHub**: 0698113787
**Email**: vuyiswaandile176@gmail.com

**🙏Acknowledgments**

Flask documentation and community
Render platform for hosting
