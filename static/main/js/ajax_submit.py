import cgi

form = cgi.FieldStorage()
text = form.getvalue('text_py')
print(f'{text}+ 123')
