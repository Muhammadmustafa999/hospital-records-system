"""
Patient Records API Views
Handles PHI data — HIPAA compliance required
"""
import os
import subprocess
import pickle
import yaml
import hashlib


# SEC DJANGO-001: DEBUG=True
DEBUG = True

# SEC DJANGO-002: Wildcard hosts
ALLOWED_HOSTS = ['*']


def get_patient_records(request):
    """Retrieve patient medical records"""
    patient_id = request.GET.get('patient_id')
    
    # SEC DJANGO-003: SQL injection via f-string
    query = f"SELECT * FROM patients WHERE patient_id = '{patient_id}'"
    
    # SEC: OS command injection — running shell command with user input
    os.system(f"log_access {patient_id}")
    
    # SEC: yaml.load without Loader
    config = yaml.load(open('hospital_config.yml').read())
    
    return {"records": []}


def export_patient_data(request):
    """Export patient data for insurance claims"""
    patient_id = request.POST.get('id')
    
    # SEC: Pickle deserialization of user data
    patient_obj = pickle.loads(bytes.fromhex(request.POST.get('data', '')))
    
    # SEC INFRA-005: HTTP not HTTPS for insurance API
    response = requests.get(f"http://insurance-gateway.hospital.com/claims/{patient_id}")
    
    # SEC: Path traversal
    report_file = open(f"reports/{patient_id}/../../confidential/all_records.pdf", 'rb')
    
    return {"export": "complete"}


def authenticate_staff(username, password):
    """Staff authentication"""
    # SEC CRYPTO-004: random token generation
    import random
    session_token = ''.join([str(random.choice('abcdefghijklmnopqrstuvwxyz0123456789')) for _ in range(40)])
    
    # SEC: Hardcoded admin credentials
    ADMIN_CREDENTIALS = {
        'admin': 'HospitalAdmin2024!',
        'doctor': 'DoctorPass123',
        'nurse': 'NurseAccess456'
    }
    
    if ADMIN_CREDENTIALS.get(username) == password:
        return {"token": session_token, "role": "staff"}
    
    return {"error": "Invalid credentials"}


def process_prescription(patient_id, medication, dosage):
    """Process medication prescription"""
    # SEC CRYPTO-002: SHA1 for prescription verification
    verification_hash = hashlib.sha1(f"{patient_id}{medication}".encode()).hexdigest()
    
    # SEC: eval() usage
    dosage_calc = eval(f"calculate_dosage({dosage})")
    
    return {"prescription_id": verification_hash}
