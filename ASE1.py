import numpy as np
import random
import copy
import time

small_table_size = 7
table_size = 400
table_size = 5000
min_number = 0
max_number = 9
small_table = [random.randint(min_number,max_number) for element in range(small_table_size)]
table = [random.randint(min_number,max_number) for element in range(table_size)]

table_used = table

def bubblesort(table):
    print('Before bubblesort', table)

    switch = True

    while(switch):
        table, switch = compare_for_whole_table(table)
        #print(table)
    print('After bubblesort: ',table)

def compare_for_whole_table(table):
    number_of_comparisons = len(table) - 1
    number_of_last = len(table) - 1
    switched = False
    for i in range(number_of_comparisons):
        table[number_of_last - i - 1], table[number_of_last - i], switched_now = compare(table[number_of_last - i -1],table[number_of_last - i])
        if(switched_now):
            switched = True

    return table, switched

def compare(almost_last,last):
    switched = False
    if (almost_last>last):
        switched = True
        return last, almost_last, switched
    return almost_last, last, switched

start = time.time()
bubblesort(copy.copy(table_used))
end = time.time()
print('Bubble sort time: ',end - start)

def selection_sort(table):
    print('Before selection sort: ',table)
    number_of_possible_switches = len(table) - 2
    for start_index in range(number_of_possible_switches):
        table = switch_if_smaller(table,start_index)
        #print(table)
    print('After selection sort: ',table)

def switch_if_smaller(table,start_index):
    checked_table = table[start_index:len(table)]
    smallest_element = min(checked_table)
    index_of_smallest_element = start_index + checked_table.index(min(checked_table))
    smaller = False
    if(table[start_index]>smallest_element):
        table[index_of_smallest_element] = table[start_index]
        table[start_index] = smallest_element
    return table

start = time.time()
selection_sort(copy.copy(table_used))
end = time.time()
print('Selection sort time: ',end - start)

def quick_sort(table):
    quicksort(table,0,len(table)-1)

def quicksort(table, lower_pointer, higher_pointer):
    if(lower_pointer<higher_pointer): #if we have more than 1 item to be sorted

        pivot_index = (lower_pointer+higher_pointer)//2
        pivot_value = table[pivot_index]
        swap(table, pivot_index, lower_pointer)
        border_pointer = lower_pointer

        for index_checked in range(lower_pointer,higher_pointer):
            if(table[index_checked]<pivot_value):
                border_pointer += 1
                swap(table,index_checked,border_pointer)
        swap(table,border_pointer,lower_pointer)

        new_border = border_pointer

        quicksort(table,lower_pointer,new_border-1)
        quicksort(table, new_border+1,higher_pointer)

def swap(table,index1,index2):
    table[index1], table[index2] = table[index2],table[index1]

print('Before quicksort: ',table_used)
mycopy = copy.copy(table_used)
start = time.time()
quick_sort(mycopy)
end = time.time()
print('After quicksort: ',mycopy)
print('Quick sort time: ',end - start)


