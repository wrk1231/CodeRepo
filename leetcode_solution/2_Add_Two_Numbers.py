# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        returnResult = result = ListNode(0); ## Actually we return 'returnResult' rather than result. it is a copy.
        ifBiggerThanTen = 0;
        ## the first element:
    	currentSum = l1.val + l2.val;

    	if(currentSum < 10):
    		ifBiggerThanTen = 0;
    		result.next = ListNode(currentSum);
    		result = result.next;
    	
    	else:
    		ifBiggerThanTen = 1;
    		result.next = ListNode(currentSum -10);
    		result = result.next;
    
        while (l1.next != None and l2.next != None):
        	l1 = l1.next;
        	l2 = l2.next;
        	currentSum = l1.val + l2.val + ifBiggerThanTen;
        	if(currentSum < 10):
	    		result.next = ListNode(currentSum);
	    		result = result.next;
        		ifBiggerThanTen = 0;
        	else:
	    		result.next = ListNode(currentSum -10);
	    		result = result.next;
        		ifBiggerThanTen = 1;
        if(l2.next == None and l1.next!= None):
        	l1 = l1.next;
        	while(l1 != None):
        		newSum = l1.val + ifBiggerThanTen;
        		if(newSum < 10):
		    		result.next = ListNode(newSum);
		    		result = result.next;
        			ifBiggerThanTen = 0;
        		
        		else:
		    		result.next = ListNode(newSum - 10);
		    		result = result.next;
        			ifBiggerThanTen = 1;
        		l1 = l1.next;
        
        	if(ifBiggerThanTen == 1):
        		result.next = ListNode(1);
        		result = result.next;
        elif(l1.next == None and l2.next!= None):
        	l2 = l2.next;
        	while(l2 != None):
        		newSum = l2.val + ifBiggerThanTen;
        		if(newSum < 10):
		    		result.next = ListNode(newSum);
		    		result = result.next;
        			ifBiggerThanTen = 0;
        		else:
		    		result.next = ListNode(newSum - 10);
		    		result = result.next;
        			ifBiggerThanTen = 1;
        		l2 = l2.next;
        	if(ifBiggerThanTen == 1):
	    		result.next = ListNode(1);
	    		result = result.next;   
        elif(l1.next == None and l2.next == None):        	
        	if(ifBiggerThanTen):
        		result.next = ListNode(1);
	    		result = result.next;
    	return returnResult.next;
        	
       

