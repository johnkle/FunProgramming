package com.company;

import java.util.ArrayList;

public class MoveZeros {
    public  void moveZeros(int[] nums){
        ArrayList<Integer> nonZeroElements = new ArrayList<Integer>();
        for (int i = 0; i<nums.length; i++)
            if(nums[i] !=0)
                nonZeroElements.add(nums[i]);

        for (int i=0;i<nonZeroElements.size(); i++)
            nums[i] = nonZeroElements.get(i);

        for (int i=nonZeroElements.size(); i<nums.length; i++)
            nums[i] = 0;
    }

    public static void main(String args[]){
        int[] arr = {0,1,0,3,12};
        (new MoveZeros()).moveZeros(arr);
        for (int i=0; i<arr.length; i++)
            System.out.println(arr[i]+"");
    }
}


