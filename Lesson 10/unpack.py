#Example of using * to unpack a list into separate elements
# Use single * to unpack list. ** to unpack Dict
def total( galleons, knuts, sickles):
    return (galleons * 17 + sickles) * 29 + knuts

coins={"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts") 