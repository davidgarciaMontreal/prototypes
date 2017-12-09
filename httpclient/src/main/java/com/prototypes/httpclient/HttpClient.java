package com.prototypes.httpclient;
import java.io.IOException;
import java.util.Collections;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class HttpClient {
    public static int SUC_CODE = 0;
    public final static void main(String[] args) throws Exception {
        System.out.println("Init http client");
        CloseableHttpClient httpclient = HttpClients.createDefault();
        try {
            HttpGet httpget = new HttpGet("https://www.google.com");
            System.out.println("Executing request " + httpget.getRequestLine());
            ResponseHandler<String> responseHandler = new ResponseHandler<String>() {

                @Override
                public String handleResponse(
                        final HttpResponse response) throws ClientProtocolException, IOException {
                    int status = response.getStatusLine().getStatusCode();
                    if (status >= 200 && status < 300) {
                        HttpEntity entity = response.getEntity();
                        return entity != null ? EntityUtils.toString(entity) : null;
                    } else {
                        throw new ClientProtocolException("Unexpected response status: " + status);
                    }
                }

            };
            String responseBody = httpclient.execute(httpget, responseHandler);
            String header_stdout = String.join("", Collections.nCopies(100, "#"));
            System.out.println(header_stdout);
            System.out.println(responseBody);
        } finally {
            httpclient.close();
        }
        System.exit(SUC_CODE);
    }
}
