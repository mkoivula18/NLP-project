from sklearn.feature_extraction.text import CountVectorizer
import csv
import numpy as np

file = 'NLP-database.csv'

text = ''

with open(file, newline='', encoding='utf8') as src:
	reader = csv.reader(src, delimiter=';')
	for row in reader:
		if row != []:
			text += row[2]
			


#https://towardsdatascience.com/natural-language-processing-count-vectorization-with-scikit-learn-e7804269bb5e
#print(text)
text = [text]
vectorizer = CountVectorizer()
vectorizer.fit(text)
#print(vectorizer.vocabulary_)
vector = vectorizer.transform(text).toarray()[0]
print(vector)
print(len(vector))
print(np.sum(vector))