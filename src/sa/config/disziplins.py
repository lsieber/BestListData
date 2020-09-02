from src.elmt.Disziplin import Disziplin 

def getDisziplinIds():
    return (x.id for x in getDisziplins())
    
def getDisziplinNames():
    return (x.name for x in getDisziplins())

def getDisziplinByid(disziplinId):
    return next((x for x in getDisziplins() if x.id == disziplinId), None)

def getDisziplinByName(disziplinName):
    return next((x for x in getDisziplins() if x.name == disziplinName), None)

def getDisziplinByTAF(tafShort):
    return next((x for x in getDisziplins() if x.tafShortName == tafShort), None)


def getDisziplins():
    return [ 
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gc6m-1nc","50 m", True, "50M"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986g3pt-79","60 m", True, "60M"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ge1f-3jr","75 m", True, "75M"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gefj-3vd","80 m", True, "80M"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gfpc-4zv","100 m", True, "100"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ggxt-64h","150 m", True, "150"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ghgt-6ks","200 m", True, "200"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gi8s-6ls","300 m", True, "300"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gihb-6m2","400 m", True, "400"),
        Disziplin("5c4o4o49-18opme-kaxxbvmg-1-kaxxd5hz-r","500 m", True, "500"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gior-6mc","600 m", True, "600"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gj3n-6mw","800 m", True, "800"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gc86-1oz","1000 m", True, "1K0"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gc9i-1rt","1500 m", True, "1K5"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gcao-1rv","1 Meile", True, "MEI"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gcbl-1rx","2000 m", True, "2K0"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gccp-1ur","3000 m", True, "3K0"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gcdv-1ut","5000 m", True, "5K0"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gcf7-1xn","10 000 m", True, "10K"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986g3q2-7d","Halbmarathon", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986g3q3-7e","Marathon", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gd5g-2nr","60 m Hürden 106.7", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdav-2tl","60 m Hürden 68.6", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdmw-357","60 m Hü 76.2 U16 W / U14 M", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gd9v-2tj","60 m Hürden 76.2 U18 W", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdpj-383","60 m Hü 60-76.2 U12 Indoor", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdqm-385","60 m Hü 76.2 U14 W Outdoor", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdrr-39n","60 m Hürden 60-76.2 U12", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdgi-2zb","80 m Hürden 84.0", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdio-2zf","80 m Hürden 68.6", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdbu-2tn","80 m Hürden 76.2", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdhm-2zd","100 m Hürden 84.0", True),
        Disziplin("5c4o3k5l-dpzv57-k25y71bj-1-k25ys8mp-s","100 m Hürden 91.4", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gddp-2wh","100 m Hürden 76.2", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdlv-355","110 m Hürden 106.7", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdkp-32b","110 m Hürden 99.1", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdjp-329","110 m Hürden 91.4", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdt4-3b1","200 m Hürden", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gduc-3b3","300 m Hürden 91.4", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdvn-3dx","300 m Hürden 84.0", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdwx-3dz","300 m Hürden 76.2", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ge0b-3gx","400 m Hürden 91.4", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gdz9-3gv","400 m Hürden 76.2", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gj21-6mu","400 m Hürden 84.0", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gcta-297","1500 m Steeple", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gcu8-2c1","2000 m Steeple", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gcvb-2c3","3000 m Steeple", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ghc9-6fz","5x frei", True, "5XF"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ghdr-6it","5x80 m", True, ""),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ghf8-6iv","6x frei", True, "6XF"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gi01-6lg","4x100 m", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gi3b-6lk","4x400 m", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gi7f-6lq","3x1000 m", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gicg-6lw","Olympische", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gift-6m0","Schwedenstaffel", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gieb-6ly","Américaine", True),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ge33-3jt","Hoch", False, "HOC"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ge47-3mn","Stab", False, "STA"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ge5c-3mp","Weit", False, "WEI"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ge6o-3mr","Stabweit", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986g3pw-7a","Weit Zone", False, "WEZ"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ge8a-3pl","Drei", False, "DRE"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986geh1-3y7","Kugel 7.26 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986geaq-3sh","Kugel 6.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ge9l-3pn","Kugel 5.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gebx-3sj","Kugel 4.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986geid-3y9","Kugel 3.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986geji-40q","Kugel 2.50 kg", False),
        Disziplin("5c4o3k52-jahqgm-jdfq56ar-1-jdfqcknb-n","Kugel 2.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986geqw-46z","Diskus 2.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gepb-44u","Diskus 1.75 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986geo6-443","Diskus 1.50 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gemx-441","Diskus 1.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gekn-415","Drehwurf", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gelr-417","Diskus 0.75 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gezg-4ct","Hammer 7.26 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gexo-4cr","Hammer 6.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gevw-49x","Hammer 5.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986geua-49v","Hammer 4.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gesp-471","Hammer 3.00 kg", False),
        Disziplin("a3c1o40-owmyla-jft8fay8-1-jftn8q4l-v","Hammer 2.00 kg", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gf9t-4lh","Speer 800 gr", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gf6a-4il","Speer 700 gr", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gf4o-4ij","Speer 600 gr", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gf2y-4fp","Speer 400 gr", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gf7r-4lf","Speer 500 gr", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gf15-4fn","Ball 80 g", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986g3py-7b","Ball 200 g", False, "BAL"),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gfb8-4ob","Fünfkampf M", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gfcn-4od","Fünfkampf U20 M", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gfxn-58j","Fünfkampf U18 M", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gg9u-5k5","Fünfkampf W", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ggb5-5k7","Fünfkampf U20 W", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ggck-5n1","Fünfkampf U18 W", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gflf-4x1","Fünfkampf U16 W", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gfqo-52p","Siebenkampf", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gfs0-52r","Siebenkampf U18 W", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gg1t-5bh","Zehnkampf M", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gg38-5eb","Zehnkampf U20 M", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gg4k-5ed","Zehnkampf U18 M", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gg5u-5h7","Zehnkampf W", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gftl-55l","Sechskampf U16 M", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986g3q0-7c","UBS Kids Cup", False, "UKC", ["60M", "WEZ", "BAL"]),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ggf8-5px","3000 m walk", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ggoi-5vt","5000 m walk", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ggrt-5yp","20000 m walk", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986ggzb-64j","5 km walk", False),
        Disziplin("5c4o3k5m-d686mo-j986g2ie-1-j986gh2b-67f","10 km walk", False)
]

