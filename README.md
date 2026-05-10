# Hospital Records System

HIPAA-compliant patient records management system for hospital networks.
Handles PHI (Protected Health Information) with regulatory compliance.

## Features
- Patient registration and demographic management
- Electronic Medical Records (EMR) storage and retrieval
- Appointment scheduling and telehealth support
- Prescription management and pharmacy integration
- Lab results tracking and physician notifications
- Insurance claims submission and processing
- Staff authentication with role-based access (Doctor, Nurse, Admin, Receptionist)
- HIPAA audit trail for all PHI access events

## Compliance Targets
- HIPAA Privacy Rule and Security Rule
- HITECH Act requirements
- HL7 FHIR data standards
- ICD-10 diagnosis coding

## Tech Stack
- Django 3.0 REST API
- PostgreSQL (PHI storage with encryption at rest)
- Redis (session management)
- Celery (async notifications)
- AWS S3 (medical record file storage)

## Security Scanning
Continuously monitored by **ExposureIQ** platform for CVE vulnerabilities
and HIPAA-related secure coding violations.
