import sys

#FILE PARSER: CREATE LIST OF CONNECTIONS
def file_parser(filename):
    newfile = open(filename)

    #initialize parameters
    eof = False
    connect_list = []

    #while not at the end of file
    while eof == False:
        #read line by line and truncate newlines
        entry = newfile.readline()
        entry = entry.rstrip("\n")
        
        #check if we are at the end of file
        if entry == "END OF INPUT":
            #change variable to get out of while loop
            eof = True
        else:   #otherwise we continue to prune the result and add to the list of cities
            entry_fix = entry.split(" ")
            connect_list.append(entry_fix)
    return connect_list

#MAP GENERATOR
def generate_map(city_list):
    
    #initializations
    unique_cities = {}       #creates a list of unique cities, could be used to make sure all inputs are valid
    index = 0                #keeps track of which city is where in the list
    city_map = []            #all possible city connections, cross referenced by the dictionary of unique cities
    
    #for each city/connection
    for group in city_list:
        
        #create placeholders for all possible scenarios
        start, end, distance = group
        city_group_start = [start, [[end,int(distance)]]]
        city_group_end = [end, [[start,int(distance)]]]
        
        #if our city has not been added to the list
        if start not in list(unique_cities.keys()):
            unique_cities[start] = index
            index += 1
            city_map.append(city_group_start)
        else:
            #add city connection to existing entry
            city_map[unique_cities[start]][1].append([end, int(distance)])
            
        #connections are bidirectional, make sure both are valid
        if end not in list(unique_cities.keys()):
            unique_cities[end] = index
            index += 1
            city_map.append(city_group_end)
        else:
            city_map[unique_cities[end]][1].append([start, int(distance)])
            
    return city_map, unique_cities

#METHOD OF FINDING THE BEST PATH
def pathfinder(start, end, city_map, city_list):

    #initialize all parameters
    tree_dict = {}                 #tree made from a dictionary, doesn't rely on external libraries
    fringe = []                    #fringe queue
    expand_node = (start, 0, 0)    #the starting node with the city name, current cost, and reference (id) number
    ref = 1                        #reference (id) number to distinguish nodes
    
    fringe.append(expand_node)     #add starting node to the fringe

    tree_dict[expand_node] = []    #add new node to the tree

    while fringe:                  #while stuff is in the fringe
        
        if ref > len(city_list.keys()) * 1500:   #if the reference numbers are 1000x the number of cities checked, it is 
                                                 #likely not possible
            placeholder = {}
            return placeholder, expand_node
        
        #otherwise, we start looking at new leaf nodes for the tree
        for city in city_map[city_list[expand_node[0]]][1]:
            new_cost = int(city[1]) + expand_node[1]          #generate the new cost
            new_group = (city[0], new_cost, ref)              #create new node
            tree_dict[new_group] = []                         #add new node to the tree
            tree_dict[expand_node].append(new_group)          #add the leaf node to its parent node
            ref += 1                                          #increment the reference number
            fringe.append(new_group)                          #add child to the fringe
            
        fringe.sort(key=lambda x: (x[1]))                     #priority sort by the lowest cost
        
        expand_node = fringe.pop(0)                           #new node to expand is that with the lowest cost
        
        #check if the node we just expanded the goal
        if expand_node[0] == end:
            return tree_dict, expand_node

#EVERYTHING TOGETHER
def find_route(filename, start, end):
    #open the file and properly initialize everything
    city_file = file_parser(filename)
    city_map, unique_cities = generate_map(city_file)

    #looplist = bfs(visit, city_map, start, unique_cities) 
    #CASE I: input cities are the same
    if start == end:
        #do the right output
        print("distance: 0 km")
        print("route:")
        print(start + " to " + end + ", 0 km")
        return
    
    #run the search
    final_tree, final_node = pathfinder(start, end, city_map, unique_cities)
    
    #CASE II: No possible route exists between the given cities
    if len(final_tree) == 0:
        #do the right output
        print("distance: infinity")
        print("route:")
        print("none")
        return
    
    #CASE III: A possible route that is not 0 exists between the two given cities
    else: 
        best_path = []
        best_path.append(final_node[0])
        search_node = final_node
        while search_node != (start, 0, 0):
            for keys in list(final_tree.keys()):
                for node in final_tree[keys]:
                    if node == search_node:
                        best_path.append(keys[0])
                        search_node = keys
        
        best_path.reverse()
        roads = []
        distance = 0
        for i in range(len(best_path)-1):
            #need to find the corresponding route from the given city
            for j in range(len(city_map[unique_cities[best_path[i]]][1])):
                if city_map[unique_cities[best_path[i]]][1][j][0] == best_path[i+1]:
                    road = city_map[unique_cities[best_path[i]]][1][j][1]
                    direction = best_path[i] + " to " + best_path[i+1] + ", " + str(road) + " km"
                    roads.append(direction)
        print()
        print("distance: " + str(final_node[1]) + " km")
        print("route:")
        for i in roads:
            print(i)
        return
    
find_route(sys.argv[1], sys.argv[2], sys.argv[3])