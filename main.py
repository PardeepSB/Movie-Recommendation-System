#######################
###Movie Recommendation System
###Author: Pardeep Bhattal
###
###
def write_perstudent_to_file(lout_Strings,the_file):
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lout_Strings:
        fileRef.write(line)
                                    
    fileRef.close()
    
    return

#function that tells user to correct themselves when input cannot be read.
def questions(prompt,n):
    x = "true"
    y = x
    while y == x:
        y = "true"
        try:
            value = int(input(prompt))
        except ValueError:
            print("What you provided is not an integer number\nPlease re-type")
            continue
        
        if value not in range(n):
            print("What you provided is an integer, but is not a valid value\nPlease re-type")
            continue
            
        else:
            y = "false"
    return value

#Function for space correction and showing user recommendation.
def Recommendation():
  print("movie            type     genres           rating            origin")
  for i in range(10):
    if v4[0][0] in newwlst[i]:
      ff = newwlst[i]
  return ff


#Read file input.
def reading_file(the_file):
    
    fileRef = open(the_file, "r")
    localList_ofstrings = []
    for line in fileRef:
        string = line[0:len(line)-1].split()
        localList_ofstrings.append(string)      # adds string (line) to list
            
    fileRef.close()

    return localList_ofstrings

#read stringed list from file.
def read_string_list_from_file(the_file):
    
  fileRef = open(the_file,"r")      # opening file to be read
  localList_ofstrings=[]            # new list being constructed   
  for line in fileRef:
    string = line[0:len(line)-1]                                 
    localList_ofstrings.append(string) 

  fileRef.close()     
  #print ("\n JUST TO TRACE, the list OF STRINGS is:\n")  
  return localList_ofstrings

#printing all possible options within stored data.
def All():
    number = len(alldata)
    #print(" JUST TO TRACE, the lists with data are:\n\n")
    print(" number of movies available: ",number,"\n")
    print("List of available movies:")
    print("movie            type     genres           rating            origin")
    for i in range(len(alldata)):
        movie=alldata[i][0:17]
        types=alldata[i][18:20]
        if 'X' in alldata[i][23:27]:
            map_object = map(int, alldata[i][23:27].replace('X', ""))
            genre = list(map_object)
        else:
            map_object= map(int, alldata[i][23:27])
            genre = list(map_object)
        rating=alldata[i][32:36]
        origin=alldata[i][36]
        if len(genre) == 2:
            ratingsp = " "*9
        if len(genre) == 3:
            ratingsp = " "*6
        if len(genre) == 4:
            ratingsp = " "*3
        ratingor = " "*12
        print(movie + types,  "     ", genre, ratingsp, rating,ratingor, origin)
        
    return ""

#Sort the user values,new list returned, narrows down the bigLST to the users choice. 
def counter(x):
  newlst = []
  for i in range(len(x)):
    if str(types) in x[i][1] : 
      newlst = newlst + [x[i]]
  return newlst


#Narrow down the new list from counter() and create a new list that is ever more narrowed down. 
def counter2(x):
  newlst = []
  for i in range(len(x)):
    if str(genres) in x[i][2] : 
      newlst = newlst + [x[i]]
  
  if newlst == []:
    newlst = v1
  return newlst

#If the user value, in this case rating, cannot narrow down the list, the returned list will be empty.
def counter3(x):
  newlst = []
  for i in range(len(x)):
    if str(rating) in x[i][3] : 
      newlst = newlst + [x[i]]
    
  if newlst == []:
    newlst = v2
  return newlst


#This function narrows down based on the origin
def counter4(x):
  newlst = []
  for i in range(len(x)):
    if str(orig) in x[i][4]: 
      newlst = newlst + [x[i]]
  
  if newlst == []:
    newlst = v3
  return newlst

#Opening recommendations csv to reset all previous values
f = open('OUT_recommendations.csv', 'r+')
f.truncate(0) # need '0' when using r+
f.close()

