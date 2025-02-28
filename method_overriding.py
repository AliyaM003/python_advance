class parent:
    def show(self):
        print("parent class")
class child(parent):
    def show(self):
        print("child class")
class Gchild(child):
    def show(self):
        print("Gchild class")
obj=Gchild()
obj.show()

#OUTPUT
Gchild class
