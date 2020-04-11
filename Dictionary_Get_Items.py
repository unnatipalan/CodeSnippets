'''
There are several ways to handle missing keys in Dictionaries.
In this code snippet, we explore a few ways we handle missing keys in Python
'''

name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert'
}

def greeting(userid):
    return print(f'Hi {name_for_userid[userid]}!')

#greeting(382) #works as expected

#greeting((22222)) #key error

#Handling Key errors
def greeting(userid):
    if userid in name_for_userid:
        return print(f'Hi {name_for_userid[userid]}!') #we are traversing the dictionary twice
    else:
        return print('Hi there!')

#greeting(382) #works as expected

#greeting(22222) #key error handled

'''The above implementation works but can be improved'''


'''In this implementation:
1. We used only one dictionary lookup
2. We used EAFP principle, to catch just KeyErrors
3. More Pythonic
'''
def greeting(userid):
    try:
        return print(f'Hi {name_for_userid[userid]}!')
    except KeyError:
        return 'Hi there!'

'''Finally Python Dictionaries have get method that supports a default fall back'''

def greetings(userid):
    customer_greeting = 'Hi %s!' % name_for_userid.get(userid, 'there')
    return customer_greeting



#greeting(950) #works as expected
print(greetings(8000))
