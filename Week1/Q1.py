
class Week1:
    def delRev(str):
        delStr = str[:-2]
        print(delStr[::-1])

    def arithOper(a,b):
        print("Sum : {}".format(a+b))
        print("Difference : {}" .format(a-b))
        print("Multiple : {}".format(a*b))
        print("Factor : {} ".format(a/b))
if __name__ =="__main__":
    str = input()
    Week1.delRev(str)
    a= int(input())
    b=int(input())
    Week1.arithOper(a,b)