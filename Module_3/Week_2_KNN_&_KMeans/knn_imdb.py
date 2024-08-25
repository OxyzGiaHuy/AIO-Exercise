import numpy as np
from datasets import load_dataset  # need to pip install
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# load dataset
imdb = load_dataset("imdb")
imdb_train, imdb_test = imdb['train'], imdb['test']

# convert text to vector using BoW
vectorizer = CountVectorizer(max_features=100)
X_train = vectorizer.fit_transform(imdb_train['text']).toarray()
X_test = vectorizer.transform(imdb_test['text']).toarray()
y_train = np.array(imdb_train['label'])
y_test = np.array(imdb_test['label'])

# scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# knn classifier
knn_model = KNeighborsClassifier(n_neighbors=5, algorithm='ball_tree')
knn_model.fit(X_train, y_train)

# predict and evaluate
y_pred = knn_model.predict(X_test)
print(accuracy_score(y_test, y_pred))
