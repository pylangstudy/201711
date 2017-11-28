import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
print(code)
