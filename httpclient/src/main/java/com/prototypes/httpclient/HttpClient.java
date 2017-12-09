package com.prototypes.httpclient;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
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
            MyHttpClient cl = new MyHttpClient(url);
            String responseBody = cl.getBody();
            String header_stdout = String.join("", Collections.nCopies(100, "#"));
            System.out.println(header_stdout);
            System.out.println(responseBody);
        }

        System.exit(SUC_CODE);
    }
}
