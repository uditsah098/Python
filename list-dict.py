########################
# list and dictionary  #
########################

#### List ####
list=[]
list.append("cat")
list.append("dog")
print(list)
num=int(input("enter the quantity that you are thinking to enter= "))
for i in range(1,num+1):
    data=input("enter "+str(i)+" data= ")
    list.append(data)
print(list)


#### Dictionary ####

dictionary={
     "name" :"rohit",
     "rollno" : "3",
     "course" : "math"

}

print(dictionary)
print(dictionary["name"])
print(dictionary["rollno"])

#### Functions ####

num=int(input("enter the number="))
if num%2==0:
    print("even number")
else:
    print("odd number")    


#### function ####
print("function run")
def check(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num=4    
print(check(num))