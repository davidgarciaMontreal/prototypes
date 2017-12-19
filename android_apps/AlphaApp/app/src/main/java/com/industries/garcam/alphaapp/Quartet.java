package com.industries.garcam.alphaapp;


import android.util.Pair;

public class Quartet {
    private Pair<String,String > low;
    private Pair<String,Integer> high;

    public Quartet(String theContentTitle, String theContentText, String theTicker,
                   int theSmallIcon) {
        low = new Pair<>(theContentTitle, theContentText);
        high = new Pair<>(theTicker, theSmallIcon);
    }

    public String getContentTitle(){
        return low.first;
    }

    public String getContextText(){
        return low.second;
    }

    public String getTicker() {
        return high.first;
    }

    public int getSmallIcon() {
        return high.second;
    }
}
