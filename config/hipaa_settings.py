"""
HIPAA Compliance Configuration
Healthcare Data Security Settings
"""

# SEC DJANGO-001: DEBUG=True in config file
DEBUG = True

# SEC DJANGO-002: ALLOWED_HOSTS too permissive
ALLOWED_HOSTS = ['*']

# SEC DJANGO-005: Hardcoded SECRET_KEY
SECRET_KEY = "hipaa-hospital-django-secret-2024-do-not-expose"

# Database — PHI storage
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'phi-db.hospital.com',
        'NAME': 'patient_records',
        'USER': 'phi_admin',
        # SEC: Hardcoded DB password
        'PASSWORD': 'PHIDatabase2024Secure!',
    }
}

# SEC: Hardcoded encryption key for PHI
PHI_ENCRYPTION_KEY = "HIPAAEncKey2024XYZ789ABC"

# SEC INFRA-003: AWS S3 credentials for medical records
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7MEDEXAMPLE"
AWS_SECRET_ACCESS_KEY = "PHI/Record/Storage/Key/Example+2024"

# Email alerts for critical patient events
EMAIL_HOST = 'smtp.hospital.com'
EMAIL_HOST_USER = 'alerts@hospital.com'
# SEC: Hardcoded email password
EMAIL_HOST_PASSWORD = 'EmailAlert2024!'

# JWT config for staff tokens
# SEC: Weak JWT secret
JWT_SECRET_KEY = "jwt_hospital_weak_secret"

# HIPAA audit logging
AUDIT_LOG_RETENTION_DAYS = 2190  # 6 years as required by HIPAA
AUDIT_LOG_ENCRYPTION = False  # SEC: Should be True for HIPAA
