import math
class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.contents_remainder = self.contents.split() #setting the contents as a list contained in self.contents_remainder

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return math.ceil(self.count_words()/ wpm )
        

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        num_words_can_read =  minutes * wpm #the number of words that a person can read given the time available
        
        if self.count_words() <= num_words_can_read: #if the time it takes to read the text is less than the availale time, it will return the text
            return self.contents
        else: # for the case where the length of the words will now be greater than that number of words the person can read in the time given
            #for the case that the length of the whole text is the same as when started, only take the first nums can read
            # or the case where now the remainder is different , i.e should be smaller, but not equal to zero
            if len(self.contents_remainder) == self.contents.split() or len(self.contents_remainder) >= num_words_can_read:
                contents_chunk = " ".join(self.contents_remainder[0:num_words_can_read]) #create the string from the joining of the list with spaces to give the contents chunk
                self.contents_remainder = self.contents_remainder[num_words_can_read:] #set the remainder to now start from the next index along, until the end
                return f"{contents_chunk}" # return the string of the contents_sliced
            # for the case where len(self.contents_remainder) <= num_words_can_read:
            else:
                the_last_bit_of_text = " ".join(self.contents_remainder)
                self.contents_remainder = self.contents.split() # resetting the clock
                return the_last_bit_of_text
                
            
        
diaryentry = DiaryEntry("Today's date", "This was a difficult task! How did it take me so  long??!?!?")
print(f"The formatted version is: {diaryentry.format()}")
print(f"the number of words is : {diaryentry.count_words()}")
print(f"the reading time is given 2 words per minute is, given i have used ceiling (conservative): {diaryentry.reading_time(2)}")
print(f"The reading chunk is this given 4 words per minute and given 3 minutes to read it!:  {diaryentry.reading_chunk(4,3)}")
print(f"The next reading chunk is this given 4 words per minute and given 3 minutes to read it!:  {diaryentry.reading_chunk(4,3)}")
print(f"The next reading chunk is this given 4 words per minute and given 3 minutes to read it!:  {diaryentry.reading_chunk(4,3)}")
print(f"The next reading chunk is this given 4 words per minute and given 3 minutes to read it!:  {diaryentry.reading_chunk(4,3)}")
print(f"The next reading chunk is this given 4 words per minute and given 3 minutes to read it!:  {diaryentry.reading_chunk(4,3)}")
print(f"The next reading chunk is this given 4 words per minute and given 3 minutes to read it!:  {diaryentry.reading_chunk(4,3)}")
print(f"The next reading chunk is this given 4 words per minute and given 3 minutes to read it!:  {diaryentry.reading_chunk(4,3)}")
print(f"The next reading chunk is this given 4 words per minute and given 3 minutes to read it!:  {diaryentry.reading_chunk(4,3)}")