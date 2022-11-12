import svgwrite, svgwrite.utils
import cairosvg
import math

# TODO Arrowheads
# TODO Auto-scale export + allow to choose size
# TODO Display Unicode

transparent = svgwrite.solidcolor.SolidColor(color='white', opacity=None, profile='tiny')

def circularGraph(graphInputs: dict, maincolor: str='red', bgcolor: str=transparent, text: bool=True, type: str='svg'):
    """Generate a graph of points and arrows.
    \nParameters :
    \n- `graphInputs`
    \nKeys 
    \n\texample : `{"A": ["B", "C", …], "B": ["C", …]}`
    \n\tA maximum a 3 characters (Latin or Cyrillic) for each point will be properly displayed
    """
    # Constants
    global centerxy
    numberofpoints = len(graphInputs)
    CircularGraphPointRadius = 140/numberofpoints+20
    CircularGraphRadius = numberofpoints*10+200
    angle = 2*math.pi/len(graphInputs)
    centerxy = CircularGraphRadius+CircularGraphPointRadius+10

   # for point in 
    for point in enumerate(graphInputs.keys()):
        graphInputs[point[1]].insert(0, ((math.cos(point[0]*(angle)-math.pi/2)*CircularGraphRadius), (math.sin(point[0]*(angle)-math.pi/2)*CircularGraphRadius)))

    dwg = svgwrite.Drawing('graph.svg')
    
    # arrowhead = dwg.marker(insert=(5,5), size=(100,100), orient="auto") # style='markerWidth="100" markerHeight="70" refX="0" refY="3.5" orient="auto"'
    # arrowhead.add(dwg.circle((5, 5), r=50, fill='red'))
    
    # dwg.add(dwg.rect((0, 0), (centerxy*2, centerxy*2), fill='blue'))

    for point in enumerate(graphInputs.keys()):
        for arrow in graphInputs[point[1]][1:]:
            angle = math.atan2((graphInputs[arrow][0][1]-graphInputs[point[1]][0][1]),(graphInputs[arrow][0][0]-graphInputs[point[1]][0][0]))
            drawn_arrow = dwg.line(start=(graphInputs[point[1]][0][0]+CircularGraphPointRadius*math.cos(angle), graphInputs[point[1]][0][1]+CircularGraphPointRadius*math.sin(angle)), end=(graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)), style='marker-end="url('+arrow+')"')
            drawn_arrow.stroke(maincolor, width=3)
            # drawn_arrow.set_markers(arrowhead)
            dwg.add(drawn_arrow)
    for point in enumerate(graphInputs.keys()):
        small_circle = dwg.circle(center=graphInputs[point[1]][0], r=CircularGraphPointRadius)
        small_circle.fill(transparent).stroke(maincolor, width=30/numberofpoints+1)
        dwg.add(small_circle)
        point_name = dwg.text(point[1], x=[graphInputs[point[1]][0][0]], y=[graphInputs[point[1]][0][1]+2], alignment_baseline="middle", text_anchor="middle", style='fill: ' + maincolor + ';  font-size: ' + str(4/5*CircularGraphPointRadius) + 'px; text-transform: capitalize; font-family: Arial, system-ui')
        dwg.add(point_name)
    dwg.save()
    print("Image Saved")
    

