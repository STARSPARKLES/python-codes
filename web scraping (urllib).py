#Code 1
#i am not importing whole urllib library to save memory ,only importing specific modules and functions that are useable for me
from urllib import request #importing request module from urllib
from urllib.parse import urljoin #importing urljoin function from urllib.parse
URL = "https://www.codewithharry.com"
webConnection = request.urlopen(URL) #connecting to the URL and get the webpage content
webConnectionBytes = webConnection.read() #read the content of the webpage 
htmlpage = webConnectionBytes.decode() #convert the html content into a string
htmlpageSplitbySpace = htmlpage.split(" ") #split the html content into words by space
for content in htmlpageSplitbySpace: #iterate through each word in the HTML content
    if "href" in content: #if the word contains 'href' 
        start = content.index("=") + 1  #find the starting index of the link
        end = None
        if '"' in content[start:]: #if the link is enclosed in double quotes
            end = content.index('"', start + 1) # find the ending index of the link
        elif "'" in content[start:]:  #if the link is enclosed in single quotes
            end = content.index("'", start + 1) #find the ending index of the link
        if end: #if the ending index of the link is found
            link = content[start:end].strip("'\"") #extract the link and remove any leading/trailing quotes
            full_link = urljoin(URL, link) #make the link absolute by joining it with the base URL
            if full_link.startswith(URL): #check if the link is an onsite link
                print("Onsite Link:", full_link) #print  onsite link
            else:
                print("Offsite Link:", full_link) #print the offsite link



