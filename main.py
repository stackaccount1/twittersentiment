from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
from dotenv import load_dotenv
import os
import tweepy
import re
import nltk.data
import requests

#nlp library load, load env lib, load sentiment analyzer
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
load_dotenv()


# twitter auth
def getClient():
    client = tweepy.Client(
        bearer_token=os.environ.get("bearer_token"),
        consumer_key=os.environ.get("consumer_key"),
        consumer_secret=os.environ.get("consumer_secret"),
        access_token=os.environ.get("access_token"),
        access_token_secret=os.environ.get("access_token_secret"))
    return client


# initliaze variables
name = 'HsakaTrades'
query = 'from:' + name
sumoftwot = []
ticker_list = []
ticker_count = []
positron_twots = []
megatron_twots = []
neutral_twots = []


# test scoring
# happy_sentence = "happy day lucky day oh joy"
# chat = sid.polarity_scores(happy_sentence)
# print(chat)

#Pull up tweets, append them to lists depending on sentiment
def return_tweets_append_sentiment(name):
    client = getClient()
    query = 'from:' + name
    tweets = client.search_recent_tweets(query=query, max_results=100)
    for tweet in tweets:
        for x in map(str, tweet):
            # print(x)
            #print("The original string : " + str(x))
            #res = isinstance(x, str)
            # print("Is variable a string ? : " + str(res))
            # print("here")
            score = sid.polarity_scores(x)
            # print(score)
            if score['pos'] > 0:
                positron_twots.append(x)
            elif score['neg'] > 0:
                megatron_twots.append(x)
            else:
                positron_twots.append(x)

#function above for multiple twitter accounts
def return_sentiment_lists():
    return_tweets_append_sentiment('HsakaTrades')
    return_tweets_append_sentiment('blknoiz06')
    return_tweets_append_sentiment('CanteringClark')
    return_tweets_append_sentiment('ShardiB2')
    return_tweets_append_sentiment('IDrawCharts')
    return_tweets_append_sentiment('Pentosh1')
    return_tweets_append_sentiment('TheCryptoDog')
    return_tweets_append_sentiment('AltcoinRadarYT')
    return_tweets_append_sentiment('mattysino')
    return_tweets_append_sentiment('RaoulGMI')
    return_tweets_append_sentiment('RealVisionBot')
    return_tweets_append_sentiment('bigdsenpai')
    return_tweets_append_sentiment('jimtalbot')
    return_tweets_append_sentiment('nebraskangooner')
    return_tweets_append_sentiment('Livercoin')
    return_tweets_append_sentiment('VegetaCrypto1')
    #return_tweets_append_sentiment('AlexjFerraro')
    #return_tweets_append_sentiment('Trader_ZO7')
    return_tweets_append_sentiment('Ninjascalp')
    return_tweets_append_sentiment('eliz883')
    return_tweets_append_sentiment('CryptoGodJohn')
    return_tweets_append_sentiment('rektcapital')
    return_tweets_append_sentiment('AltcoinPepe')
    return_tweets_append_sentiment('trader1sz')
    return_tweets_append_sentiment('bloodgoodBTC')
    return_tweets_append_sentiment('EmperorBTC')
    return_tweets_append_sentiment('Phoenix_Ash3s')
    return_tweets_append_sentiment('tedtalksmacro')
    return_tweets_append_sentiment('Anbessa100')
    return_tweets_append_sentiment('MooijCapital')
    return_tweets_append_sentiment('ByzGeneral')
    return_tweets_append_sentiment('ConquererCrypto')
    #return_tweets_append_sentiment('edwardmorra_btc')
    return_tweets_append_sentiment('MuroCrypto')
    #return_tweets_append_sentiment('CelldwellerGee')
    print(len(positron_twots))
    print(len(megatron_twots))
    print(len(neutral_twots))
    return (positron_twots, megatron_twots)


def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))


