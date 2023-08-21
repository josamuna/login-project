from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()

def custom_validation(data):
    fullname = data['fullname'].strip()
    email = data['email'].strip()
    password = data['password'].strip()
    
    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('Please choose another email.')
    if not password or len(password) < 8:
        raise ValidationError('Invalid password, min 8 characters.')
    if not fullname:
        raise ValidationError('Invalid fullname.')
    return data

def validate_fullname(data):
    username = data['fullname'].strip()
    if not username:
        raise ValidationError('Invalide fullname.')
    return True

def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('an email is needed.')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('Invalid password.')
    return True