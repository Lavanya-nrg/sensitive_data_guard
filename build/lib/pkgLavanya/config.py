patterns = [
    r"^Username:[a-zA-Z0-9_@.-]{3,}$",  # Username: Starts with 'Username:' followed by at least 3 alphanumeric or special characters
    r"^Password:[a-zA-Z\d@!#$%^&*()-_+=]{8,}$",  # Password: Starts with 'Password:' followed by at least 8 characters including letters, digits, or specified special characters
    r"^SSN:\d{3}-\d{2}-\d{4}$",  # SSN: Matches the pattern of Social Security Numbers (SSN)
    r"^CreditCard:\d{4}-\d{4}-\d{4}-\d{4}$",  # CreditCard: Matches the pattern of Credit Card Numbers
    r"^MedicalRecord:MR\d+$",  # MedicalRecord: Starts with 'MedicalRecord:' followed by 'MR' and one or more digits
    r"^FingerprintMatching:FingerprintData\d+$",  # FingerprintMatching: Starts with 'FingerprintMatching:' followed by 'FingerprintData' and one or more digits
]
