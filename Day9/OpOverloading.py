class MyDT:
    def __init__(self, val):
        self.val = val
        
    def __str__(self):
        return str(self.val)
    
    def __add__(self, ano_obj):
        return MyDT(self.val + ano_obj.val)
    
    # def add(self, *args):
    #     sum = self.val
    #     for i in args:
    #         sum += i.val
    #     return sum
    
    def __sub__(self, ano_obj):
        return MyDT(self.val - ano_obj.val)
    
    def __mul__(self, ano_obj):
        return MyDT(self.val * ano_obj.val)
    
    def __truediv__(self, ano_obj):
        return MyDT(self.val / ano_obj.val)
    
    def __floordiv__(self, ano_obj):
        return MyDT(self.val // ano_obj.val)
    
    def __mod__(self, ano_obj):
        return MyDT(self.val % ano_obj.val)
    
    
#     def __truediv__(self, ano_obj):
#         return self.val / ano_obj.val
    
#     def __floordiv__(self, ano_obj):
#         return self.val // ano_obj.val
    
#     def __mod__(self, ano_obj):
#         return self.val % ano_obj.val
    
# print(MyDT(10) / MyDT(20))
# print(MyDT(10) // MyDT(20))
# print(MyDT(10) % MyDT(20))


print(MyDT(10) + MyDT(20) + MyDT(30) + MyDT(40))
print(MyDT(10) - MyDT(20) - MyDT(30) - MyDT(40))
print(MyDT(10) * MyDT(20) * MyDT(30) * MyDT(40))
print(MyDT(10) / MyDT(20) / MyDT(30) / MyDT(40))
print(MyDT(10) // MyDT(20) // MyDT(30) // MyDT(40))
print(MyDT(10) % MyDT(20) % MyDT(30) % MyDT(40))

# print(MyDT.add(MyDT(100) + MyDT(10) + MyDT(20) + MyDT(30) + MyDT(40)))