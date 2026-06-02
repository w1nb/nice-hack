import requests
#from fake_useragent import UserAgent

'''
# GET request
target_url = 'https://cn.bing.com/search'
#headers={'User-Agent':UserAgent().random}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
}
params={
    'q':'反恐精英'
}
response = requests.get(url=target_url,headers=headers,params=params)
response.encoding = 'utf8'    # gbk / utf8
#print(response)
#print(response.url)
#print(response.text)
#print(response.request.headers)
with open('1.html','w',encoding='utf8') as f:
    f.write(response.text)
'''

'''
# POST request  
target_url = 'https://www.aa7a.cn/user.php'
data = {
    'username':'wwb801914@163.com',
    'password':'dvsbssrb',
    'captcha':'4Yc6',
    'remember':'1',
    'ref':'http://www.aa7a.cn',
    'act':'act_login',
}
#headers={'User-Agent':UserAgent().random}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'}
response = requests.post(url=target_url,headers=headers,json=data)
print(response.text)
print(response.cookies.items())
'''

'''
# Example
target_url = 'https://stock.xueqiu.com/v5/stock/quote.json?symbol=SH000001&extend=detail'
#headers={'User-Agent':UserAgent().random}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
    'Cookie':'aliyungf_tc=ca7df9702b9a83e3eb2d6ffdb9245c0dee6bc2756ac02fcf106088c2f307cc07; xq_a_token=20458f74230aee45906ecb90d8c70ff43daa3837; xqat=20458f74230aee45906ecb90d8c70ff43daa3837; xq_r_token=fa5fac8aea31fef0733c31a1c3670554e9365bda; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc4MTA1NDU5NiwiY3RtIjoxNzc5NTQxNzUyMTIzLCJjaWQiOiJkOWQwbjRBWnVwIn0.VxNJkXymMHG-EH_liZZ1LnhKRNppmb8X-6THlL0oIu4Bu7xIUheb8JIJxV-OK6fkrqAlWYZYgSB-W0yCxTGZZPa6c6dfFwbBQU5THema3PIktaccestUqzBt-xLePVDUr3328JJYelLXXrdHPBZQG0thxkTtGOAjWdGmw0--FBhdsDy74K1EsfpZlE3Qk0S0W08mKYhn-7kGqCIU2HxkqAQ_1EF3Bn2-lxsL_aqrZ18EAc0RzvsI9ap1K743OuhiATaPev25VdhcS7E9j7tH_rY3QbYDcf6wcgSDvfqzeW--reO7zqwlX4kYcAZEeVOrTuUMTIhYWtjkANfvAv2vOQ; cookiesu=721779541810186; u=721779541810186; device_id=4fcfe8bfeda0876db97606806a14e05d; Hm_lvt_1db88642e346389874251b5a1eded6e3=1779541811; HMACCOUNT=09AE97D532493A85; smidV2=20260523211011df947b51dc81e9fbce3635b10e74b225004d97e6b59cb0940; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=XyT3WdpE/coaIxEcd8UCid5NOkPvcPvHERGWF5tFf5gM3gq1xsI1xAWJAmdV4X+bezfVYGZjHFw7j22oARgxCA%3D%3D; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1779541923'
}
response = requests.get(url=target_url,headers=headers)
print(response.text)
'''

'''
# Request Simulation to the web page to obtain cookies (with proxy poll)
#def get_proxy():
#    return requests.get('http://127.0.0.1:5010/get/').json()
def get_cookie():
    target_url = 'https://xueqiu.com/'
#    proxy = {
#        'http': f'http://{get_proxy()['proxy']}/'
#    }
#    print(proxy)
#    response = requests.get(url=target_url,proxies=proxy)
    response = requests.get(url=target_url)
    print(response.text)
    print(response.cookies.items())
get_cookie()
'''

'''
# Request Simulation to the web page to obtain cookies
def get_cookies():
    target_url = 'https://xueqiu.com/'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
}
    response = requests.get(url=target_url,headers=headers)
    cookie_params = dict(response.cookies)
    return cookie_params
# Request data carrying cookies
def get_data():
    target_url = 'https://stock.xueqiu.com/v5/stock/quote.json?symbol=SH000001&extend=detail'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
    }
    cookie_params = get_cookies()
    response = requests.get(url=target_url,headers=headers,cookies=cookie_params)
    data_bytes = response.content
    data_bytes = data_bytes.decode('utf-8')
    print(data_bytes)
get_data()
'''

'''
# with session
session = requests.session()
def get_data():
    target_url = 'https://xueqiu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
    }
    session.get(url=target_url,headers=headers)
    target_url = 'https://stock.xueqiu.com/v5/stock/quote.json?symbol=SH000001&extend=detail'
    response = session.get(url=target_url, headers=headers)
    data_bytes = response.content
    data_bytes = data_bytes.decode('utf-8')
    print(data_bytes)
get_data()
'''

'''
# Response
target_url = 'https://i0.hdslb.com/bfs/new_dyn/541d7828d89e1c07b601e8db4d082b96119104724.jpg'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
}
response = requests.get(url=target_url, headers=headers)
#print(response.status_code)
#print(response.headers)
#print(response.text)
print(response.content)
#print(response.json())
with open("1.jpg", "wb") as f:
    f.write(response.content)
'''

'''
# chunks
target_url = 'https://i0.hdslb.com/bfs/new_dyn/541d7828d89e1c07b601e8db4d082b96119104724.jpg'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
}
response = requests.get(url=target_url, headers=headers)
for chunks in response.iter_content(chunk_size=1024):
    print(chunks)
'''
