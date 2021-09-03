package com.company;

public class MoveZeros2 {
    public void moveZeros(int[] nums){
        int k = 0;
        for (int i=0; i<nums.length; i++)
            if (nums[i] != 0)
                nums[k++] = nums[i];

        for (int i=k; i<nums.length; i++)
            nums[i] = 0;
    }

    public static void main(String args[]){
        int[] arr = {0,1,0,6,12};
        (new MoveZeros()).moveZeros(arr);
        for (int i=0; i<arr.length; i++)
            System.out.println(arr[i]+"");
    }
}
