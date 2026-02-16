import requests

url = "https://raw.githubusercontent.com/amir-zeldes/gum/refs/heads/master/xml/GUM_interview_chomsky.xml"

r = requests.get(url)

with open("data.xml", "wb") as f:
    f.write(r.content)