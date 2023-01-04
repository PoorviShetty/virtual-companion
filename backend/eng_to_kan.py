import requests

endpoint_url = "https://hf.space/embed/ai4bharat/IndicTrans-English2Indic/+/api/predict/" 

def translate(text, lang = "Kannada"):
    response = requests.post(
        endpoint_url,
        json={
            "data": [text, lang]
        },
    )
    
    return response.json()['data'][0]