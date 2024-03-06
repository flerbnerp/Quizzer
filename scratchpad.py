from urllib.parse import quote, unquote

key = "no words"
if ("/" in key) or ("\\" in key):
    print("valid directory")