#List created to specify spacing
newwlst = ['Harry_Potter 	 1        [2, 3, 4, 5]     0 		         1','The_Matrix 	     1 	      [0, 3, 4] 	   4 		         1',
'Black_mirror 	 0    	  [4, 5]    	   3    	      	 1',
'Avenger 	     1 	      [0, 4] 	       2 		         1',
'Cinderella 	     1 	      [3, 6] 	       0 	     	     1',
'Snow_white 	     1 	      [3, 6] 	       0 	        	 1',
'Rapunzel 	     1 	      [3, 6] 	       0 		         1',
'Anne_with_an_E 	 0 	      [2, 4] 	       0 		         0',
'Invented 	     0 	      [1, 2, 6, 7]     1 		         0',
'Invented2 	     1 	      [6, 7] 	       4 		         1']  


#Initialize list for all data
lstBIG = reading_file("IN_all_data.txt")

#Start Proram for user interface
print("=" * 55)
print("WELCOME to the Movies Recommendation System!\n" + "=" * 55)

print("Please select from the given options as presented \nfor the system to give you recommendations based on your selections.")
print()

#TRACE
'''
print("The files that will be used by default (and need to be in this folder!) are:")
print(" " * 8 + "IN all data: IN_all_data.txt")
print(" " * 8 + "IN genres: IN_genres.txt\n")

print("Initial processing ... \n")

INgenre = read_string_list_from_file("IN_genres.txt")
print(INgenre)

alldata = read_string_list_from_file("IN_all_data.txt")
print(alldata)
print()
print(" JUST TO TRACE, the lists with data are:\n\n")
print(All())

print("\nFeatures\n")
print("TYPE: 0-tv series 1-movies")
print("RATING: 0-G 1-PG 2-PG13 3-NC17 4-R")
print("ORIGIN: 0-Canadian 1-Foreign")
print("GENRES: from file\n")

'''


#Main level of the program starts
lstNames = []

INgenre = read_string_list_from_file("IN_genres.txt")
alldata = read_string_list_from_file("IN_all_data.txt")

#User prompted to make a request
ans = input("\n **Would you like to make a request? (y/n) --> ").lower()
y = ans
while y == ans: 
  lst = []
  #User inputs selection process begins
  if ans == "y":  
    print("\n\n Please provide the features for your movie (type the number code): ")       
    print("\nType\n0 - tv series\n1 - movies\n")
    types = questions("The type --> ",2)

    print("\nRating\n0 - G\n1 - PG\n2 - PG13\n3 - NC17\n4 - R\n")
    rating = questions("The rating? --> ",5)

    print("\nOrigin\n0 - Canadian\n1 - foreign\n")
    orig = questions("The origin? --> ",2)
    
    print("\nGenres")
    for n in range(len(INgenre)):
      print(str(n) + "-" + str(INgenre[n]))
    genres = questions("\nOne genre that you prefer? --> ",7)

    print("\n We recommend...")

    #list sorting
    v1 = counter(lstBIG)
    v2 = counter2(v1)
    v3 = counter3(v2)
    v4 = counter4(v3)
                 
    print(Recommendation())
    lstNames += [v4[0][0]]
    
    #return next value in the list of recommendations and use that value to find the position of the movie in another list
    i = 0
    var = ""
    while i < len(v4):
      i = i + 1
      z = input("\nMore recommendations, same features? (y/n) --> ")
      if z == "y":
        if i >= len(v4):
          print("Sorry thats all the selection we have")
          i = i + 20
        else:
          print("\n We recommend...")
          print("movie            type     genres           rating            origin")
            
          #This loop lets the first word to be in the second selection (which would be the movie name)
          for n in range(i,10):
            if v4[i][0] in newwlst[n]:
              fnf = newwlst[n]
              lstNames += [v4[i][0]]
          print(fnf)

      else:
        i = i + 20
    ans = input("\n\n **Would you like to make another request? (y/n) --> ").lower()
  else:
    y = "false"

#save all recommendations within a list
lst1 = []
for length in range(len(lstNames)):
  lst1 += [lstNames[length]+"\n"] 

lst1 = list(dict.fromkeys(lst1))

#List used to write onto the output file to user
#List of Movies is saved into a .csv file depending on user
saving = input("\nWould you like to save you recommended movies? (y/n) --> ").lower()
if saving == "y":
  save = write_perstudent_to_file(lst1,"OUT_recommendations.csv")
  print("\nList of strings ready to save to output file, one per line\n")
  for i in range(len(lst1)):
    print(str(lst1[i]))
  print("All done! Bye!")
else: 
  print("All done! Bye!")
