import MontyLemmatiser

# theTagger = MontyLingua.MontyLingua()

String = "Yeah , it will . Did you pour it on your guitar ? Strings are cheap and replaced every month . Hopefully it was all that got Sulfur on it ."

p = MontyLemmatiser.MontyLemmatiser()

newString = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), String.split())
print "old string: " + String

print "new string: " + " ".join(newString)
#tokenized the String
#Tag the tokenized String
# tagString = theTagger.tag_tokenized(tokenizedString)
#A more simple way to tag the String
# tagString = theTagger.jist(String)