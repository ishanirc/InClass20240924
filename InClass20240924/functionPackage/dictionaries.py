# dictionaries.py

def demo():
    '''
    demonstrate basic dictionary stuff
    '''
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)
        
    # iterate by key/value
    for item in myDictionary.items():
        print(item)

    # iterate by value
    for value in myDictionary.values():
        print(value)

    # add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"
    
    print(len(myDictionary))

    # cause an exception
    # add try/except logic to gracefully handle this
    try:
        print(myDictionary["Ohio State"])
    except :
        # we end up here if an exception is thrown in the try block
        print("Ohio State is an invalid key")
    
    # remove Xavier by key and print the entire dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)
    
    # create another dictionary called newTeams
    # add several key/value pairs
    # combine that with myDictionary and print the results
    newTeams = {"University of Arizona": "Wildcats", "Oklahoma State University": "Cowboys", "Kansas University": "Jayhawks"}
    myDictionary.update(newTeams)
    print(myDictionary)