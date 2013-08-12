#!/usr/bin/perl

use strict;
use warnings;
use CGI;

my $form = new CGI;
my $status = $form->param('code');
$status = 404 unless ($status =~ m/^[0-9]{3}$/);

# see http://www.ietf.org/rfc/rfc2616.txt
# WEBDAV http://www.ietf.org/rfc/rfc2518.txt
# WEBDAV(2) http://www.ietf.org/rfc/rfc4918.txt
# WebDAV(3) http://www.ietf.org/rfc/rfc5842.txt
# RFC 3229  http://www.ietf.org/rfc/rfc3229.txt
# RFC 2817 http://www.ietf.org/rfc/rfc2817.txt
# RFC 2295 http://www.ietf.org/rfc/rfc2295.txt
# RFC 2774 http://www.ietf.org/rfc/rfc2774.txt
# RFC 2324 http://www.ietf.org/rfc/rfc2324.txt

my %ST_STRING = (
  "100" => "Continue",
  "101" => "Switching Protocols",
  "102" => "Processing",  #webdav, rfc2518.txt
  "200" => "OK",
  "201" => "Created",
  "202" => "Accepted",
  "203" => "Non-Authoritative Information",
  "204" => "No Content",
  "205" => "Reset Content",
  "206" => "Partial Content",
  "207" => "Multi-Status", #webdav, RFC 4918
  "208" => "Already Reported", #webdav, RFC 5842
  "226" => "IM Used", # Delta encoding in HTTP RFC 3229 
  "300" => "Multiple Choices",
  "301" => "Moved Permanently",
  "302" => "Found",
  "303" => "See Other",
  "304" => "Not Modified",
  "305" => "Use Proxy",
  "306" => "Switch Proxy",  # unused
  "307" => "Temporary Redirect",
  "308" => "Permanent Redirect", #draft, http://datatracker.ietf.org/doc/draft-reschke-http-status-308/
  "400" => "Bad Request",
  "401" => "Unauthorized",
  "402" => "Payment Required",
  "403" => "Forbidden",
  "404" => "Not Found",
  "405" => "Method Not Allowed",
  "406" => "Not Acceptable",
  "407" => "Proxy Authentication Required",
  "408" => "Request Timeout",
  "409" => "Conflict",
  "410" => "Gone",
  "411" => "Length Required",
  "412" => "Precondition Failed",
  "413" => "Request Entity Too Large",
  "414" => "Request-URI Too Long",
  "415" => "Unsupported Media Type",
  "416" => "Requested Range Not Satisfiable",
  "417" => "Expectation Failed",
  "418" => "I'm a teapot", # RFC2324
  "422" => "Unprocessable Entity", #webdav, RFC 4918
  "423" => "Locked", #webdav, RFC 4918
  "424" => "Failed Dependency", #webdav, RFC 4918
  "426" => "Upgrade Required", #RFC 2817 
  "428" => "Precondition Required", #draft, http://tools.ietf.org/html/draft-nottingham-http-new-status-04
  "429" => "Too Many Requests", #draft, http://tools.ietf.org/html/draft-nottingham-http-new-status-04
  "431" => "Request Header Fields Too Large", #draft, http://tools.ietf.org/html/draft-nottingham-http-new-status-04
  "500" => "Internal Server Error",
  "501" => "Not Implemented",
  "502" => "Bad Gateway",
  "503" => "Service Unavailable",
  "504" => "Gateway Timeout",
  "505" => "HTTP Version Not Supported",
  "506" => "Variant Also Negotiates", # RFC 2295
  "507" => "Insufficient Storage", #RFC 4918
  "508" => "Loop Detected", #Webdav, RFC 5842
  "510" => "Not Extended", #RFC 2774
  "511" => "Network Authentication Required", #draft, http://tools.ietf.org/html/draft-nottingham-http-new-status-04
);

my $ret_status;
if (exists $ST_STRING{$status}) {
  $ret_status = "$status $ST_STRING{$status}";
} else {
  $ret_status = "404 Not Found";
}

if (($status ne "304") && ($status =~ m/^3/)) {
  print $form->header(-type=>'text/html', -charset=>'utf-8', -status=>$ret_status, -location=>"http://ozuma.sakura.ne.jp/httpstatus/");
} else {
  print $form->header(-type=>'text/html', -charset=>'utf-8', -status=>$ret_status);
}


