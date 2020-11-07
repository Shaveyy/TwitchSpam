from datetime import date

def log(string):
    print(string)
    f = open("log.txt","a+")
    if type(string) is not str:
        string = repr(string)

    if f.closed:
        print("Error logging to file")
        
    try:
        today = date.today()
        f.write(f"[{today}] {string}\r\n")
        f.close()
    except:
        print("Error logging to file")