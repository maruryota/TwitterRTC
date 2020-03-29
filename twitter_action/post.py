def post_tweet(url, twitter, tweet):
	params = {"status": tweet}
	res = twitter.post(url, params = params)

	if res.status_code == 200:
		print("Success.")
	else:
		print("Failed. : %d"% res.status_code)

