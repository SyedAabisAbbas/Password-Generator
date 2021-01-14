import random,string
def password(length,num = False,strength='weak'):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    dig = string.digits
    letters = lower + upper
    punct = string.punctuation
    pwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(1):
                pwd += random.choice(dig)
                pwd += random.choice(punct)
        for i in range(length):
            pwd +=random.choice(lower)
    elif strength == 'normal':
        if num:
            length -= 2
            for i in range (1):
                pwd += random.choice(dig)
                pwd += random.choice(punct)
        for i in range (length):
            pwd += random.choice(letters)
    elif strength == 'strong':
        if num:
            length -= 2
            for i in range (1):
                pwd += random.choice(dig)
                pwd += random.choice(punct)
        for i in range (length):
            pwd += random.choice(letters)
    elif strength == 'very':
        if num:
            length -= 2
            for i in range (1):
                pwd += random.choice(dig)
                pwd += random.choice(punct)
        for i in range (length):
            pwd += random.choice(punct)
    pwd=list(pwd)
    random.shuffle(pwd)
    print(''.join(pwd))

password(8,num=True,strength='strong')
