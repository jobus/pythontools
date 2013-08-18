""" A simple file reader
"""
import sys

try:
	file = open('newfile.txt', 'r')
	fromFile = file.read()
	strippedFile = int(s.strip())
	print strippedFile
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
