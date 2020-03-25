

def lower_clean_str(x):
  punc='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~1234567890'
  lowercased_str = x.lower()
  for ch in punc:
    lowercased_str = lowercased_str.replace(ch, '')
  return lowercased_str

input_file_1 = sc.textFile("C:\\Users\\sures\\OneDrive\\Documents\\Downloaded_data_files\\assignment_2_datafile.txt")
one_RDD = input_file_1.map(lower_clean_str)
map_words = one_RDD.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
filtered = map_words.filter(lambda word: len(word[0])>3)
counts_filtered = filtered.reduceByKey(lambda a, b: a + b)
counts_filtered.saveAsTextFile("C://Users//sures//OneDrive//Documents//spark_assignment_2_final_submission.txt")