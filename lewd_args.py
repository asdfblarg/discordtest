import requests
import random
from bs4 import BeautifulSoup

urls = (
    "http://danbooru.donmai.us/posts/random/?tags=cat_ears+nude",
    "http://danbooru.donmai.us/posts/random/?tags=cat_ears+ass",
)
def is_tag(tag):
    tagsearch = requests.get("https://danbooru.donmai.us/posts?tags="+str(tag))
    tagcontent = tagsearch.content
    tagsoup = BeautifulSoup(tagcontent, "html.parser")
    search = tagsoup.find('img')
    if search == None:
        return False
    else:
        return True
def check_tagsearch(tag1,tag2):
    tagsearch = requests.get("https://danbooru.donmai.us/posts?tags="+str(tag1)+"+"+str(tag2))
    tagcontent = tagsearch.content
    tagsoup = BeautifulSoup(tagcontent, "html.parser")
    search = tagsoup.find('img')
    if search == None:
        return False
    else:
        return True

def default(args):
    count = 0
    while True:
        if len(args) == 1:
            choice = random.choice(urls)
        elif len(args) == 2:
            #print(check_tag(args[1]))
            if is_tag(args[1]) == False:
                return("\""+str(args[1])+"\" is not a tag!")
            choice = "http://danbooru.donmai.us/posts/random/?tags="+str(args[1])
        elif len(args) == 3:
            if is_tag(args[1]) == False:
                return("\""+str(args[1])+"\" is not a tag!")
            if is_tag(args[2]) == False:
                return("\""+str(args[2])+"\" is not a tag!")
            if check_tagsearch(args[1],args[2]) == False:
                return("No images with both tags found!")
            choice = "http://danbooru.donmai.us/posts/random/?tags=" + str(args[1]) + "+" + str(args[2])
        else:
            return('Too many inputs! No more than 2!\nhttp://puu.sh/otAFk/4ddf396335.jpg')
        response = requests.get(choice)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        imagelink = soup.find(id="image-container")
        if imagelink:
            break
        count = count + 1
        if count == 10:
            return "failed after 10 attempts, please get dvd to fix the lewds"
    return "<"+str(response.url)+">\nhttp://danbooru.donmai.us"+imagelink.get('data-file-url')

#args = ['!test','tits']
#args = ['!lewd','cat']
#args = ['!lewd','1boy', 'nude']
#print(default(args))
