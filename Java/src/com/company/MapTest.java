package com.company;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class MapTest {
    public static void main(String[] args){
        Map map = new HashMap();
        map.put("a",1);
        map.put("b",2);
        map.put("c",3);
        System.out.println(map);
        map.remove("a");
        map.put("c",5);
        System.out.println(map.get("c"));
        System.out.println(map.containsKey("a"));
        for (Object key:map.keySet())
            System.out.println(key+":"+map.get(key));
        System.out.println(map.keySet());
    }
}
