class SortedList:
    theList = []
    
    def add(self, number):
        self.theList.append(number)
        for x in range(1,len(self.theList)):
            position = x
            current = self.theList[x]
            while position > 0 and self.theList[position-1] > current :
                self.theList[position]=self.theList[position-1]
                position = position-1
            self.theList[position]=current
        return self.theList
    
    def remove(self, number):
        if number in self.theList:
            self.theList.remove(number)
        else:
            return "Please only try to remove numbers which included in 'theList'"
        return self.theList
    
    def printList(self):
        print(self.theList)
        return self.theList
    
    def binarSearch(self, number):
        head=0
        tail=len(self.theList)
        while True:
            middle=(head+tail)//2
            if head == tail or head == tail-1:
                if int(self.theList[middle]) == int(number):
                    return "Found!"
                    break
                else:
                    return "Not Found!"
                    break
            if middle == 0:
                if int(self.theList[middle]) == int(number):
                    return "Found!"
                    break
                else:
                    return "Not Found!"
                    break
            elif head == (len(self.theList)-1) :
                if (self.theList[head]) == number:
                    return "Found!"
                    break
                else:
                    return "Not Found!"
                    break
            elif int(self.theList[middle]) == int(number):
                return "Found"
                break
            elif int(self.theList[middle]) < int(number):
                head = middle
            elif int(self.theList[middle]) > int(number):
                tail = middle
        
sorted = SortedList() #create a SortedList object 

