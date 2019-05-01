
#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

x=int(input("Enter the digit : "))
n1=int("%s" % x)
n2=int("%s%s" % (x,x))
n3=int("%s%s%s "% (x,x,x))
n4=int("%s%s%s%s"% (x,x,x,x))
print(n1+n2+n3+n4)
