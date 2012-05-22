import java, javax, sys
from com.ziclix.python.sql import zxJDBC
from javax.servlet.http import HttpServlet


class pop(javax.servlet.http.HttpServlet):

	'''

	Pop item from stack.

	'''
	def doGet(self,request, response):
		self.doPost(request,response)

	def doPost(self,request, response):
		DB_URL = "jdbc:mysql://dbhost/db"
		DB_DRIVER = "com.mysql.jdbc.Driver"
		DB_USER = "username"
		DB_PASS = "password"

		try:
			db = zxJDBC.connect(DB_URL, DB_USER, DB_PASS, DB_DRIVER)
			c = db.cursor()
			stmt = "DELETE FROM stack ORDER BY id DESC LIMIT 1"
			c.execute(stmt)
			c.close()
			db.close()
			request.setAttribute("result","Entry successfully popped from stack.")	

		except Exception, err:
			request.setAttribute("result",err)
							
		dispatcher = request.getRequestDispatcher("index.jsp")
		dispatcher.forward(request,response)

		

