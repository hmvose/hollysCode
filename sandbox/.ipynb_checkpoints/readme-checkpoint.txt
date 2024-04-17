1. Holly Vose, CWID: 10850093

2. I am using Python 3.11 for my source code

3. The program was built, tested, and run on Windows 10. 

4. My code structure is as follows:
- Uses a file parsing function to parse through the given map file
- A map is generated and city connections are recorded via a function and a set of lists.
- The input is parsed. First, the input cities are checked to see if they are the same. If they are, then the correct 
output of 0 km is returned. If they are different, we proceed with the function.
- A pathfinding function uses a dictionary as a pseudo-tree to find the optimal path. The function returns the
tree and the final node (with the final cost).
- The final tree is quickly checked to make sure a real path exists. If the tree returned is empty, then the pathfinding
function did not find a possible path, and therefore is impossible.
- If the tree is not empty, then the tree is parsed backwards in order to determine the city to city connections. By
cross-referencing the original map generated, the final route is determined and printed to the terminal.

5. TO RUN THE CODE (for Windows users)
 0) Before running this program, please ensure that the necessary text files are in THE SAME FOLDER as the program. The text     files must be in the same folder in order for the program to access them. Also make sure that python is properly             installed on your machine. I wrote this program in Python 3.11, so I am unsure of its functionality with older versions.
 1) Open the command prompt. This can be done by typing cmd into the search bar. 
 2) Once the command prompt is open, navigate to the folder where the Project file has been unzipped in the command window.
 Folders can be navigated to by using cd <filename>.
 3) Once the folder shows up in the path of the command window, type the following command and hit Enter:
 
 python3 find_route.py <map_file> <city 1> <city 2>

 where <map_file> is the name of the .txt file with the city connections,
 <city 1> is the starting city
 <city 2> is the ending city
 4) You should now see an output for your selected cities!