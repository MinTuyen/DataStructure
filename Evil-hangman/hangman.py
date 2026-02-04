

# Name of the dictionary file.
# Change to dictionary.txt for full version of the game.
#DICTIONARY_FILE = "smallDictionary.txt"
DICTIONARY_FILE = "dictionary.txt"
import random
class Hangman:
    """
    Manages the details of Evil Hangman. This class keeps
    tracks of the possible words from a dictionary during
    rounds of hangman, based on guesses so far.
    """

    def __init__(self, words, debug=True):
        """
        Create a new Hangman from the provided set of words and phrases.
        :param words: A set with the words for this instance of Hangman.
        :param debug: True if we should print out debugging to terminal.
        """
        self.__difficulty = None
        self.__player_guesses = []
        self.__debug = debug
        self.__secret_word=None
        self.__originaldict=words
        self.wordlist=words
        self.__guess=None
        self.__pattern=None
        self.__num_guesses=None
        self.__map_pattern=None
        

    def num_words(self, length):
        """
        Get the number of words in this Hangman of the given length.
        :param length: The given length to check.
        :return: the number of words in the original Dictionary
        with the given length
        """
       
        self.__length = length
        wordlist = [word for word in self.__originaldict if len(word) == self.__length]

        return len(wordlist)

    def prep_for_round(self, word_len, num_guesses, diff):
        """
        Get for a new round of Hangman.
        :param word_len: the length of the word to pick this time.
        :param num_guesses: the number of wrong guesses before the
                            player loses the round.
        :param diff: The difficulty for this round.
        """
        self.__difficulty = diff.lower()
        self.__length=word_len
        self.__num_guesses=num_guesses
        self.__player_guesses = []
        self.__secret_word=None
        self.wordlist=self.__originaldict
        self.__guess=None
        self.__pattern="-"*word_len
        self.__map_pattern=None
        

        
    def num_words_current(self):
        """
        The number of words still possible (active) based on the guesses so far.
        :return: the number of words that are still possibilities based on the
        original dictionary and the guesses so far.
        """
        wordlist=[]
        for i in self.wordlist:
            if len(i)==self.__length:
                wordlist.append(i)
        self.wordlist=wordlist
        return len(self.wordlist)

    def get_guesses_left(self):
        
        """
        Get the number of wrong guesses the user has left in
        this round (game) of Hangman.
        :return: the number of wrong guesses the user has left
                in this round (game) of Hangman.
        """

        return self.__num_guesses

    def get_guesses_made(self):
        """
        Return a string that contains the letters the user has guessed so far during this round.
        The characters in the string are in alphabetical order.
        The string is in the form [let1, let2, let3, ... letN].
        For example, if the user has guessed 'a', 'c', 'e', 's', 't', and 'z', the string would be '[a, c, e, s, t, z]'.
        
        :return: A string that contains the letters the user has guessed so far during this round.
        """
        if len(self.__player_guesses)==0:
            return "[]"
        
        return "['"+ "', '".join(self.sort(self.__player_guesses)) +"']"

    def already_guessed(self, guess):
        """
        Check the status of a character.
        :param guess: The character to check.
        :return: true if guess has been used or guessed this round of Hangman,
                 false otherwise.
        """
        if guess in self.__player_guesses:
            return True
        else:
            return False
        

    def get_pattern(self):
        """
        Get the current pattern. The pattern contains '-''s for
        unrevealed (or guessed) characters and the actual character
        for "correctly guessed" characters.
        :return: the current pattern.
        """
        wordlist=[]
        for i in self.wordlist:
            if len(i)==self.__length:
                wordlist.append(i)
        self.wordlist=wordlist

        return self.__pattern

    def make_guess(self, guess):
        """
        Update the game status (pattern, wrong guesses, word list),
        based on the given guess.
        :param guess: the current guessed character
        :return: a dict with the resulting patterns and the number of
        words in each of the new patterns.
        The return value is for testing and debugging purposes.
        """
        self.__guess = guess
        
        dict_pattern=dict()
        return_dict=dict()
        
        self.__player_guesses.append(self.__guess)

        for word in self.wordlist:
            if self.make_dash_pattern(word, self.__guess) not in dict_pattern:
                dict_pattern[self.make_dash_pattern(word, self.__guess)]=set()
            dict_pattern[self.make_dash_pattern(word, self.__guess)].add(word)

        pattern_ordered=self.order_entries(dict_pattern)
        if self.__difficulty == "hard":
            self.wordlist=list(pattern_ordered[0][3])
            self.__pattern=pattern_ordered[0][2]
        if self.__difficulty=="medium" or self.__difficulty=="easy":
            self.wordlist=list(pattern_ordered[self.get_difficulty(pattern_ordered)][3])
            self.__pattern=pattern_ordered[self.get_difficulty(pattern_ordered)][2]
        if self.__num_guesses != None and self.already_guessed(self.__guess) == False or self.__guess not in self.__pattern:
            
            self.__num_guesses -= 1
        for pattern, words in dict_pattern.items():
            return_dict[pattern] = len(words)            
        
        return return_dict
    

    def get_map_pattern(self, guess):
        """
        Precondition: guess has not been guessed before in this round.
        Postcondition: Returns a dictionary that maps patterns to a list of words that 
                       follow said pattern.
        
        :param guess: The current guessed character.
        :return: A dictionary that maps patterns to a list of words that follow said pattern.
        """
        dict_pattern=dict()
        for word in self.wordlist:
            pattern= self.make_dash_pattern(word,guess)
            if pattern not in dict_pattern:
                dict_pattern[pattern]=[word]
            else:
                dict_pattern[pattern].append(word)
        self.__map_pattern=dict_pattern
        return self.__map_pattern

    def make_dash_pattern(self, word, guess):
        """
        Precondition: guess has not been guessed before in this round, word is not None.
        Postcondition: Builds possible word patterns for each word based on the user's guess and 
                       the previous pattern.
        
        :param word: The word to build the pattern for.
        :param guess: The current guessed character.
        :return: The dash pattern for the given word based on the user's guess and the previous 
                 dash pattern.
        """

        self.__guess=guess
        pattern=""

        for l in word:
            if l in self.__player_guesses:
                pattern += l
            else:
                pattern += "-"
        self.__pattern= pattern
        return pattern

    def sort(self, entries):
        '''
        Return sorted data. When called by order_entries, entries will be tuples sorted 
        by the number of words in the word list, then the number of dashes in the pattern, 
        then the pattern, and finally the word list itself. 
        Otherwise, entries will be any sortable list. 
        You must make sure that your merge_sort method is generalized with the ability 
        to also sort lists. You must implement merge sort.

        Precondition: entries must be a list of tuples 
        (-size word list, -dash count, pattern, word list) OR any sortable list
        Postcondition: return sorted list of entries. If tuple, first sort by number of words in word list,
        then the dash amount in the pattern, next the lexicographic ordering for the pattern,
        and finally the word list itself
        :param entries: The Family tuples to sort or any sortable list.
        :returns: a new sorted list.
        '''
       

        if len(entries) <= 1:
            return entries[:]
    
        result = []
        mid = len(entries) // 2

        left_list = self.sort(entries[:mid])
        right_list = self.sort(entries[mid:])

        i = 0
        j = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                result.append(left_list[i])
                i += 1
            else:
                result.append(right_list[j])
                j += 1

        for k in range(i, len(left_list)):
            result.append(left_list[k])

        for k in range(j, len(right_list)):
            result.append(right_list[k])
        return result


    def order_entries(self, word_family):
        """
        
        Precondition: word_family is not None.
        Postcondition: For each key-value pair of (pattern, word list) in word_family, a Family 
        tuple (-size word list, -dash count, pattern, word list) is created and added to a list. 
        The entry list is then sorted based on the size of each word list, the number
        of characters revealed in the pattern, and the lexicographical ordering of the patterns.
        
        :param word_family: A dictionary containing patterns as keys and lists of words as values.
        :return: A sorted list of Entry tuples (-size word list, -dash count, pattern, word list).
        """
        list_entries=[]
        for pattern, word_list in word_family.items():
            entry=(-len(word_list), -pattern.count("-"), pattern, word_list)
            list_entries.append(entry)
        
        return self.sort(list_entries)

    def get_diff(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Returns an integer that describes the state of the selection process 
        of word list based on a player's turn and game difficulty.
        Returns a 2 if the AI CAN pick the 2nd hardest word list. For easy mode, it's
        every other valid guess. For medium, it's every 4th valid guess.
        Returns 1 if the AI SHOULD pick the 2nd hardest word list on easy/medium mode,
        but entries.size() <= 1, so it picks the hardest.
        Returns 0 if the AI is picking the hardest list.
        
        :param entries: A list of tuples () representing patterns and associated word lists.
        :return: An integer representing the state of the selection process.
        """
        if not entries:
            raise ValueError("Entries can't be None")
        medium_guess = 4
        easy_mode = "easy"
        medium_mode = "medium"
        if ((self.__difficulty == medium_mode and len(self.__player_guesses) % medium_guess == 0) or
            (self.__difficulty == easy_mode and len(self.__player_guesses) % 2 == 0)):
            if len(entries) > 1:
                return 2
            return 1
        return 0

    def get_difficulty(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Returns the index of the Entry tuple from the list that the AI 
        will choose for its word list/family depending on the state of the selection process.
        
        :param entries: A list of Entry tuples representing patterns and associated word lists.
        :return: The index of the Entry tuple that the AI will choose.
        """
        if not entries:
            raise ValueError("Entries can't be None")
        diff = self.get_diff(entries)
        if diff == 2:
            return 1
        return 0

    def get_secret_word(self):
        """
        Return the secret word this Hangman finally ended up picking 
        for this round. You must sort your word list before picking a 
        secret word. If there are multiple possible words left, one is 
        selected at random. The seed should be initialized to 0 before picking.

        :return: return the secret word the manager picked.
        """
        if len(self.wordlist)==0:
            return None
        if len(self.wordlist)==1:
            self.__secret_word=self.wordlist[0]
            return self.__secret_word

        else:
            sorted_list= self.sort(self.wordlist)
    
            
            random.seed(0)
            self.__secret_word=random.choice(sorted_list)
            return self.__secret_word

    def debugging(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Prints out custom debugging messages about which word family 
        and pattern is chosen depending on difficulty and player's turn.
        """
        sb = []
        diff = self.get_diff(entries)
        sb.append("DEBUGGING: ")
        if diff == 2:
            sb.append("Difficulty second hardest pattern and list.\n\n")
        elif diff == 1:
            sb.append("Should pick second hardest pattern this turn, "
                    + "but only one pattern available.\n")
            sb.append("\nDEBUGGING: Picking hardest list.\n")
        else:
            sb.append("Picking hardest list.\n")

        sb.append("DEBUGGING: New pattern is: ")
        sb.append(self.get_pattern())
        sb.append(". New family has ")
        sb.append(str(self.num_words_current()))
        sb.append(" words.")
        print(''.join(sb))
