from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_otp(otp):
    return ph.hash(otp)


def verify_otp(db_otp, otp):
    try:
        return ph.verify(db_otp, otp)
    except VerifyMismatchError:
        return False