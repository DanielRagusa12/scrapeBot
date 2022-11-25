import os
import shutil
import time
import win32api
from print import *

log = open("log.txt","w+")

def searchFiles(dir, ext):

    counter = 0
    for root, dirs, files in os.walk(dir):
        for file in files:

            try:
                foundPath = os.path.join(root, file)

                # Get the path to the file
                if file.endswith(ext):

                    counter+=1
                    
                    print(f"Found : {foundPath}")
                    log.write(foundPath + "\n")
            except PermissionError:

                    print("Permission denied")

            except OSError:

                print("OS error")

            except UnicodeEncodeError:

                print("Unicode error")

            except UnicodeDecodeError:

                print("Unicode error")

            

    return counter


def copyFiles(dir, ext):


    # Get the path to current directory
    curDir = os.getcwd()

    # Get the path to the destination directory
    destPath = os.path.join(curDir, "scraped")

    extPath = os.path.join(destPath, ext[1:])
                
    # Create the directory if it doesn't exist
    if os.path.exists(destPath) == False:
        os.mkdir(destPath)

    if os.path.exists(extPath) == False:
        os.mkdir(extPath)

    
    counter = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext) and os.path.exists(os.path.join(extPath, file)) == False:
                try:
                    counter +=1
                    foundPath = os.path.join(root, file)
                    # print(foundPath)
                    shutil.copyfile(foundPath,f"{extPath}\\{file}")
                    print(f"Copied From : {foundPath}")
            
                except shutil.SameFileError:

                    print("File already exists")

                except PermissionError:

                    print("Permission denied")

                except OSError:

                    print("OS error")

                except UnicodeEncodeError:

                    print("Unicode error")

                except UnicodeDecodeError:

                    print("Unicode error")
                

    return counter


    

def main():


    printOnStart()

    while(True):

        copyMode = False

        # Get list of drives
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]

        # Print list of drives
        printDrive(drives)
        printPlaceHolder()


        # User chooses drive
        try:
            choice = int(input())-1

            if  choice > len(drives):
                print("Invalid drive")
                continue
        except ValueError:
            print("Invalid drive")
            continue
        
        # Get the path to the chosen drive
        dir = (drives[choice])


        # Print options
        print(dir.center(63))

        print("enter extension .ext")
        printPlaceHolder()


        # Get the choice of extension
        ext = input()


        # Path of copied files
        destPath = f"{os.getcwd()}\scraped\{ext.lstrip('.')}"

        # Print options
        printOptions(ext,destPath)
        # Print placeholder
        printPlaceHolder()

        # Validate user input
        try:
            choice = int(input())

            if choice == 2:
                copyMode = True

            if choice != 1 and choice != 2:
                print("Invalid choice")
                continue
                

        except ValueError:
            print("Invalid choice")
            continue

        
        start_time = time.time()

        #  Log files
        if copyMode == False:
            count = searchFiles(dir,ext)
            searchElapsed = round(time.time()-start_time, 2)
            print(f"\nFound {count} {ext} files in {searchElapsed} seconds")


        #  Copy files
        else:
            count = copyFiles(dir, ext)
            print(f"Copied {count} {ext} files to {destPath}")

        
        searchElapsed = round(time.time()-start_time, 2)

        print(f"Process took {searchElapsed} seconds")




        


        # Print options
        print(f"\n1: Continue\n2: Exit")
        print("scrapeBot->", end=" ")
        choice = int(input())
        if choice == 2:
            break


    log.close()





if __name__ == "__main__":
    main()