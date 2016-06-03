#!/usr/bin/python
import sys, os, ntpath, shutil

def help():
    print "Usage: python copy.py [PATH]\nPATH refers to the path to a file that you want to be copied to the usb"
	
#first one
def main(argv):
    if len(argv) == 1 or argv[1] == "help":
        help()
    else:
		file = argv[1]
        #Move the file to the USB!
		if(os.path.isfile(file)):
			file_name = ntpath.basename(file)
			if(len(argv) == 2):
				
				
			shutil.copyfile(file, "D:/"+file_name)
			#os.rename(file, "D:/"+file_name)
		elif(os.path.isdir(file)):
			dir = ntpath.basename(file)
			#print "DIR " + dir
			shutil.copytree(file, "D:/"+dir)
#main
if __name__ == '__main__':
    main(sys.argv);
