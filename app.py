from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def index():
        return render_template("index.html")

@app.route('/process_sentence', methods=['POST'])
def process_sentence():
    sentence = request.form['sentence']
    # You can process the sentence here
    print("Input Sentence:", sentence)
    tweet = sentence
    # preprocess tweet
    tweet_words = []

    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
            
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)

    tweet_proc = " ".join(tweet_words)

    print(tweet_words)
    print(tweet_proc)

    # load model and tokenizer
    roberta = "cardiffnlp/twitter-roberta-base-sentiment"

    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)

    labels = ['Negative', 'Neutral', 'Positive']

    # sentiment analysis
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    # output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    for i in range(len(scores)):

        l = labels[i]
        s = scores[i]*100
        scores[i] *= 100
        print(l,s)

    try:
        # Process the sentence and return an array of integers
        result_array = scores
        print (result_array)
    except Exception as e:
        # Handle any exceptions here, and return an empty array as a fallback
        print("Error:", e)
        result_array = []

    return render_template('result.html', result_array=result_array)

if __name__ == '__main__':
    app.run(debug=True)