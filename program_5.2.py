#Kevin Lee
#assign 2

prompt = 'what is a?\n'
a = input(prompt)
prompt = 'what is b?\n'
b = input(prompt)
prompt = 'what is c?\n'
c = input(prompt)
prompt = 'what is n?\n'
n = input(prompt)
n = int(n)
a = int(a)
b = int(b)
c = int(c)
if n > 2  and a^n + b^n == c^n:
    print("Holy smokes, Fermat was wrong!")
else:
    print("No, that doesn’t work.")

