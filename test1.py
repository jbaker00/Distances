import numpy as np

lines = [] #declair array of lines
strMi = 'mi\n' #Miles abbv in string, could put it inlin at comparison but keeping things clean and python complier will optimize this in assembly anyway, note the EOL at the end of the line due to the read in for this HPFS file system on ipad with Darwin, may diff on other OSs
strKm = 'km\n' #Kilimeters abbv in string
strYd = 'yd\n' #Yards abbv in string
MiKm = 0.0 #Miles converted to Km
YdKm = 0.0 #Yards converted to Km
KmKm = 0.0 #Kilometers converted to KM
largestDist = 0.00000 #tracking the longest distance
longestPeresonLine = [] #line with the longest distance

#open the file and read all the lines into a list of strings (array)
with open('distances.txt','r') as f:
    lines = f.readlines()
#f.close() //not needed since with statement used


#much of this shold be broken into functions for reuse and ease of reading
#loop through each line
for line in lines:
    listElements = line.split(" ") #split out the line by space deliitation
    print(listElements[3]) #debug print out the line  
    
    #check to see if Mies were used
    if listElements[3] == strMi:
        print(listElements[2] + " Miles evaluated") #Debug print out 
        MiKm = float(listElements[2]) * 1.6
        print(str(MiKm) + " KM Evaluated for longest comparson") #Debug print out
        if MiKm > largestDist: #convert to inches
            print(listElements[2] + " Miles is the current largest distance which is " + str(MiKm) + " Kilometers")
            largestDist = float(listElements[2]) * 1.6 #store out the longest distance full line curretly
            longestPersonLine = listElements
    #check to see if Kilometers were used
    elif listElements[3] == strKm:
        print(listElements[2] + "Kilimeters used") #Debug print out
        KmKm = float(listElements[2])
        print(str(KmKm) + " KM Evaluated for longest comparsion") #Debug print out
        if float(listElements[2])  > largestDist:
            print(listElements[2] + " Kilometers is the current largest distance which is " + str(KmKm) + "Kilometers")
            largestDist = float(listElements[2])
            longestPersonLine = listElements
    #check to see if yards were used
    elif listElements[3] == strYd:
        print (listElements[2] + " Yards used") #Debug print out
        YdKm = float(listElements[2]) * 0.0009144
        print(str(YdKm) + " KM Evaluated for longest comparsion") #Debug print out
        if YdKm *  0.0009144 > largestDist:
            print(listElements[2] + " Yards is the current largest distance which is " + str(YdKm) + "Kilometers")
            largestDist = float(listElements[2])*  0.0009144
            longestPersonLine = listElements

print("The longest distance line is")
print(longestPersonLine)

new_array = np.array(longestPersonLine)
file = open("winner.txt", "w+")

content = str(new_array)
file.write(content)
file.close

