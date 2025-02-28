class RecursionTypes:
    def indirect_recursion_a(self,n):
        if n<=0:
            return
        print(f"indirect_recursion_A:{n}")
        self.indirect_recursion_b(n-1)
    def indirect_recursion_b(self,n):
        if n<=0:
            return
        print(f"indirect_recursion_B:{n:}")
        self.indirect_recursion_a(n-2)
obj=RecursionTypes()
obj.indirect_recursion_a(4)

#OUTPUT
indirect_recursion_A:4
indirect_recursion_B:3
indirect_recursion_A:1
