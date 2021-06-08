# About

Backend server for Infaux Wars project built using Flask and deployed on Heroku. Server has two main routes:

- Scrape
- Preprocess

### Scrape

Scrape takes a URL and returns the main article text

### Preprocess

The goal of this route is to prepare a body of text for our Fake News model. In order to minimize noise for the predictive analysis, the preprocess route will remove all unecessary text: numbers, html tags, contraction, etc.

It alsos uses "term frequency–inverse document frequency" to extract keywords from the body of text. Basically, it returns which words are most significant in the text. Keywords are then later used to find similar news articles for the user.

Further reading on article preprocessing: [Fake News Detection: Text Pre-Processing](https://jon-dagdagan.medium.com/fake-news-detection-pre-processing-text-d9648a2854e5)
