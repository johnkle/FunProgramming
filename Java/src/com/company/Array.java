package com.company;

import java.util.Arrays;

public class Array {
    public static void main(String[] args){
        int[] arr1 = new int[]{2,1,3};
        int[] arr2 = new int[3];
        for(int i = 0;i<arr1.length;i++)
            arr2[i] = arr1[i];
        //System.out.println(arr2[0]==arr1[0]);
        //System.out.println(Arrays.equals(arr1,arr2));

//        for(int e:arr2)
//            System.out.println(e);

        int[] arr3 = new int[3];
        Arrays.fill(arr3,-1);
//        System.out.println(arr3[0]);
//        Arrays.sort(arr2);
//        for(int e: arr2)
//            System.out.println(e);
//        System.out.println(Arrays.toString(arr2));

        int[][] arr4 = new int[3][];
        arr4[0] = arr3;
        for(int i =0; i<3; i++)
            System.out.println(arr4[0][i]);


    }
}
