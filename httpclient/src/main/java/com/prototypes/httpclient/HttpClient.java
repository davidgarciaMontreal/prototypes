package com.prototypes.httpclient;

import org.apache.commons.cli.*;

import java.util.Collections;
import java.util.List;

public class HttpClient {
    private static final int SUC_CODE = 0;
    private static final int FAIL_CODE = -1;
    public static void main(String[] args) throws Exception {

        Options opts = CliParserFactory.getOptions();
        CommandLineParser parser = new DefaultParser();
        List<String> myArgs = null;
        try {
            CommandLine line = parser.parse(opts, args);
            if ( line.hasOption("help")){
                HelpFormatter formatter = new HelpFormatter();
                formatter.printHelp( "httpClient", opts);
                System.exit(SUC_CODE);
            }
            myArgs = line.getArgList();
        } catch (ParseException exp) {
            System.out.println("Unexpected exception:" + exp.getMessage());
            System.exit(FAIL_CODE);
        }

        System.out.println("Init http client");
        for (String url : myArgs) {
            MyHttpClient cl = new MyHttpClient("https://www.google.com");
            String responseBody = cl.getBody();
            String header_stdout = String.join("", Collections.nCopies(100, "#"));
            System.out.println(header_stdout);
            System.out.println(responseBody);
        }

        System.exit(SUC_CODE);
    }
}
