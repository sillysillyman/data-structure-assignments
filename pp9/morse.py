#
# Decoder for the Morse alphabet
#

# The tree nodes

class Morse():
  def __init__(self, symbol=None, dot=None, dash=None):
    self.symbol = symbol
    self.dot = dot
    self.dash = dash

  def decode(self, morse):
    raise NotImplementedError

# The decoding tree

morse_table = Morse(None, 
                    Morse('E', 
                          Morse('I',
                                Morse('S',
                                      Morse('H'),
                                      Morse('V')),
                                Morse('U',
                                      Morse('F'))),
                          Morse('A',
                                Morse('R',
                                      Morse('L')),
                                Morse('W',
                                      Morse('P'),
                                      Morse('J', 
                                            None, 
                                            Morse('1'))))),
                    Morse('T',
                          Morse('N',
                                Morse('D',
                                      Morse('B'),
                                      Morse('X')),
                                Morse('K',
                                      Morse('C'),
                                      Morse('Y'))),
                          Morse('M',
                                Morse('G',
                                      Morse('Z'),
                                      Morse('Q')),
                                Morse('O'))))

# --------------------------------------------------------------------

def decode_transmission(s):
  rwords = []
  words = s.split("  ")
  for word in words:
    rword = ""
    letters = word.split(" ")
    for letter in letters:
      rword += morse_table.decode(letter)
    rwords.append(rword)
  return " ".join(rwords)

# --------------------------------------------------------------------

if __name__ == "__main__":
  tests = [ ('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'), ('-..', 'D'),
          ('.---', 'J'), ('-.-', 'K'),
          ('.----', '1'),
          ('..---', '2'),
          ('...--', '3'),
          ('....-', '4'),
          ('... --- ...', 'SOS') ]

  for m, s in tests:
    print("Decoding %20s " % m, end="")
    decoded = decode_transmission(m)
    print("--> '%s': %s" % (decoded, "CORRECT" if decoded == s else "WRONG!"))

  examples = [ "-.-. ... ..--- ----- -....  .. ...  ..-. ..- -.",
               "--. --- --- -..  .-.. ..- -.-. -.-  --- -.  - .... .  ..-. .. -. .- .-..",
               "-....  - .. -- . ...  --...  .. ...  ....- ..---"
  ]
  
  print("A few more examples:")
  for m in examples:
    decoded = decode_transmission(m)
    print("%72s --> '%s'" % (m, decoded))

# --------------------------------------------------------------------
