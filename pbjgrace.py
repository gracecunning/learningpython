bread = 11

peanut_butter = 6

jelly = 3

if bread >= 2 and jelly >= 1 and peanut_butter >= 1:
	print "You can make this many pbj sandwiches: " 
else:
	print "Sorry, no lunch for you."

if bread/2.0 >= 1 and bread/2.0 <= peanut_butter and bread/2 <= jelly:
	print bread/2.0

if peanut_butter >= 1 and peanut_butter <= bread/2 and peanut_butter <= jelly:
	print peanut_butter

if jelly >=1 and jelly <= bread/2 and jelly <= peanut_butter:
	print jelly

if bread % 2 == 1 and bread/2 <= peanut_butter and bread/2 <= jelly and jelly >= 1 and peanut_butter >= 1:
	print "plus one open face sandwich"

if bread == 0:
	print "you need more bread"

if jelly == 0:
	print "you need more jelly"
if peanut_butter == 0:
	print "you need more peanut butter"

if jelly >=1 and jelly <= bread/2 and jelly <= peanut_butter:
	print "and you can make", (peanut_butter - jelly), "peanut butter sandwiches. (Ew, you're wierd)"
