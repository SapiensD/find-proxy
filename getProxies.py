import requests
from bs4 import BeautifulSoup as bs


def write_proxies_in_file(proxyFileName):
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "html.parser")
    proxies_rows = soup.find("textarea").text
    proxies_rows = proxies_rows[75:]
    print(proxies_rows)
    proxyFile = open(proxyFileName, "w")
    proxyFile.write(proxies_rows)
    proxyFile.close()