def create_x_and_y_graph():
    # positive sentiment
    posistring = ""
    negitivestring = ""
    positron_twots, megatron_twots = return_sentiment_lists()
    #print(positron_twots)
    posistring = listToString(positron_twots).lower()
    #regex
    ticker_record = 'Eth |Btc |BNB |SOL |ADA |bitcoin|ethereum|XRP |DOT |MUTE |OHM |SPELL |SAMO |RAY |SRM |COPE |LRC |PYR |RELAY |DOGE |AVAX |SHIB |WOOF |CRO |LUNA |LTC |UNI |LINK |MATIC |ALGO |BCH |EGLD |VET |AXS |XLM |MANA |ICP |TRX | UST |ATOM |FTT |THETA |BAT |FIL | $ETC |FTM |HBAR |NEAR |SAND |HNT |XTZ |XMR |LRC |GRT |EOS |FLOW |MIOTA |KLAY |AAVE |CAKE | $ONE |ENJ |LEO |XEC |ZEC |MKR |BSV |KSM |QNT | AMP |GALA |NEO |KDA | RUNE |STX |CHZ | HOT |WAVES |BTT |CRV |DASH |KCS |CELO |IOTX |COMP |TFUEL |XEM |NEXO |IMX |DCR |OKB |WAXP |QTUM |ROSE |ICX |MINA |VGX |ZEN |OMG |XDC |RVN |YFI | REV |SCRT |SUSHI '
    positive_x_list = re.findall(ticker_record, posistring, flags=re.IGNORECASE)
    # print(positive_x_list)
    d = {}
    for i in range(len(positive_x_list) - 1):
        x = positive_x_list[i]
        c = 0
        for j in range(i, len(positive_x_list)):
            c = positive_x_list.count(x)
        count = dict({x: c})
        if x not in d.keys():
            d.update(count)
    #print(d)
    new_d = dict(sorted(d.items(), key=lambda item: item[1]))
    positive_key_list = list(new_d.keys())
    positive_key_list = positive_key_list[-20:]
    positive_value_list = list(new_d.values())
    positive_value_list = positive_value_list[-20:]
    print("Positive Plot:")
    print(positive_key_list)
    print(positive_value_list)
    negitivestring = listToString(megatron_twots).lower()
    negative_x_list = re.findall(ticker_record, negitivestring, flags=re.IGNORECASE)
    # print(positive_x_list)
    dneg = {}
    for i in range(len(negative_x_list) - 1):
        xneg = negative_x_list[i]
        cneg = 0
        for j in range(i, len(negative_x_list)):
            cneg = negative_x_list.count(xneg)
        count = dict({xneg: cneg})
        if xneg not in dneg.keys():
            dneg.update(count)
    print(dneg)
    new_dneg = dict(sorted(dneg.items(), key=lambda item: item[1]))
    negative_key_list = list(new_dneg.keys())
    negative_key_list = negative_key_list[-20:]
    negative_value_list = list(new_dneg.values())
    negative_value_list = negative_value_list[-20:]
    print("Negative Plot:")
    print(negative_key_list)
    print(negative_value_list)
    return(positive_key_list, positive_value_list, negative_value_list, negative_key_list)

#set some objects
positron = []
megatron = []
limit = 100
timeframe = 'month' #hour, day, week, month, year, all
listing = 'top'

