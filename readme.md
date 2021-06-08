# About

Backend server for [Infaux Wars project](https://github.com/j-dags/InfauxWars) built using Flask and deployed on Heroku. Server has two main routes:

- Scrape
- Preprocess

<br>

### Scrape

Takes a given URL, scrapes the webpage, and returns the main body text of the page.

<br>

### Preprocess

The goal of this route is to prepare a body of text for our Fake News model. In order to minimize noise in the predictive analysis, the preprocess route will remove all unecessary text: numbers, html tags, contraction, etc.

It also uses "term frequency–inverse document frequency" to extract keywords from the body of text. Basically, it returns which words are most significant in the text. Keywords are then later used to find similar news articles for the user.

Further reading on text preprocessing: [Fake News Detection: Text Pre-Processing](https://jon-dagdagan.medium.com/fake-news-detection-pre-processing-text-d9648a2854e5)
