# import re
# import requests
# import random
# from bs4 import BeautifulSoup

# url_1= "http://danbooru.donmai.us/posts/random/?tags=cat_ears+nude"
# url_2 = "http://danbooru.donmai.us/posts/random/?tags=cat_ears+ass"
# urls = [url_1,url_1]
# # rc = requests.get(random.choice(urls)).content
# # soup = BeautifulSoup(rc, "html.parser")
# # imagelink = soup.find(itemprop="contentSize").get('href')

# while(True):
	# #imagelink = BeautifulSoup(requests.get(random.choice(urls)).content, "html.parser").find(itemprop="contentSize").get('href')
	# rc = requests.get(random.choice(urls)).content
	# soup = BeautifulSoup(rc, "html.parser")
	# imagelink = soup.find(itemprop="contentSize")
	# if imagelink:
		# break
# print("http://danbooru.donmai.us"+imagelink.get('href'))

# import re
# import requests
# from urllib.parse import urljoin
# import random
# from bs4 import BeautifulSoup


# urls = (
	# "http://danbooru.donmai.us/posts/random/?tags=cat_ears+nude",
	# "http://danbooru.donmai.us/posts/random/?tags=cat_ears+ass",
# )
# while True:
	# choice = random.choice(urls)
	# response = requests.get(choice)
	# html = response.content
	# soup = BeautifulSoup(html, "html.parser")
	# image = soup.find("img", {"id": "image"})
	# if image:
		# break

# print(response.url)
# print(image['src'])	
# #urljoin(response.url, image['src'])
	
import re
import requests
import random
from bs4 import BeautifulSoup

urls = (
	"http://danbooru.donmai.us/posts/random/?tags=cat_ears+nude",
	"http://danbooru.donmai.us/posts/random/?tags=cat_ears+ass",
)
def default():
	while True:
		choice = random.choice(urls)
		response = requests.get(choice)
		html = response.content
		soup = BeautifulSoup(html, "html.parser")
		imagelink = soup.find(itemprop="contentSize")
		if imagelink:
			break

	return "<"+str(response.url)+">\nhttp://danbooru.donmai.us"+imagelink.get('href')
