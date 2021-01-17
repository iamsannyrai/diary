import jwt
from diary import app


class JWTUtils:
    @staticmethod
    def decode(header):
        try:
            if header:
                jwt_token = header[7:] if header.startswith('Bearer ') else header
                return jwt.decode(jwt_token, key=app.config['JWT_SECRET_KEY'], algorithms='HS256')
        except:
            return None
