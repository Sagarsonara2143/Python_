class Point:

    def __init__(self,x,y):             # It will called automatically when object for class is created
        print("init function called")
        self.x = x
        self.y = y

    def __str__(self):                  # it will called when we will print the object of class 
        print("Str function called")
        return " ({0},{1})".format(self.x,self.y)       # always return value require

    def __add__(self,obj):          # it will called when addition of two objected will be appear
        x = self.x + obj.x
        y = self.y + obj.y
        return Point(x,y)

    
p1=Point(10,20)             # it will called __init__ function
print(p1)                           # It will called __str__ function
p2 = Point(30,40)                # it will called __init__ function
print(p2)                                # it will called __str__ function   
print("Addition is : ",p1 + p2)  # it will called __str__ and __add__ function
