
# Name 1: Hoang Minh Nguyen
# EID 1: htn937

# Name 2:
# EID 2:

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size(s, const):
    key_value = 0
    for char in s:
        letter = ord(char) - 96
        key_value = (key_value * 26 + letter)
    return const - (key_value%const)

def insert_word(s, hash_table):
    index = hash_word(s, len(hash_table))
    step = step_size(s, 3)
    while hash_table[index] != "":
        index = (index + step) % len(hash_table)
    hash_table[index] = s
    

def find_word(s, hash_table):
    index = hash_word(s, len(hash_table))
    step = step_size(s, 3)
    while hash_table[index] != "":
        if hash_table[index] == s:
            return True
        index = (index + step) % len(hash_table)
    return False

def english_list(word, hash_table):
    reducible_words = []
    if not find_word(word,hash_table):
        return reducible_words
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in ["a","o","i"] or find_word(new_word,hash_table):
                
            reducible_words.append(new_word) 
         
    return reducible_words
def is_reducible(s, hash_table, hash_memo):
    
    if s == "a" or s == "o" or s == "i":
        if not find_word(s, hash_memo):
            insert_word(s, hash_memo)
        return True
    if find_word(s,hash_memo):
        return True
    reducible = False            
    for english_word in english_list(s, hash_table):
        if is_reducible(english_word, hash_table, hash_memo):
            if not find_word(english_word, hash_memo) :        
                insert_word(english_word,hash_memo)
            reducible =True
    if reducible:
        insert_word(s,hash_memo)
    return reducible

def get_longest_words(string_list):
    longest_words = []
    max_length = 0
    for string in string_list:
        if len(string) > max_length:
            max_length = len(string)
            longest_words = [string]
        elif len(string) == max_length:
            longest_words.append(string)
    return longest_words
def main():
    # create an empty word_list

    word_list = []
    
    # read words from words.txt and append to word_list
    # This is an alternative way to input()
    # since sys.stdin is standard input, and standard input
    # can be treated like a file.
    # Recall that standard input is just your terminal,
    # or whatever file you use input redirection with
    for line in sys.stdin:
        line = line.strip()
       
        word_list.append(line)

    # find length of word_list
    length_word_list=len(word_list)
    
    # determine prime number N that is greater than twice
    # the length of the word_list
    N = length_word_list * 2
    while not is_prime(N):
        N += 1
   
    # create an empty hash_list
    # populate the hash_list with N blank strings
    hash_list=[""] * N
    # hash each word in word_list into hash_list
    # for collisions use double hashing 

    for word in word_list:
        
        insert_word(word,hash_list)
    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list
 
    M = length_word_list * 0.2
    while not is_prime(N):
        M += 1

    # populate the hash_memo with M blank strings
    hash_memo_table=[""]*int(M)
    # create an empty list reducible_words
    reducible_words=[]
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.
    for word in word_list:
        if find_word (word,hash_memo_table) is True:
            reducible_words.append(word)
            continue
        if is_reducible(word,hash_list,hash_memo_table) is True:
            reducible_words.append(word)

    #print(hash_memo_table[hash_word("a",len(hash_list))],hash_memo_table[hash_word("i",len(hash_list))],hash_memo_table[hash_word("o",len(hash_list))])
    # find the largest reducible words in reducible_words
    longest_reducible_wordlist=get_longest_words(reducible_words)
    # print the reducible words in alphabetical order
    # one word per line

    longest_reducible_wordlist.sort()
    
    for i in longest_reducible_wordlist:
        print(i,sep="\n")

if __name__ == "__main__":
    main() 