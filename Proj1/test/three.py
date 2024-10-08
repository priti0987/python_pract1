# # mylist= [2,5,1,8,7]
# # mylist1=[3,9,1,5,6]
# #
# #
# # def maxProfit(list):
# #     profit = 0
# #     maxP = 0
# #     for i in range(len(mylist1)-1):
# #         if mylist1[i]>mylist1[i+1]:
# #             profit = (mylist1[i] - mylist1[i+1])
# #         else:
# #             profit = (mylist1[i+1] - mylist1[i])
# #
# #
# #     return maxP
# #     pass
# #
# # print(maxProfit(mylist1))
# # # print(mylist1[1])
# #
#
#
#
# str1 ="Alice was beginning to get very bored. She and her sister were sitting under the trees. Her sister was reading, but Alice had nothing to do. Once or twice she looked into her sister's room to check out what she was doing."
#
# #16, Alice was
# #len1 = len(str1)
# def printmystring(len1,str1):
#     newString = ""
#     for i in range(len1):
#         if str1[i] != " ":
#             newString = newString + str1[i]
#     return print(newString)
#
#
# printmystring(16,str1)

mylist =[5,2,7,8,9,3,6,18,19,20,21,22,45,24,27,56,57,59,58]
print(len(mylist))
newlist = []
list1=[]
for i in range(len(mylist)-1):
    if (mylist[i+1]-mylist[i]==1) :
        list1.append(mylist[i])
        print(list1)


