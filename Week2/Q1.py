class Week2:
    def fullname(fname,lname):
        return fname +" " + lname

    def string_alternative(fullname):
        names = fullname.split(" ")
        fname = names[0]
        lname = names[1]
        #print(fname[0:-1:2] )
        #print(lname[0:-1:2])
        return fname[0:-1:2] + " " + lname[0:-1:2]

if __name__ =="__main__":
    fname = input()
    lname = input()
    fullname = Week2.fullname(fname,lname)
    print(Week2.string_alternative(fullname))