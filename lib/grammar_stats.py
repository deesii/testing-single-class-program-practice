class GrammarStats:
    def __init__(self):
        self.int_pass = 0
        self.int_not_pass = 0
        pass

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if type(text) == str and len(text) > 0 and text[0] == text[0].upper() and text[-1] in '!?.':
            self.int_pass += 1
            return True
        else:
            self.int_not_pass += 1
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        try:
            return int(self.int_pass/(self.int_not_pass + self.int_pass)*100)
        except ZeroDivisionError:
            return 0

