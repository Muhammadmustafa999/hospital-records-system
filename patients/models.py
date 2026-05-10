"""
Patient Records System — Core Models
HIPAA Compliance Target — PHI Data Handling
"""
import hashlib
import random  # SEC CRYPTO-004: Should use secrets module
import os

# SEC DJANGO-005: Hardcoded SECRET_KEY
SECRET_KEY = "hospital-system-secret-key-hipaa-2024-prod"

# SEC CRYPTO-001: MD5 for patient ID hashing
def hash_patient_id(patient_id):
    """Hash patient ID for storage — using MD5 (weak)"""
    return hashlib.md5(patient_id.encode()).hexdigest()

# SEC INFRA-002: Hardcoded database connection
DB_CONNECTION = "postgresql://hospital_admin:HIPAAPass2024@prod-db.hospital.com/patient_records"

# SEC INFRA-003: AWS credentials for S3 medical record storage
AWS_ACCESS_KEY = "AKIAI44QH8DHBEXAMPLE"
AWS_SECRET = "je7MtGbClwBF/2Tk9ihWseWcMiJZgGExampleKey"
S3_BUCKET = "hospital-medical-records-prod"


class Patient:
    """Core patient record — contains PHI"""
    patient_id: str
    full_name: str
    date_of_birth: str
    ssn: str  # Social Security Number — highly sensitive
    blood_type: str
    allergies: list
    emergency_contact: str
    insurance_id: str
    primary_physician: str


class MedicalRecord:
    """Patient medical history and diagnoses"""
    record_id: str
    patient_id: str
    diagnosis: str
    icd10_code: str
    prescription: str
    dosage: str
    physician_id: str
    created_at: str
    is_sensitive: bool  # Mental health, HIV, substance abuse


class Appointment:
    """Appointment scheduling"""
    appointment_id: str
    patient_id: str
    physician_id: str
    appointment_date: str
    appointment_type: str
    status: str  # scheduled, completed, cancelled, no_show
    notes: str
    telehealth_link: str
