# -----------------------------------------------------------------------------
# 
# File Name: Crawler.py
#
# Author: Donald Summers
#
# Description:  A web crawler that recursively goes through every webpage on
#               the given system arguement website to then traverse to other
#               sites and do the same thing until it goes through as many links
#               as outlined by another system arguement. Outputs visited websites
#               and amount of times visited to a text file.
#
# How to use:   Run it in the terminal with 2 system arguements, a link to a
#               website and the maximum links it should travel from the starting site
#
# Example use:  >python Crawler.py https://mtech.edu/ 2
#
# -----------------------------------------------------------------------------

import sys
import urllib.request
import re

# -----------------------------------------------------------------------------
# Function: crawl
#
# Inputs:
#   resLevel: system arguement that represents the recursion level
#   website: website that gets checked for all available website links
#   linkDict: dictionary that stores hopw often a site was visited
#
# Return Value:
#   a dictionary that stores how often sites are visited while crawling
#
# Example Use:
#   emptyDict = {}
#   crawl(2, https://mtech.edu/, emptyDict)
#
# Description:
#   Recursively goes through a website to go through every link it has on it
#   and continue to go through links on the next page if the recursion hasn't
#   ended, updates dictionary that has how often sites were visited
#
# Exceptions:
#   If a page cannot be loaded and read, terminate that recursive branch
# -----------------------------------------------------------------------------
def crawl(resLevel, website, linkDict):
    href = "http[s]*://[^\"]*/"
    try:
        page = urllib.request.urlopen(website)
        html = str(page.read())
    except:
        return 0
    listSites = re.findall(href, html)
    for newWebsite in listSites:
        if newWebsite not in linkDict:
            linkDict[newWebsite] = 1
            if int(resLevel) >= 1:
                crawl(int(resLevel)-1, newWebsite, linkDict)
        elif newWebsite in linkDict:
            linkDict[newWebsite] += 1
    return linkDict

if __name__ == "__main__":
    newDict = {sys.argv[1]: 1}
    lastDict = crawl(sys.argv[2], sys.argv[1], newDict)
    file = open("links.txt","wt")
    for x in lastDict:
        file.write(f"{lastDict[x]} {x}\n")
    
