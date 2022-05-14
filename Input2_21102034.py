#Q1

string = "Python is a case sensitive language"
length=len(string)
print("<A>The length of the string is:", length)
reverse=string[::-1]
print("<B>The reverse order of the string in one line code is:", reverse)
sliced_string=string[10:26]
print("<C>The new sliced string is;", sliced_string)
replaced_string=string.replace("a case sensitive", "object oriented")
print("<D>The new replaced string i:", replaced_string)
indexed=string.index("a")
print("<E>The index of substring a is:", indexed)

#Q2

Name ="Shivansh Khurana"
SID = 21102034
Department = "Civil"
CGPA = 9.9
Line1="Hey, {} Here!".format(Name)
Line2="My SID is {}".format(SID)
Line3="I am from {} Department and my CGPA is {}".format(Department, CGPA)

print(Line1)
print(Line2)
print(Line3)

#Q3

a=56
b=18
A=a&b
B=a|b
C=a^b
D=a<<2 , b<<2
E=a>>2 , b>>4
print("Output of a&b is:", A)
print("Output of a|b is:", B)
print("Output of a^b is:", C)
print("Left shift both a and b with 2 bits is:", D)
print("Right shift a with 2 bits and b with 4 bits is:", E)
print("\n")

#Q4

String=input("Enter the string:")
if 'name' in String:
    print("Yes")
else:
    print("No")
    
print("\n")

#Q5

s1=int(input("Enter the first side of traingle:"))
s2=int(input("Enter the second side of traingle:"))
s3=int(input("Enter the third side of traingle:"))
while(s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
    print("Triangle is valid")
    break
print("\n")

#Q6

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
num = a^b
Count_flipped_bit=0
while (num!=0):
    num=num & (num-1)
    Count_flipped_bit += 1
    print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)
    
      