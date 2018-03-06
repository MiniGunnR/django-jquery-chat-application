from instagram.client import InstagramAPI
class instagramSearch(object):

	def _init_(self):
		self.public_users = []
	def instagram(self, nameIn = None):
		if(nameIn == None):
			raise ValueError('TwitterSearch.instagram: name is necessary')
		access_token  = "2941460406.4011edb.8d81ba564aa340aca6d77b690e16b415"
		client_secret = "27f2a6304afe420fa5d12123648a65c9"
		api = InstagramAPI(access_token=access_token, client_secret=client_secret)
		result = api.user_search(nameIn)
		return result	

a = instagramSearch()
print a.instagram("Qian")
print a.instagram("Tom")
