#!/data/data/com.termux/files/usr/bin/env python3
print ("\nonly_green\n")

try:
	def bluegreen():
		print (" - Just Copy & Paste The Generated Messages - \n")
		colors = ["#2EB62C","#57C84D","#83D475","#ABE098",'#C5E8B7','#ABE098','#83D475','#57C84D','#2EB62C']
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
