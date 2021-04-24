# Hello World Example 

How to run the example:

g++ --static hw_cpp.cc -o hw_cpp  # Compile to the c++ program
./create_thunk.py    # create thunk
gg force --jobs 1 --engine=lambda thunk.out       # force to Lambda