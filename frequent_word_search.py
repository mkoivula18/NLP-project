import csv
from collections import Counter


file = 'NLP-database.csv'
def main():
	word1 = 'iloinen'
	word2 = 'surullinen'
	search_frequent_words(word1)
	search_frequent_words(word2)

def search_frequent_words(used_word):
	final_words = []
	with open(file, newline='', encoding='utf8') as src:
		reader = csv.reader(src, delimiter=';')
		i = 0
		for row in reader:
			#if i == 0:
			
			if row != []:
				text = row[2]
				#print(text)
				#print(type(text))
				text_to_list = text.split()
				#print(text_to_list)
				for index, word in enumerate(text_to_list):
					#print(f"ID: {index} - word: {word}")
					if word == used_word:
						#print(index, word)
						lexical_distance_words = []
						try:
							lexical_distance_word1 = text_to_list[index-2]
						except IndexError as e:
							#print(e)
							lexical_distance_word1 = ''
						finally:
							lexical_distance_words.append(lexical_distance_word1)


						try:
							lexical_distance_word2 = text_to_list[index-1]
						except IndexError as e:
							#print(e)
							lexical_distance_word2 = ''
						finally:
							lexical_distance_words.append(lexical_distance_word2)


						try:
							lexical_distance_word3 = text_to_list[index+1]
						except IndexError as e:
							#print(e)
							lexical_distance_word3 = ''
						finally:
							lexical_distance_words.append(lexical_distance_word3)


						try:
							lexical_distance_word4 = text_to_list[index+2]
						except IndexError as e:
							#print(e)
							lexical_distance_word4 = ''
						finally:
							lexical_distance_words.append(lexical_distance_word4)

						#print(f"2 units lexical distance words for word \"{word1}\" are: "
						#	f"1. {lexical_distance_words[0]} - 2. {lexical_distance_words[1]} - 3. {lexical_distance_words[2]} - 4. {lexical_distance_words[3]} ")
						for lexical_distance_word in lexical_distance_words:
							if lexical_distance_word != '':
								final_words.append(lexical_distance_word)


			i += 1
		#print(i)

	#print(final_words)

	word_counts = Counter(final_words)
	print(f"10 Most common word in 2 units lexical distance for word: \"{used_word}\" are:")
	print(word_counts.most_common(10))

if __name__ == '__main__':
	main()