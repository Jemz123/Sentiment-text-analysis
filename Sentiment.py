from textblob import TextBlob
from newspaper import Article

Urls = [
    "https://en.wikipedia.org/wiki/Saivam"
]

for url in Urls:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.summary
    # Print summary after decoding to handle Unicode characters
    print("Summary:", text)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print("Sentiment Polarity:", sentiment)
