#/****************************************************************/ 
# Program:  bubbleSort
# Version:  1.0
# Date:     05/14/2014
# Website:  http://www.HumairAhmed.com
#
# Lead Developer:   Humair Ahmed 
#
# Written for educational purposes. Program takes a list of numbers as arguments
# and sorts the list while displaying each iteration. Displays the final sorted list 
# at end and how long it took to sort in seconds.
#
#  
# License:
# 
# Open source software being distributed under GPL license. For more information see here:
# http://www.gnu.org/copyleft/gpl.html. 
# 
# Can edit and redistribute code as long as above reference of authorship is kept within the code.
#/****************************************************************/

import sys, time


#function takes unsorted list of numbers as arguments, does a bubble sort, and returns a sorted list
def bubbleSort(unsorted_list):
    global iterations #holds # of sort iterations
    list_size = len(unsorted_list)
    result = True
  
    nosort = 1  #as bubble sort progresses, less numbers to sort
    while result:
        result = False
        i=0
        while (i < list_size - nosort):
            if (unsorted_list[i] > unsorted_list[i + 1]):
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                result = True
            i += 1
            iterations += 1
            print("Sorting: ", unsorted_list)
        nosort += 1
    return unsorted_list #returns sorted list


#main function
def main():
    global iterations #holds # of sort iterations
    
    input_list=[]
    if (len(sys.argv) < 2):
        print("\nInput list items to sort as arguments.")
        print("\nEx: ./bubblesort.py <item1> [item2] [item3] ...")
        quit()
        
    #map function is used to convert each string item in the list to an int; a list of ints is stored in the 'input_list' variable   
    input_list = list(map(int, sys.argv[1:])) 
        
    iterations= 0
    time_started = time.time()
    sorted_list = bubbleSort(input_list)
    time_stopped = time.time()
    time_passed = time_stopped - time_started
    
    print("\nSorted after", iterations, "iterations.")
    print("Sorted:  ", sorted_list) 
    print("\nOverall Time:", time_passed, "seconds\n") 
    
 
#start of program - call main function   
main()