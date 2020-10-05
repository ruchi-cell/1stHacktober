s = 'ihkopolleh'
s = [::-1]
a = ''
b = ' '
for i in range(len(s)):
  if i%2 == 0:
    a += s[i]+' '
  else:
    b += s[i]+' '
print(a)
print(b)
