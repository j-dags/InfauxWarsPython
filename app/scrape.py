from newspaper import Article
from newspaper import Config

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

def scrape(url):
  article = Article(url, config=config)

  article.download()
  article.parse()
  text = ' '.join(article.text.split(' ')[:1000])

  export = {
    "title": article.title,
    "text": text
  }

  return export

