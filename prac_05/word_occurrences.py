# text = input("Text: ")
word_count = {}
text = "hello my name is kieren hello"
words = text.split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

words = list(word_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))

