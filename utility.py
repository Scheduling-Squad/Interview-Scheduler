def generate_pwd_hash(password:str):
    f = Fernet(password)
    token = f.encrypt(password)
    return token