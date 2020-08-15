
def log(string):
    f = open("log.txt","a+")
    if type(string) is not str:
        string = repr(string)

    if f.closed:
        print("Error logging to file")
        
    try:
        f.write(string + "\r\n")
        f.close()
    except:
        print("Error logging to file")