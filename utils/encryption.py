import hashlib

# Global Constants
REFERENCE_DATE = "2024-12-26 12:24:36"
REFERENCE_USER = "MohamedMeftouh21"
SECRET_SALT = "EL46M#kP9$mN"  # Add an additional salt for security

# Global Encryption Key Generation
def generate_global_key():
    key_components = f"{REFERENCE_DATE}_{REFERENCE_USER}_{SECRET_SALT}"
    return hashlib.sha256(key_components.encode()).hexdigest()