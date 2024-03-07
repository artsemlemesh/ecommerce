# def findSmallest(arr):
#     smallest = arr[0]
#     smallestIndex = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallestIndex = i
#     return smallestIndex
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr) #finds the smallest element in the array and adds it to the new array
#         newArr.append(arr.pop(smallest))
#     return newArr
#
# s = selectionSort([3, 4, 1, 6, 3, 23, -4, -345, 3425323])
# print(s)

# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         print(x)
#         return x * fact(x-1)
#
#
# print(fact(8))

# def countNum(x):
#     if not x:
#         return 0
#     else:
#         return 1 + countNum(x[1:])
#
# print(countNum([4, 2, 4, 1]))



# def Max(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         # m = Max(arr[1:])
#         if Max(arr[1:]) > arr[0]:
#             return Max(arr[1:])
#         else:
#             return arr[0]
#
# print(Max([5, 2, 7, 5, 4, 10, -3, 100]))




# def bin_search(arr, item, low=0, high=None):
#     if high is None:
#         high = len(arr) - 1
#
#     if low > high:
#         return -1
#
#     mid = (low+high) // 2
#
#     if arr[mid] == item:
#         return mid
#     elif arr[mid] < item:
#         return bin_search(arr, item, mid+1, high)
#     else:
#         return bin_search(arr, item, low, mid-1)
#
#
#
# arr = [1, 3, 5, 7, 8]
# target = 5
# print(bin_search(arr, target))



# def quicksort(arr):
#     if len(arr)<2:
#         return arr
#     else:
#         pivot = arr[0]
#         low = [i for i in arr[1:] if i <= arr[0]]
#         high = [i for i in arr[1:] if i > arr[0]]
#         return quicksort(low) + [pivot] + quicksort(high)
#
# print(quicksort([3, 1, 6, 12, 69, -3, 34, 199, 9]))

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-2] == 'n'

from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph['you']
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False
search('mike')
























