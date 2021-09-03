package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class SetLearn {
    public static void main(String[] args){
        List list1 = new ArrayList(Arrays.asList(1,2,3,4,5));
        HashSet set1 = new HashSet();
        for (Object num : list1)
            set1.add(num);
        set1.add('a');
        set1.add('b');
        System.out.println(set1);
    }
}
