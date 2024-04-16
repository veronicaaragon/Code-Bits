# A utility function to print the constructed MST stored in parent[] 

    def printMST(self, parent): 
        print("Edge \tWeight") 
        for i in range(1, self.V): 
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]]) 

  
