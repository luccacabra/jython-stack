import java, javax, sys, smtplib, email.utils
from com.ziclix.python.sql import zxJDBC
from email.mime.text import MIMEText

class email(javax.servlet.http.HttpServlet):

	'''

	Email last pushed item on stack to given e-mail address.

	'''
	def doGet(self,request, response):
		self.doPost(request,response)

	def doPost(self,request, response):
		MAIL_SERV = "smtp.gmail.com"
		MAIL_PORT = 587
		MAIL_USER = "username"
		MAIL_FROM = "username@gmail.com"
		MAIL_PASS = "password"

		DB_URL = "jdbc:mysql://dbhost/db"
		DB_DRIVER = "com.mysql.jdbc.Driver"
		DB_USER = "username"
		DB_PASS = "password"


		try:
			db = zxJDBC.connect(DB_URL, DB_USER, DB_PASS, DB_DRIVER)
			c = db.cursor()
			stmt = "SELECT * FROM stack"
			c.execute(stmt)
			body = "Python stack \n\n"
			for entry in c.fetchall():
				body += '%s %s\t%s\n' % (entry[0], entry[1], entry[2])
			c.close()

			content = MIMEText(body)
			server = smtplib.SMTP(MAIL_SERV,MAIL_PORT)
			server.ehlo()
			server.starttls()
			server.login(MAIL_USR,MAIL_PASS)
			failed = server.sendmail(MAIL_USR,[MAIL_FROM],content.as_string())
			server.quit()
			if failed:
				request.setAttribute("result","Could not send message.")
			else:
				request.setAttribute("result","Stack successfully e-mailed to: \""+content.as_string()+"\"")	

		except Exception, err:
			request.setAttribute("result",err)
									
		dispatcher = request.getRequestDispatcher("index.jsp")
		dispatcher.forward(request,response)
		


