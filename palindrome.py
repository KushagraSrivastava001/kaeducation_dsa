def palindrome(string):
  i=0
  j=len(string)-1
  while(i<=j):
    if(string[i]!=string[j]):
      return False
    else:
      i+=1
      j-=1
  return True
  
