class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rHead = ListNode(0)
                
        carry =0
        
        
        if l1 == None:
            currX=0
        else:
            currX=l1.val
        
        if l2 == None:
            currY=0
        else:
            currY=l2.val
        
        if(currX+currY+carry>=10):
            rHead = ListNode(currX+currY-10)
            carry=1
        else:
            rHead = ListNode(currX+currY)
            
        currHead = rHead
            
        while(l1.next != None or l2.next!=None):
            
            
            if l1.next == None:
                currX=0
            else:
                l1=l1.next
                currX=l1.val

            if l2.next == None:
                currY=0
            else:
                l2=l2.next
                currY=l2.val

            if(currX+currY+carry>=10):
                currHead.next = ListNode(currX+currY+carry-10)
                carry=1
            else:
                currHead.next = ListNode(currX+currY+carry)
                carry=0
            currHead = currHead.next
            
        if carry>0:
            currHead.next = ListNode(carry)
        

        
        
        return rHead