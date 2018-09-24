#!/usr/bin/perl
use strict;
use warnings;
use LWP;

my $ua = LWP::UserAgent->new;

open LOG , ">download_log.txt" or die $!;
######## make sure the file with the ids/urls is in the
######## same folder as the perl script
open DLIST, "downloadlist.txt" or die $!;
my @file = <dlist>;

foreach my $line (@file) {
    my ($nr, $get_file) = split /,/, $line;
    chomp $get_file;
    $get_file = "http://www.sec.gov/Archives/" . $get_file;
    if ($get_file =~ m/([0-9|-]+).txt/ ) {
        my $filename = $nr . ".txt";
        open OUT, ">$filename" or die $!;
        print "file $nr \n";
        my $response =$ua->get($get_file);
        if ($response->is_success) {
            print OUT $response->content;
            close OUT;
        } else {
            print LOG "Error in $filename - $nr \n" ;
        }
    }
}
#ignore the line below (inserted by Forum engine because it wants to 'close' a similar tag used to load the file)
</dlist>
