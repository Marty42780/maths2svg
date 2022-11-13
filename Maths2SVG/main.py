import svgwrite, svgwrite.utils, svgwrite.base
import cairosvg
import math

# TODO Arrowheads
# TODO Auto-scale export + allow to choose size
# TODO Display Unicode



def circularGraph(graphInputs: dict, fileType: str='svg', label: bool=True, outputWidth: float=-1, outputHeight: float=-1, mainColor: str='lightgrey', bgColor: str='transparent', pointColor: str='grey', labelColor: str='black'):
    """ Generate a circular graph of points and arrows.
    \n Parameters :
    \n - `graphInputs` : Dictionary with such format : 
    \n\t `{"A": ["B", "C", …], "B": ["C", …], …}`
    \n - `fileType` : Generated file extension. Among : 
    \n\t - SVG
    \n\t - PNG
    \n\t - PS
    \n\t - PDF
    \n - `label` : Show point names
    \n - `outputWidth` : Output file width (-1 for auto-width)
    \n - `outputHeight` : Output file height (-1 for auto-height)
    \n - `mainColor` : Color of the arrows and point strokes
    \n - `bgColor` : Color behind the graph [can be transparent]
    \n - `pointColor` : Color of the points [can be transparent]
    \n - `labelColor` : Color of the point labels [can be transparent]
    \n A maximum a 3 characters (Latin or Cyrillic) for each point will be properly displayed
    """
    # Constants
    numberofpoints = len(graphInputs)
    CircularGraphPointRadius = 140/numberofpoints+20
    CircularGraphRadius = numberofpoints*10+200
    insideAngle = 2*math.pi/len(graphInputs)
    centerxy = CircularGraphRadius+CircularGraphPointRadius+15/numberofpoints+0.5+10

    # Colors
    transparent = svgwrite.solidcolor.SolidColor(color='white', opacity=None, profile='tiny')

    # Markers
    arrowhead = svgwrite.container.Marker(size = (100, 100), orient ='auto')


    for point in enumerate(graphInputs.keys()):
        graphInputs[point[1]].insert(0, ((math.cos(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius), (math.sin(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius)))

    dwg = svgwrite.Drawing('gengraph.svg')
    
    # arrowhead = dwg.marker(insert=(5,5), size=(100,100), orient="auto") # style='markerWidth="100" markerHeight="70" refX="0" refY="3.5" orient="auto"'
    # dwg.add(arrowhead)
    if mainColor == 'transparent':
        mainColor=transparent
    if pointColor == 'transparent':
        pointColor=transparent
    

    if bgColor != 'transparent':
        dwg.add(dwg.rect((-centerxy, -centerxy), (centerxy*2, centerxy*2), fill=bgColor))
        


    for point in enumerate(graphInputs.keys()):
        for arrow in graphInputs[point[1]][1:]:
            if arrow!=point[1]:
                angle = math.atan2((graphInputs[arrow][0][1]-graphInputs[point[1]][0][1]),(graphInputs[arrow][0][0]-graphInputs[point[1]][0][0]))
                drawn_arrow = dwg.line(start=(graphInputs[point[1]][0][0]+CircularGraphPointRadius*math.cos(angle), graphInputs[point[1]][0][1]+CircularGraphPointRadius*math.sin(angle)), end=(graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle))) #, style='marker-end="url('+arrow+')"'
                drawn_arrow.stroke(mainColor, width=3)
                # drawn_arrow.set_markers(arrowhead)
                dwg.add(drawn_arrow)
            else:
                pass
                # angle = math.atan2((graphInputs[arrow][0][1]-centerxy),(graphInputs[arrow][0][0]-centerxy))
                # drawn_arrow = dwg.viewbox()
    for point in enumerate(graphInputs.keys()):
        small_circle = dwg.circle(center=graphInputs[point[1]][0], r=CircularGraphPointRadius)
        small_circle.fill(pointColor).stroke(mainColor, width=30/numberofpoints+1)
        dwg.add(small_circle)
    if label and labelColor != 'transparent':
        for point in enumerate(graphInputs.keys()):
                point_name = dwg.text(point[1], x=[graphInputs[point[1]][0][0]], y=[graphInputs[point[1]][0][1]+2], alignment_baseline="middle", text_anchor="middle", style='fill: ' + labelColor + ';  font-size: ' + str(4/5*CircularGraphPointRadius) + 'px; text-transform: capitalize; font-family: Arial, system-ui')
                dwg.add(point_name)
    
    # dwg.fit(horiz='center', vert='middle', scale='slice') 
    # PILlow to resize auto ?
    dwg.save()
    print("Image Saved")

    # Resize and scale svg

    if 'svg' in fileType:
        print("Converting to SVG…")
        cairosvg.svg2svg(url="./gengraph.svg", write_to="../doc/graph.svg", output_width=centerxy*2, output_height=centerxy*2)
    if 'png' in fileType:
        print("Converting to PNG…")
        cairosvg.svg2png(url="./gengraph.svg", write_to="../doc/graph.png", output_width=centerxy*2, output_height=centerxy*2)
    if 'ps' in fileType:
        print("Converting to PS…")
        cairosvg.svg2ps(url="./gengraph.svg", write_to="../doc/graph.ps", output_width=centerxy*2, output_height=centerxy*2)
    if 'pdf' in fileType: 
        print("Converting to PDF…")
        cairosvg.svg2pdf(url="./gengraph.svg", write_to="../doc/graph.pdf", output_width=centerxy*2, output_height=centerxy*2)



if __name__== "__main__":
    circularGraph({
        "a":["a", "d", "g", "eu", "ex"],
        "b":["a", "c", "g", "eu", "ex"],
        "c":["a", "d", "g", "eu", "ex"],
        "d":["a", "d", "g", "eu", "ex"],
        "e":["a", "d", "g", "eu", "ex"],
        "f":["a", "d", "g", "eu", "ex"],
        "g":["a", "d", "g", "eu", "ex"],
        "h":["a", "d", "g", "eu", "ex"],
        "i":["a", "d", "g", "eu", "ex"],
        "j":["a", "d", "g", "eu", "ex"],
        "k":["a", "d", "g", "eu", "ex"],
        "l":["a", "d", "g", "eu", "ex"],
        "m":["a", "d", "g", "eu", "ex"],
        "n":["a", "d", "g", "eu", "ex"],
        "o":["a", "d", "g", "eu", "ex"],
        "p":["a", "d", "g", "eu", "ex"],
        "q":["a", "d", "g", "eu", "ex"],
        "r":["a", "d", "g", "eu", "ex"],
        "s":["a", "d", "g", "eu", "ex"],
        "t":["a", "d", "g", "eu", "ex"],
        "u":["a", "d", "g", "eu", "ex"],
        "v":["a", "d", "g", "eu", "ex"],
        "w":["a", "d", "g", "eu", "ex"],
        "x":["a", "d", "g", "eu", "ex"],
        "y":["a", "d", "g", "eu", "ex"],
        "z":["a", "d", "g", "eu", "ex"],
        "aa":["a", "d", "g", "eu", "ex"],
        "ab":["a", "d", "g", "eu", "ex"],
        "ac":["a", "d", "g", "eu", "ex"],
        "ad":["a", "d", "g", "eu", "ex"],
        "ae":["a", "d", "g", "eu", "ex"],
        "af":["a", "d", "g", "eu", "ex"],
        "ag":["a", "d", "g", "eu", "ex"],
        "ah":["a", "d", "g", "eu", "ex"],
        "ai":["a", "d", "g", "eu", "ex"],
        "aj":["a", "d", "g", "eu", "ex"],
        "ak":["a", "d", "g", "eu", "ex"],
        "al":["a", "d", "g", "eu", "ex"],
        "am":["a", "d", "g", "eu", "ex"],
        "an":["a", "d", "g", "eu", "ex"],
        "ao":["a", "d", "g", "eu", "ex"],
        "ap":["a", "d", "g", "eu", "ex"],
        "aq":["a", "d", "g", "eu", "ex"],
        "ar":["a", "d", "g", "eu", "ex"],
        "as":["a", "d", "g", "eu", "ex"],
        "at":["a", "d", "g", "eu", "ex"],
        "au":["a", "d", "g", "eu", "ex"],
        "av":["a", "d", "g", "eu", "ex"],
        "aw":["a", "d", "g", "eu", "ex"],
        "ax":["a", "d", "g", "eu", "ex"],
        "ay":["a", "d", "g", "eu", "ex"],
        "az":["a", "d", "g", "eu", "ex"],
        "ba":["a", "d", "g", "eu", "ex"],
        "bb":["a", "d", "g", "eu", "ex"],
        "bc":["a", "d", "g", "eu", "ex"],
        "bd":["a", "d", "g", "eu", "ex"],
        "be":["a", "d", "g", "eu", "ex"],
        "bf":["a", "d", "g", "eu", "ex"],
        "bg":["a", "d", "g", "eu", "ex"],
        "bh":["a", "d", "g", "eu", "ex"],
        "bi":["a", "d", "g", "eu", "ex"],
        "bj":["a", "d", "g", "eu", "ex"],
        "bk":["a", "d", "g", "eu", "ex"],
        "bl":["a", "d", "g", "eu", "ex"],
        "bm":["a", "d", "g", "eu", "ex"],
        "bn":["a", "d", "g", "eu", "ex"],
        "bo":["a", "d", "g", "eu", "ex"],
        "bp":["a", "d", "g", "eu", "ex"],
        "bq":["a", "d", "g", "eu", "ex"],
        "br":["a", "d", "g", "eu", "ex"],
        "bs":["a", "d", "g", "eu", "ex"],
        "bt":["a", "d", "g", "eu", "ex"],
        "bu":["a", "d", "g", "eu", "ex"],
        "bv":["a", "d", "g", "eu", "ex"],
        "bw":["a", "d", "g", "eu", "ex"],
        "bx":["a", "d", "g", "eu", "ex"],
        "by":["a", "d", "g", "eu", "ex"],
        "bz":["a", "d", "g", "eu", "ex"],
        "aa":["a", "d", "g", "eu", "ex"],
        "ab":["a", "d", "g", "eu", "ex"],
        "ac":["a", "d", "g", "eu", "ex"],
        "ad":["a", "d", "g", "eu", "ex"],
        "ae":["a", "d", "g", "eu", "ex"],
        "af":["a", "d", "g", "eu", "ex"],
        "ag":["a", "d", "g", "eu", "ex"],
        "ah":["a", "d", "g", "eu", "ex"],
        "ai":["a", "d", "g", "eu", "ex"],
        "aj":["a", "d", "g", "eu", "ex"],
        "ak":["a", "d", "g", "eu", "ex"],
        "al":["a", "d", "g", "eu", "ex"],
        "am":["a", "d", "g", "eu", "ex"],
        "an":["a", "d", "g", "eu", "ex"],
        "ao":["a", "d", "g", "eu", "ex"],
        "ap":["a", "d", "g", "eu", "ex"],
        "aq":["a", "d", "g", "eu", "ex"],
        "ar":["a", "d", "g", "eu", "ex"],
        "as":["a", "d", "g", "eu", "ex"],
        "at":["a", "d", "g", "eu", "ex"],
        "au":["a", "d", "g", "eu", "ex"],
        "av":["a", "d", "g", "eu", "ex"],
        "aw":["a", "d", "g", "eu", "ex"],
        "ax":["a", "d", "g", "eu", "ex"],
        "ay":["a", "d", "g", "eu", "ex"],
        "az":["a", "d", "g", "eu", "ex"],
        "ba":["a", "d", "g", "eu", "ex"],
        "bb":["a", "d", "g", "eu", "ex"],
        "bc":["a", "d", "g", "eu", "ex"],
        "bd":["a", "d", "g", "eu", "ex"],
        "be":["a", "d", "g", "eu", "ex"],
        "bf":["a", "d", "g", "eu", "ex"],
        "bg":["a", "d", "g", "eu", "ex"],
        "bh":["a", "d", "g", "eu", "ex"],
        "bi":["a", "d", "g", "eu", "ex"],
        "bj":["a", "d", "g", "eu", "ex"],
        "bk":["a", "d", "g", "eu", "ex"],
        "bl":["a", "d", "g", "eu", "ex"],
        "bm":["a", "d", "g", "eu", "ex"],
        "bn":["a", "d", "g", "eu", "ex"],
        "bo":["a", "d", "g", "eu", "ex"],
        "bp":["a", "d", "g", "eu", "ex"],
        "bq":["a", "d", "g", "eu", "ex"],
        "br":["a", "d", "g", "eu", "ex"],
        "bs":["a", "d", "g", "eu", "ex"],
        "bt":["a", "d", "g", "eu", "ex"],
        "bu":["a", "d", "g", "eu", "ex"],
        "bv":["a", "d", "g", "eu", "ex"],
        "bw":["a", "d", "g", "eu", "ex"],
        "bx":["a", "d", "g", "eu", "ex"],
        "by":["a", "d", "g", "eu", "ex"],
        "bz":["a", "d", "g", "eu", "ex"],
        "ca":["a", "d", "g", "eu", "ex"],
        "cb":["a", "d", "g", "eu", "ex"],
        "cc":["a", "d", "g", "eu", "ex"],
        "cd":["a", "d", "g", "eu", "ex"],
        "ce":["a", "d", "g", "eu", "ex"],
        "cf":["a", "d", "g", "eu", "ex"],
        "cg":["a", "d", "g", "eu", "ex"],
        "ch":["a", "d", "g", "eu", "ex"],
        "ci":["a", "d", "g", "eu", "ex"],
        "cj":["a", "d", "g", "eu", "ex"],
        "ck":["a", "d", "g", "eu", "ex"],
        "cl":["a", "d", "g", "eu", "ex"],
        "cm":["a", "d", "g", "eu", "ex"],
        "cn":["a", "d", "g", "eu", "ex"],
        "co":["a", "d", "g", "eu", "ex"],
        "cp":["a", "d", "g", "eu", "ex"],
        "cq":["a", "d", "g", "eu", "ex"],
        "cr":["a", "d", "g", "eu", "ex"],
        "cs":["a", "d", "g", "eu", "ex"],
        "ct":["a", "d", "g", "eu", "ex"],
        "cu":["a", "d", "g", "eu", "ex"],
        "cv":["a", "d", "g", "eu", "ex"],
        "cw":["a", "d", "g", "eu", "ex"],
        "cx":["a", "d", "g", "eu", "ex"],
        "cy":["a", "d", "g", "eu", "ex"],
        "cz":["a", "d", "g", "eu", "ex"],
        "da":["a", "d", "g", "eu", "ex"],
        "db":["a", "d", "g", "eu", "ex"],
        "dc":["a", "d", "g", "eu", "ex"],
        "dd":["a", "d", "g", "eu", "ex"],
        "de":["a", "d", "g", "eu", "ex"],
        "df":["a", "d", "g", "eu", "ex"],
        "dg":["a", "d", "g", "eu", "ex"],
        "dh":["a", "d", "g", "eu", "ex"],
        "di":["a", "d", "g", "eu", "ex"],
        "dj":["a", "d", "g", "eu", "ex"],
        "dk":["a", "d", "g", "eu", "ex"],
        "dl":["a", "d", "g", "eu", "ex"],
        "dm":["a", "d", "g", "eu", "ex"],
        "dn":["a", "d", "g", "eu", "ex"],
        "do":["a", "d", "g", "eu", "ex"],
        "dp":["a", "d", "g", "eu", "ex"],
        "dq":["a", "d", "g", "eu", "ex"],
        "dr":["a", "d", "g", "eu", "ex"],
        "ds":["a", "d", "g", "eu", "ex"],
        "dt":["a", "d", "g", "eu", "ex"],
        "du":["a", "d", "g", "eu", "ex"],
        "dv":["a", "d", "g", "eu", "ex"],
        "dw":["a", "d", "g", "eu", "ex"],
        "dx":["a", "d", "g", "eu", "ex"],
        "dy":["a", "d", "g", "eu", "ex"],
        "dz":["a", "d", "g", "eu", "ex"],
        "ea":["a", "d", "g", "eu", "ex"],
        "eb":["a", "d", "g", "eu", "ex"],
        "ec":["a", "d", "g", "eu", "ex"],
        "ed":["a", "d", "g", "eu", "ex"],
        "ee":["a", "d", "g", "eu", "ex"],
        "ef":["a", "d", "g", "eu", "ex"],
        "eg":["a", "d", "g", "eu", "ex"],
        "eh":["a", "d", "g", "eu", "ex"],
        "ei":["a", "d", "g", "eu", "ex"],
        "ej":["a", "d", "g", "eu", "ex"],
        "ek":["a", "d", "g", "eu", "ex"],
        "el":["a", "d", "g", "eu", "ex"],
        "em":["a", "d", "g", "eu", "ex"],
        "en":["a", "d", "g", "eu", "ex"],
        "eo":["a", "d", "g", "eu", "ex"],
        "ep":["a", "d", "g", "eu", "ex"],
        "eq":["a", "d", "g", "eu", "ex"],
        "er":["a", "d", "g", "eu", "ex"],
        "es":["a", "d", "g", "eu", "ex"],
        "et":["a", "d", "g", "eu", "ex"],
        "eu":["a", "d", "g", "eu", "ex"],
        "ev":["a", "d", "g", "eu", "ex"],
        "ew":["a", "d", "g", "eu", "ex"],
        "ex":["a", "d", "g", "eu", "ex"],
        "ey":["a", "d", "g", "eu", "ex"],
        "ez":["a", "d", "g", "eu", "ex"]
    }, 'psvgpngpdf')