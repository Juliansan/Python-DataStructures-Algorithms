# Example Creating a Class Array
class Array():
    def __init__(self, initialSize):
        self.__a = [None] * initialSize             # Array it's stored as a list
        self.__nItems = 0                           # No item in the Array initially

    def __len__(self):                              # Overwrite special method
        return self.__nItems                        # Return the number of items inserted

    def get(self, n):                               # Return the value at index n
        if 0 <= n and n < self.__nItems:            # Check if n is in bounds
            return self.__a[n]                      # return value if in bounds

    def set(self, n, value):                        # Set the value at index n
        if 0 <= n and n < self.__nItems:            # Check if n is in bounds
            self.__a[n] = value                     # update value 

    def insert(self, item):
        self.__a[self.__nItems] = item               # Item gets inserted on the current item
        self.__nItems += 1                           # __nItems increment by 1


    def find(self, item):                           # Find index for item
        for j in range(self.__nItems):              # Loop over array
            if self.__a[j] == item:                 # If the item is found
                return j                            # return index
        return -1                                   # Not found -> Return -1

    def search(self, item):
        return self.get(self.find(item))

    def delete(self, item):                         # Delete first occurence 
        for j in range(self.__nItems):              # Loop Array items
            if self.__a[j] == item:                 # if Item found
                self.__nItems -= 1                  # Remove size of Array, as we removed item found                
                for k in range(j, self.__nItems):   # Loop Array 
                    self.__a[k] = self.__a[k+1]     # Move items to j position
                return True                         # Return True as item it's deleted
        return False                                # Return False as item has not been found



    def traverse(self, function=print):             # Traverse all items
        for j in range(self.__nItems):              # Loop over items
            function(self.__a[j])                   # apply function to items
