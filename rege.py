#!/data/data/com.termux/files/usr/bin/env python3

print ("\nNice_Blue_Green\n")

try:
	def bluegreen():
		print (" - Just Copy & Paste The Generated Messages - \n")
		colors = ["#f44336","#f4511e","#fb8c00","#ffb300",'#fdd835','#c0ca33','#7cb342','#43a047']
		s = 0
		new = ""
		msgb = ""
		while 1:
			msg = input("Message: ")
			if len(msg) >= 100:
				msgb = msg[100:]
				msg = msg[:100]
			msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == "":
					new = new + ""
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + _
				s = s + 1
			print ("[c][b][i]" + new + msgb + "\n")
			new = ""
			msgb = ""
			s = 0
	bluegreen()
except KeyboardInterrupt:
        exit()
