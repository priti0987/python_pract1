# list1 = ['india', 'is', 'my', 'country']
# duppli = []
# str = ' '.join(list1)
# for i in str:
#     if str.count(i) > 1 and i not in duppli:
#         duppli.append(i)
#
# print(duppli)
# print(str)
# print(*list1)
#
# print([word for word in list1 if word.startswith("i")])
#
# print("ok".isalpha())
# print("12".isupper())
#
#
#
# sttt= "india"
#
# revs=""
# for i in sttt:
#     revs =  i+ revs
#
# print(revs)
#
# list123 = [2,33,123,54,6]
# print(sorted(list123))
#
#
# m="my name is priti and bhavika is my daughter"
#
# print(len(set(m)))
#
#
# t1=('r',6,4,66)
# t2=('p',43,23)
# print(t1+t2)
#
# text = "I'm gonna make him an offer he can't refuse"
# words = text.split()
# leng= list(map(lambda word : len(word),words))
# print(leng)


class A:
    def a(self):
        print("a")


class B:
    def a(self):
        print('b')

class C(B,A):
    def a(self):
        self.a()


o = C()
o.c()
