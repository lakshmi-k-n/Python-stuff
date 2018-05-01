import sys
import string
import random


text1="""The evening of the very day on which they went brought a note
from Mr. Elton to Mr. Woodhouse, a long, civil, ceremonious note,
to say, with Mr. Elton's best compliments, "that he was proposing
to leave Highbury the following morning in his way to Bath;
where, in compliance with the pressing entreaties of some friends,
he had engaged to spend a few weeks, and very much regretted
the impossibility he was under, from various circumstances of
weather and business, of taking a personal leave of Mr. Woodhouse,
of whose friendly civilities he should ever retain a grateful sense--
and had Mr. Woodhouse any commands, should be happy to attend to them."

Emma was most agreeably surprized.--Mr. Elton's absence just
at this time was the very thing to be desired.  She admired
him for contriving it, though not able to give him much credit
for the manner in which it was announced.  Resentment could not
have been more plainly spoken than in a civility to her father,
from which she was so pointedly excluded.  She had not even a
share in his opening compliments.--Her name was not mentioned;--
and there was so striking a change in all this, and such an
ill-judged solemnity of leave-taking in his graceful acknowledgments,
as she thought, at first, could not escape her father's suspicion."""

text="""Yeah, yeah (Deko)
Whoa, hold on (OG Parker)
Uh
Walk it, like I talk it (walk it)
Walk it, like I talk it
Walk it, walk it like I talk it (woo!)
Walk it, like I talk it (yeah!)
Walk it, like I talk it (walk it)
Walk it, like I talk it
Walk it, walk it like I talk it (woo!)
Walk it, like I talk it (hey!)
Walk it, like I talk it (walk it)
Walk it, like I talk it (walk it)
Walk it, like I talk it
Walk it, walk it like I talk it (woo!)
Walk it, like I talk it (talk it)
Walk it, like I talk it (ayy!)
Walk it, like I talk it
Walk it, walk it (woo)
Like I talk it (yeah!)
Take my shoes and walk a mile
Something that you can't do (woo, hey!)
Big talks of the town, big boy gang moves (gang moves!)
I like to walk around with my chain loose (chain, chain!)"""

text3="""The evening of the very day on which they went brought a note
from Mr. Elton to Mr. Woodhouse, a long, civil, ceremonious note,
to say, with Mr. Elton's best compliments, "that he was proposing
to leave Highbury the following morning in his way to Bath;
where, in compliance with the pressing entreaties of some friends
"""
dict={}
w=""
def mark_dict(text,offset):
  global dict
  global w
  list=text.split(" ")
  l=len(list)
  off2=0
  for i in range(l):
    if i+offset+1 <= l-1:
      off2+=i+offset+1
     # print off2,
      w=" ".join(list[i:i+offset])   
     # print w 
      if w in dict:
        dict[w].append(list[i+offset])
      else:
        dict[w]=[list[i+offset]]
    else:
      print "\n\n"
      return 

#print dict
def mark_text():
  global dict
  l=dict.keys()
  #print l[0]
  lel=random.choice(dict.keys())
  print lel,
  #print words
  #print "\n\n\n",dict[lel],"\n\n\n"
  for i in range(200):
    if lel in dict:
      ran=random.choice(dict[lel])
      lphrase=lel.split(" ")
      print ran,
      lphrase.append(ran) 
      lel=" ".join(lphrase[1:])
    else:
      print ""
      lel=random.choice(dict.keys())
      print lel,


#print dict
#print text
