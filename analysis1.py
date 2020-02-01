from tweepy.streaming import StreamListener
from tweepy import OAuthHandler,Stream,Cursor
import twiiter_secret
from textblob import TextBlob
import tweepy
import pprint
import json
import matplotlib.pyplot as plt

def main():
    search_item=input("Enter the term you want to search :")
    no_of_searchT=int(input("Enter the no of tweets you will take :"))
    auth=OAuthHandler(twiiter_secret.CONSUMER_KEY,twiiter_secret.CONSUMER_SECERT)
    auth.set_access_token(twiiter_secret.ACCESS_TOKEN,twiiter_secret.ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)
    pos=0;neg=0;neut=0;pol=0
    tweets=tweepy.Cursor(api.search,q=search_item).items(no_of_searchT)
    for tweet in tweets:
        #print(tweet.text)
        analysis=TextBlob(tweet.text)
        pol+=analysis.sentiment.polarity
        if analysis.sentiment.polarity==0:
            neut+=1
        elif analysis.sentiment.polarity>0:
            pos+=1
        else:
            neg+=1
    posp=(pos/no_of_searchT)*100
    negp=(neg/no_of_searchT)*100
    neutp=(neut/no_of_searchT)*100
    polp=(pol/no_of_searchT)*100
    pie_li=[posp,negp,neutp]
    plt.figure(figsize=(20,20))
    patches,text=plt.pie(pie_li)
    label=['positive '+str(posp)+'%','negative '+str(negp)+'%','neutral '+str(neutp)+'%']
    plt.legend(patches,label)
    plt.title(f'Twitter sentiment analysis of {search_item} on {no_of_searchT} tweets')
    plt.show()

if __name__=="__main__":
    main()
