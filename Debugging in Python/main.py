# debugging 

# We're always going to make mistakes and programs are constantly being improved.
# We constantly improve our code as we find more and more mistakes because programs are full of errors
# or what we call bugs or exceptions at runtime when the code is running.
# You see, the act of finding and removing these bugs or errors from our code is called debugging.
# In a big chunk of our time as programmers is debugging code, whether it's our own code or other people's

# Linting - allow us to detect our code before we run it 

#  num + 4 

# 4 + 'asedrfadf'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

import pdb

def add(n1 , n2):
    pdb.set_trace()
    print(n1 , n2)
    return(n1 + n2)

add(4 , 'qasdgqsdgoikhn')


# *** SyntaxError: invalid decimal literal
# (Pdb) n1
# 4
# (Pdb) n2
# 'qasdgqsdgoikhn'
# (Pdb)



# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt
# alias  clear      disable  ignore    longlist  r        source   until
# args   commands   display  interact  n         restart  step     up
# b      condition  down     j         next      return   tbreak   w
# break  cont       enable   jump      p         retval   u        whatis
# bt     continue   exit     l         pp        run      unalias  where

# Miscellaneous help topics:
# ==========================
# exec  pdb