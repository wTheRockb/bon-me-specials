import requests
import base64
from datetime import date, datetime, timedelta

KEY = 'bqM4F3O9SpfQ4NSB4I5Hi0Rnx'

def load_secret():
	with open('secret.txt', 'r') as fp:
		secret = fp.readline()
		return secret

def request_auth_token(key, secret):
	key = key.encode()
	secret = secret.encode()
	token_cred =  key + b':' + secret
	encoded_cred =b'Basic ' + base64.b64encode(token_cred)
	headers = {'Authorization': encoded_cred, 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
	payload = {'grant_type': 'client_credentials'}
	r = requests.post('https://api.twitter.com/oauth2/token', headers=headers, params=payload)
	data = r.json()
	token = b'Bearer ' + data['access_token'].encode()
	return token


def main():
	resource_url = 'https://api.twitter.com/1.1/search/tweets.json'
	payload = {'q': '#BonMeTruckSpecials', 'result_type': 'recent', 'count': 5, 'tweet_mode': 'extended'}
	secret = load_secret()
	auth_token = request_auth_token(KEY, secret)
	headers = {'Authorization':auth_token}
	r = requests.get(resource_url, params=payload, headers=headers)
	data = r.json()
	tweets = data["statuses"]
	shredded_tweets = map(lambda x: {"text": x["full_text"], "date": x["created_at"]}, tweets)
	for i in shredded_tweets:
		tweet_date = datetime.strptime(i["date"], '%a %b %d %H:%M:%S +%f %Y')
		today = datetime.today()
		if tweet_date > (today - timedelta(days=1)):
			print(i["text"])


if __name__ == '__main__':
	main()