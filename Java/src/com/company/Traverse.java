package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class Traverse {
    public static void main(String[] args)
    {
        ArrayList nums = new ArrayList(Arrays.asList("1","2","3","4","5"));
        Iterator it = nums.iterator();
        while (it.hasNext())
        {
        String num = (String)it.next();
        System.out.println(num);
        if (num.equals("5")){
            it.remove();
        }
        num = "测试字符串";
    }
        System.out.println(nums);
    }
}
