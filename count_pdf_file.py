
import os
import sys
import re
import time
import PyPDF2


def getWordCount(data):
	# get list of strings sperated by white space
	data=data.split()
	#print(data)
	return len(data)

def main():
	if len(sys.argv)!=2:
		print('command usage: python know_count.py FileName')
		exit(1)
	else:
		pdfFile = sys.argv[1]
		# check if the specified file exists or not
		try:
			if os.path.exists(pdfFile):
				print("file found!")
		except OSError as err:
			print(err.reason)
			exit(1)
		# get the word count in the pdf file
		totalWords = 0

		pdfFileObj = open(pdfFile, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		numPages = pdfReader.numPages

		for i in range(numPages):
			# get the first page of the pdf
			pageObj = pdfReader.getPage(i)
			# extract all text as a string
			text = pageObj.extractText()
			#new_text = re.sub('\s+',' ',text)
			totalWords+=getWordCount(text.strip())


		time.sleep(1)
		print (str(totalWords) +" words in "+pdfFile)

if __name__ == '__main__':
	main()
