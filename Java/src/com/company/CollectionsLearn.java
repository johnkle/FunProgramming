package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class CollectionsLearn {
    public static void main(String[] args){
        ArrayList list = new ArrayList(Arrays.asList(1,2,3,4,5));
        ArrayList list1 = new ArrayList();
        ArrayList list2 = new ArrayList();
        Collections.shuffle(list);
        System.out.println(list);
        Collections.sort(list);
        System.out.println(list);
        Collections.reverse(list);
        System.out.println(list);
        Collections.swap(list,1,2);
        System.out.println(list);
        System.out.println(Collections.max(list));
        System.out.println(Collections.min(list));
        Collections.replaceAll(list,1,2);
        System.out.println(list);
    }
}
