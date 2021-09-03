package com.company;

import javax.rmi.CORBA.Util;

public class BinarySearch {
    private BinarySearch() {
    }

    public static int binarySearch(Comparable[] arr, int n, Comparable Target){
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid].compareTo(Target) == 0) return mid;
            if (arr[mid].compareTo(Target) < 0)
                l = mid + 1;
            else
                r = mid - 1;
        }
        return -1;
    }
}
