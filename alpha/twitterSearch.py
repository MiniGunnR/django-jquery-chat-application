import tweepy
class twitterSearch(object):



	def _init_(self):
		self.public_users = []

	def searchName(self, nameIn=None):
		if(nameIn == None):
			raise ValueError("TwitterSearch.searchName: name is necessary")
		auth = tweepy.OAuthHandler('FkTGiMwC31vAyBfUpJz6Fufwl', 'vvxlbyfW76QJNgVWO6rJ26BYoOzYPqehLlamefLFBzSHQVJUJf')
		auth.set_access_token('1965122641-9PQ8264p3RDbY4K1nxXDDV8bB3BVHtBGT1D80Pp', 'JbcQxTUBwwaommlDcNNMcqedKl0fLlFHxtfNBUkMp9NRc')

		api = tweepy.API(auth)
		self.useruserInfo = "Name found in Twitter: \n"
		self.public_users = api.search_users(nameIn)
		result=[]
		for users in self.public_users:
			result.append([users.id_str, users.name, users.location])
		return result


