package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
//list增删改查遍历排序截取
public class ListTest {
    public static void main(String[] args) {
        List list1 = new ArrayList(Arrays.asList(1, 2, 3, 4, 5));
        list1.add(12);
        list1.remove(4);
        list1.set(0, 6);
        System.out.println(list1.get(0));
        for (Object e: list1)
            System.out.println(e);
        System.out.println(list1.subList(0,3));
        //System.out.println(list1.sort());
    }
}
