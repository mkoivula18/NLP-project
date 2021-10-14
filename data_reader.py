from datetime import datetime

import progressbar as pb

import csv



start = datetime.now()
file = 'C:/lipasto/NLP/data/s24_2001_short.vrt'
num_lines = sum(1 for line in open(file, encoding='utf8'))
print(f"Num of lines: {num_lines}")


with open(file, encoding='utf8') as src:
	
		in_sentence = False
		text_body = ''
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
					csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

					#do something with the data
					#print("######################################")
					thread_start = True
					for i in text:

						if i.startswith("<text"):
							#sentence = []
							#text_body = ''
							attributes = i.split()
							if "msg_type=\"thread_start\"" not in attributes:
								thread_start = False
								break
							else:
								thread_start = True
							for attribute in attributes:

								if attribute.startswith('datetime='):
									#pass
									#save data
									datetime = attribute.lstrip("datetime=\"")
									sentence.append(datetime)
									#print(attribute)
								elif attribute.startswith('thread_id='):
									#pass
									#save data
									attribute = attribute.lstrip("thread_id=")
									attribute = attribute.lstrip("\"")
									attribute = attribute.rstrip("\"")
									thread_id = attribute
									sentence.append(thread_id)
									#print(attribute)
						if thread_start == False:
							break
						elif i.startswith("<sentence id="):
							in_sentence = True
							#sentence = []
							#text_body = ''
							#sentence.append(datetime)
							#sentence.append(thread_id)
							continue
						elif i.startswith("</sentence>"):
							
							in_sentence = False
							
							#print(sentence)
							continue
						elif in_sentence == True:
							#a single word inside a sentence
							words = i.split()
							text_body += words[2] + ' '
					if thread_start:
						sentence.append(text_body)
						csv_writer.writerow(sentence)
						sentence = []
						text_body = ''
				

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