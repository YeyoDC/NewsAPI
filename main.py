import requests

api_key = "c58e48396c6049f4b2771b65f72047a3"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-11-16&sortBy=publishedAt&apiKey=c58e48396c6049f4b2771b65f72047a3"

request = requests.get(url)
content = request.json()


for article in content['articles']:
    print(article['title'])
