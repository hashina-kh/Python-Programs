#using normal function
def addition(x,y):
    return x+y
print(addition(20,2))


#using lambda keyword
num1 = int(input("Enter First number  ="))
num2 = int(input("Enter Second number  ="))

sum = lambda a,b: a+b
print("Sum is =",sum(num1,num2))

sub = lambda a,b: a-b
print("Differrnce is =",sub(num1,num2))

mul = lambda a,b: a*b
print("Product is =",mul(num1,num2))


