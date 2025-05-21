a = True
b = False
c = 3 + True
print('c:',c)
d = 7
if d == 0:
    print('d is false')

if (b<=c and c<=d):
    print('c is between b and d')
if not(c < b or c > d):
    print('c is still between b and d')