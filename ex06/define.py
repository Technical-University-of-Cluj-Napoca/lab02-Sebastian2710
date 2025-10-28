import sys
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    if len(sys.argv)<2: 
        print("no word to define")
        sys.exit(0)
    word=sys.argv[1]
    path =f"https://dexonline.ro/definitie/{word.lower()}"
    web_response = requests.get(path)
    soup = BeautifulSoup(web_response.content,'html.parser')
    definition = soup.find("span", class_="tree-def html").text
    print(definition)

    #try for english
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"}

    word=sys.argv[2]
    path=f"https://www.oxfordlearnersdictionaries.com/definition/english/{word.lower()}_1?q={word.lower()}"
    web_response=requests.get(path,headers=headers)
    soup = BeautifulSoup(web_response.content,'html.parser')
    definition = soup.find("span", class_="def", attrs={"hclass": "def"})
    print(definition.text.strip())


