#import urllib2
import json
import requests

class FB(object):
	def __init__(self):
		self.token = 'CAACEdEose0cBAPlZArphUVSxcY3hRkZCjFlqyGQsWejxEbQ2Sr4vYBcHLubGZCpmnb8OAm4zOWwZCZAr5Hggew8RughA2z3hBg3t7AB1VmUBsm5dOiZBSA4H4vft0FIUP1aNWkANi7Ah6XQZCnDeG14GddfZBPsMewbBdWGzEHWKrih8JvGK189zMAbn544f7ekqKdGQlE0G8QZDZD'
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
					#pict = requests.get('https://graph.facebook.com/v2.5/'+i[u'id']+'/picture/')
					result[i[u'id']] =i[u'name']#,pict.url) 
				return result
		
	def searchDetailInfo(self,id):
		originalData = requests.get('https://graph.facebook.com/'+id+'?access_token='+self.token)
		data = originalData.json()
		picurl = requests.get('https://graph.facebook.com/'+id+'/picture').url
		result=dict()
		result['pic'] = picurl
		if u'name' in data:
			result[u'name'] = data[u'name']
		if u'category' in data:
			result[u'category'] = data[u'category']
		if u'birthday' in data:
			result[u'birthday'] = data[u'birthday']
		if u'about' in data:
			result[u'about'] = data[u'about']
		return result


# test=FB()
# hello = test.searchUser("yusheng ding")
# for i,y in hello.iteritems():
# 	print i+" "+y[0]
# 	print y[1]
# he = test.searchDetailInfo("216311481960")
# for i,y in he.iteritems():
# 	print i+":	"+y