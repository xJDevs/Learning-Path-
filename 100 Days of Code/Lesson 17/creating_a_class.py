import random

class User2:   # Pascal casing is used to name classes. Ex: UserClass
    def __init__(self):
        pass

user_2 = User2()
'''
To create attributes, just use dot notation after the object is created as shown below. 
Reminder: An attribute is a variable assciated with an object. 
'''
user_2.id = '001'
user_2.username = 'Jagz'

'''
-----------------------------------------------------------------------------------------------------
'''

'''
Thee best practice is to create the attributes inside the class and initialize them with the 
     __init__ function
IMPORTANT: Init will be called every time an object is created. 
'''

'''
This works as a regular function: If I add parameters to the init function, 
they MUST be provided when the object is created, otherwise, Error will pop up
'''
class User:
    def __init__(self, user_id, username):   
        self.id = user_id
        self.username = username  # Usually, attributes are named the same as the parameters, but is not a rule of thumb 
        self.followers = 0
        self.following = 0
        '''
        I can also initialize variables with default values such as ''followers''. Imagine I'm coding instagram. All acounts start  with 
        0 followers. Instead of passing it as a parameter, I just initialize it on a 0 default value, that can be modified later on. 
        '''

        # Methods

    def follow(self, user):
        # 'user' is the person who RECEIVES the action
        # Example: if A follows B → user = B
        user.followers += 1  # Increase the follower count of the person being followed
    
        # 'self' is the person who PERFORMS the action
        # Example: if A follows B → self = A
        self.following += 1  # Increase the number of accounts this user is following
            

main_user = User('117810291', 'Joe')
user_3 = User('002', 'Cami')
main_user.follow(user_3)

print(main_user.followers, main_user.following)
print(user_3.following, user_3.followers)

# Experiment just to check how an attribute is modified 

if random.choice([True, False]):
    main_user.followers += 5000

print(main_user.followers)

'''
Attributes: Class variables that the object has
Methods: Object functionalities 
'''


