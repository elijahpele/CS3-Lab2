# CS2302
# Elijah Pele
# LAB 2
# Instructor: Diego Aguirre
# TA: Manoj Pravaka Saha
#
# The purpose of this program is to sort file containing 
# employee ID's using Bubble Sort or Merge Sort. Also, 
# this program will find and print any duplicate
# ID numbers found in the list.
#
# Date last modified 11-10-2018
class Node(object):
    val = -1
    next = None
    
    def __init__(self,val):
        self.val = val
        self.next = None
        self.seen = False
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, val):        
        temp = Node( val)
        if (self.head is None):
            self.head = temp
            return
        lastNode = self.head
        while (lastNode.next != None):
            lastNode = lastNode.next
        lastNode.next = temp
  
      
# This method contained in the class Linked List will implement Bubble Sort.    
def bubbleSort(head, count):
    while(count > 2):
        temp = head
        subcount = count
        while(subcount > 2):
            if(temp.val > temp.next.val):
                holder = temp.val
                temp.val = temp.next.val
                temp.next.val = holder
                
                temp = temp.next
                subcount-=1
            else:
                temp = temp.next
                subcount -= 1
        count -= 1
    while(temp.next is not None):
        if(temp.val == temp.next.val):           
            print(temp.val)
        temp = temp.next
    
   
# This method will implement Merge Sort on a given Linked List        
def mergeSort(head):
    if(head.val == -1):
        return
    if(head is None or head.next is None):
        return head
    list1, list2 = divideList(head)
    list1 = mergeSort(list1)
    list2 = mergeSort(list2)
    head = merge(list1, list2)
    return head


# Second auxiliary method to mergeSort   
def merge(l1, l2):  
    temp = None
    if(l1 is None):        
        return l2
    if(l2 is None):
         return l1
     
    if(l1.val <= l2.val):
        temp = l1
        temp.next = merge(l1.next, l2)
    else:
         temp = l2
         temp.next = merge(l1, l2.next)
    return temp


# Auxiliary method to mergeSort()
def divideList(head):
    slow = head
    fast = head
    if fast and fast.val != -1:
        fast = fast.next
    # 'fast' will traverse the list two nodes at time.
    # 'slow' will be at the middle of the list once fast.next is None
    while fast and fast.val != -1:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    # 'mid' will contain the second half of the list
    # 'head' will contain the first.
    mid = slow.next
    slow.next = None
    return head, mid


# Basic while-loop implementation to find duplicate ID's
def findDupsWithLoops(head): 
    item1 = head 
    while(item1.next != None):
        item2 = item1.next
        while(item2 != None):
            if(item1.val == item2.val):
                print(item1.val)
                break
        
            else:
                item2 = item2.next
        item1 = item1.next


# This method will find duplicate ID's by
# mapping the ID to the index in the boolean
# array. After iterating through all the ID's
# the array should be populated with a False, or True 
# statement at each inde. 
def findDupsWithBoolArray(head):
    boolArray = [False] *30
    temp = head
    while(temp.next != None):
        
        if(boolArray[temp.val] is False):
            boolArray[temp.val] = True
        
        elif(boolArray[temp.val] == True):
            temp.seen = True
        temp = temp.next
           
    temp = head
    print("\n")
    while(temp.next != None):
        if(temp.seen == True):
            print(temp.val)
        temp = temp.next
      
        
# Makes linked list.        
def makeBigList(file1, file2):        
    file_act = open(file1, "r")
    file_viv = open(file2, "r")
    list1 = LinkedList()

    temp = Node(None)
    list1.head = temp
    
    for line in file_act:
        if(line != None):
            temp.val = int(line)
            temp.next = Node(-1)
        temp = temp.next
    for line in file_viv:
        if(line != None):
            temp.val = int(line)
            temp.next = Node(-1)
        temp = temp.next
    
    return list1.head


# This method is necessary to use the Bubble Sort method.
def count(node):
    count = 0 
    temp = node
    while temp is not None:
        count += 1
        temp = temp.next
    return count


# This method is used to print the merge sort method to find duplicates.        
def print_merge_sort_dups(node):
    temp = node
    while(temp.next is not None):
        if(temp.val == temp.next.val):           
            print(temp.val)
        temp = temp.next


# The linked list is created then populated by the two .txt files below.
list1 = LinkedList()
list1.head = makeBigList("activision.txt", "vivendi.txt")
count = count(list1.head) #Needed for Bububle Sort


# The user's input is taken on which solution they would like performed.
user_input = input("How would you like to find duplicates? Press 1 if you would like to use solution 1, etc." +"\n")
if(int(user_input) == 1):
    print("\n")
    bubbleSort(list1.head, count)
if(int(user_input) == 2):
     print("\n")
     list1.head = mergeSort(list1.head)
     print_merge_sort_dups(list1.head)
if(int(user_input) == 3):
    print("\n")
    findDupsWithLoops(list1.head)
if(int(user_input) == 4):
    print("\n")
    findDupsWithBoolArray(list1.head)