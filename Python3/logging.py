
### log function to avoid building the string by hand everytime
### the cond argument allow to group your logs and enable/disable them by group
### TO_IMPROVE : format each element of the table according to its type, recurrently (to avoid 4.000000017 values)
def log(toLog, cond=True):
    if not cond:
        return
    s = ""
    for i in toLog:
        if type(i) is float:
            ss = "{:.2f}".format(s)
        else:
            ss = str(i).strip()
        s+= ss+" "
    print(s, file=sys.stderr, flush=True)

###example
#printLogExample = True
#tableExample = [3, 4]
#log(["my table",tableExample,"has a length of", len(tableExample)], printLogExample)