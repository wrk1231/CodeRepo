/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	ListNode result = new ListNode(0);
    	ListNode returnResult = result;

    	int ifBiggerThanTen = 0;
    	int currentSum = l1.val + l2.val;
    	int newSum = 0;
    	
    	if(currentSum <10){
    		ifBiggerThanTen = 0;
    		result.next = new ListNode(currentSum);
    		result = result.next;
    	}else{
    		ifBiggerThanTen = 1;
    		result.next = new ListNode(currentSum -10);
    		result = result.next;
    	}

    	while(l1.next != null && l2.next != null){
    		l1 = l1.next;
    		l2 = l2.next;
    		currentSum = l1.val + l2.val + ifBiggerThanTen;
    		if(currentSum < 10){
    			result.next = new ListNode(currentSum);
    			result = result.next;
    			ifBiggerThanTen = 0;
    		}else{
    			result.next = new ListNode(currentSum -10);
    			result = result.next;
    			ifBiggerThanTen = 1;
    		}
    	}
    	if(l2.next == null || l1.next!= null){
    		l1 = l1.next;
        	while(l1 != null){
        		newSum = l1.val + ifBiggerThanTen;
        		if(newSum < 10){
        			result.next = new ListNode(newSum);
		    		result = result.next;
        			ifBiggerThanTen = 0;
        		}else{
        			result.next = new ListNode(newSum - 10);
		    		result = result.next;
        			ifBiggerThanTen = 1;

        		}
		    		
        		l1 = l1.next;

        	}
        		
        
        	if(ifBiggerThanTen == 1){
        		result.next = new ListNode(1);
        		result = result.next;
        	}
        		

    	}
        	
        else if(l1.next == null || l2.next!= null){
        	l2 = l2.next;
        	while(l2 != null){
        		newSum = l2.val + ifBiggerThanTen;
        		if(newSum < 10){
        			result.next = new ListNode(newSum);
		    		result = result.next;
        			ifBiggerThanTen = 0;

        		}else{
        			result.next = new ListNode(newSum - 10);
		    		result = result.next;
        			ifBiggerThanTen = 1;

        		}
        		l2 = l2.next;

        	}
        		

        	if(ifBiggerThanTen == 1){
        		result.next = new ListNode(1);
	    		result = result.next;   

        	}

        }
        	
	    		
        else if(l1.next == null || l2.next == null){
        	if(ifBiggerThanTen){
	       		result.next = new ListNode(1);
	    		result = result.next;

        	}
 

        }       	
        	
    	return returnResult.next;

        
    }
}