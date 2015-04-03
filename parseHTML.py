from bs4 import BeautifulSoup
import sys
import re

def parseHTML(file, fname):
	output = open("Redditors.txt","a")

	# parse the file with BeautifulSoup
	soup = BeautifulSoup(file)
	#print soup
	try:
		# get total karma list <div class="panel panel-default" id="totalkarma">
		total_karma = soup.find("div", {"id": "totalkarma"})
		#print total_karma
		# get user names from the list <ul class="list-group">
		users = total_karma.find("ul", {"class": "list-group"})
		userlist = users.find_all("a", {"class": "list-group-item"})
		if bool(userlist) != False:
			print fname
		for user in userlist:
			#print user
			userinfo_1 = re.sub(',','',user.text)
			userinfo_2 = re.sub('\.','',userinfo_1)
			
			# parse the individual user info
			userinfo = re.sub('\n', ' ' ,userinfo_2)
			#print userinfo[1:]
			output.write(str(userinfo[1:]) + '\n')
		output.close()
	except:
		e = sys.exc_info()[0]
		print ( "<p>Error: %s</p>" % e )
