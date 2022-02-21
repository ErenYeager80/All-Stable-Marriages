from termcolor import colored
from itertools import permutations
# guyprefers = {
# 'A': ['c', 'b', 'd', 'a'],
# 'B': ['b', 'a', 'c', 'd'],
# 'C': ['b', 'd', 'a', 'c'],
# 'D': ['c', 'a', 'd', 'b']}
# galprefers = {
# 'a': ['A', 'B', 'D', 'C'],
# 'b': ['C', 'A', 'D', 'B'],
# 'c': ['C', 'B', 'D', 'A'],
# 'd': ['B', 'A', 'C', 'D']}

guyprefers = {
'A': ['a', 'b', 'c'],
'B': ['b', 'c', 'a'],
'C': ['c', 'a', 'b']}
galprefers = {
'a': ['B', 'C', 'A'],
'b': ['C', 'A', 'B'],
'c': ['A', 'B', 'C']}

guys = sorted(guyprefers.keys())
gals = sorted(galprefers.keys())


def check(engaged):
inverse_engaged = dict((v, k) for k, v in engaged.items())
for she, he in engaged.items():
she_likes = galprefers[she]
she_likes_better = she_likes[:she_likes.index(he)]
he_likes = guyprefers[he]
he_likes_better = he_likes[:he_likes.index(she)]
for guy in she_likes_better:
guys_girl = inverse_engaged[guy]
guy_likes = guyprefers[guy]
if guy_likes.index(guys_girl) > guy_likes.index(she):
return (False,"%s and %s like each other better than "
"their present partners: %s and %s"
%(she, guy, he, guys_girl))
for gal in he_likes_better:
girls_guy = engaged[gal]
gal_likes = galprefers[gal]
if gal_likes.index(girls_guy) > gal_likes.index(he):
return (False,"%s and %s like each other better than "
"their present partners: %s and %s"
%(he, gal, she, girls_guy))
return True, ''


valid_pairings = [sorted(zip(i, guys)) for i in permutations(gals)]
color = 'green'
for pair in valid_pairings:
(r,m)=check(dict(pair))
if r:
color='green'
else:
color='red'
print(colored("Man",color),colored( "Woman",color))
for (woman, man) in pair:
print('',colored( man,color), ' ',colored( woman,color))
print(colored(m,'red'))

print('--------')
