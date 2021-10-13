def sentence_maker(phrase):
    checking = ("How","Why","When","What")
    captitalizedphrase = phrase.capitalize()
    if captitalizedphrase.startswith(checking):
        return "%s?" % captitalizedphrase
    else:
        return "%s." % captitalizedphrase

results = []
while(True):
    user_input = input("Say something: ")
    if user_input == '\end':
        break
    else:
        results.append(sentence_maker(user_input))

print(' '.join(results))