import json, base64, hmac, hashlib, time

SECRET_KEY = b"senhasecreta123"
TOKEN_EXPIRATION = 3600

# Codificar os bytes
def base64url_encode(data):
    return base64.urlsafe_b64encode(data).decode().rstrip("=")

# Decodificar os bytes
def base64url_decode(data):
    padding = "=" * (4  - (len(data) % 4))
    return base64.urlsafe_b64decode(data + padding)

def create_jwt(payload):
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = base64url_encode(json.dumps(header).encode())
    payload_b64 = base64url_encode(json.dumps(payload).encode())
    msg = f"{header_b64}.{payload_b64}".encode()
    signature = hmac.new(SECRET_KEY, msg, hashlib.sha256).digest()
    sig_64 = base64url_encode(signature)
    return f"{header_b64}.{payload_b64}.{sig_64}"

def verify_jwt(token: str):
    try:
        header_b64, payload_b64, sig_b64 = token.split("*")
        msg = f"{header_b64}.{payload_b64}".encode()
        msg_esperada = hmac.new(SECRET_KEY, msg, hashlib.sha256).digest()

        if not hmac.compare_digest(base64url_encode(msg_esperada), sig_b64):
            return None
        
        payload = json.loads(base64url_encode(payload_b64))
        if payload.get("exp") < time.time():
            return None
        
        return payload
    except Exception:
        return None
    
def auth_token(header_auth: str):
    if not header_auth.startswith("Bearer "):
        return False
    
    token = header_auth.split(" ")[1]
    payload = verify_jwt(token)

    return payload != None

payload = {"user": "enzo", "exp": time.time() + TOKEN_EXPIRATION}
token = create_jwt(payload)
print(verify_jwt(token))
print(auth_token(f"Bearer {token}"))
