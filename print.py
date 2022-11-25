from art import *

def printOnStart():
    # print(text2art("scrapeBot", font="small"))
    # tprint(f"N1","twisted")
    try:
        tprint("scrapeBot V1.0", font="small")

        # tprint("test","rnd-xlarge")
        
        print('DRIVES'.center(63))

    except artError:
        print("scrapeBot V1.0")
        print('DRIVES')




def printDrive(drives):
    for i in drives:
        print(f"{drives.index(i)+1} - {i}")




def printOptions(ext,destPath):
    print('OPTIONS'.center(63))
    print(f"1 - log {ext} files")
    print(f"2 - copy {ext} files to {destPath}")






def printPlaceHolder():
    print("scrapeBot->", end=" ")


    

    


