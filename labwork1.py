# %% [markdown]
# # ex1

# %%
n = int(input("enter the radius :"))

while n < 0:
    print("invalid")
    n = int(input("enter the radius :"))

area = 3.14 * (n * n)

print(f"the area is : {area}")

# %% [markdown]
# # ex2
# 

# %%
f = float(input("enter the temperature :"))
c = (f - 32) * 1.8
print(f"the temperature is {c} ")


# %% [markdown]
# # ex3

# %%
n = int(input("enter the number:"))


while n <= 1 :
    print(" not prime")
    n = int(input("enter the number:"))
a = True
for i in range(2,n):

    if n % i == 0:
        a = False
        break
    
if a == True :
    print(" prime")
else:
    print("not prime")


# %% [markdown]
# # ex 4
# 

# %%
n = int(input("enter the number:")) 

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum +i

if sum == n:
    print("perfect number")
else:
    print("not perfect number")



# %% [markdown]
# # ex 5

# %%
n = input("what is your favorite color? :") 
color =  ['black','red','pink','blue','white','green' ]


if n in color:
    print(f"your colod is at index :{color.index(n)}")
else:
    print("Sorry, I could not find your color")

# %% [markdown]
# # ex 6

# %%
r1 = list(range(0,7))
r2 = list(range(1,11,3))
r3 = list(range(5,0,-1))
r4 = list(range(6,-3,-2))
print(f"range1 ={r1}")
print(f"range2 ={r2}")
print(f"range3 ={r3}")
print(f"range4 ={r4}")

# %% [markdown]
# # ex 7
# 

# %%
def remove_dolar_sign(s):
    n = s.replace("$","s")
    return n
    

s = input("enter a string: ")
r = remove_dolar_sign(s)
print(r)

# %% [markdown]
# # ex 8

# %%
def exreact_even():
    even_list = []
    for i in my_list :
        if i % 2 == 0 :
            even_list.append(i) # of even list += [i]
    return even_list 
            

my_list = [1,4,5,-1,10]
print(f"my origrin lish{my_list}")

even_list = exreact_even()
print(f"even list : {even_list}")









# %% [markdown]
# # ex 9

# %%
def factorial(n):
    s = 1
    for i in range(1 ,n+1):
        s = s * i
    return s

r = int(input("enter a number : "))
result = factorial(r)
print(result)

# %% [markdown]
# # EX 10
# 

# %%
def get_divisor(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0 :
            result.append(i)
    return result

r = int(input("enter your number : "))
a = get_divisor(r)
print(a)

# %% [markdown]
# # ex 11

# %%
import math

def  get_distance(x1,y1,x2,y2):
    s = ((x2 - x1)**2) + ((y2 - y1)**2)
    d = math.sqrt(s)
    return d

x1 = int(input("enter x1 ="))
y1 = int(input("enter y1 ="))
x2 = int(input("enter x2 ="))
y2 = int(input("enter y2 ="))

result = get_distance(x1,y1,x2,y2)
print(result)

# %% [markdown]
# # ex 12

# %%
def rectagle(m,n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                print("*",end ="")
            else:
                print(" ", end= "")
        print()

m = int(input("enter rows: "))
n = int(input("enter column: "))

rectagle(m,n)



