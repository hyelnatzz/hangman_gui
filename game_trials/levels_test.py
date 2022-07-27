import random
import db

word_count = db.getRowCount('four')

word_choice_indices = [random.randint(1,word_count) for i in range(4)]

wrd, dfn = db.getWordDetails('four', word_choice_indices[0])
print(dfn)

print(word_count)
print(word_choice_indices)
