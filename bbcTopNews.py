# new idea is: With using gTTS and not win32com.client or pypiwin32
# also playing itself  
import os
import requests
from gtts import gTTS
def NewsFromBBC():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "4dbc17e007ab436fb66416009dfb59a8"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
		
	for i in range(len(results)):
		print(i + 1, results[i])
        
        
	myobj = gTTS(text=str(results), lang="en", slow=False)
	myobj.save("text_to_speech.mp3")
    #Execute created file in windows
	os.system("text_to_speech.mp3")
    
if __name__ == '__main__':
	
	# function call
	NewsFromBBC()



