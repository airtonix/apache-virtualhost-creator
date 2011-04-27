#!/usr/bin/env python
from shutil import copy2, copystat, Error
import os, sys
import glob

def copytree(src, dst, symlinks=False, ignore=None):
	names = os.listdir(src)
	if ignore is not None:
		ignored_names = ignore(src, names)
	else:
		ignored_names = set()

	try:
		os.makedirs(dst)
	except OSError, exc:
		# XXX - this is pretty ugly
		if "file already exists" in exc[1]:	# Windows
			pass
		elif "File exists" in exc[1]:				# Linux
			pass
		else:
			raise

	errors = []
	for name in names:
		if name in ignored_names:
			continue
		srcname = os.path.join(src, name)
		dstname = os.path.join(dst, name)
		try:
			if symlinks and os.path.islink(srcname):
				linkto = os.readlink(srcname)
				os.symlink(linkto, dstname)
			elif os.path.isdir(srcname):
				copytree(srcname, dstname, symlinks, ignore)
			else:
				copy2(srcname, dstname)
			# XXX What about devices, sockets etc.?
		except (IOError, os.error), why:
			errors.append((srcname, dstname, str(why)))
		# catch the Error from the recursive copytree so that we can
		# continue with other files
		except Error, err:
			errors.extend(err.args[0])
	try:
		copystat(src, dst)
	except OSError, why:
		errors.extend((src, dst, str(why)))
	if errors:
		raise Error, errors

def read_file(filepath=None):
	if filepath == None :
		return "file not found : {0}".format(filepath)

	doc_file = open(filepath)
	doc_file_contents = doc_file.read()
	doc_file.close()
	return doc_file_contents

