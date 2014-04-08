#! /usr/bin/python

import fileinput
import re
import rumor_detect
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
signalfile = open( 'signal','w+' )
nsignalfile = open( 'nsignal','w+')

for line in fileinput.input():
	line_s = re.sub('\n','',line)
	texts = line_s.split('\t')
	if texts.__len__() >= 5:
		lan = texts[5]
		text = texts[3]
		tid = texts[0]
		ctime = texts[4]
		if lan == 'en':
			signaltext = rumor_detect.in_match(text)
			if signaltext is not None:
				signalfile.write( tid+'\t'+text+'\t'+ctime+'\t'+signaltext+'\n')
				print( tid+'\t'+text+'\t'+ctime+'\t'+signaltext )
			else:
				nsignalfile.write( tid+'\t'+text+'\t'+ctime+'\n')
