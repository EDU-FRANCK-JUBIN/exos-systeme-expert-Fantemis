from pyDatalog import pyDatalog
pyDatalog.clear()
pyDatalog.create_terms('frog,croakes,eatflies,canary,chrips,sings,green,yellow,X')
frog(X) <= croakes(X) & eatflies(X)
canary(X) <= chrips(X) & sings(X)
green(X) <= frog(X)
yellow(X) <= canary(X)

+croakes("fritz")
+eatflies("fritz")

+chrips("titi")
+sings("titi")

query = "frog(X)"
answers = pyDatalog.ask(query).answers
print(answers)

query = "yellow(X)"
answers = pyDatalog.ask(query).answers
print(answers)

print(pyDatalog.ask("frog('fritz')"))
print(pyDatalog.ask("frog('bretzel')"))