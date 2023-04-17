#!/usr/bin/python3
""" 
User module defines a class that  
"""

class User():
    """ Creates a User  """

    def __init__(self):
        """ Initializes the user class instance with a None self.email value """
        self.__email = None

    @property
    def email(self):
        """ Returns the self.__email private instance attribute """
        return self.__email
   
    @email.setter
    def email(self, value):
        """Sets a user's email to the value supplied

        Args:
            value (str): user's email address
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
