# def cal(a,b):
#     sum = a+b
#     print(sum)
# cal(1,2)
# def cal1(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# cal1(7,7)
# def cal2(a,b):
#     return a+b
# print(cal2(7,8))
# def list_length(list):
#     print(len(list))
#     return len(list)
# list_length([1,2,3,4])
# def ele_list(list):
#     for ele in list:
#         print(ele, end=" ")
# ele_list(["w","e","r","t","y"])  
def fact(n):
    fact = 1
    for i in range(1,n+1):
         fact *=i
    print(fact)
    return fact
fact(4)
def conv(x):
     y = x*83
     print(y)
conv(2)
def sum(n):
     if (n==0):
        return 0 
     return sum(n-1) + n
print(sum(10))
def rec(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    rec(list,idx+1)
fruits = ["s","k","l","i"]
rec(fruits)
    

