# 1.4 strings
a = 'flowers are pretty'
b = "the dirt is wet"
c = """
real eyes
realize
real lies
"""

print(a,b,c)

d = "hi comeback to me, \rthe carriage"
print(d)

e = '\xf1'
f = "\N{FOR ALL}"
print(e,f)

string='hello wall'
b=string[0]
c=string[1]
d=string[-1]
print(b,c,d,e)

b=string[1:4]
c=string[5:]
d=string[:5]
e=string[-6:]
print(b,c,d,e)

a="blin"+"g"
b="    ta"+a
print(b)
print(len(b),len("ta"))
t = 'ling' in a
print(t)

clone_jutsu = "bling" * 7
print(clone_jutsu)
c = b.strip()
d = c.replace("ta","cob")
print(d.upper())
b.lower()

# immutable : All operations and methods that manipulate 
# string data, always create new strings.
byte_string = b'Hello world'
print(len(byte_string),byte_string[:5], byte_string[1])
text_string = byte_string.decode('utf-8')
byte_string2 = text_string.encode('utf-8')
print(text_string,byte_string2)

rs = r'c:\people\sanso'
print(rs)

#f string (string lietrals), allow for interpolation
name = "Yahil"
age = "18"
print(f"My name is {name} and I'm {age} years old")