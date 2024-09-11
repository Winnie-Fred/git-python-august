# class BankAccount:

#     LEN_ACCT_NUMBER = 10

#     def __init__(self, bank_name, owner, account_number, balance):
#         self.bank_name = bank_name
#         self.account_name = owner
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             return "Amount must be greater than or equal to zero"
        
#         self.balance += amount
#         return "Deposit successful"
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Amount must be greater than or equal to zero"
        
#         if amount > self.balance:
#             return "Insufficient funds"
        
#         self.balance -= amount 
#         return "Withdrawal successful"
    
#     def account_info(self):
#         return f"Account Name: {self.account_name}\nAccount Number: {self.account_number}\nLength of Account number: {BankAccount.LEN_ACCT_NUMBER}"
    

# khalid_acct = BankAccount("Moniepoint", "Olorunlambe Khalid", "7088550054", 7500)
# bolu_acct = BankAccount("Union Bank", "Adekunle Bolu", "0141888186", 2500)

# print(khalid_acct.withdraw(1650))
# print(khalid_acct.balance)
# print(khalid_acct.withdraw(-5900))
# print(khalid_acct.balance)

# print(khalid_acct.account_info())


# bank_accounts = {
#     "Khalid": {
#         'account_name': "Olorunlambe Khalid",
#         'bank_name': "Moniepoint",
#         'account_number': "7088550054",
#         'balance': 7500,
#     },
#     "Bolu" : {
#         'account_name': "Adekunle Bolu",
#         'bank_name': "Union Bank",
#         'account_number': "0141888186",
#         'balance': 2500,
#     }
# }



# def deposit(amount, owner):

#     owner_acct = bank_accounts[owner]

#     if amount <= 0:
#         return "Amount must be greater than or equal to zero"
    
#     owner_acct['balance'] += amount
#     return "Deposit successful"

# def withdraw(amount, owner):
#     if amount <= 0:
#         return "Amount must be greater than or equal to zero"
    
#     owner_acct = bank_accounts[owner]

#     if amount > owner_acct['balance']:
#         return "Insufficient funds"
    
#     owner_acct['balance'] -= amount 
#     return "Withdrawal successful"

# def check_balance(owner):
#     return bank_accounts[owner]['balance']



# print(withdraw(3500, "Khalid"))
# print(check_balance("Khald"))

# Create a class called Person who has a name, age, is_male
# and can introduce, walk and stand



class Animal:
    def __init__(self, name, type, sound, has_wings, has_legs, hair_color, has_whiskers, number_of_legs):
        self.name = name
        self.type = type
        self.sound = sound
        self.has_wings = has_wings
        self.has_legs = has_legs
        self.hair_color = hair_color
        self.has_whiskers = has_whiskers
        self.number_of_legs = number_of_legs

    def speak(self):
        return f"{self.sound}!"
    
    def introduction(self):
        has_wings = "have wings" if self.has_wings else "do not have wings"
        has_whiskers = "have whiskers" if self.has_whiskers else "do not have whiskers"
        has_legs = f"have {self.number_of_legs} legs" if self.has_legs else "do not have legs"


        return f"My name is {self.name}. I am a/an {self.type}. I {has_wings}. I {has_whiskers}. My hair color is {self.hair_color} and I {has_legs}."
    

# dog = Animal("Miles", "dog", "woof", False, True, "brown", True, 4)
# cat = Animal("Molly", "cat", "meow", False, True, "black", True, 4)
# bird = Animal("Mr. Beaks", "bird", "chirp", True, True, "white", True, 2)

# print(dog.introduction())
# print(cat.introduction())
# print(bird.introduction())

# class Dog(Animal):
#     def __init__(self, name, hair_color, breed):
#         super().__init__(name=name, hair_color=hair_color, sound="woof", has_legs=True, type="dog", has_wings=False, has_whiskers=True, number_of_legs=4)
#         self.breed = breed

#     # def __str__(self):
#     #     return self.introduction()

#     def __repr__(self):
#         return f"Dog(name={self.name!r}, hair_color={self.hair_color!r}, breed={self.breed!r})"

#     def introduction(self):
#         animal_introduction = super().introduction()
#         return f"{animal_introduction} I am a {self.breed}"
    
# rocky = Dog("Rocky", "light brown", "Husky")
# bella = Dog("Bella", "black", "German Shepherd")

# print(rocky.introduction())
# print(bella.introduction())

# print(isinstance(rocky, Animal))
# print(isinstance(cat, Dog))

# print(issubclass(Animal, Dog))
# print(issubclass(Dog, Animal))

# created_instance = Dog(name='Rocky', hair_color='light brown', breed='Husky')
# print(created_instance)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    

# sum_of_points = Point(3, 4) + Point(5, 6) + Point(-3, -2) + Point(-10, -5)
# print(sum_of_points)

# my_list = {"name1":"Khalid", "name2":"Bolu"}
# print(len(my_list))


# class Book:
#     def __init__(self, number_of_pages, author, title, year_published, is_fiction):
#         self.number_of_pages = number_of_pages
#         self.author = author
#         self.title = title
#         self.year_published = year_published
#         self.is_fiction = is_fiction

#     def __len__(self):
#         return self.number_of_pages

# frankenstein = Book(200, "Mary Shelley", "Frakenstein", 1998, True)
# kokubaboni = Book(70, "Winnie Matt", "Kokubaboni", 1973, True)

# books = [kokubaboni, frankenstein]

# for book in books:
#     print(book.title)
#     print(book.number_of_pages)
#     print(book.author)
#     print(book.is_fiction)
    

class Gadget:
    def operate(self):
        return "Operating the Gadget"
    
class SmartPhone(Gadget):
    def operate(self):
        return "Operating the smart phone"
    
class Tablet(Gadget):
    def operate(self):
        return "Operating the tablet"
    

smartphone = SmartPhone()
tablet = Tablet()

print(smartphone.operate())
print(tablet.operate())