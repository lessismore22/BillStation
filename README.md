<<<<<<< HEAD
<<<<<<< HEAD
#  Django Auth Service

A robust, production-ready user authentication system built with Django REST Framework, featuring JWT authentication, PostgreSQL database, Redis caching, and secure password management.

##  Features

-  **Email-based Authentication** - Modern approach without usernames
-  **JWT Token Management** - Secure access/refresh token system
-  **Redis-Cached Password Reset** - Time-limited tokens for security
-  **Email Integration** - Beautiful HTML templates for notifications
-  **Advanced Security** - Token blacklisting, IP tracking, validation
-  **Docker Ready** - One-command local development setup
-  **Cloud Deployable** - Railway, Render, and Docker configurations
-  **User Management** - Profiles, password changes, activity logs
-  **Testing Suite** - Comprehensive API test coverage

##  Quick Start
=======
# 🔐 Django Auth Service
=======
#  Django Auth Service
>>>>>>> 7fea630 (modified the README.md)

A robust, production-ready user authentication system built with Django REST Framework, featuring JWT authentication, PostgreSQL database, Redis caching, and secure password management.

##  Features

-  **Email-based Authentication** - Modern approach without usernames
-  **JWT Token Management** - Secure access/refresh token system
-  **Redis-Cached Password Reset** - Time-limited tokens for security
-  **Email Integration** - Beautiful HTML templates for notifications
-  **Advanced Security** - Token blacklisting, IP tracking, validation
-  **Docker Ready** - One-command local development setup
-  **Cloud Deployable** - Railway, Render, and Docker configurations
-  **User Management** - Profiles, password changes, activity logs
-  **Testing Suite** - Comprehensive API test coverage

<<<<<<< HEAD
## 🚀 Quick Start
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Quick Start
>>>>>>> 7fea630 (modified the README.md)

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (recommended)
- Or PostgreSQL 12+ and Redis 6+ (manual setup)

### 1. Setup Project

```bash
# Clone repository
git clone <your-repo-url>
cd auth_service

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

Create `.env` file:

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=auth_service_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT (minutes/days)
JWT_ACCESS_TOKEN_LIFETIME=15
JWT_REFRESH_TOKEN_LIFETIME=7

# Email (Gmail example)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password  # Not your regular password!

# Frontend
FRONTEND_URL=http://localhost:3000
```

### 3. Start Services

```bash
# Option 1: Docker (Recommended)
docker-compose up -d

# Option 2: Local services
# Ensure PostgreSQL and Redis are running locally
```

### 4. Initialize Django

```bash
# Database setup
python manage.py makemigrations authentication
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

<<<<<<< HEAD
<<<<<<< HEAD
 **API ready at:** http://localhost:8000/api/auth/
=======
🎉 **API ready at:** http://localhost:8000/api/auth/
>>>>>>> 1e85d32 (updated the README.md)
=======
 **API ready at:** http://localhost:8000/api/auth/
>>>>>>> 7fea630 (modified the README.md)

### 5. Test API

```bash
python test_api.py
```

<<<<<<< HEAD
<<<<<<< HEAD
##  API Reference
=======
## 📖 API Reference
>>>>>>> 1e85d32 (updated the README.md)
=======
##  API Reference
>>>>>>> 7fea630 (modified the README.md)

### Base URL: `http://localhost:8000/api/auth/`

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/register/` | POST | ❌ | User registration |
| `/login/` | POST | ❌ | User login |
| `/logout/` | POST | ✅ | User logout |
| `/profile/` | GET | ✅ | Get user profile |
| `/profile/update/` | PUT | ✅ | Update profile |
| `/forgot-password/` | POST | ❌ | Request reset |
| `/reset-password/` | POST | ❌ | Reset with token |
| `/change-password/` | POST | ✅ | Change password |
| `/refresh/` | POST | ❌ | Refresh JWT |

### Authentication
Include JWT token in requests:
```bash
Authorization: Bearer <access_token>
```

### Example Usage

**Register User:**
```bash
curl -X POST localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "full_name": "John Doe",
    "password": "SecurePass123!",
    "password_confirm": "SecurePass123!"
  }'
```

**Login:**
```bash
curl -X POST localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePass123!"
  }'
```

**Get Profile:**
```bash
curl -X GET localhost:8000/api/auth/profile/ \
  -H "Authorization: Bearer <your_token>"
```

<<<<<<< HEAD
<<<<<<< HEAD
##  Docker Development
=======
## 🐳 Docker Development
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Docker Development
>>>>>>> 7fea630 (modified the README.md)

```bash
# Start all services
docker-compose up --build

# Background mode
docker-compose up -d --build

# View logs
docker-compose logs -f web

# Stop all
docker-compose down
```

Services available:
- **Django API:** http://localhost:8000
- **PostgreSQL:** localhost:5432
- **Redis:** localhost:6379

<<<<<<< HEAD
<<<<<<< HEAD
##  Deployment
=======
## 🚀 Deployment

### Railway

```bash
# Install CLI
npm install -g @railway/cli

# Deploy
railway login
railway init
railway add postgresql
railway add redis
railway up
```
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Deployment
>>>>>>> 7fea630 (modified the README.md)

### Render

1. Connect GitHub repository
2. Add PostgreSQL and Redis add-ons
3. Set environment variables
4. Deploy from dashboard

### Docker Production

```bash
# Build image
docker build -t auth-service .

