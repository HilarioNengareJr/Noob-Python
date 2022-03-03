import hashlib

class User:
    
    """This is a dummy auntication program.And implementation of self-defined exceptions!"""
    
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False
        
    #implementation of the password encryption process
    def _encrypt_pw(self, password):
        
        """ Encrypt the password with the username concatenated to it, return a sha output. """
        
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf-8")
        hash_lib = hashlib.sha256(hash_string)
        
        return hash_lib.hexdigest()
        
    def check_password(self, password):
        
        """ A function to compare passwords. """
        
        encrypted = self._encrypt_pw(password)
        
        return encrypted==self.password
    
class AuthException(Exception):
    
    """ Exception handling: """
    def __init__(self, username, user=None):
        super().__init__(username, user)#user is an instance of user class associated with the username
        self.username = username
        self.user = user

class UserAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class Authentic_User:
    
    """ Manage users logging in and out """
    def __init__(self):
        
        self.users = {}
        
    def add_user(self, username, password):
        
        if username in self.users:
            raise UserAlreadyExists(username)
        
        if password < 8:
            raise PasswordTooShort(password)
        
        
        
        
        
        
        
        
        
        
        
        