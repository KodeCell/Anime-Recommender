from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def distances(data):
    cv = CountVectorizer(max_features=50,stop_words='english')
    vectors = cv.fit_transform(data['tags']).toarray()
    return vectors

def similarity(data):
    similarity = cosine_similarity(data)
    return similarity




