import tweepy
class twitterSearch(object):



	def _init_(self):
		self.userInfo = "Name found in Twitter: "

	def searchName(self, nameIn=None):
		if(nameIn == None):
			raise ValueError("TwitterSearch.searchName: name is necessary")
		auth = tweepy.OAuthHandler('FkTGiMwC31vAyBfUpJz6Fufwl', 'vvxlbyfW76QJNgVWO6rJ26BYoOzYPqehLlamefLFBzSHQVJUJf')
		auth.set_access_token('1965122641-9PQ8264p3RDbY4K1nxXDDV8bB3BVHtBGT1D80Pp', 'JbcQxTUBwwaommlDcNNMcqedKl0fLlFHxtfNBUkMp9NRc')

		api = tweepy.API(auth)
		userInfo = "Name found in Twitter: \n"
		public_users = api.search_users(nameIn)
		for users in public_users:
			userInfo += "id: " + users.id_str + " ";
			if(users.name):
				userInfo += "  Name: " + users.name + " "
			else:
				userInfo += "  Name: not found "
				continue
			if(users.location):
				userInfo += "  Location: " + users.location + "\n"
			else:
				userInfo += "  Location: not found \n"
				continue
			
		return userInfo


a = twitterSearch()
print a.searchName("QIAN")