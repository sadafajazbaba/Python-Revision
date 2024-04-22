marks = [1,2,3,4,5,6]
print(marks[2])
movie1 = input("Enter your first favourite movie")
movie2 = input("Enter your second favourite movie")
movie3 = input("Enter your third favourite movie")
list=[]
list.append(movie1)
list.append(movie2)
list.append(movie3)
print(list)
list1 = [1,2,3,2,1]
list1copy = list1.copy()
list1copy.reverse()
if list1 == list1copy:
    print("palindrome")
else:
    print("not a palindrome")
tup =("c","d","a","a","b","b","a")
print(tup.count("a"))
tup.sort()

