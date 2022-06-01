from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np
import pandas as pd

tweet = '@rektulungrek today the weather is not good for traveling https://upperstairs.wordpress.com'

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

#load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']

#sentiment analysis
encoded_tweet = tokenizer(preprocess(tweet), return_tensors='pt')
output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
scores = output[0][0].detach().numpy()
scores = softmax(scores)
for i in range(len(scores)):
    l = labels[i]
    s = scores[i]
    print(l, s)

#by max value
max_value = max(scores)
list_scores = list(scores)
index = list_scores.index(max_value)
print(labels[index], max_value)