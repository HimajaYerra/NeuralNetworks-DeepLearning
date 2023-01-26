class inchtocm:
    def loopmethod(lst):
        newlist = [1] * len(lst)
        for i in range(len(lst)):
            newlist[i] = lst[i]*2.54
        print(newlist)
    def lstcompmethod(lst):
        newlist = [x*2.54 for x in lst]
        print(newlist)


if __name__ =="__main__":
    total = int(input("Enter total no of heights: "))
    lst = []
    print("Enter heights in inches:")
    for i in range(total):
        lst.append(float(input()))
    inchtocm.loopmethod(lst)
    inchtocm.lstcompmethod(lst)