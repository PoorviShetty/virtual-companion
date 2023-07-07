# print("hello")
# import dill
# import nltk
# [RegexpTokenizer, WhitespaceTokenizer, laplace_smoothing] = dill.load(open('./models/sent_helpers.pkl', 'rb'))

# w_tokenizer = WhitespaceTokenizer()
# sent_params = dill.load(open('./models/sent_params.pkl', 'rb'))
# loaded_model = dill.load(open('./models/sentiment_model.pkl', 'rb'))
# print(loaded_model(sent_params[0], sent_params[1], sent_params[2], sent_params[3], sent_params[4], ['i am sad']))

import pickle
#import sklearn

# Step 1: Load the pickled pipeline
with open('./models/naive_bayes_pipeline.pickle', 'rb') as f:
    sent_model = pickle.load(f)

def get_sentiment(text):
    predicted_sentiment = sent_model.predict([text])

    # Step 4: Map sentiment to [0] for positive, [1] for negative
    if predicted_sentiment[0] == 'positive':
        sentiment = 1
    else:
        sentiment = 0

    return sentiment