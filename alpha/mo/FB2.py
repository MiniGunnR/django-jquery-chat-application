import urllib2
import json
import requests

class FB(object):
	def __init__(self):
		self.token = 'CAACEdEose0cBAJLk4NK2YLeqESNuqCNdVyRtsZCVlCnyngy55Mlk0Du1ZCZAZAoTtdfcJDKFNo9MM75gzhZCZBks10U9Gpn8oqRzioaCLrOtf5AFUMmZCYS6RXvuxddJfBZBCAmzKDh3hd6RZCt4QIh39lZA9Y5IzIgTUKKw2nOiBTytPUPMv3dsMUlHSPh5QDRBt7RfRzxEupWQZDZD'
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