import requests
from bs4 import BeautifulSoup
    
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def rhymer(word):
    syl = syllable_count(word)
    url = ('https://www.rhymer.com/%s.html' % word)
    r = requests.get(url)
    r_html = r.text
    page = BeautifulSoup(r_html, 'html.parser')
    rhymes = page.select('div#syl-%s div div span a' % syl)
    return print(rhymes[random.randint(0,len(rhymes))].text)
