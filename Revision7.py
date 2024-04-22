
# f = open("myfile2.txt", "r")
# data = f.read()
# # # print(data)
# # # print(type(data))
# # # # f.close()
# # # line1 = f.readline()
# # # print(line1)
# # f.write("\nI have to finish learning python soon")
# # with open("myfile2.txt","r") as f:
# #     data = f.read()
# #     print(data)
# # import os
# # os.remove("myfile.txt")
# new = data.replace("Sadaf","Basrah")
# print(new)
# f = open("myfile2.txt", "w")
# f.write(new)
word = "Basrah"
with open("myfile2.txt","r") as f:
    data = f.read()
    if(data.find(word) == 1):
        print("Found")
    else:
        print("Not found")
    

    