# Run with environment
docker run -p 8000:8000 --env-file .env auth-service
```

<<<<<<< HEAD
<<<<<<< HEAD
##  Configuration
=======
## ⚙️ Configuration
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Configuration
>>>>>>> 7fea630 (modified the README.md)

### JWT Tokens

```env
<<<<<<< HEAD
<<<<<<< HEAD
JWT_ACCESS_TOKEN_LIFETIME=10    # 10 minutes
=======
JWT_ACCESS_TOKEN_LIFETIME=15    # 15 minutes
>>>>>>> 1e85d32 (updated the README.md)
=======
JWT_ACCESS_TOKEN_LIFETIME=10    # 10 minutes
>>>>>>> 7fea630 (modified the README.md)
JWT_REFRESH_TOKEN_LIFETIME=7    # 7 days
```

**Recommendations:**
- **Development:** 60 minutes / 30 days
- **Production:** 5-15 minutes / 1-7 days

### Email Setup

**Gmail (App Password Required):**
1. Enable 2FA in Google Account
2. Generate App Password: Account → Security → App passwords
3. Use 16-character app password

**Other Providers:**
```env
# SendGrid
EMAIL_HOST=smtp.sendgrid.net
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your_sendgrid_api_key

# Mailgun
EMAIL_HOST=smtp.mailgun.org
EMAIL_HOST_USER=smtp_login
EMAIL_HOST_PASSWORD=smtp_password
```

<<<<<<< HEAD
<<<<<<< HEAD
##  Security Features

-  Email-based authentication (no username enumeration)
-  JWT with configurable expiry
-  Token blacklisting on logout
-  Password complexity validation
-  Time-limited password reset tokens
-  IP address tracking
-  CORS protection
-  Environment-based secrets

##  Project Structure
=======
## 🔐 Security Features
=======
##  Security Features
>>>>>>> 7fea630 (modified the README.md)

-  Email-based authentication (no username enumeration)
-  JWT with configurable expiry
-  Token blacklisting on logout
-  Password complexity validation
-  Time-limited password reset tokens
-  IP address tracking
-  CORS protection
-  Environment-based secrets

<<<<<<< HEAD
## 📁 Project Structure
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Project Structure
>>>>>>> 7fea630 (modified the README.md)

```
auth_service/
├── auth_service/           # Django project settings
├── authentication/        # Main auth app
│   ├── models.py          # Custom User model
│   ├── serializers.py     # API serializers
│   ├── views.py           # API endpoints
│   ├── utils.py           # Helper functions
│   └── admin.py           # Admin interface
├── templates/emails/       # Email templates
├── requirements.txt        # Dependencies
├── docker-compose.yml     # Development services
├── Dockerfile             # Container config
├── test_api.py           # API tests
└── .env                  # Environment variables
```

<<<<<<< HEAD
<<<<<<< HEAD
##  Testing
=======
## 🧪 Testing
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Testing
>>>>>>> 7fea630 (modified the README.md)

```bash
# API test suite
python test_api.py

# Django tests
python manage.py test

# Coverage report
pip install coverage
coverage run manage.py test
coverage report
```

<<<<<<< HEAD
<<<<<<< HEAD
##  Troubleshooting
=======
## 🐛 Troubleshooting
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Troubleshooting
>>>>>>> 7fea630 (modified the README.md)

**Database Issues:**
```bash
# Check services
docker-compose ps

# Reset database
docker-compose down -v
docker-compose up -d db redis
python manage.py migrate
```

**Redis Issues:**
```bash
# Test connection
redis-cli ping

# Clear cache
redis-cli flushall
```

**Email Issues:**
- Gmail: Ensure 2FA enabled and using App Password
- Check EMAIL_HOST_PASSWORD in .env
- Verify EMAIL_HOST and EMAIL_PORT settings

**Token Issues:**
- Check JWT_ACCESS_TOKEN_LIFETIME settings
- Ensure server time is correct
- Clear Redis cache if needed

<<<<<<< HEAD
<<<<<<< HEAD
##  Contributing
=======
## 🤝 Contributing
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Contributing
>>>>>>> 7fea630 (modified the README.md)

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit Pull Request

<<<<<<< HEAD
<<<<<<< HEAD
##  Support
=======
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support
>>>>>>> 1e85d32 (updated the README.md)
=======
##  Support
>>>>>>> 7fea630 (modified the README.md)

Need help? 

1. Check [troubleshooting](#-troubleshooting) section
2. Search [existing issues](../../issues)
3. Create [new issue](../../issues/new) with:
   - Environment details
   - Error messages
   - Steps to reproduce

---

<<<<<<< HEAD
<<<<<<< HEAD
**Built with  using Django, PostgreSQL, and Redis**

 **Star this repo if it helped you!**
=======
**Built with ❤️ using Django, PostgreSQL, and Redis**

⭐ **Star this repo if it helped you!**
>>>>>>> 1e85d32 (updated the README.md)
=======
**Built with  using Django, PostgreSQL, and Redis**

 **Star this repo if it helped you!**
>>>>>>> 7fea630 (modified the README.md)
