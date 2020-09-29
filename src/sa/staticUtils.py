
def findbyIdentifiers(string, startIdentifier, endIdentifier):
    start = string.find(startIdentifier)+len(startIdentifier)
    end = string.find(endIdentifier, start, -1)
    return string[start:end]