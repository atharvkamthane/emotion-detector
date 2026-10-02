import requests


def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        'grpc-metadata-mm-model-id':
            'emotion_aggregated-workflow_lang_en_stock'
    }

    payload = {
        'raw_document': {
            'text': text_to_analyze
        }
    }

    response = requests.post(
        URL,
        json=payload,
        headers=headers
    )

    response.raise_for_status()

    data = response.json()
    emotion_data = data["emotionPredictions"][0]["emotion"]

    anger_score = emotion_data["anger"]
    disgust_score = emotion_data["disgust"]
    fear_score = emotion_data["fear"]
    joy_score = emotion_data["joy"]
    sadness_score = emotion_data["sadness"]

    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    dominant_emotion = max(
        emotion_scores,
        key=emotion_scores.get
    )

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }
