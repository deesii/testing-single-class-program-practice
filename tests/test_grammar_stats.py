from lib.grammar_stats import *

# the story:
# I want to see what % of the tests that have been checked so far which passed out of the total
# I want to check whether the first letter and the last index is ok.



#Given an empty string, returns False
def test_input_is_an_empty_string():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("sdsd") == False

#Given a text that starts with capital letter and end with punctuation mark, it returns True
def test_where_text_starts_with_capital_ends_with_suitable_punc_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, today is a very cloudy day!")
    assert result == True

#Given a text that starts with capital letter but doesnt end with suitable punctuation mark, return False
def test_where_text_starts_with_capital_but_doesnt_end_with_suitable_punc_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, today is a very cloudy day")
    assert result == False

#Given a text that doesnt start with capital letter but ends with suitable punctuation mark, return False
def test_where_text_doesnt_start_with_capital_but_ends_with_suitable_punc_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello, today is a very cloudy day!")
    assert result == False

#Given a text which includes multiple punctuation and has a starting capital letter but doesnt have an ending punctuation mark. Outputs False
def test_where_text_has_multiple_punctuation_with_but_first_and_last_letters_are_correct():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Bonjour, today? is a very! cloudy day!")
    assert result == True

#Given a text is not a string, it is a list, returns False
def test_where_input_is_a_list():
    grammar_stats = GrammarStats()
    result = grammar_stats.check(['B','s', 'd', '?'])
    assert result == False

#Given a text is not a string, returns False
def test_where_input_is_not_string():
    grammar_stats = GrammarStats()
    result = grammar_stats.check({'Adam': 'apple', 'Donna': 'pear!'})
    assert result == False


#Given that there is a number of passed checks, and we want to output the correct integer
    
def test_where_only_passed_checks_returns_integer():
    grammar_stats = GrammarStats()
    grammar_stats.check("Bonjour, today? is a very! cloudy day!")
    grammar_stats.check("Hello, today is a very cloudy day!")
    grammar_stats.check("Booopy hiii you're great.")
    grammar_stats.check("Booopy hiii you're silly?")

    assert grammar_stats.percentage_good() == 100

#Given that there is a number of not passed checks, and we want to output the correct integer
    
def test_where_only_non_passed_checks_returns_integer():
    grammar_stats = GrammarStats()
    grammar_stats.check("bonjour, today? is a very! cloudy day!")
    grammar_stats.check("hello, today is a very cloudy day!")
    grammar_stats.check("Booopy hiii you're great/")
    grammar_stats.check("booopy hiii you're silly'")

    assert grammar_stats.percentage_good() == 0


#Given that there is a mix of pass and not passed checks that will not divide to whole number, and we want to output the correct integer, truncate the %
    
def test_where_mixed_passed_checks_returns_integer():
    grammar_stats = GrammarStats()
    grammar_stats.check("Bonjour, today? is a very! cloudy day!")
    grammar_stats.check("spooooot on!!!")
    grammar_stats.check("hello, today is a very cloudy day!")
    grammar_stats.check("Booopy hiii you're great/")
    grammar_stats.check("booopy hiii you're silly'")

    assert grammar_stats.percentage_good() == 20


#Given no checks carried out will output 0
    
def test_where_no_checks_returns_integer():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good() == 0