from user_agent import generate_user_agent
import requests
import unique_string_in_file

# сайт, возвращающий только ip адрес подключаемого
url = "http://icanhazip.com"

# проверяет прокси из одного файла и выписывает их в отдельный файл
# на входе нужны названия файлов
def cheсk_proxies(proxyFileName, validProxyFileName):
    proxyFile = open(proxyFileName, "r")
    validProxyFile = open(validProxyFileName, "a")
    for proxy in proxyFile:
        proxy = proxy[:len(proxy) - 1]
        header = generate_user_agent()
        proxyDict = {"http": "http://" + proxy,
                     "https": "https://" + proxy}
        session = requests.Session()
        session.proxies = proxyDict
        session.headers = header
        try:
            response = session.get(url, timeout=1.5)
            print(response)
            if response.status_code == 200:
                if unique_string_in_file.unique_string_in_file(proxy, validProxyFileName):
                    validProxyFile.write(proxy + "\n")
                    print(proxy)
        except Exception as e:
            print("Not valid : ", e)
