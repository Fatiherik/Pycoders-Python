import random
import string

def random_password(string_length=6):
    letters= random.sample(string.ascii_uppercase,2)
    numbers= random.sample(string.digits,2)
    specials= random.sample(string.punctuation,2)
    password_characters= letters+numbers+specials
    other_characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.sample(password_characters,6))+"".join(random.sample(other_characters,4))

print ("Random Password: ",random_password())
