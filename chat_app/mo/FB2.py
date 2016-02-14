import json
import requests

class FB(object):
	def __init__(self):
		self.token ='CAACEdEose0cBALKZAd93Ukoz7vyM86VJtGFCpquOZCB4DT82RXpS7Tk40mpoHCY3K38yXZA4c92JXPlQkOHmIXQ3dzZA1vtZAZAZAznxQED9wvj6LZAS62sZBZBnWmLUSf31piiHnv1kYUUgMLxon2ADldGOKmmdivpFondarJU6VJB9I6mhIycgrwUQ3D1h7EZClNHM4qI4I7kxQZDZD'
	def searchUser(self,name):
		if not isinstance(name,str) or len(name)<=0:
			raise Exception("Error type")
		originalData = requests.get('https://graph.facebook.com/search?q='+name+'&type=user&access_token='+self.token)
		data = originalData.json()
		if u'data' in data:
			if len(data[u'data'])<0:
				print "No Result in facebook"
				return
			else:
				result = dict()
				for i in data[u'data']:
					pict = requests.get('https://graph.facebook.com/v2.5/'+i[u'id']+'/picture/')
					result[i[u'id']] =(i[u'name'],pict.url) 
				return result
		
	def searchDetailInfo(self,id):
		originalData = requests.get('https://graph.facebook.com/'+id+'?access_token='+self.token)
		data = originalData.json()
		result=dict()
		if u'name' in data:
			result[u'name'] = data[u'name']
		if u'category' in data:
			result[u'category'] = data[u'category']
		if u'birthday' in data:
			result[u'birthday'] = data[u'birthday']
		if u'about' in data:
			result[u'about'] = data[u'about']
		return result


test=FB()
hello = test.searchUser("yusheng ding")
for i,y in hello.iteritems():
	print i+" "+y[0]
	print y[1]
he = test.searchDetailInfo("216311481960")
for i,y in he.iteritems():
	print i+":	"+y
