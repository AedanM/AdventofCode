import argparse
import numpy as np
def getBounds(line):
    line = line.replace('through',',').replace(' ','')
    lineArr = [int(x) for x in line.split(',')]
   
    return ((lineArr[0],lineArr[1]),(lineArr[2],lineArr[3]))

def TurnOn(line,mArr):
    bounds = getBounds(line.replace('turn on',''))
    for i in range(bounds[0][1], bounds[1][1]+1):
        for j in range(bounds[0][0], bounds[1][0]+1):
            mArr[j][i] = 1
            
def TurnOff(line,mArr):
    bounds = getBounds(line.replace('turn off',''))
    for i in range(bounds[0][1], bounds[1][1]+1):
        for j in range(bounds[0][0], bounds[1][0]+1):
            mArr[j][i] = 0
            
def Toggle(line,mArr):
    bounds = getBounds(line.replace('toggle',''))
    for i in range(bounds[0][1], bounds[1][1]+1):
        for j in range(bounds[0][0], bounds[1][0]+1):
            mArr[j][i] =  0 if mArr[j][i] else 1
    
def TurnOn2(line,mArr):
    bounds = getBounds(line.replace('turn on',''))
    for i in range(bounds[0][1], bounds[1][1]+1):
        for j in range(bounds[0][0], bounds[1][0]+1):
            mArr[j][i] += 1
            
def TurnOff2(line,mArr):
    bounds = getBounds(line.replace('turn off',''))
    for i in range(bounds[0][1], bounds[1][1]+1):
        for j in range(bounds[0][0], bounds[1][0]+1):
            mArr[j][i] -= 1
            if(mArr[j][i] < 0):
                mArr[j][i] = 0
            
def Toggle2(line,mArr):
    bounds = getBounds(line.replace('toggle',''))
    for i in range(bounds[0][1], bounds[1][1]+1):
        for j in range(bounds[0][0], bounds[1][0]+1):
            mArr[j][i] += 2
        
def main(filePath):
    masterArr = np.zeros((1000,1000))
    masterArr2 = np.zeros((1000,1000))
    runningCount = 0
    runningCount2 = 0
    with open(filePath, "r") as fp:
        for line in fp:
            if('on' in line):
                TurnOn(line,masterArr)
            elif('off' in line):
                TurnOff(line,masterArr)
            elif('toggle' in line):
                Toggle(line,masterArr)
            if('on' in line):
                TurnOn2(line,masterArr2)
            elif('off' in line):
                TurnOff2(line,masterArr2)
            elif('toggle' in line):
                Toggle2(line,masterArr2)
    for j in masterArr:
        for i in j:
            print(i,end = '')
            if(i):
                
                runningCount += 1
        print('')
    print('')
    print('')
    
    for j in masterArr2:
        for i in j:
            print(i, end = '')
            if(i):
                
                runningCount2 += i
        print('')
        
    print(runningCount)
    print(runningCount2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AOC Day6")
    parser.add_argument("-f", "--file", required="True")
    args = parser.parse_args()
    main(args.file)
