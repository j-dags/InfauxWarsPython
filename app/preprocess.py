############################
###### OLD PROCESSING ######
############################
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

def main(dataset):
  ##Creating a list of stop words and adding custom stopwords
  stop_words = set(stopwords.words("english"))
  ##Creating a list of custom stopwords
  new_words = ["using", "show", "result", "large", "also", "iv", "one", "two", "new", "previously", "shown", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" "us", "u.s."]
  stop_words = stop_words.union(new_words)
  corpus = []

  ## PREPROCESS DATA
  text = re.sub(r'http\S+', '', dataset) #Remove URLs
  text = re.sub('[^a-zA-Z]', ' ', text) #Remove punctuations
  text = text.lower() #Convert to lowercase
  text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text) #remove tags
  text=re.sub("(\\d|\\W)+"," ",text) # remove special characters and digits
  text = text.split() #Convert to list from string
  lem = WordNetLemmatizer() #Lemmatisation
  text = [lem.lemmatize(word) for word in text if not word in stop_words]
  text = " ".join(text)
  corpus.append(text)
  corpus.append('the') #countVectorizer needed an array so I append a dummy word


  ## TEXT VECTORIZER
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_df=0.8,stop_words=stop_words, max_features=10000, ngram_range=(1,3))
  X=cv.fit_transform(corpus)

  ## CONVERT TEXT TO INT MATRIX
  from sklearn.feature_extraction.text import TfidfTransformer

  tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
  tfidf_transformer.fit(X)
  # get feature names
  feature_names=cv.get_feature_names()
  # fetch document for which keywords needs to be extracted
  doc=corpus[0]
  #generate tf-idf for the given document
  tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))

  #Function for sorting tf_idf in descending order
  from scipy.sparse import coo_matrix
  def sort_coo(coo_matrix):
      tuples = zip(coo_matrix.col, coo_matrix.data)
      return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

  def extract_topn_from_vector(feature_names, sorted_items, topn=10):
      """get the feature names and tf-idf score of top n items"""

      #use only topn items from vector
      sorted_items = sorted_items[:topn]

      score_vals = []
      feature_vals = []

      # word index and corresponding tf-idf score
      for idx, score in sorted_items:

          #keep track of feature name and its corresponding score
          score_vals.append(round(score, 3))
          feature_vals.append(feature_names[idx])

      #create a tuples of feature,score
      #results = zip(feature_vals,score_vals)
      results= {}
      for idx in range(len(feature_vals)):
          results[feature_vals[idx]]=score_vals[idx]

      return results
  #sort the tf-idf vectors by descending order of scores
  sorted_items=sort_coo(tf_idf_vector.tocoo())
  #extract only the top n; n here is 10
  keywords=extract_topn_from_vector(feature_names,sorted_items, 10)


  export = {
    "text": doc,
    "keywords": list(keywords.keys())
  }

  return export
