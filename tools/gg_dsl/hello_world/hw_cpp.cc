#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main(int argc, char* argv[]) {

    cout << "Hello Juy!" << "\n";

    ofstream my_ofile;   // Create an file object to write
    my_ofile.open("thunk.out");    // Open a file named as "thunk.out" (Should be same name as the thunk file)
    my_ofile << "comes back from Lambda 2" << "\n";  // Write the string to the file
    my_ofile.close(); 

    return 0;
}
    
