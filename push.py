import java, javax, sys
from com.ziclix.python.sql import zxJDBC
from javax.servlet.http import HttpServlet

class push(javax.servlet.http.HttpServlet):

	'''

	Push item onto stack.

	'''
	def doGet(self,request, response):
		self.doPost(request,response)

	def doPost(self,request, response):
		entry = request.getParameter("entry")
		DB_URL = "jdbc:mysql://dbhost/db"
		DB_DRIVER = "com.mysql.jdbc.Driver"
		DB_USER = "username"
		DB_PASS = "password"

		
		if not entry:
			request.setAttribute("result","Please enter a value to be pushed to the stack.")
		if len(entry) > 256 :
			request.setAttribute("result","Please limit input to 256 characters.")			
		else:
			try:
				db = zxJDBC.connect(DB_URL, DB_USER, DB_PASS, DB_DRIVER)
				c = db.cursor()
				stmt = "INSERT INTO stack (value) VALUES (\""+entry+"\")" 
				c.execute(stmt)
				c.close()
				db.close()
				request.setAttribute("result","\""+entry+"\" successfully added to database")	
			except Exception, err:
				request.setAttribute("result",err)
			
		dispatcher = request.getRequestDispatcher("index.jsp")
		dispatcher.forward(request, response)
		
