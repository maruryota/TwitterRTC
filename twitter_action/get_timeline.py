def get_timeline(url, twitter, timeline_count):
	params ={'count' : timeline_count}
	res = twitter.get(url, params = params)

	if res.status_code == 200:
		timelines = json.loads(res.text)
		for line in timelines:
			print(line['user']['name']+'::'+line['text'])
			print(line['created_at'])
			print('*******************************************')
	else:
		print("Failed: %d" % res.status_code)