#reddit functions
def get_reddit(subreddit,listing,limit,timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    r = request.json()
    posts = []
    for post in r['data']['children']:
        x = post['data']['title']
        score = sid.polarity_scores(x)
        if score['pos'] > 0:
            positron.append(x)
        elif score['neg'] > 0:
            megatron.append(x)
        else:
            positron.append(x)
    return positron, megatron

def find_all_reddit_posts_append():
    get_reddit('cryptocurrency', listing, limit, timeframe)
    get_reddit('CryptoMarkets', listing, limit, timeframe)
    get_reddit('CryptoCurrencies', listing, limit, timeframe)
    get_reddit('altcoin', listing, limit, timeframe)
    get_reddit('CryptoCurrencyTrading', listing, limit, timeframe)
    #get_reddit('ethtrader', listing, limit, timeframe)
    return (positron, megatron)

def create_x_and_y_graph_reddit():
    # positive sentiment
    posi = ""
    negitive = ""
    positron, megatron = find_all_reddit_posts_append()
    posi = listToString(positron).lower()
    ticker_record = 'Eth |Btc |BNB |SOL |ADA |Cardano |Ethereum Classic |bitcoin cash |bitcoin |ethereum |XRP |DOT |MUTE |OHM |SPELL |SAMO |RAY |SRM |COPE |LRC |PYR |RELAY |DOGE |AVAX |SHIB |WOOF |CRO |LUNA |LTC |UNI |LINK |MATIC |ALGO |BCH |EGLD |VET |AXS |XLM |MANA |ICP |TRX | UST |ATOM |FTT |THETA |BAT |FIL | $ETC |FTM |HBAR |NEAR |SAND |HNT |XTZ |XMR |LRC |GRT |EOS |FLOW |MIOTA |KLAY |AAVE |CAKE | $ONE |ENJ |LEO |XEC |ZEC |MKR |BSV |KSM |QNT | AMP |GALA |NEO |KDA | RUNE |STX |CHZ | HOT |WAVES |BTT |CRV |DASH |KCS |CELO |IOTX |COMP |TFUEL |XEM |NEXO |IMX |DCR |OKB |WAXP |QTUM |ROSE |ICX |MINA |VGX |ZEN |OMG |XDC |RVN |YFI | REV |SCRT |SUSHI '
    positive_x = re.findall(ticker_record, posi, flags=re.IGNORECASE)
    # print(positive_x_list)
    d = {}
    for i in range(len(positive_x) - 1):
        x = positive_x[i]
        c = 0
        for j in range(i, len(positive_x)):
            c = positive_x.count(x)
        count = dict({x: c})
        if x not in d.keys():
            d.update(count)
    #print(d)
    new_d_r = dict(sorted(d.items(), key=lambda item: item[1]))
    positive_key = list(new_d_r.keys())
    positive_key = positive_key[-20:]
    positive_value = list(new_d_r.values())
    positive_value = positive_value[-20:]
    print("Positive Plot:")
    print(positive_key)
    print(positive_value)
    negitive = listToString(megatron).lower()
    negative_x = re.findall(ticker_record, negitive, flags=re.IGNORECASE)
    # print(positive_x_list)
    dneg_r = {}
    for i in range(len(negative_x) - 1):
        xneg = negative_x[i]
        cneg = 0
        for j in range(i, len(negative_x)):
            cneg = negative_x.count(xneg)
        count = dict({xneg: cneg})
        if xneg not in dneg_r.keys():
            dneg_r.update(count)
    print(dneg_r)
    new_dneg_r = dict(sorted(dneg_r.items(), key=lambda item: item[1]))
    negative_key = list(new_dneg_r.keys())
    negative_key_list = negative_key[-20:]
    negative_value = list(new_dneg_r.values())
    negative_value = negative_value[-20:]
    print("Negative Plot:")
    print(negative_key)
    print(negative_value)
    return(positive_key, positive_value, negative_value, negative_key)

#create_x_and_y_graph()

#flask functionsama
app = Flask(__name__)

@app.route("/")
def chart():
    positive_key_list, positive_value_list, negative_value_list, negative_key_list = create_x_and_y_graph()
    positive_key, positive_value, negative_value, negative_key = create_x_and_y_graph_reddit()
    labels_1 = positive_key_list
    values_1 = positive_value_list
    values_2 = negative_value_list
    labels_2 = negative_key_list
    values_3 = positive_value
    labels_3 = positive_key
    values_4 = negative_value
    labels_4 = negative_key
    return render_template('chart.html', values=values_1, labels=labels_1, values_2=values_2, labels_2=labels_2, values_3=values_3, labels_3=labels_3, values_4=values_4, labels_4=labels_4)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#print(token_xyz)
