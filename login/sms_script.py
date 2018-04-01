import requests
from bs4 import BeautifulSoup

class SMSClient :
	def __init__(self,username,password, verbose=False):
        
		self.isLoggedIn = False
		self.verbose = verbose
		self.username = username
		self.password = password


		self.url='http://site24.way2sms.com/Login1.action?'
		self.details={'username':username,'password':password}

		self.sess=requests.session()

		
		self.sess.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"


		if(verbose):
			print("Logging in.....")

		query=self.sess.post(self.url,data=self.details)



		if query.status_code == 200 :
		    self.LoggedIn=True

		# get session id
		self.id=self.sess.cookies.get_dict()['JSESSIONID'][4:]

		self.messages_left_url = 'http://site24.way2sms.com/sentSMS?Token='+self.id
		self.message_url='http://site24.way2sms.com/smstoss.action'
        

	def count(self):
      
        
		query = self.sess.get(self.messages_left_url)

		
		soup = BeautifulSoup(query.text,'html.parser')

		data = soup.find("div",{"class":"hed"}).h2.text

		sent=0

		if(self.verbose):
			print("Getting message count....")

		for i in data:
		    if i.isdecimal():
		        sent=10*sent +int(i)

		return sent


	def send(self,number,message) :

		if len(message)>139 or len(number)!=10 or not number.isdecimal():
		    return False

		self.payload={
		    'ssaction':'ss',
		    'Token':self.id,
		    'mobile':number,
		    'message':message,
		    'msglen':129,
		}

		if(self.verbose):
			print("Sending messsage.....")

		query=self.sess.post(self.message_url,data=self.payload)

		return ( query.status_code == 200)
         
	def Logout(self):

		if(self.verbose):
			print("Logging out....")

		self.sess.get('http://site24.way2sms.com/entry?ec=0080&id=dwks')
		self.sess.close()
		self.isLoggedIn=False


if __name__ == '__main__':

	smsClient = SMSClient('9029168990', 'chaitya6262')
	
	smsClient.send("9029168990","Hello,World!")