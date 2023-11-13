import requests



resource = requests.get("https://coinmarketcap.com")
if resource.status_code==200:
    soup = BeautifulSoup(resource.text,features="Html.parser")
    soup_list = soup.Find_all("a","")
    #for i in soup_list:
        #print(i)
    rez = soup_list[0].find("span")
    print(rez.text)



    #print(resource.status_code)








#resource = requests.post("https://httpbin.org/post", data="Test Data",
                         #headers={"h1":"Test Title"})
#print(resource.text)
#print(f"DataType - {type(resource.content)}")

