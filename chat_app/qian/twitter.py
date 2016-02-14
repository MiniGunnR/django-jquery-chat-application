import tweepy

auth = tweepy.OAuthHandler('FkTGiMwC31vAyBfUpJz6Fufwl', 'vvxlbyfW76QJNgVWO6rJ26BYoOzYPqehLlamefLFBzSHQVJUJf')
auth.set_access_token('1965122641-9PQ8264p3RDbY4K1nxXDDV8bB3BVHtBGT1D80Pp', 'JbcQxTUBwwaommlDcNNMcqedKl0fLlFHxtfNBUkMp9NRc')

api = tweepy.API(auth)

public_users = api.search_users("QIAN")
for users in public_users:
    print users.name
    print users.location 
    print "\n"
