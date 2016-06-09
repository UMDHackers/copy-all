#!/usr/bin/python
import sys, os, ntpath, shutil, time, datetime

def help():
	print "Usage: python copy.py [all][file][dir] [type]-t [date begin]-b [date from]-e [size low]-s [size high]-l [name]-strict [name]-leninent force"
	print "command all will copy all the files from the Main Drive of the computer, you can specfy which location this is in the config.txt file line 2"
	print "command File will simply move one file to another"
	print "type you can specfy the type, if you want all of the files ignore this"
	print "date begin, get files from after this date, keep in MM/DD/YYYY format"
	print "date end, get file before this date, keep in the MM/DD/YYYY format"
	print "to change the output directory change line 1 in the config.txt"
	print "Size is the same idea, have a size of bytes you wanna be over [size]-s or if you want to be under [size]-l or both"
	print "name, name of the file -strict meaning the exact file name has to be allowed or -leninent meaning if the string is in the file name"
	print "force, will remove the orginal copy of the file"
def details(argv):
	ret = set(), temp_ret = set()
	curr_cmd = ""
	cmds = argv.split(" ")
	spe_dir = cmds[1]
	force = False
	for i in range(2, len(cmds)):
		curr_cmd = cmds[i]
		if curr_cmd.endswith("-t"):
			curr_cmd.replace("-t","")
			for path, dirs, files in os.walk(spe_dir):
				for file in files:
					if file.endswith(cmd_1):
						temp_ret.add(path+os.sep+file)
		elif curr_cmd.endswith("-b"):
			curr_cmd.replace("-b", "")
			s_time = curr_cmd.split("/")
			s_month = s_time[0]
			s_day = s_time[1]
			s_year = s_time[2]
			s_sec = datetime.datetime(s_year, s_month, s_day, 0, 0)
			s_sec = (s_sec - datetime.datetime(1970, 1, 1)).total_seconds()
			for path, dirs, files in os.walk(spe_dir)::
				for file in files:
					if time.ctime(os.path.getmtime(path+os.sep+file)) >= s_sec
						temp_ret.add(path+os.sep+file)
		elif curr_cmd.endswith("-e"):
			curr_cmd.replace("-e", "")
			e_time = curr_cmd.split("/")
			e_month = e_time[0]
			e_day = e_time[1]
			e_year = e_time[2]
			e_sec = datetime.datetime(e_year, e_month, e_day, 0, 0)
			e_sec = (e_sec - datetime.datetime(1970, 1, 1)).total_seconds()
			for path, dirs, files in os.walk(spe_dir)::
				for file in files:
					if time.ctime(os.path.getmtime(path+os.sep+file)) <= e_sec
						temp_ret.add(path+os.sep+file)
		elif curr_cmd.endswith("-s"):
			curr_cmd.replace("-s","")
			for path, dirs, files in os.walk(spe_dir):
				for file in files:
					if os.path.getSize(path+os.sep+file) >= int(curr_cmd):
						temp_ret.add(path+os.sep+file)
		elif curr_cmd.endswith("-l"):
			curr_cmd.replace("-l", "")
			for path, dirs, files in os.walk(spe_dir):
				for file in files:
					if os.path.getSize(path+os.sep+file) <= int(curr_cmd):
						temp_ret.add(path+os.sep+file)
					
		elif curr_cmd.endswith("-strict"):
			curr_cmd.replace("-strict", "")
			for path, dirs, files in os.walk(spe_dir):
				for file in files:
					if file == curr_cmd:
						temp_ret.add(path+os.sep+file)
						
		elif curr_cmd.endswith("-leninent"):
			curr_cmd.replace("-leninent", "")
			for path, dirs, files in os.walk(spe_dir):
				for file in files:
					if curr_cmd in file:
						temp_ret.add(path+os.sep+file)
		
		else:
			print "failed, please check your command you typed in"
			return	
		
		ret.intersection(temp_ret)
	
	if not force:
		for file in ret:
			shutil.copyfile(file, output+file)
	else:
		for file in ret:
			shutil.move(file, output+file)
		
#first one
def main(argv):
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
#variables 
config = open("config.txt", "r")	
loc = config.read().split("\n")
output = loc[0]
main_dir = loc[1]

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
