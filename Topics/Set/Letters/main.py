word = input()  # the input word
set_of_seen_letters = set()
count = 0

for i in word:
    if i not in set_of_seen_letters:
        set_of_seen_letters.add(i)
        count += 1

print(count)