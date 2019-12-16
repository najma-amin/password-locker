import random 
import string
import  pyperclip

class User:
    '''
    class that will generate new instances of users.
    '''
    user_list = []
    def __init__(self,lastname ,password):
        
        '''
        init method that gives the blueprint of the object instantiated
        '''
        self.lastname = lastname
        self.password = password
        
    def save_user (self):
        '''
        amethod  to save uset object to user_list
        '''
        User.user_list.append(self)
        
class Credential:
    '''
    class that defines the credential behaviours
    '''
    credential_list = []
    user_credential_list = []
    
    @classmethod
    def confirm_login (cls,lastname, password):
        '''
        method for login the user
        '''
        for user in User.user_list:
            if user.lastname == lastname and user.password == password:
                current_user =user.lastname
        return current_user
    def __init__(self, account_name, username, password):
        '''
        method to define the properties for user object
        '''
        self.account_name = account_name
        self.username = username
        self. password = password
        
    def save_credential (self):
        '''
        amethod  to save uset object to user_list
        '''
        Credential.credential_list.append(self)
        
    @classmethod
    def display_credential(cls, username):
        '''
        function to diplay saved account
        '''
        user_credential_list = []
        for  credential in cls.credential_list:
            if credential.username == username:
                user_credential_list.append(credential)
        return user_credential_list   
