# cprogram is a string in python
#
cProgram = """
#include<stdio.h>
int main(){
print("Hello World");
return 0;
}
"""
pyProgram = """
print("Hello World")
"""

# file = open("E:\Created File\myapp.c","w")
# file.write(cProgram)
file = open("E:\Created File\myapp.py","w")
file.write(pyProgram)
file.close()
print(">> Data Written inn File")
