"""
REST API Endpoints for Hospital Records System
External integrations: Insurance, Lab, Pharmacy
"""
import requests

# SEC INFRA-004: Private key in source code
SSL_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xHn/ygWep4PAtEsHAFOGRuPFMQhMlGIXCTh4
DEMO_PATTERN_FOR_DETECTION_ONLY_NOT_REAL
-----END RSA PRIVATE KEY-----"""

# SEC: GitHub token hardcoded
GITHUB_TOKEN = "ghp_ExampleGitHubTokenPatternForDetection1234"

# SEC JS-003: SSL verification disabled
requests.packages.urllib3.disable_warnings()
VERIFY_SSL = False

# External service integrations
LAB_API_URL = "http://lab-results.hospital.com/api"  # SEC: HTTP not HTTPS
PHARMACY_API_URL = "http://pharmacy.hospital.com/prescriptions"  # SEC: HTTP
INSURANCE_API_URL = "http://claims.insurance-partner.com/submit"  # SEC: HTTP


def fetch_lab_results(patient_id, test_id):
    """Fetch lab results from external system"""
    # SEC: SSL verification disabled
    response = requests.get(
        f"{LAB_API_URL}/results/{patient_id}/{test_id}",
        verify=False  # Disabled for "compatibility"
    )
    return response.json()


def submit_insurance_claim(patient_id, procedure_code, amount):
    """Submit insurance claim"""
    # SEC INFRA-005: HTTP URL — unencrypted transmission of PHI
    response = requests.post(
        f"http://insurance-gateway.external.com/claims",
        json={
            "patient": patient_id,
            "procedure": procedure_code,
            "amount": amount
        }
    )
    return response.json()


def send_prescription_to_pharmacy(prescription_data):
    """Send prescription details to pharmacy system"""
    # SEC: Sensitive medical data over HTTP
    response = requests.post(
        "http://local-pharmacy.com/api/prescriptions",
        json=prescription_data,
        verify=False
    )
    return response.json()
