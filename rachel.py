#!/usr/bin/env python

import sys
import os
import argparse
import subprocess
import shutil


def exists(p):
	return os.path.isfile(p) or os.path.isdir(p)

def check_arguments():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-x', '--kiwix', default = False)
	args = parser.parse_args()
	if not args.kiwix:
		return False
	return True

def cmd(c):
	new_env = os.environ.copy()
	new_env["DEBIAN_FRONTEND"] = "noninteractive"
	result = subprocess.Popen(c, shell = True, env = new_env)
	try:
		result.communicate()
	except KeyboardInterrupt:
		pass
	return (result.returncode == 0)

def sudo(s):
	return cmd("sudo %s" % s)

def die(d):
	print d
	sys.exit(1)


# Run the script
os.chdir("/tmp/rachel_installer")
if check_arguments():
	sudo("python installer.py --kiwix") or die("Installation (+KiwiX) failed.")
else:
	sudo("python installer.py") or die("Installation failed.")