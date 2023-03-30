# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
            
        if list1 and list2:
            array = []
            while list1 != None:
                
                array.append(list1.val)
                list1 = list1.next

            while list2 != None:
                array.append(list2.val)
                list2 = list2.next

            array.sort()
            
            output = ListNode(array[0])
            temp = output 
            for i in range(1,len(array)):
                output.next = ListNode(array[i])
                output= output.next
            return temp
            
