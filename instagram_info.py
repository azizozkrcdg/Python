from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

URL = "https://www.instagram.com/"

def get_data(username):
    end_url = URL + username
    request = Request(end_url, headers={"User-Agent":"Mozilla/5.0"})
    html_data = urlopen(request).read()

    soup = BeautifulSoup(html_data, "html.parser")
    data = soup.find("meta", property="og:description").attrs["content"]
    data = data.split("-")[0]
    data = data.split(" ")

    print(f"""
        Takipçi Sayisi : {data[0]}
        Takip Edilen Kişi Sayisi : {data[2]}
        Gönderi Sayisi : {data[4]}
    """)

user_name = input("Kullanıcı Adı : ")
get_data(user_name)
