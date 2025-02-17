import requests
import json

def sentiment_analyzer(text_to_analyse):
    URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label': label, 'score': score}