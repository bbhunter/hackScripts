import requests
import json 
import urlparse
import operator
import argparse

parser = argparse.ArgumentParser(description="A tool to pull url parameters from WayBack Machine and Common Crawl and make a sorted-by-frequency parameter bruteforcing list")
parser.add_argument("domain", help="The domain from which to pull the urls from which the parameters are extracted")
args = parser.parse_args()

def waybackurls(host):
    url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=list&fl=original&collapse=urlkey' % host
    r = requests.get(url)   
    return r.text.strip().split("\n")
    
def commoncrawl(host):
    url = 'http://index.commoncrawl.org/CC-MAIN-2018-22-index?url=*.%s/*&output=json' % host
    r = requests.get(url)   
    results = r.text.split("\n")
    urls = []
    for line in results:
        try:
            line = json.loads(line)
            if "url" in line:
                urls.append(line['url'])
        except Exception as e:
            pass
    return urls

urls = waybackurls(args.domain)
urls.extend(url for url in commoncrawl(args.domain) if url not in urls) 
params = {}
for url in urls:
    ps = urlparse.parse_qs(urlparse.urlparse(url).query).keys()
    for param in ps:
        if param not in params:
            params[param]=1
        else:
            params[param]=params[param]+1

sorted_params = map(lambda i: i[0], sorted(params.items(), key=operator.itemgetter(1), reverse=True))
print "\n".join(sorted_params)
