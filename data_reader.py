from datetime import datetime

import progressbar as pb

import csv



start = datetime.now()
file = 'C:/lipasto/NLP/data/s24_2001.vrt'
num_lines = sum(1 for line in open(file, encoding='utf8'))
print(f"Num of lines: {num_lines}")


with open(file, encoding='utf8') as src:
	
		in_sentence = False
		#print(src)
		sentence = []
		j = 0
		text = []
		for line in src:
			#print(f"{i} ---- {line}")
			if line.startswith('<text'):
				#empty the list
				text = []
			if line.startswith('<!--'):
				continue
			text.append(line)
			if line.startswith('</text>'):
				with open('NLP-database.csv', mode='a', encoding='utf8') as csv_file:
					csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

					#do something with the data
					#print("######################################")
					thread_start = True
					for i in text:

						if i.startswith("<text"):
							attributes = i.split()
							for attribute in attributes:
								if "msg_type=\"thread_start\"" not in attributes:
									thread_start = False
									break
								else:
									thread_start = True
								if attribute.startswith('datetime='):
									#pass
									#save data
									datetime = attribute.lstrip("datetime=\"")
									#print(attribute)
								if attribute.startswith('thread_id='):
									#pass
									#save data
									attribute = attribute.lstrip("thread_id=")
									attribute = attribute.lstrip("\"")
									attribute = attribute.rstrip("\"")
									thread_id = attribute
									#print(attribute)
						if thread_start == False:
							break
						elif i.startswith("<sentence id="):
							in_sentence = True
							sentence = []
							sentence.append(datetime)
							sentence.append(thread_id)
							continue
						elif i.startswith("</sentence>"):
							in_sentence = False
							csv_writer.writerow(sentence)
							#print(sentence)
							continue
						elif in_sentence == True:
							#a single word inside a sentence
							words = i.split()
							sentence.append(words[2])
			

				#print(i)
#print(datetime.now()-start)
"""
for text in texts:
	print(type(text))
	words = text.split()
	for word in words:
		if word.startswith('datetime='):
			print(word)
		elif word.startswith('author='):
			print(word)
		elif word.startswith('thread_id='):
			print(word)
	#for letter, num in enumerate(text):
	#	print(letter, num)

"""