import glob, os

def batchSetter():
    batchPosition = int(input("Specify Batch position (start counting from 1, not 0): "))
    batchQuantity = int(input("Specify the number of unique Batches in File: "))
    dictionaryOfBatches= {}

    for i in range (0,batchQuantity):
        i_batchValue= int(input('Specify the value of Batch {}: '.format(i+1)))
        i_batchQuantity = int(input('Specify the quantity of lines to be updated with Batch {}: '.format(i+1)))
        dictionaryOfBatches[i_batchValue] = i_batchQuantity

    currentDirectory = os.getcwd()
    os.chdir(currentDirectory)

    startCounter = 0
    for fileTXT in glob.glob("*.txt"):
        headerFound = False
        with open(fileTXT, "r") as file:
            lineList = []
            count = sum(1 for _ in file)
            file.close()
            for key, value in dictionaryOfBatches.items():
                if os.path.isfile(fileTXT):
                    with open(fileTXT, "r+") as file1:
                        if (headerFound == False ):
                        #loop for Header finding
                            for j in range(0, count ):
                                lineHeader = next(file1).strip()
                                y = lineHeader.split(",", )
                                if len(y) > 3 :
                                    if headerFound == False:
                                        startCounter += 1
                                        headerFound = True
                                if (headerFound == False):
                                    startCounter += 1
                                lineList.append(','.join(y))
                        #loop for lines in file iteration
                        for k in range(startCounter + 1,startCounter + 1 + value):
                            x = lineList[k].split(",", )
                            if len(x) > 3 :
                                #batch position is decremented by 1 due to more understandable counting from 1 in user Input in line #5
                                x[batchPosition - 1] = str(key)
                                lineList[k] = ",".join(x)
                            else :
                                startCounter += 1
                        startCounter += value
                        file1.seek(0)
                        file1.write("\n".join(lineList))
                        file1.truncate()
batchSetter()