from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")


def get_sentiment_label(query):
    model_path = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
    sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
    res = sentiment_task(query)
    return res[0]['label']

# Example usage:
# query = "Covid cases are increasing fast!"
# sentiment_label = get_sentiment_label(query)
# print("Sentiment Label:", sentiment_label)
