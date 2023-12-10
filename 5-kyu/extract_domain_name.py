"""
Extract the domain name from a URL

DESCRIPTION:
Write a function that when given a URL as a string, parses out just the 
domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
* url = "www.xakep.ru"                        -> domain name = xakep"

"""
import re

def domain_name(url):
    # Updated regex to extract just the domain name, excluding top-level domain
    domain_pattern = re.compile(r'(https?://)?(www\.)?([^/:.]+)')
    match = domain_pattern.search(url)
    if match:
        return match.group(3)
    else:
        return None  

domain_name("http://github.com/carbonfive/raygun")
domain_name("http://www.zombie-bites.com")
domain_name("https://www.cnet.com")
domain_name("www.xakep.ru")

