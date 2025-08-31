import secrets
import string
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def generate_reset_token():
    """Generate a secure random token for password reset"""
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))

def store_reset_token(email, token):
    """Store password reset token in Redis with expiry"""
    cache_key = f"password_reset:{token}"
    cache.set(cache_key, email, timeout=settings.PASSWORD_RESET_TIMEOUT)
    return cache_key

def get_email_from_token(token):
    """Retrieve email associated with reset token"""
    cache_key = f"password_reset:{token}"
    return cache.get(cache_key)

def invalidate_reset_token(token):
    """Remove reset token from cache"""
    cache_key = f"password_reset:{token}"
    cache.delete(cache_key)

def send_password_reset_email(user, token):
    """Send password reset email to user"""
    reset_url = f"{settings.FRONTEND_URL}/reset-password?token={token}"
    
    subject = 'Password Reset Request'
    html_message = render_to_string('emails/password_reset.html', {
        'user': user,
        'reset_url': reset_url,
        'timeout_minutes': settings.PASSWORD_RESET_TIMEOUT // 60
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.EMAIL_HOST_USER,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )

def get_client_ip(request):
    """Get client IP address from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip