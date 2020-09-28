import csv

#Read the CSV with filename, line, original, translated
#Make every ansewer from original and translated columns a single txt file. This text file will be submitted to Biber's tagger to count the features

def save(original, translated, filename):
    #saving original
	transArray = translated.split(".")
	origArray = translated.split(".")
	if (len(transArray) <= 2):
		print("Alert found one")
		print(transArray)
	newfile_original = 'C:\\Users\\Tyler\\Downloads\\or_' + filename + '.txt'
	with open(newfile_original, "w+") as or_file:
		for listItem in range(len((origArray))):
			if (listItem == 0):
				or_file.write(origArray[listItem] + ".\n")
			elif (origArray[listItem] == ""):
				or_file.write(origArray[listItem][1:])
			else:
				or_file.write(origArray[listItem][1:] + ".\n")
		or_file.write("\n")
		#or_file.write(original + "\n")
	or_file.close()
	#saving translated
	newfile_translated = 'C:\\Users\\Tyler\\Downloads\\tr_' + filename + '.txt'

	if (len(origArray) <= 2):
		print("Alert found one")
		print(origArray)

	with open(newfile_translated, "w+") as tr_file:
		for listItem in range(len((transArray))):
			if (listItem == 0):
				tr_file.write(transArray[listItem] + "\n")
			elif (transArray[listItem] == ""):
				tr_file.write(transArray[listItem][1:])
			else:
				tr_file.write(transArray[listItem][1:] + ".\n")
		tr_file.write("\n")
	tr_file.close()

"""MAIN FUNCTION"""
with open('FramesStudy_Sentences - Final.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		#if line_count != 0:
			filename = '_'.join([row["Filename"],row["Line"]])
			print(filename)
			original = row["Original"]
			translated = row["Translated"]
			save(original, translated, filename)
		#else:
		#	print(row)
			line_count += 1
	print(f'Processed {line_count} lines.')
	
	