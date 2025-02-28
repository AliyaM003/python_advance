class Father:
    #def __init__(self,name):
        #self.name="sankar"
    def show(self):
        print("parent1")
class Mother:
    def show(self):
        print("parent2")
class child(Father,Mother):
        pass
obj=child()
obj.show()

#OUTPUT
parent1
