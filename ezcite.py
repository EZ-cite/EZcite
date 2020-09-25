import time
import pyperclip
import datetime


#prompt user what url they want to site
url = input("entire url including https and www: ")

#use python to access data that we can to format citation



#websiteTitleSplit = websiteTitle.split()



changeInput = input("Article Name: ")


articleName = changeInput

dateAccessed = str(datetime.date.today())




#possibly ask for other missing data
missing_data_ask = input("Any other missing data? y/n :")
missing_data_ask.lower()

if missing_data_ask == "y":
    missing_data = input("Enter exact string of missing data: ")
else:
    missing_data = ""
    pass
#add missing data as var 'add' to final, if not final gets defined as raw

# auto copy to clipboard so you can just paste
final = ( "\"" + articleName +"\"" +", Bob Jefferson III, \n" + url + ",\nAccessed " + str(dateAccessed) + ", " + missing_data)


def copy_paste():
    try:
        pyperclip.copy(final)
    except:
        print("ERROR ! ! ! !  :(  ")

    print(pyperclip.paste())



copy_paste()

#articleName, dateAccessed, url, 'Bob Jefferson'
#final = (" \"articleName\" " + ", Bob Jefferson III, \n" + url + "\"dateAccessed\"")
    
#bib structure lol
#title, publisher
##url, access date
