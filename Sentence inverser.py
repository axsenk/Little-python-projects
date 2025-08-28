def inver(word):
  inv=word[::-1]
  return inv

def aff(p):
  inverse=[]
  mots = p.split(' ')
  for mot in mots:
    ab = inver(mot)
    pi= "".join(ab)
    inverse.append(pi)
  print(" ".join(inverse))

ph = input()
aff(ph)