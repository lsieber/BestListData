
from src.elmt.Category import Category

def getCategoryIds():
    return (x.id for x in getCategories())
    
def getCategoryNames():
    return (x.name for x in getCategories())

def getCategoryByid(categoryId):
    return next((x for x in getCategories() if x.id == categoryId), None)

def getCategoryByName(categoryName):
    return next((x for x in getCategories() if x.name == categoryName), None)


# def getCategoryIds():
#     ids = {
#         "Alle Männer" : "M",
#         "Alle Frauen" : "W",
#         "U12M" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45k-bg",
#         "U12W" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45m-bh",
#         "U14M" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45o-bi",
#         "U14W" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45q-bj",
#         "U16M" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45s-bk",
#         "U16W" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45u-bl",
#         "U18M" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45w-bm",
#         "U18W" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45y-bn",
#         "U20M" : "5c4o3k5m-d686mo-j986g2ie-1-j986g45z-bo",
#         "U20W" : "5c4o3k5m-d686mo-j986g2ie-1-j986g461-bp",
#         "U23M" : "5c4o3k5m-d686mo-j986g2ie-1-j986g463-bq",
#         "U23W" : "5c4o3k5m-d686mo-j986g2ie-1-j986g465-br",
#         "Männer" : "5c4o3k5m-d686mo-j986g2ie-1-j986g467-bs",
#         "Frauen" : "5c4o3k5m-d686mo-j986g2ie-1-j986g469-bt"
#         }
#     return ids
    
def getCategories():
    return [
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45k-bg", "U12M", "M"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45m-bh", "U12W", "W"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45o-bi", "U14M", "M"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45q-bj", "U14W", "W"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45s-bk", "U16M", "M"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45u-bl", "U16W", "W"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45w-bm", "U18M", "M"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45y-bn", "U18W", "W"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g45z-bo", "U20M", "M"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g461-bp", "U20W", "W"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g463-bq", "U23M", "M"),
        Category("5c4o3k5m-d686mo-j986g2ie-1-j986g465-br", "U23W", "W"),
        Category("M", "M", "M"),
        Category("W", "W", "W")
        ]
    
# def getCategoryFromName(categoryName):
#     for category in getCategories():
#         if categoryName == category.name:
#             return category