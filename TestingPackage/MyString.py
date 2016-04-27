
class MyString():
    def __init__(self, str=""): # initializes  the object
        self.str=str

    #Returns the current string.

    def getString(self):
        return self.str

    #Returns a string that consists of all and only the vowels in the current string.
    #Only letters a, e, i, o, and u (both lower and upper case) are considered vowels.
    #The returned string contains each occurrence of a vowel in the current string.
    def getVowels(self):
        lowercase=self.str
        lowercase=lowercase.lower()
        vowels=""
        count=len(lowercase)

        for a in range(0,count):
            if lowercase[a]=='a'or lowercase[a]=='e' or lowercase[a]== 'i' or lowercase[a]=='o' or lowercase[a]== 'u':
                vowels=vowels+self.str[a]
        return vowels

    #Returns a string that consists of the substring between start and end indexes (both included) in the current string.
    #Index 1 corresponds to the first character in the current string.'''
    def getSubstring( self,start,end):
        c=""
        try:
            if start<=0:
                return("Invalid range")
            else:
                for b in range(start-1,end):
                    c=c+self.str[b]
                return c
        except IndexError:
                return("Invalid range")

    #Breaks the string down, and returns it as a character string
    def getCharList(self):
        mylist=[]
        count=len(self.str)

        for d in range (0,count):
            mylist.append(self.str[d])

        return mylist

    #Returns the index of the first occurrence of a character in the current string.
    #Index 1 corresponds to the first character in the current string.
    # return 0 if no match is found
    def indexOf(self,c):
        '''length=len(self.str)
        start=length-length+1
            for e in range(start,length):
                if c=e:
                    return e=-1 '''




        return 0


    # Removes all occurrences of the specified character from the current string.
    def removeChar(self,c):

        return 1


    #Invert the current string.
    def invert(self):


        return 1
