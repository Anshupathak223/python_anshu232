input("hello world")
v= input()
a=int(input())
b=int(input())
if a>b:
    print(a+"is greater than"+b)
elif a==b:
    print("a is equal to b")
else:
  print(b+"is greater than"+a)
#   short hand if
if a>b:print(a+"is greater than"+b)
# short hand if else
print(a) if a>b else print(b)
