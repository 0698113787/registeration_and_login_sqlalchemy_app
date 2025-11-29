# 🔐 Flask Authentication App

A secure and user-friendly web application built with Flask that provides user registration, login, and authentication functionality. This app features a modern dark-themed responsive design and implements secure password hashing for user data protection.

## 🌟 Features

- **Secure User Registration** - Create new accounts with password confirmation and real-time strength indicator
- **User Authentication** - Login with username and password validation
- **Password Security** - Passwords are hashed using Werkzeug's security functions
- **User Profile Management** - View, edit, and manage your profile information
- **Account Deletion** - Secure account deletion with confirmation modal
- **Flash Messages** - User-friendly feedback for all actions
- **Responsive Design** - Modern dark grey UI with Font Awesome icons
- **SQLite Database** - Lightweight database for user data storage
- **Form Validation** - Client-side and server-side validation
- **Session Management** - Secure user sessions with logout functionality

## 🚀 Live Demo

**Check out the live application:** [https://registeration-and-login-auth.onrender.com](https://registeration-and-login-auth.onrender.com)

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher installed
- pip package manager
- Git (for cloning the repository)

## 🔧 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Flask** | Python web framework |
| **SQLite** | Database management |
| **SQLAlchemy** | ORM for database operations |
| **Werkzeug** | Password hashing and security |
| **HTML5/CSS3** | Frontend structure and styling |
| **JavaScript** | Client-side interactions |
| **Font Awesome** | Professional icon library |
| **Gunicorn** | WSGI HTTP Server for deployment |
| **Render** | Cloud hosting platform |

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/0698113787/flask-auth-app.git
   cd flask-auth-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   pythom -m flask run or 
   python app.py
   ```

6. **Access the app**
   
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 📁 Project Structure

```
flask-auth-app/
│
├── app.py                 # Main Flask application
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment configuration
├── README.md             # Project documentation
│
├── static/               # Static files
│   ├── home.css         # Home page styles
│   ├── login.css        # Login page styles
│   ├── register.css     # Registration page styles
│   ├── dashboard.css    # Dashboard styles
│   └── profile.css      # Profile page styles
│
├── templates/            # HTML templates
│   ├── home.html        # Landing page
│   ├── login.html       # Login form
│   ├── register.html    # Registration form
│   ├── dashboard.html   # User dashboard
│   └── profile.html     # User profile
│
└── instance/             # Instance folder (auto-generated)
    └── users.db         # SQLite database
```

## 📱 Pages Overview

### 🏠 Home Page
- Welcome message and platform introduction
- Feature highlights (Secure Login, Personal Dashboard, Fast & Reliable)
- Quick access buttons to Login and Register
- Modern dark-themed design with gradient background

### 📝 Registration Page
- User registration form with full name, username, and password
- Password confirmation validation
- Real-time password strength indicator
- Secure password hashing before database storage
- Immediate feedback with flash messages

### 🔑 Login Page
- User authentication form with username and password
- Flash message support for login feedback
- Redirect to dashboard on successful login
- Professional icon integration

### 📊 Dashboard
- Personalized welcome message
- Feature cards highlighting app capabilities
- Quick access to profile and logout
- Project information and tech stack display

### 👤 Profile Page
- View user information (name, username, ID)
- Edit profile functionality
- Account deletion option with confirmation modal
- Secure session-based access

## 🔐 Security Features

- **Password Hashing** - Uses Werkzeug's `generate_password_hash()` for secure password storage
- **Password Verification** - Implements `check_password_hash()` for login authentication
- **Session Management** - Flask sessions keep users logged in securely
- **CSRF Protection** - Secret key configuration for form security
- **Input Validation** - Both client-side and server-side validation
- **SQL Injection Protection** - SQLAlchemy ORM prevents SQL injection attacks
- **Secure Account Deletion** - Confirmation required before account removal

## 🎨 Design Features

- **Dark Grey Theme** - Professional color scheme with slate grey tones
- **Font Awesome Icons** - Modern, professional iconography throughout
- **Responsive Layout** - Works seamlessly on desktop, tablet, and mobile
- **Smooth Animations** - Hover effects and page transitions
- **Glassmorphism** - Semi-transparent backgrounds with blur effects
- **User-Friendly Interface** - Intuitive navigation and clear visual hierarchy

## 🚀 Deployment on Render

This application is configured for easy deployment on Render:

### Steps to Deploy:

1. **Prepare your repository**
   - Ensure `requirements.txt` includes all dependencies
   - Add `Procfile` with: `web: gunicorn app:app`
   - Push all changes to GitHub

2. **Create a new Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Build Settings**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3

4. **Set Environment Variables** (Optional)
   - `SECRET_KEY` - Your Flask secret key
   - `DATABASE_URL` - Database connection string (if using PostgreSQL)

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app

### Requirements for Deployment

Create a `requirements.txt` file:
```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.1
gunicorn==21.2.0
```

Create a `Procfile`:
```
web: gunicorn app:app
```

## 📝 Environment Variables

For production, set these environment variables:

```bash
SECRET_KEY=your-secret-key-here
FLASK_ENV=production
```


## 🐛 Bug Reports

If you find any bugs, please open an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)

## 📄 License

This project is licensed under the MIT License - feel free to use it for your own projects!

## 👤 Author

**Andile Ntshangase Mgazi**

- 📧 Email: vuyiswaandile176@gmail.com
- 🐙 GitHub: [@0698113787](https://github.com/0698113787)
- 🌐 Live Demo: [Flask Auth App](https://registeration-and-login-auth.onrender.com)

## 🙏 Acknowledgments

- **Flask Documentation** - Comprehensive framework guides
- **Font Awesome** - Professional icon library
- **Render Platform** - Reliable cloud hosting
- **SQLAlchemy Community** - Database ORM support
- **Stack Overflow** - Community support and solutions

## 📊 Project Stats

- **Lines of Code:** ~2000+
- **Languages:** Python, HTML, CSS, JavaScript
- **Files:** 10+ templates and style files
- **Database:** SQLite with SQLAlchemy ORM

## 🔮 Future Enhancements

- [ ] Email verification for registration
- [ ] Password reset functionality
- [ ] Two-factor authentication (2FA)
- [ ] Social media login integration
- [ ] User role management (Admin/User)
- [ ] Activity logging and audit trails
- [ ] Profile picture upload
- [ ] Dark/Light theme toggle

---

⭐ Made with ❤️ by Andile Ntshangase Mgazi