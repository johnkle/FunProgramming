package com.company;

import java.util.*;
//https://www.jianshu.com/p/2b113f487e5e
public class array1 {
    public static void main(String[] args){
        Integer [] arr1 = {2,1,3,4,5};
        Integer [] arr2 = Arrays.copyOf(arr1,5);
        List arr3 = new ArrayList(Arrays.asList(arr1));
        //List arr3 = new ArrayList();
        //arr3 = Arrays.asList(arr1);
        arr3.add(6);
        for (int i=0; i<arr3.size(); i++) {
            System.out.println(arr3.get(i));
        }
    }
}
