#!/usr/bin/env python
import re, sys
import urllib2
from BeautifulSoup import BeautifulSoup

def validateInput(sysinput):
    #sysinput = sys.argv
    argLen = len(sysinput)
    if argLen < 2:
        print("")
        sys.exit("Well that's embarrassing...You didn't specify any arguements.\n\nTry something like 'python reversedns.py google.com' or 'python reversedns.py 1.1.1.1'\n")
    else:
        arg1 = sysinput[1]
        argStr = str(sysinput)
        if argLen > 2:
            print("\n")
            print("----------------------------------------------------------------")
            print("")
            print("I see you have entered multiple queries: " + argStr )
            print("")
            print ("Only the first entry will be processed: " + arg1 )
            print("")
            print("----------------------------------------------------------------")
            print("\n")
        if (re.search(r'[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})', arg1, re.IGNORECASE)) or (re.search(r'[0-9]+(?:\.[0-9]+){3}', arg1)):
            main(arg1)
        else:
            print("")
            print("Your input of: " + arg1 + " was not recognized as a valid domain name or IP address.")
            print("")

def setURL(q):
    if re.search(r'[0-9]+(?:\.[0-9]+){3}', q):
        return "ip"
    else:
        return "name"

def openURL(searchType, input):
    url = "https://reverse.report/" + searchType + "/" + input
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    s_results = soup.find('div', attrs={'class': 'two-thirds column'})
    rows = s_results.findAll('div', attrs={'class': 'row'})
    tagPattern = re.compile("<.*?>")
    whtspc = re.compile(r"\s+")
    print("")
    print("IP Address\tReverse DNS")
    print("-----------------------------------")
    for row in rows:
         names = row.find('div', attrs={'class': 'two-thirds column'})
         namesStr = str(names)
         namesStr = tagPattern.sub("", namesStr)
         namesStr = whtspc.sub("", str(namesStr))
         ips = row.find('div', attrs={'class': 'one-third column'})
         ipsStr = str(ips)
         ipsStr = tagPattern.sub("", ipsStr)
         ipsStr = whtspc.sub("", str(ipsStr))
         line = str(ipsStr) + '\t' + str(namesStr)
         if line != 'None\tNone':
              print line
    print("")

def main(arg):
    openURL(setURL(arg), arg)

validateInput(sys.argv)
