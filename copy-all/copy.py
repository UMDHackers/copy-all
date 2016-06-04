#!/usr/bin/python
import sys, os, ntpath, shutil, time, datetime

def help():
	print "Usage: python copy.py [all][file][dir] [type] [date begin]-b [date from]-e"
	print "command all will copy all the files from the Main Drive of the computer, you can specfy which location this is in the config.txt file line 2"
	print "command File will simply move one file to another"
	print "type you can specfy the type, if you want all of the files ignore this"
	print "date begin, get files from after this date, keep in MM/DD/YYYY format"
	print "date end, get file before this date, keep in the MM/DD/YYYY format"
	print "to change the output directory change line 1 in the config.txt"

def details(argv):
	ret = []
	cmds = argv.split(" ")
	if(len(cmds) == 5):
		cmd_1 = cmds[2]
		cmd_2 = cmds[3]
		cmd_3 = cmds[4]
		cmd_2 = cmd_2.replace("-b","")
		cmd_3 = cmd_3.replace("-e", "")
		s_time = cmd_2.split("/")
		e_time = cmd_3.split("/")
		s_month = s_time[0]
		e_month = e_time[0]
		s_day = s_time[1]
		e_day = e_time[1]
		s_year = s_time[2]
		e_year = e_time[2]
		s_sec = datetime.datetime(s_year, s_month, s_day, 0, 0)
		e_sec = datetime.datetime(e_year, e_month, e_day, 0, 0)
		s_sec = (s_sec - datetime.datetime(1970, 1, 1)).total_seconds()
		e_sec = (e_sec - datetime.datetime(1970, 1, 1)).total_seconds()
		for path, dirs, files in os.walk(cmds[1])::
			for file in files:
				if file.endswith(cmd_1) and 
				time.ctime(os.path.getmtime(path+os.sep+file)) >= s_sec and 
				time.ctime(os.path.getmtime(path+os.sep+file)) <= e_sec:
					ret.add(path+os.sep+file)
	elif(len(cmds) == 4):
		cmd_1 = cmds[2]
		cmd_2 = cmds[3]
		if(!cmd_1.endswith("-b") or !cmd_1.endswith("-e")):
			for path, dirs, files in os.walk(cmds[1])::
				for file in files:
					if file.endswith(cmd_1):
						ret.add(path+os.sep+file)
		elif(cmd_1.endswith("-b")):
			cmd_1 = cmd_1.replace("-b","")
			s_time = cmd_1.split("/")
			s_month = s_time[0]
			s_day = s_time[1]
			s_year = s_time[2]
			s_sec = datetime.datetime(s_year, s_month, s_day, 0, 0)
			s_sec = (s_sec - datetime.datetime(1970, 1, 1)).total_seconds()
			for path, dirs, files in os.walk(cmds[1])::
				for file in files:
					if time.ctime(os.path.getmtime(path+os.sep+file)) >= s_sec:
						ret.add(path+os.sep+file)
		else:
			help()
		
		if(cmd_2.endswith("-b")):
			tmp = []
			cmd_2 = cmd_2.replace("-b","")
			s_time = cmd_2.split("/")
			s_month = s_time[0]
			s_day = s_time[1]
			s_year = s_time[2]
			s_sec = datetime.datetime(s_year, s_month, s_day, 0, 0)
			s_sec = (s_sec - datetime.datetime(1970, 1, 1)).total_seconds()
			for file in ret:
				if time.ctime(os.path.getmtime(file)) >= s_sec:
					tmp.add(file)
			ret = tmp
		elif(cmd_2.endswith("-e")):
			tmp = []
			cmd_2 = cmd_2.replace("-e","")
			e_time = cmd_2.split("/")
			e_month = e_time[0]
			e_day = e_time[1]
			e_year = e_time[2]
			e_sec = datetime.datetime(e_year, e_month, e_day, 0, 0)
			e_sec = (e_sec - datetime.datetime(1970, 1, 1)).total_seconds()
			for file in ret:
				if time.ctime(os.path.getmtime(file)) <= s_sec:
					tmp.add(file)
			ret = tmp
		else:
			help()
	elif(len(cmds) == 3):
		cmd_1 = cmds[2]
		if(cmd_1.endswith("-e")):
			cmd_1 = cmd_1.replace("-b","")
			s_time = cmd_1.split("/")
			s_month = s_time[0]
			s_day = s_time[1]
			s_year = s_time[2]
			s_sec = datetime.datetime(s_year, s_month, s_day, 0, 0)
			s_sec = (s_sec - datetime.datetime(1970, 1, 1)).total_seconds()
			for path, dirs, files in os.walk(cmds[1])::
				for file in files:
					if time.ctime(os.path.getmtime(path+os.sep+file)) >= s_sec:
						ret.add(path+os.sep+file)
		elif(cmd_1.endswith("-b")):
			cmd_1 = cmd_1.replace("-e","")
			e_time = cmd_1.split("/")
			e_month = e_time[0]
			e_day = e_time[1]
			e_year = e_time[2]
			e_sec = datetime.datetime(e_year, e_month, e_day, 0, 0)
			e_sec = (e_sec - datetime.datetime(1970, 1, 1)).total_seconds()
			for path, dirs, files in os.walk(cmds[1])::
				for file in files:
					if time.ctime(os.path.getmtime(path+os.sep+file)) <= e_sec:
						ret.add(path+os.sep+file)
		else:
			for path, dirs, files in os.walk(cmds[1]):
				for file in files:
					if file.endswith(cmd_1):
						ret.add(path+os.sep+file)
	for file in ret:
		
		
#first one
def main(argv):
	config = open("config.txt", "r")	
	loc = config.read().split("\n")
	output = loc[0]
	main_dir = loc[1]
	
	if len(argv) == 1 or argv[1] == "help":
		help()
	else:
		file = argv[1]
		#Move the file to the USB!
		if(os.path.isfile(file)):
			file_name = ntpath.basename(file)
			shutil.copyfile(file, output+file_name)
		elif(os.path.isdir(file)):
			#type of file
			if(len(argv) > 2):
				details(argv)
			else:
				dir = ntpath.basename(file)
				shutil.copytree(file, output+dir)
		elif(file == "all"):
			if(len(argv) > 2):
				details(argv)
			else:
				dir_collection = []
				for path, dirs, files in os.walk(main_dir):
					# go only one level deep
					dir_collection = list(dirs)
					del dirs[:] # go only one level deep
				for d in dir_collection:
					shutil.copytree(d, output+d)
				for f in files:
					shutil.copyfile(f, output+f)
#main
if __name__ == '__main__':
    main(sys.argv)





'''
os.rename(file, "D:/"+file_name)
print "DIR " + dir
for root, dirs, files in os.walk("C:/Document", topdown = False):
	for name in files:
		print(name)
	for name in dirs:
		print(name)

'''
