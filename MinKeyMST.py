 # A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree 

    def minKey(self, key, mstSet): 

        # Initialize min value 
        min = sys.maxsize 

        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 

        return min_index 

  
