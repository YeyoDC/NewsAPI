import requests
import send_email as email
api_key = "c58e48396c6049f4b2771b65f72047a3"
url = "https://newsapi.org/v2/everything?" \
       "q=tesla&from=2024-11-16&" \
       "sortBy=publishedAt" \
       "&apiKey=c58e48396c6049f4b2771b65f72047a3" \
       "&language=en"

request = requests.get(url)
content = request.json()
print(content)
news = ""
subject = "Subject: todays news"
for article in content['articles'][0:20]:
    if article['title'] is not None:
        news += subject
        news += str(article['title'])
        news += "\n"
        news += str(article['description'])

email.send_email(news.encode('utf-8'))