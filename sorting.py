import time
import math

def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array





