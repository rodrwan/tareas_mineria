from svmlight import *
f = DocumentFactory()
resto = [f.new(x.split()) for x in [
        "this is a nice long document",
        "this is another nice long document",
        "this is rather a short document",
        "a horrible document",
        "another horrible document",
        "MC DONALDS CANTAG",
        "JOHNNY ROCKETS",
        "RESTAURANTE MANCH",
        "POP Y ROLL S",
        "TIP Y TAP",
        "AKAI SUSHI RESTAU",
        "DOMINOS PIZZA COS",
        "MC DONALDS EST.CE",
        "APPLEBEE`S",
        "STARBUCKS COFFE"]]

for r in resto:
  print r
print

l = Learner()
model = l.learn(resto, [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1])
# judgments = [model.classify(d) for d in docs]

# print model.plane # Vectores de soporte
# print model.bias # bias del modelo
# print
# text = "COMPRA DOMINOS PIZZA COS" # good example
thresh_hold = 0.7
text = "COMPRA PORTAL 1" # bad example
d = f.new(text.split())
if thresh_hold < model.classify(d):
  print "Clasifica"
else:
  print "No clasifica"