def compute_score(common):
    if not common:
        return 0
    score = 0
    for c in common:
        if c.isupper():
            score += ord(c) - 38
        else:
            score += ord(c) - 96
    return score

def find_common(rucksack):
    midpoint = int((len(rucksack)) / 2)
    section1, section2 = rucksack[:midpoint], rucksack[midpoint:]
    return set(section1) & set(section2)
with open("input.dat") as fp:
    rucksacks = fp.readlines()

score = 0
for rucksack in rucksacks:
    common = find_common(rucksack)
    score += compute_score(common)
    
print(score)

# Part two
score = 0
def find_common_multiple(window):
    return set(window[0].replace("\n", "")) & set(window[1].replace("\n", "")) & set(window[2].replace("\n", ""))

for i in range(0, len(rucksacks), 3):
    common = find_common_multiple(rucksacks[i:i+3])
    score += compute_score(common)

print(score)
