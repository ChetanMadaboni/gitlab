Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def rev(text):
	return text[::-1]
KeyboardInterrupt
>>> rev(chetan)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    rev(chetan)
NameError: name 'rev' is not defined
>>> def rev(text):
	return text[::-1]
rev(chetan)
SyntaxError: invalid syntax
>>> def rev(text):
	return text[::-1]
