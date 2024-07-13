import sys

def read_fasta(filename):
    #print filename
    print(filename)
    #print file content
    try:
        with open(filename, 'r') as file:
            contents = file.read()

    #error handling
    except FileNotFoundError:
        print(f"File {filename} not found.")
    
    totalCount=0
    countG=0
    countC=0
    
    
    for i in contents:
        totalCount+=1
        if (i == 'G'):
            countG+=1
        elif (i == 'C'):
            countC+=1


    print(totalCount)
    print(countC)
    print(countG)
    percentageC = countC/totalCount
    percentageG = countG/totalCount
    print(percentageC)
    print(percentageG)


    
    
#main
if __name__ == '__main__':
    arguments = sys.argv[1:]
    filename = arguments[0]
    
    read_fasta(filename)