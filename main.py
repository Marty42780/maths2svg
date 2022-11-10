import svgwrite, svgwrite.utils
import math

# Colors 
transparent = svgwrite.solidcolor.SolidColor(color='white', opacity=None, profile='tiny')


def circularGraph(graphInputs: dict):
    
    # Constants
    numberofpoints = len(graphInputs)
    CircularGraphPointRadius = 1/numberofpoints*140+20
    CircularGraphRadius = numberofpoints*10+200
    centerxy = numberofpoints*10+300
    angle = 2*math.pi/len(graphInputs)

    for point in enumerate(graphInputs.keys()):
        graphInputs[point[1]].insert(0, ((math.cos(point[0]*(angle)-math.pi/2)*CircularGraphRadius+centerxy), (math.sin(point[0]*(angle)-math.pi/2)*CircularGraphRadius+centerxy)))
    print(graphInputs)
    

    dwg = svgwrite.Drawing('test.svg')
    # dwg.add(dwg.rect((0, 0), (centerxy*2, centerxy*2), fill='blue'))

    for point in enumerate(graphInputs.keys()):
        print(point)
        for arrow in graphInputs[point[1]][1:]:
            print(graphInputs[point[1]][0], graphInputs[arrow][0])
            drawn_arrow = dwg.line(start=(graphInputs[point[1]][0]), end=(graphInputs[arrow][0]))
            drawn_arrow.fill('white').stroke('white', width=3)
            dwg.add(drawn_arrow)
        small_circle = dwg.circle(center=graphInputs[point[1]][0], r=CircularGraphPointRadius)
        small_circle.fill('white').stroke('white', width=30/numberofpoints+1)
        
        
        dwg.add(small_circle)
    print("Image Saved")
    dwg.save()

if __name__== "__main__":
    circularGraph({
        "a":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "b":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "c":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "d":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "e":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "f":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "g":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "h":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "i":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "j":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "k":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "l":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "m":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "n":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "o":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "p":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "q":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "r":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "s":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "t":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "u":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "v":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "w":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "x":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "y":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "z":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        # "aa":["a", "b", "c"],"ab":["a", "b", "c"],"ac":["a", "b", "c"],"ad":["a", "b", "c"],"ae":["a", "b", "c"],"af":["a", "b", "c"],"ag":["a", "b", "c"],"ah":["a", "b", "c"],"ai":["a", "b", "c"],"aj":["a", "b", "c"],"ak":["a", "b", "c"],"al":["a", "b", "c"],"am":["a", "b", "c"],"an":["a", "b", "c"],"ao":["a", "b", "c"],"ap":["a", "b", "c"],"aq":["a", "b", "c"],"ar":["a", "b", "c"],"as":["a", "b", "c"],"at":["a", "b", "c"],"au":["a", "b", "c"],"av":["a", "b", "c"],"aw":["a", "b", "c"],"ax":["a", "b", "c"],"ay":["a", "b", "c"],"az":["a", "b", "c"],"ba":["a", "b", "c"],"bb":["a", "b", "c"],"bc":["a", "b", "c"],"bd":["a", "b", "c"],"be":["a", "b", "c"],"bf":["a", "b", "c"],"bg":["a", "b", "c"],"bh":["a", "b", "c"],"bi":["a", "b", "c"],"bj":["a", "b", "c"],"bk":["a", "b", "c"],"bl":["a", "b", "c"],"bm":["a", "b", "c"],"bn":["a", "b", "c"],"bo":["a", "b", "c"],"bp":["a", "b", "c"],"bq":["a", "b", "c"],"br":["a", "b", "c"],"bs":["a", "b", "c"],"bt":["a", "b", "c"],"bu":["a", "b", "c"],"bv":["a", "b", "c"],"bw":["a", "b", "c"],"bx":["a", "b", "c"],"by":["a", "b", "c"],"bz":["a", "b", "c"],"ca":["a", "b", "c"],"cb":["a", "b", "c"],"cc":["a", "b", "c"],"cd":["a", "b", "c"],"ce":["a", "b", "c"],"cf":["a", "b", "c"],"cg":["a", "b", "c"],"ch":["a", "b", "c"],"ci":["a", "b", "c"],"cj":["a", "b", "c"],"ck":["a", "b", "c"],"cl":["a", "b", "c"],"cm":["a", "b", "c"],"cn":["a", "b", "c"],"co":["a", "b", "c"],"cp":["a", "b", "c"],"cq":["a", "b", "c"],"cr":["a", "b", "c"],"cs":["a", "b", "c"],"ct":["a", "b", "c"],"cu":["a", "b", "c"],"cv":["a", "b", "c"],"cw":["a", "b", "c"],"cx":["a", "b", "c"],"cy":["a", "b", "c"],"cz":["a", "b", "c"],"da":["a", "b", "c"],"db":["a", "b", "c"],"dc":["a", "b", "c"],"dd":["a", "b", "c"],"de":["a", "b", "c"],"df":["a", "b", "c"],"dg":["a", "b", "c"],"dh":["a", "b", "c"],"di":["a", "b", "c"],"dj":["a", "b", "c"],"dk":["a", "b", "c"],"dl":["a", "b", "c"],"dm":["a", "b", "c"],"dn":["a", "b", "c"],"do":["a", "b", "c"],"dp":["a", "b", "c"],"dq":["a", "b", "c"],"dr":["a", "b", "c"],"ds":["a", "b", "c"],"dt":["a", "b", "c"],"du":["a", "b", "c"],"dv":["a", "b", "c"],"dw":["a", "b", "c"],"dx":["a", "b", "c"],"dy":["a", "b", "c"],"dz":["a", "b", "c"],"ea":["a", "b", "c"],"eb":["a", "b", "c"],"ec":["a", "b", "c"],"ed":["a", "b", "c"],"ee":["a", "b", "c"],"ef":["a", "b", "c"],"eg":["a", "b", "c"],"eh":["a", "b", "c"],"ei":["a", "b", "c"],"ej":["a", "b", "c"],"ek":["a", "b", "c"],"el":["a", "b", "c"],"em":["a", "b", "c"],"en":["a", "b", "c"],"eo":["a", "b", "c"],"ep":["a", "b", "c"],"eq":["a", "b", "c"],"er":["a", "b", "c"],"es":["a", "b", "c"],"et":["a", "b", "c"],"eu":["a", "b", "c"],"ev":["a", "b", "c"],"ew":["a", "b", "c"],"ex":["a", "b", "c"],"ey":["a", "b", "c"],"ez":["a", "b", "c"]
    })