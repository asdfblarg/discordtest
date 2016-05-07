import urllib.request
from bs4 import BeautifulSoup

# EXAMPLE of downloading an image
# urllib.request.urlretrieve('https://static-cdn.jtvnw.net/emoticons/v1/4337/1.0', 'YouWHY.jpg')
# NOTE: if you want bigger images, you want to change size "1.0" to 2.0 or 3.0
# I ignored the rest of the stupid Robot Emotes and Turbo Emotes

def download_special_turbo_emotes():
    urllib.request.urlretrieve("https://static-cdn.jtvnw.net/jtv_user_pictures/emoticon-2867-src-f02f9d40f66f0840-28x28.png", 'KappaHD.jpg')
    urllib.request.urlretrieve("https://static-cdn.jtvnw.net/jtv_user_pictures/emoticon-2868-src-5a7a81bb829e1a4c-28x28.png", 'MiniK.jpg')
    urllib.request.urlretrieve("https://static-cdn.jtvnw.net/emoticons/v1/62837/1.0", 'imGlitch.jpg')
    urllib.request.urlretrieve("https://static-cdn.jtvnw.net/emoticons/v1/62841/1.0", 'copyThis.jpg')
    urllib.request.urlretrieve("https://static-cdn.jtvnw.net/emoticons/v1/62842/1.0", 'pastaThat.jpg')

def download_face_emotes(size):
    url = "https://twitchemotes.com"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    for divs in soup.find_all('img',):
        # print(divs.attrs)
        if divs.get('data-tooltip'):
            img_link = divs.get('src')[:-3]
            emoticon_name = divs.get('data-regex')
            # emoticon_name = divs.get('data-tooltip')[8:-9]
            print(img_link+size,emoticon_name)
            urllib.request.urlretrieve(img_link+size, emoticon_name+'.jpg')

#########################
# start of code
#########################


# download_special_turbo_emotes()
download_face_emotes(size = '1.0')
