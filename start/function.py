# def square(x):
#     return x*x

# list1 =[2 , 3 ,4  , 55]
# print(list(map(square, list1)))


# def square(x):
#     return x%2==0

# list1 =[2 , 3 ,4  , 55]
# print(list(filter(square, list1)))
if 10<5:
    print("true")
else:
    print('false')



marks = int(input("enter your marks"))

if marks>= 90:
    print("grade A")
    
elif marks>=80:
    print("grade B ")
elif marks>=70:
    print("grade B+ ")
elif marks>=60:
    print("grade c ")
else:
    print("you only pass")

i=1
while i<= 5:
    print(i*2)
    i=i+1

def outer():
    print("outer calling")
def inner():
    print("inner call")
    outer()
    