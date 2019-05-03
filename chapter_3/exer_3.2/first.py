def print_spam():
 print("spam")


def do_twice(f,n):
 for i in range(n):
   f()
 



#do_twice(print_spam,4)

def do_four(f,n):
 for i in range(n):  
  f()

do_four(print_spam, 4)
