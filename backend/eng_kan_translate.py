import requests

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


def translate_to_kan(text):
    response = requests.get(
        "https://api.mymemory.translated.net/get?q=" + text + "&langpair=en|kan"
    )

    return (response.json()['responseData']['translatedText'])

def translate_to_en(text):
    response = requests.get(
        "https://api.mymemory.translated.net/get?q=" + text + "&langpair=kan|en"
    )

    return (response.json()['responseData']['translatedText'])


#print(translate_to_en("ನಮಸ್ಕಾರ"))