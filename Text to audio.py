import gtts

txt = "kardile magiii"
speech = gtts(text = txt ,lang = 'en',slow = False,tld= 'com.au')

speech()
speech.save(Use.mp3)