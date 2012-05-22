<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>PaaS Jython Eval</title>
    </head>
    <body>
	<p>${result}</p>
	<br /><br /><br /><br />
        <form method="GET" action="push.py">
		<legend>Stack</legend>
		<label>Entry:
            		<input type="textarea" name="entry" rows="40" cols="100"></textarea>
             		<input type="submit" title="Push">
		</label>
        </form>
	<br /><br />
	<form method="GET" action="pop.py">	
		<p>Pop last entry?</p>
		<input type="submit" title="pop">
	</form>
	<br /><br />
	<form method="GET" action="email.py">	
		<p>Email stack?</p>
		<input type="submit" title="pop">
	</form>
    </body>
</html>


