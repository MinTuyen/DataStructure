# Name 1:Hoang Minh Nguyen
# EID 1:htn937

# Name 2:
# EID 2:

import sys
#  Input: string is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of string
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(string, key):
    "rail fence encode"
    word=string
    rows= key
    cols= len(string)
    str = ""
    cipher_list = [[0 for i in range (cols)] for j in range (rows)]
    a=0
    b=key-1
    for c in range (cols):
        if a<rows:
            for r in range (rows):
                if r==a:
                    cipher_list[r][c]=word[c]
            a+=1
        if a==rows:
            for r in range (rows-1,-1,-1):
                if r==b:
                    cipher_list[r][c]=word[c]
            b-=1
            if b==0:
                a=0
                b=key-1
    for r in range (rows):
        for c in range (cols):
            if cipher_list[r][c]!= 0:
                str += cipher_list[r][c]
            else:
                str += ""
    return str # placeholder for the actual return statement


#  Input: string is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of string
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(string, key):
    "rail fence decode"
    word=string
    rows= key
    cols= len(string)
    str = ""
    cipher_list = [[0 for i in range (cols)] for j in range (rows)]
    a=0
    b=key-1
    p=0
    for c in range (cols):
        if a<rows:
            for r in range (rows):
                if r==a:
                    cipher_list[r][c]="yes"
            a+=1
        if a==rows:         
            for r in range (rows-1,-1,-1):
                if r==b:
                    cipher_list[r][c]="yes"
            b-=1
            
            if b==0:
                a=0
                b=key-1
    for r in range (rows):
        for c in range (cols):
            if cipher_list[r][c] != 0:
                cipher_list[r][c]= word[p]
                p+=1
            else:
                str += ""
    for c in range(cols):
        for r in range(rows):
            if cipher_list[r][c]!=0:
                str += cipher_list[r][c]
            else:
                str +=""
    return str  # placeholder for the actual return statement
#  Input: string is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(string):
    "filter string"
    lowercase= string.lower()
    letter_list= [l for l in lowercase if l.isalpha()==True ]
    str =""
    for i in letter_list:
        str += i
    return str # placeholder for the actual return statement
#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
 # placeholder for actual return statement
#  Input: p is a character in the pass phrase and s is a character
#         in the cipher text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
# placeholder for actual return statement
#  Input: string is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(string, phrase):
    "vigenere encode"
    pass_phrase=phrase
    words=filter_string(string)
    encoded_word=""
    phrase_word=""
    while len(phrase_word) < len(words):
        for i in pass_phrase:
            if len(phrase_word) < len(words):
                phrase_word += i
            else:
                break
    for l in range (len(words)):
        letter= chr(ord(phrase_word[l])+((ord(words[l])-ord("a"))))
        if ord(letter)>ord("z"):
            letter=chr(ord(letter)-ord("z")+ord("a")-1)
        encoded_word+=letter

    return encoded_word  # placeholder for the actual return statement


#  Input: string is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(string, phrase):
    "vigenere decode"
    pass_phrase=phrase
    words=filter_string(string)
    decoded_word=""
    phrase_word=""
    while len(phrase_word) < len(words):
        for i in pass_phrase:
            if len(phrase_word) < len(words):
                phrase_word += i
            else:
                break
    for l in range (len(words)):
        letter= chr(ord("a")+((ord(words[l])-ord(phrase_word[l]))))
        if ord(letter)<ord("a"):
            letter=chr(ord("z")-(ord("a")-ord(letter)-1))
        decoded_word+=letter
    return decoded_word 
      # placeholder for the actual return statement


def main():
    "main run all code"
    input_list=[]
    for line in sys.stdin:
        input_list.append(line.strip())
     # read the plain text from stdin
    print()
    print("Rail Fence Cipher")
    print()
    input_plain_text=input_list[0]
    print("Plain Text:", input_plain_text)
    # read the key from stdin
    key_encode=int(input_list[1])
    print("Key:", key_encode)
    # encode and print the encoded text using rail fence cipher
    print("Encoded Text:", rail_fence_encode(input_plain_text,key_encode))
    # read encoded text from stdin
    print()
    input_encoded_text=input_list[2]
    print("Encoded Text:", input_encoded_text)
    # read the key from stdin
    key_decode=int(input_list[3])
    print("Enter Key:", key_decode)
    # decode and print the plain text using rail fence cipher 
    print("Decoded Text:", rail_fence_decode(input_encoded_text,key_decode))
    # read the plain text from stdin
    print()
    print("Vigenere Cipher")
    print()
    input_text=input_list[4]
    print("Plain Text:", input_text)
    # read the pass phrase from stdin
    pass_phrase=input_list[5]
    print("Pass Phrase:", pass_phrase)
    # encode and print the encoded text using Vigenere cipher
    print("Encoded Text:", vigenere_encode(input_text,pass_phrase))
    # read the encoded text from stdin
    print()
    encoded_text=input_list[6]
    print("Encoded Text:", encoded_text)
    # read the pass phrase from stdin
    pass_phrase2=input_list[7]
    print("Pass Phrase:", pass_phrase2)
    # decode and print the plain text using Vigenere cipher
    print("Decoded Text:",vigenere_decode(encoded_text,pass_phrase2))
    # placeholder for the main function


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
