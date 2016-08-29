# reversereport-py

Simple Python 2.7 script that scrapes https://reverse.report for Reverse DNS entries. Currently, only the first page of results are displayed.


# Required Libraries

re 

sys

urllib2

BeautifulSoup


# How-To

Domain Name Lookup:

    tor1-01:~$ python reversereport.py google.com

IP Address Lookup:

    tor1-01:~$ python reversereport.py 1.1.1.1


# Caveats

This script does basic validation of input. For example, TLD's are not verified before they are submitted to https://reverse.report.

At the time this script was written, no AUP, EULA, or restrictions of use were posted on https://reverse.report preventing the use or creation of this script.
