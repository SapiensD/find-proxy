import getProxies
import checkProxies
import unique_string_in_file


proxyFileName = "proxy.txt"
validProxyFileName = "validProxy.txt"

getProxies.write_proxies_in_file(proxyFileName)
checkProxies.cheсk_proxies(proxyFileName, validProxyFileName)


"""
proxy_file = open("validProxy.txt", "r")
proxy_file2 = open("valid_proxy.txt", "a")

for validProxy in proxy_file:
    if unique_string_in_file.unique_string_in_file(validProxy[:len(validProxy)-1], "valid_proxy.txt"):
        proxy_file2.write(validProxy)
"""