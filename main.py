import requests



resource = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%87%D1%83%D0%B3")
if resource.status_code==200:
    soup = BeautifulSoup(resource.text,features="Html.parser")
    soup_list = soup.Find_all("a","https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%87%D1%83%D0%B3")
    #for i in soup_list:
        #print(i)
    rez = soup_list[0].find("span")
    print(rez.text)



    #print(resource.status_code)








#resource = requests.post("https://httpbin.org/post", data="Test Data",
                         #headers={"h1":"Test Title"})
#print(resource.text)
#print(f"DataType - {type(resource.content)}")

