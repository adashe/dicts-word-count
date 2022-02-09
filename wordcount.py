"""Count words in file."""


# put your code here.

word_count = {}



def count_words(file):
    
    """Opens a text file and counts each comma-separated word"""

    text = open(file)
    for line in text:
        line = line.rstrip()
        words = line.split(' ')
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(word, count)

# count_words('test.txt')
count_words('twain.txt')