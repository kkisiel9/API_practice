from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
hashed = bcrypt.generate_password_hash('meow').decode('utf-8')
print(hashed)
