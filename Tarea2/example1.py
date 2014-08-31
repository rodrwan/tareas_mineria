import MontyLemmatiser
import MontyLingua

theTagger = MontyLingua.MontyLingua()

String = "Yeah , it will . Did you pour it on your guitar ? Strings are cheap and replaced every month . Hopefully it was all that got Sulfur on it ."

String = "I had a debt judgement in 2008 , has the statute of limitations passed ? I'm in New York ?"
p = MontyLemmatiser.MontyLemmatiser()

newString = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), String.split())
print "old string: " + String

print "new string: " + " ".join(newString)
print
#tokenized the String
tokenizedString = theTagger.tokenize(String)
#Tag the tokenized String
tagString = theTagger.tag_tokenized(tokenizedString)
print tagString
print
#A more simple way to tag the String
tagString = theTagger.jist(String)
print tagString