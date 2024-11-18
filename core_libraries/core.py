val_tracker = []


def addVal(name):
    val_tracker.append({name: 0})
    print("value created")

def viewVal(name):
    for x in val_tracker:
        try:
            print(x[name])
            break
        except:
            print("not found")
            continue

def allVals():
    print(val_tracker)

def changeVal(name, newVal):
    for x in range(len(val_tracker)):
        try:
            val_tracker[x][name] = newVal
            print(val_tracker[x][name])
            break
        except:
            print("value not found")
            continue