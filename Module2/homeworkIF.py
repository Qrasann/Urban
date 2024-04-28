x = 38

print('Hello!')
if x < 0:
    print('Less than zero')
print('Bye!')

######################################

a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('success1')

if (a > b) and (a > 0 or b < 1000):
    print('success2')

if 5 < b and b < 10:
    print('success3')

############################################

if '34' > '123':
    print('success4')

if '123' > '12':
    print('success5')

if [1, 2] > [1, 1]:
    print('success6')

#################################

if '6' > 5:
    print('success7')

if [5, 6] > 5:
    print('success8')

if '6' != 5:
    print('success9')