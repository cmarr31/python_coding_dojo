about_me = {"Name": "Chris", 
	"Age": 21, 
	"Home Country": "United States", 
	"Favorite Language": "Ruby"
	}

def info_about_myself():
	for key,data in about_me.iteritems():
		print key, "=", data

info_about_myself()
