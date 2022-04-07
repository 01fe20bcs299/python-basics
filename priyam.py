mystring="priyam"
print(len(mystring))
print(mystring[-2])
string1="hello"
string2="world"
bigstring="""Hello my name is priyam.i am from katihar"""
print(bigstring)
#checking r in mystring
print('r' in mystring)
print('z' in mystring)
mystringupper=mystring.upper()
print(mystringupper)
mystringlower=mystringupper.lower()
print(mystringlower)
notmystring="dower"
ismystring=notmystring.replace("d","t")
print(ismystring)
#newstring=input()
#print(newstring)
new="coding"
#print(new[0:4:2])
#print(new[-3:])
#print(new[-3:-1:2])
print(new[::2])
#tuples
tuple=(0,"priyam",5.8)
print(0 in tuple)
def sum(*args):
    return args[0]+args[1]+args[2]
d=sum(20,30,40)
print(d)
li=[]
#for i in range(0,5,1):
 #   n=int(input("enter n"))
  #  li.append(n) 
li.sort()
print(li)   
#return count of 2 in li
d=li.count(2)
print(d)
mydict={}
for i in range(0,5,1):
    n=int(input("enter key"))
    m=int(input("enter value"))
    mydict[n]=m
print(mydict)
p="tiger is national animal"
list1=list(p.strip(" "))
print(list1)
k=5
for key,value in mydict.items():
    if key==k:
        print("found")
    else:
        continue
    
    
