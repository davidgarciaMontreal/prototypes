package com.prototypes.httpclient;

import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;

public class CliParserFactory {
    public static Options getOptions() {
        Options options = new Options();
        options.addOption( "a", "all", false, "do not hide entries starting with ." );
        options.addOption( "h", "help", false, "disply this help menu" );
        options.addOption(Option.builder().longOpt( "block-size" )
                .desc( "use SIZE-byte blocks" )
                .hasArg()
                .argName("SIZE")
                .build() );
        return options;
    }
}
