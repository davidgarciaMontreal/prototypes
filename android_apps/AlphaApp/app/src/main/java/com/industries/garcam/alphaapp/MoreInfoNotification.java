package com.industries.garcam.alphaapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class MoreInfoNotification extends AppCompatActivity {
    private int cnt;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        TextView mTextView = (TextView) findViewById(R.id.textView);
        mTextView.setText("Hello Tutty. Me voy!!!! " + cnt);
        cnt += 1;
    }

}
