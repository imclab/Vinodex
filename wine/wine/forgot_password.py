from Crypto.Cipher import AES
from django.core.mail import send_mail

aes_key = 'FQndi4lndf34qqqq'

# encrypter = AES.new(aes_key, AES.MODE_CBC)
# TODO: Encrypt
def send_password_forgot_message(user):
    ciphertext = encrypt_userid(user.id)
    print "Password reset for user:", user.id
    send_mail("Reset your password", "Go here:"
          "http://vinodex.us/resetpassword.html#%s" % ciphertext,
          "admin@vinodex.us", [user.email])

# TODO: Encrypt
def encrypt_userid(user_id):
    return user_id
    # ciphertext = encrypter.encrypt(user.id)

# TODO: Descrypt
def decrypt_userid(cipher):
    return int(cipher)
    # return int(encrypter.decrypt(ciphertext))
