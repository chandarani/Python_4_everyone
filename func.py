def thing():
    print('Hello') 

print('There')
def func(x) :
    print(x)

func(10)
func(20)
def stuff():
    print('Hello')
    return
    print('World')

stuff()
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')