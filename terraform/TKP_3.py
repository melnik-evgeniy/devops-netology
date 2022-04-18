import requests
with open('/Users/Melnik/Desktop/Scrin/2bentok.txt', 'r') as file:
    ln = 0
    for line in file.readlines():
        a = line.rstrip()
        c = (a.split(';'))
        url = "https://securepayments.sberbank.ru%s" % (c[0])
        ln = ln + 1
        req = requests.post(url, data=c[1], headers={"content-type":"application/json"})
        print(str(ln) + '_http_code=' + str(req.status_code) + ';' + str(req.content) + ';' + 'query=' + c[1])
        print(req.content)
        print(url)