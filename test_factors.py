import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from nltk.corpus import stopwords

# Step 1: Collect the replies
replies = [...]  # List of reply texts

# Step 2: Clean the data
cleaned_replies = []
stop_words = set(stopwords.words('english'))
for reply in replies:
    # Remove URLs and special characters
    cleaned_text = re.sub(r"http\S+|[^a-zA-Z0-9]+", " ", reply)
    # Remove stopwords and convert to lowercase
    cleaned_text = ' '.join([word.lower() for word in cleaned_text.split() if word.lower() not in stop_words])
    cleaned_replies.append(cleaned_text)

# Step 3: Vectorize the replies
vectorizer = TfidfVectorizer()
reply_matrix = vectorizer.fit_transform(cleaned_replies)

# Step 4: Perform factor analysis
pca = PCA(n_components=2)
factors = pca.fit_transform(reply_matrix.toarray())

# Step 5: Interpret the factors
factor_loadings = pd.DataFrame(pca.components_.T, index=vectorizer.get_feature_names(), columns=['Factor 1', 'Factor 2'])
print(factor_loadings)
