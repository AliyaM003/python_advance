#METHOD_OVERLOADING 1
class Example:
    def add(self,*a):
        return sum(a)
    def add(self,a=1,b=2,c=3):
        return a+b+c
obj=Example()
print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add(4,6))

#OUTPUT1
6
6
13

#METHOD_OVERLOADING 2
class Example:
    def add(self,*a):
        return sum(a)
    def add(self,a=1,b=2,c=3):
        if(a!=0 and b!=0 and c==0):
            return a+b+c
        elif(a!=0 and b!=0 and c==0):
            return a+b
        else:
            return a
obj=Example()
print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add())

#OUTPUT2
1
1
1



