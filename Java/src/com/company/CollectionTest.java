package com.company;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;

public class CollectionTest {
    public static void main(String[] args){
        Collection c = new ArrayList();
        c.add("孙悟空");
        c.add(6);
        System.out.println(c);
        c.remove(6);
        System.out.println(c);
        System.out.println(c.contains(6));
        System.out.println(c.size());

        Collection books = new HashSet();
        books.add("a");
        books.add("b");
        books.add("b");
        books.add("c");
        books.remove("a");
        System.out.println(books);
        for (Object book: books){
            if (book.equals("b")){
                System.out.println(book);
            }

        }
        books.forEach(obj -> System.out.println(obj));
    }
}
