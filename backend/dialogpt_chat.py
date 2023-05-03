# import dill

# with open('models/chat_model.pkl', 'rb') as f:
#     lmodel = dill.load(f)

# with open('models/chat_tokenizer.pkl', 'rb') as g:
#     ltokenizer = dill.load(g)

# UTTERANCE = "My friends are cool but they eat too many carbs."
# inputs = ltokenizer([UTTERANCE], return_tensors="pt")
# reply_ids = lmodel.generate(**inputs)
# print(ltokenizer.batch_decode(reply_ids))


import json
import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
API_TOKEN = open("./notebooks/hf_token.txt","r").read()
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def get_chat_response(past_user_inputs, generated_responses, text):
    def query(payload):
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
    data = query(
        {
            "inputs": {
                "past_user_inputs": past_user_inputs,
                "generated_responses": generated_responses,
                "text": text,
            },
        }
    )

    return(data['generated_text'])


# past_user_inputs = ["Which movie is the best ?"]
# generated_responses = ["It's Die Hard for sure."]
# text = "Can you explain why?"
# print(get_chat_response(past_user_inputs, generated_responses, text))