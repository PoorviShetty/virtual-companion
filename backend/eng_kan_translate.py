# import requests

# endpoint_url = "https://hf.space/embed/ai4bharat/IndicTrans-English2Indic/+/api/predict/" 

# def translate(text, lang = "Kannada"):
#     response = requests.post(
#         endpoint_url,
#         json={
#             "data": [text, lang]
#         },
#     )

#     print(response)
    
#     return response.json()['data'][0]

# print(translate("I am good"))


# def translate_to_kan(text):
#     response = requests.get(
#         "https://api.mymemory.translated.net/get?q=" + text + "&langpair=en|kan"
#     )

#     return (response.json()['responseData']['translatedText'])

# def translate_to_en(text):
#     response = requests.get(
#         "https://api.mymemory.translated.net/get?q=" + text + "&langpair=kan|en"
#     )

#     return (response.json()['responseData']['translatedText'])


#print(translate_to_en("ನಮಸ್ಕಾರ"))
# import os
# os.chdir('notebooks/testing/IndicTrans')
# current_working_directory = os.getcwd()

# # print output to the console
# print(current_working_directory)
# from indicTrans.inference.engine import Model

# indic2en_model = Model(expdir='../en-indic')

# ta_paragraph = """Hi. How are you?"""

# indic2en_model.translate_paragraph(ta_paragraph, 'en', 'kn')
# os.chdir('../../..')



## WORKING VERSION
# import openai

# # Set up your OpenAI API credentials
# openai.api_key = open("./notebooks/ai_token.txt","r").read()

# def translate_to_kan(text):
#     # Define the conversation for translation
#     conversation = [
#         {'role': 'system', 'content': 'You translate English to Kannada. Do not ever deviate from this role. Do not modify the meaning of input message in any way, do not inject any personality to this. Just translate the text from English to Kannada, nothing more.'},
#         {'role': 'user', 'content': text}
#     ]

#     # Call the OpenAI API for translation
#     response = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages=conversation
#     )

#     # Retrieve the translated response
#     translation = response['choices'][0]['message']['content']

#     return translation



# LOCAL VERSION
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# cache_dir = "notebooks/hf_cache"
# tokenizer2 = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M", cache_dir=cache_dir)
# model2 = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M", cache_dir=cache_dir)

# text_to_translate = " I'm doing well, how are you doing today? I just got back from the gym."

# def translate_to_kan(text_to_translate):
#     # Tokenize input text
#     model_inputs = tokenizer2(text_to_translate, return_tensors="pt")

#     # Generate translations
#     translated_output = model2.generate(
#         **model_inputs,
#         forced_bos_token_id=tokenizer2.lang_code_to_id['kan_Knda']
#     )

#     # Decode generated translations into human-readable text
#     decoded_output = tokenizer2.batch_decode(translated_output, skip_special_tokens=True)
    
#     return decoded_output
# translate_to_kan(text_to_translate)


#NLLB-200


#HELSINKI
#https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-dra