input_string=""
#input_string2="bbz"
a1count=[]

for i in range(97,123):
    char=chr(i)
    print(char)
    count=input_string.count(char)
    a1count.append(count)
print(a1count)

#OUTPUT
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