# 
# def getDisziplinsIds():
#     ids = {
#         "60m" : "5c4o3k5m-d686mo-j986g2ie-1-j986g3pt-79",
#         "80m" : "5c4o3k5m-d686mo-j986g2ie-1-j986gefj-3vd",
#         "100m" : "5c4o3k5m-d686mo-j986g2ie-1-j986gfpc-4zv",
#         "200m" : "5c4o3k5m-d686mo-j986g2ie-1-j986ghgt-6ks",
#         "400m" : "5c4o3k5m-d686mo-j986g2ie-1-j986gihb-6m2",
#         "600m" : "",
#         "800m" : "",
#         "1000m" : "",
#         "1500m" : "",
#         "3000m" : "",
#         "80m Hürden" : "",
#         "100m Hürden 76" : "",
#         "100m Hürden 84" : "",
#         "110m Hürden 91" : "",
#         "110m Hürden 91" : "",
#         "110m Hürden 99" : "",
#         "110m Hürden 107" : "",
#         "Weit" : "",
#         "Hoch" : "",
#         "Stab" : "",
#         "Drei" : "",
#         "Kugel 3kg" : "",
#         "Kugel 4kg" : "",
#         "Kugel 5kg" : "",
#         "Kugel 6kg" : "",
#         "Kugel 7.25kg" : "",
#         "Diskus 0.75" : "",
#         "Diskus 1" : "",
#         "Diskus 1.5" : "",
#         "Diskus 1.75" : "",
#         "Diskus 2" : "",
#         "Speer 400" : "",
#         "Speer 500" : "",
#         "Speer 600" : "",
#         "Speer 700" : "",
#         "Speer 800" : ""
#         }
#     return ids
#     
# def getId2Disziplin():
#     return dict((v,k) for k,v in getDisziplinsIds().items())

    

    
# def getDisziplinFromName(disziplinName):    
#     for disziplin in getDisziplins():
#         if disziplinName == disziplin.name:
#             return disziplin