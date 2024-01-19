from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://github.com/Kamilla1533?tab=repositories").text
soup = BeautifulSoup(html_text, "lxml")
repositories = soup.find_all("li", class_="col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source")
with open("List of repositories.txt", "w") as f:
    for repository in repositories:
        name_rep = repository.find("a", itemprop="name codeRepository").text.replace(" ", "")
        new_name_rep = name_rep.replace("\n", "")
        f.write(new_name_rep + "\n")
    print("File saved!")
