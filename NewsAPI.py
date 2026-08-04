import requests

#r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-2-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
#content = r.json()
#articles = content['articles']
#print(type(content))

#for article in articles:
#    print("TITLE\n", article['title'], "Description\n", article['description'])

def get_news(topic, from_date, to_date, language='en', api_key = 'ac1014efb79c4aa5a63c7f40de83ad4a'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n' {article['title']}, '\nDESCRIPTION\n' {article['description']}")
        return results

    print(get_news(topic='space', from_date='2022-2-27', to_date='2022-2-28'))


def get_news_headlines(country, api_key = 'ac1014efb79c4aa5a63c7f40de83ad4a'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n' {article['title']}, '\nDESCRIPTION\n' {article['description']}")
        return results

    print(get_news(country='us'))