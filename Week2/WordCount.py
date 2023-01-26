import json


class wordcount:
    def count(lines):
        map = {}
        outfile = open("output.txt","w")
        for line in lines:
            outfile.write(line.strip() + "\n")
            for word in line.split():
                if word not in map:
                    map[word] = 1
                else:
                    map[word] +=1
        outfile.write("Word_Count: \n")
        for k,v in map.items():
            outfile.write(k + " : " + str(v)+"\n")
        outfile.close()
if __name__ =="__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    f.close()
    wordcount.count(lines)