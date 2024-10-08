# #absolute value
#
# print(abs(-9))
# print(abs(-100.89))
#
#
# class immabs:
#     def __init__(self, string):
#         self.string = string
#
#     def __abs__(self):
#         return self.string.lower()
#
# o = immabs("HELLO")
# print(abs(immabs("HELLO")))


class myc:
    def __init__(self,x):
        self.x = x

c = myc(10)
print(hasattr(c,"x"))