class User:
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password


user1 = User("Suyash", "yash@123mail.com", "123mail.com")
user2 = User("yash", "yash@1234mail.com", "1234mail.com")

user1.say_hi_to_user(user2)

print(user1.email) #yash@123mail.com
