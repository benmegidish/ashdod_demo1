

class User():
    def __init__(self, name, email = None):
        self.name = name
        self.email = email
        
        
user = User("name")
user= user.__dict__
print(user)
    
for i in user:
    print(user[i])