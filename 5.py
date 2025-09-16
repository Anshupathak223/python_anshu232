#list
list1=["rohan",1,7,34]
print(list1)
print(len(list1))
# 
# list construction
list2=list(["rohan",1,2,"anshu","anshika"])
print(list2[1:4])
if 9 in list2:
    print("yes")
else :
    print("no")
list2[0]="ram"
list2[3:5]="anu","tanu","manu"
print(list2)
list1.insert(2,"hello")
print(list1)
list2.append("world")
print(list2)
list1.extend(list2)
print(list1)