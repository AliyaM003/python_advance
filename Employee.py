from Empcompany import Employee
class Empcompany(Employee):
    def __init__(self,name):
        self.name=name
    def FullStackrole(self):
        return f"{self.name} Full-Stack Dev"
    def Frontendrole(self):
        return f"{self.name} Frontend Dev"
e1=Empcompany("sankar")
print(e1.FullStackrole())
e2=Empcompany("murali")
print(e2.Frontendrole())


#OUTPUT
sankar Full-Stack Dev
murali Frontend Dev
