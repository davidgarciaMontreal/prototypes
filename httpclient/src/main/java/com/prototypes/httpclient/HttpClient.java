package com.prototypes.httpclient;

import java.util.Collections;

public class HttpClient {
    private static final int SUC_CODE = 0;

    public static void main(String[] args) throws Exception {

        System.out.println("Init http client");

        MyHttpClient cl = new MyHttpClient("https://www.google.com");
        String responseBody = cl.getBody();
        String header_stdout = String.join("", Collections.nCopies(100, "#"));
        System.out.println(header_stdout);
        System.out.println(responseBody);
        System.exit(SUC_CODE);
    }
}
