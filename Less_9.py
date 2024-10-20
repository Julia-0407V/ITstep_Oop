"""import requests

#opener = urllib.request.build_opener()
response = requests.get("https://httpbin.org/get")
print(response.content)
print(f"Datatype {type(response.content)}")
"""

"""import requests

res_parse = []

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse= response.text.split("<span>")
for response_element_1 in response_parse:
    if response_element_1.startswith ("$"):
       for response_element_2 in response_element_1.split ("</span>"):
           if response_element_2.startswith ("$") and response_element_2[1].isdigit():
               res_parse.append(response_element_2)

znach_bitcoin = res_parse[0]
print(znach_bitcoin)
"""


from  bs4 import BeautifulSoup

import requests
response = requests.get("https://www.binance.com/uk-UA/price/bitcoin")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    soup_list = soup.find_all("div", {"class": "css-1267ixm"})

    if soup_list:
        price_div = soup_list[0]
        price = price_div.find("div")

        if price:
          print(price.text)
    else:
        print("Element not found")
else:
    print("Response code is not 200")




