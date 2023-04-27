import dill

[RegexpTokenizer, WhitespaceTokenizer, laplace_smoothing] = dill.load(open('./models/sent_helpers.pkl', 'rb'))

w_tokenizer = WhitespaceTokenizer()
sent_params = dill.load(open('./models/sent_params.pkl', 'rb'))
loaded_model = dill.load(open('./models/sentiment_model.pkl', 'rb'))

print(loaded_model(sent_params[0], sent_params[1], sent_params[2], sent_params[3], sent_params[4], ['i am sad']))
