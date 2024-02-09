#!/data/data/com.termux/files/usr/bin/env python3

print ("\nGrey\n")

try:
	def moonlight():
		print (" - Just Copy & Paste The Generated Messages - \n")
		colors = ["#20","#30","#40","#30",'#50','#40','#30','#20','#30','#40','#50','#60','#70','#60','#50','#40','#60','#30']
		s = 0
		new = ""
		msgb = ""
		while 1:
			msg = raw_input("Message: ").decode('utf8')
			if len(msg) >= 48:
				msgb = msg[48:]
				msg = msg[:48]
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
	moonlight()
except KeyboardInterrupt:
        exit()
