import argparse
import os
import requests

def main(year,day):
    currentDir = os.getcwd()
    yearDir = os.path.join(currentDir, year)
    try:
        os.mkdir(year)
        print("Made Year Directory")
    except  FileExistsError: 
        print("Year Directory Already Exists")
        
    os.chdir(year)
    
    try:
        os.mkdir(f"Day {day}")
        print("Made Day Directory")
    except  FileExistsError: 
        print("Day Directory Already Exists")
        
    os.chdir(f"Day {day}")
    if(not os.path.exists(f"Day{day}.py")):
        with open(f"Day{day}.py",'w') as fp:
            with open(os.path.join(currentDir,"BoilerPlate.py"),'r') as bp:
                for line in bp:
                    fp.write(line.replace('XXX',day))
        print(f"Made Script for Day {day}")
    else:
        print("Python Script Already Exists")
        
    if(not os.path.exists(f"Day{day}.txt")):
        with open(f"Day{day}.txt",'w') as fp:
            print(f"Made Blank Puzzle Input for Day {day}")
    else:
        print("Blank Puzzle Input Already Exists")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Directory Creator")
    parser.add_argument("-y", "--Year", required="True")
    parser.add_argument("-d", "--Day", required="True")
    args = parser.parse_args()
    main(args.Year, args.Day)
