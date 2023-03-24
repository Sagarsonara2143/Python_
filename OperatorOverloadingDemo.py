class MagicMethod:

    def __init__(self,x,y):
        print("Init Function Called")
        self.x = x
        self.y = y

    def __str__(self):
        print("Str function Called")
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,obj):
        x = self.x + obj.x
        y = self.y + obj.y
        return MagicMethod(x,y)



a = MagicMethod(20,30)
print(a)
b = MagicMethod(40,50)
print(b)
print("Addition is : - ",a+b)
