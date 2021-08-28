import sys
import os
import pydownsongs
import time

def main():
	pydownsongs.createDirIfNotExists(os.path.join(os.path.expanduser("~"), ".cache"))
	try:
		args = sys.argv[1:]
	except:
		print("Invalid Usage")
		sys.exit()

	if len(args) > 1:
		if args[0] == "-f":
			file = args[1]
			try:
				quality = args[2]
			except:
				print("Invalid Usage")
				sys.exit()
			if not os.path.exists(file):
				print("{} not found. Try again.".format(file))
				time.sleep(0.1)
				print("Exiting...")
				time.sleep(0.3)
				sys.exit()
			if quality.isnumeric() == False:
				print("Invalid usage")
				sys.exit()
			quality = int(quality)
			file = open(file, "r")
			Counter = 0
			Content = file.read() 
			CoList = Content.split("\n")
			for i in CoList: 
				if i: 
					Counter += 1
			Counter += 1
			iterationNo= 1
			file.seek(0)
			while iterationNo < Counter:
				try:
					inputquery = file.readline()
					inputquery = inputquery.rstrip()
					if inputquery == "":
						continue
					pydownsongs.checkInternet()
					pydownsongs.download(inputquery, quality)
				except Exception as e:
					print("Some error has occured")
					print(e)
					tempfile = open("failedtemp.txt", "a")
					tempfile.write(inputquery+"\n")
					tempfile.close()
				iterationNo += 1
			file.close()


		# spotify play list ----------------------------
		elif args[0] == "-s":
			link = args[1]
			try:
				quality = args[2]
			except:
				print("Invalid Usage")
				sys.exit()
			if quality.isnumeric() == False:
				print("Invalid usage")
				sys.exit()
			quality = int(quality)
			pydownsongs.checkInternet()
			pydownsongs.dl_spotlist(link, quality)

			# ---------------------------------------
		else:
			# direct command usage ---------------------
			if str(args[-1]).isnumeric() == False:
				print("Quality level not supplied")
				print("Try:")
				print("pydownsongs {} 3".format(" ".join(args)))
			else:
				arr = args[:-1]
				quality = int(args[-1])
				pydownsongs.checkInternet()
				pydownsongs.downloadarray(arr, quality)
			# ---------------------------------------
	else:
		print("Invalid Usage")

	try:
		os.remove(".google-cookie.")
	except:
		try:
			os.remove(".google-cookie")
		except:
			pass

if __name__ == "__main__":
	main()