if __name__== "__main__":
    circularGraph({
        "𒀰":["c"],
        "BBB":["d"],
        "c":["e"],
        "d":["𒀰"],
        "e":["BBB"],
        # "f":[],
        # "g":[],
        # "h":[],
        # "i":[],
        # "j":[],
        # "k":[],
        # "l":[],
        # "m":[],
        # "n":[],
        # "o":[],
        # "p":[],
        # "q":[],
        # "r":[],
        # "s":[],
        # "t":[],
        # "u":[],
        # "v":[],
        # "w":[],
        # "x":[],
        # "y":[],
        # "z":[],
        # "aa":[],
        # "ab":[],
        # "ac":[],
        # "ad":[],
        # "ae":[],
        # "af":[],
        # "ag":[],
        # "ah":[],
        # "ai":[],
        # "aj":[],
        # "ak":[],
        # "al":[],
        # "am":[],
        # "an":[],
        # "ao":[],
        # "ap":[],
        # "aq":[],
        # "ar":[],
        # "as":[],
        # "at":[],
        # "au":[],
        # "av":[],
        # "aw":[],
        # "ax":[],
        # "ay":[],
        # "az":[],
        # "ba":[],
        # "bb":[],
        # "bc":[],
        # "bd":[],
        # "be":[],
        # "bf":[],
        # "bg":[],
        # "bh":[],
        # "bi":[],
        # "bj":[],
        # "bk":[],
        # "bl":[],
        # "bm":[],
        # "bn":[],
        # "bo":[],
        # "bp":[],
        # "bq":[],
        # "br":[],
        # "bs":[],
        # "bt":[],
        # "bu":[],
        # "bv":[],
        # "bw":[],
        # "bx":[],
        # "by":[],
        # "bz":[],
        # "aa":[],
        # "ab":[],
        # "ac":[],
        # "ad":[],
        # "ae":[],
        # "af":[],
        # "ag":[],
        # "ah":[],
        # "ai":[],
        # "aj":[],
        # "ak":[],
        # "al":[],
        # "am":[],
        # "an":[],
        # "ao":[],
        # "ap":[],
        # "aq":[],
        # "ar":[],
        # "as":[],
        # "at":[],
        # "au":[],
        # "av":[],
        # "aw":[],
        # "ax":[],
        # "ay":[],
        # "az":[],
        # "ba":[],
        # "bb":[],
        # "bc":[],
        # "bd":[],
        # "be":[],
        # "bf":[],
        # "bg":[],
        # "bh":[],
        # "bi":[],
        # "bj":[],
        # "bk":[],
        # "bl":[],
        # "bm":[],
        # "bn":[],
        # "bo":[],
        # "bp":[],
        # "bq":[],
        # "br":[],
        # "bs":[],
        # "bt":[],
        # "bu":[],
        # "bv":[],
        # "bw":[],
        # "bx":[],
        # "by":[],
        # "bz":[],
        # "ca":[],
        # "cb":[],
        # "cc":[],
        # "cd":[],
        # "ce":[],
        # "cf":[],
        # "cg":[],
        # "ch":[],
        # "ci":[],
        # "cj":[],
        # "ck":[],
        # "cl":[],
        # "cm":[],
        # "cn":[],
        # "co":[],
        # "cp":[],
        # "cq":[],
        # "cr":[],
        # "cs":[],
        # "ct":[],
        # "cu":[],
        # "cv":[],
        # "cw":[],
        # "cx":[],
        # "cy":[],
        # "cz":[],
        # "da":[],
        # "db":[],
        # "dc":[],
        # "dd":[],
        # "de":[],
        # "df":[],
        # "dg":[],
        # "dh":[],
        # "di":[],
        # "dj":[],
        # "dk":[],
        # "dl":[],
        # "dm":[],
        # "dn":[],
        # "do":[],
        # "dp":[],
        # "dq":[],
        # "dr":[],
        # "ds":[],
        # "dt":[],
        # "du":[],
        # "dv":[],
        # "dw":[],
        # "dx":[],
        # "dy":[],
        # "dz":[],
        # "ea":[],
        # "eb":[],
        # "ec":[],
        # "ed":[],
        # "ee":[],
        # "ef":[],
        # "eg":[],
        # "eh":[],
        # "ei":[],
        # "ej":[],
        # "ek":[],
        # "el":[],
        # "em":[],
        # "en":[],
        # "eo":[],
        # "ep":[],
        # "eq":[],
        # "er":[],
        # "es":[],
        # "et":[],
        # "eu":[],
        # "ev":[],
        # "ew":[],
        # "ex":[],
        # "ey":[],
        # "ez":[]
    })
        
    cairosvg.svg2png(url="./gengraph.svg", write_to="./graph.png", output_width=centerxy*2, output_height=centerxy*2)
    cairosvg.svg2svg(url="./gengraph.svg", write_to="./graph.svg", output_width=centerxy*2, output_height=centerxy*2) #
