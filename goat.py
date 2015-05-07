from random import shuffle
def main():
    switch = 0.0
    no_switch = 0.0
    for n in range(10000001):
        #choose 1 door, open 1 of the 2 doors that contain goat, switch or no switch
        #1 is car, 2 are goats
        arr = [1, 2, 2]
        
        shuffle(arr)
        
        #assume you always choose the left most door
        if arr[1] == 2:
            arr.pop(1)
        else:
            arr.pop(2)

        if 0 == arr.index(1):
            no_switch += 1
        else:
            switch += 1

        if (n) % 100 == 0 and n != 0:
            print "After %d passes: " % n
            print "Switch Success: %.2f%%"  % (switch/n * 100)
            print "No switch Success: %.2f%%" % (no_switch/n * 100)
            print "\n"

if __name__ == "__main__": main()
