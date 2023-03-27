# Create a dictionary with both cities

web_url = urllib.request.urlopen("https://conferencealerts.com/show-event?id=")
data = str(web_url.read())

for id in range(249862, 249866, 1):

    link = "https://conferencealerts.com/show-event?id={}".format(id)
    print(link)

    try:
    
        web_url = urllib.request.urlopen(link)

    except:
        continue

    print('it worked!')
    data = str(web_url.read())
    #print(data)