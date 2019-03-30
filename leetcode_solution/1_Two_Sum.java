import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


class Solution {
    public int[] twoSum(int[] nums, int target) {

    	Map<Integer,Integer> dictionary = new HashMap<Integer,Integer>();

    	int residual;
    	int [] resultArray = new int[2];
    	for(int index = 0; index < nums.length; index++){
    		
    		List<Integer> keys = new ArrayList<Integer>(dictionary.keySet());

    		if(keys.contains(nums[index])){
    			resultArray[0] = dictionary.get(nums[index]);
    			resultArray[1] = index;
    			break;
    			
    		}else{
    			residual = target - nums[index];
    			dictionary.put(residual,index);

    			}
    		}

        return resultArray;
    }
}