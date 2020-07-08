# formeting

x=4.33343
y=6.34897
print("\nOrginal Number: ",x)
print("Formatted nuber: "+"{: .2f}".format(x));
# {before decimal :.2f means after decimal 2 digit f means float means decimal(round function)}

print("\nOrginal Number: ",y)
print("Formatted nuber: "+"{: .2f}".format(y));
print()



#formeting 2

a=1
b=2
print("{}-{}".format(a,b))

# no eroor in any python version
print("{0}-{1}".format(a,b))

q=9
e=10
d=90
y=45
print("{}+{}+{}-{}".format(e,d,q,y))
print("{3}+{2}+{1}-{0}".format(e,d,q,y))