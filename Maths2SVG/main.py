import svgwrite, svgwrite.utils, svgwrite.base
import cairosvg
import math
import random
import time

# TODO Display Unicode
# TODO Arrows weight
# TODO Possibility to show logs in shell

randomColors =  'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'grey', 'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'
CGdefaults = {
    "fileType": 'svg', 
    "graphInputs": {"Why": ["not"], "not": ["try"], "try": ["try"]}, 
    "oriented": True, 
    "allowLoops": True, 
    "label": True, 
    "labelCapitalize": False,
    "outputSize": -1,
    "mainColor": 'random',
    "bgColor": 'transparent',
    "pointColor": 'transparent',
    "labelColor": 'random',
    "globalOpacity": 1,
}

def circularGraph(
    fileType: str=CGdefaults["fileType"],
    graphInputs: dict=CGdefaults["graphInputs"],
    oriented: bool=CGdefaults["oriented"],
    allowLoops: bool=CGdefaults["allowLoops"],
    label: bool=CGdefaults["label"],
    labelCapitalize: bool=CGdefaults["labelCapitalize"],
    outputSize: int=CGdefaults["outputSize"],
    mainColor: str=CGdefaults["mainColor"],
    bgColor: str=CGdefaults["bgColor"],
    pointColor: str=CGdefaults["pointColor"],
    labelColor: str=CGdefaults["labelColor"],
    globalOpacity: float=CGdefaults["globalOpacity"]):
    
    """ Generate a circular graph of points and arrows.
    \n Parameters :
    \n - `graphInputs` : Dictionary with such format : 
    \n\t `{"A": ["B", "C", …], "B": ["C", …], …}`
    \n - `fileType` : Generated file extensions (concatted in lowercase) Among : 
    \n\t - SVG
    \n\t - PNG
    \n\t - PS
    \n\t - PDF
    \n\t Example (to generate all possible formats) : 'svgpngpspdf'
    \n - `oriented` : generated graph will be oriented (with arrows instead of just lines) when `True`
    \n - `allowLoops` : Allow arrows to point at their origin point [enlarges output size]
    \n - `label` : Show point names
    \n - `labelCapitalize` : Make point names uppercase
    \n - `outputSize` : Output file width=height (pixels)
    \n - `mainColor` : Color of the arrows and point borders [can be 'random'  or 'linkedrandom' ('linkedrandom'='random' if not oriented) or HTML color string]
    \n - `bgColor` : Color behind the graph [can be 'transparent' or 'random' or HTML color string]
    \n - `pointColor` : Color of the points [can be 'transparent' or 'random' or 'linkedrandom' or HTML color string]
    \n - `labelColor` : Color of the point names [can be or 'random' or 'linkedrandom' or HTML color string]
    \n - `globalOpacity` : Opacity of the whole output
    \n A maximum a 3 characters (Latin or Cyrillic) for each point will be properly displayed.
    \n Graph proportion is automatic.
    \n Maximum export size is 32767x32767.
    """

    startTime = time.time()
    # Constants
    numberofpoints = len(graphInputs)
    if outputSize<=0:
        outputSize=2000+numberofpoints*10
    if outputSize>32767:
        outputSize=32767
    insideAngle = 2*math.pi/numberofpoints
    centerxy = outputSize/2 # CircularGraphRadius+CircularGraphPointRadius+15/numberofpoints+0.5
    CircularGraphPointRadius = math.pi*centerxy/numberofpoints/(2+10/numberofpoints**2) # 140/numberofpoints+20 # x = 
    CircularGraphRadius = centerxy - 11*CircularGraphPointRadius/10 # numberofpoints*10+200
    if allowLoops:
        addLoopRad=CircularGraphPointRadius*3
    else:
        addLoopRad=0

    dwg = svgwrite.Drawing('Maths2SVG/gengraph.svg', profile='tiny')


    if mainColor=='linkedrandom' or pointColor=='linkedrandom' or labelColor=='linkedrandom':
        for point in enumerate(graphInputs.keys()):
            graphInputs[point[1]].insert(0, ((math.cos(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius), (math.sin(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius)))
            graphInputs[point[1]].insert(1, (randomColors[random.randint(0, 146)]))
        slicefrom2 = 1
    else:
        for point in enumerate(graphInputs.keys()):
            graphInputs[point[1]].insert(0, ((math.cos(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius), (math.sin(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius)))
        slicefrom2 = 0

    if bgColor != 'transparent':
        if bgColor !='random':
            dwg.add(dwg.rect((-centerxy-addLoopRad, -centerxy-addLoopRad), (centerxy*2+addLoopRad, centerxy*2+addLoopRad), fill=bgColor, opacity=globalOpacity))
        else:
            dwg.add(dwg.rect((-centerxy-addLoopRad, -centerxy-addLoopRad), (centerxy*2+addLoopRad, centerxy*2+addLoopRad), fill=randomColors[random.randint(0, 146)], opacity=globalOpacity))



    for point in enumerate(graphInputs.keys()):
        if mainColor == 'random':
            arrowColor = randomColors[random.randint(0, 146)]
        elif mainColor == 'linkedrandom':
            if oriented:
                arrowColor = graphInputs[point[1]][1]
            else:
                arrowColor = randomColors[random.randint(0, 146)]
        else:
            arrowColor = mainColor
        for arrow in graphInputs[point[1]][1+slicefrom2:]:
            if arrow in graphInputs:
                if arrow!=point[1]:
                    angle = math.atan2((graphInputs[arrow][0][1]-graphInputs[point[1]][0][1]),(graphInputs[arrow][0][0]-graphInputs[point[1]][0][0]))
                    drawn_arrow = dwg.line(
                        start=(graphInputs[point[1]][0][0]+CircularGraphPointRadius*math.cos(angle), graphInputs[point[1]][0][1]+CircularGraphPointRadius*math.sin(angle)), 
                        end=(graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)))
                    drawn_arrow.stroke(arrowColor, opacity=globalOpacity, width=CircularGraphPointRadius/10)
                    dwg.add(drawn_arrow)
                    if oriented:
                        drawn_arrow_marker = dwg.polygon(points=[
                                (graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)), 
                                (graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle)*1.5-CircularGraphPointRadius*0.25*math.sin(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)*1.5+CircularGraphPointRadius*0.25*math.cos(angle)), 
                                (graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle)*1.5+CircularGraphPointRadius*0.25*math.sin(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)*1.5-CircularGraphPointRadius*0.25*math.cos(angle))
                        ])
                        drawn_arrow_marker.fill(arrowColor, opacity=globalOpacity)
                        dwg.add(drawn_arrow_marker)

                elif allowLoops:
                    angle = math.atan2((graphInputs[arrow][0][1]),(graphInputs[arrow][0][0]))
                    pointcoor = graphInputs[point[1]][0]
                    temp_points = (
                        str(pointcoor[0]+CircularGraphPointRadius*math.cos(angle-math.pi/6)), 
                        str(pointcoor[1]+CircularGraphPointRadius*math.sin(angle-math.pi/6)), 
                        str(pointcoor[0]+3*CircularGraphPointRadius*math.cos(angle-math.pi/6)), 
                        str(pointcoor[1]+3*CircularGraphPointRadius*math.sin(angle-math.pi/6)), 
                        str(pointcoor[0]+3*CircularGraphPointRadius*math.cos(angle+math.pi/6)), 
                        str(pointcoor[1]+3*CircularGraphPointRadius*math.sin(angle+math.pi/6)), 
                        str(pointcoor[0]+CircularGraphPointRadius*math.cos(angle+math.pi/6)), 
                        str(pointcoor[1]+CircularGraphPointRadius*math.sin(angle+math.pi/6))
                    )
                    drawn_arrow = dwg.path(d="M"+temp_points[0]+","+temp_points[1]+" C"+temp_points[2]+","+temp_points[3]+" "+temp_points[4]+","+temp_points[5]+" "+temp_points[6]+","+temp_points[7], stroke=arrowColor, stroke_width=str(CircularGraphPointRadius/10)) # , transform = 'rotate('+str(angle)+')')
                    drawn_arrow.fill('white', opacity=0.0).stroke(arrowColor, opacity = globalOpacity)
                    dwg.add(drawn_arrow)
                    if oriented:
                        drawn_arrow_marker = dwg.polygon(points=[
                                (pointcoor[0]+CircularGraphPointRadius*math.cos(angle+math.pi/6), pointcoor[1]+CircularGraphPointRadius*math.sin(angle+math.pi/6)), 
                                (pointcoor[0]+1.5*CircularGraphPointRadius*math.cos(angle+math.pi/6)+CircularGraphPointRadius*0.25*math.sin(angle+math.pi/6), pointcoor[1]+1.5*CircularGraphPointRadius*math.sin(angle+math.pi/6)-CircularGraphPointRadius*0.25*math.cos(angle+math.pi/6)),
                                (pointcoor[0]+1.5*CircularGraphPointRadius*math.cos(angle+math.pi/6)-CircularGraphPointRadius*0.25*math.sin(angle+math.pi/6), pointcoor[1]+1.5*CircularGraphPointRadius*math.sin(angle+math.pi/6)+CircularGraphPointRadius*0.25*math.cos(angle+math.pi/6)), 
                        ])
                        drawn_arrow_marker.fill(arrowColor, opacity=globalOpacity)
                        dwg.add(drawn_arrow_marker)

    for point in enumerate(graphInputs.keys()):
        if mainColor == 'random':
            strokeColor = randomColors[random.randint(0, 146)]
        elif mainColor == 'linkedrandom':
            strokeColor = graphInputs[point[1]][1]
        else:
            strokeColor = mainColor
        small_circle = dwg.circle(center=graphInputs[point[1]][0], r=CircularGraphPointRadius)
        if pointColor!='transparent':
            if pointColor=='random':
                small_circle.fill(randomColors[random.randint(0, 146)], opacity=globalOpacity/2).stroke(strokeColor, opacity=globalOpacity, width=CircularGraphPointRadius/5)
            elif pointColor=='linkedrandom':
                small_circle.fill(graphInputs[point[1]][1], opacity=globalOpacity/2).stroke(strokeColor, opacity=globalOpacity, width=CircularGraphPointRadius/5)
            else:
                small_circle.fill(pointColor, opacity=globalOpacity).stroke(strokeColor, opacity=globalOpacity, width=CircularGraphPointRadius/5)

        else:
            small_circle.fill('white', opacity=0.0).stroke(strokeColor, opacity=globalOpacity, width=CircularGraphPointRadius/5)
        dwg.add(small_circle)

    if label and labelColor != 'transparent':
        for point in enumerate(graphInputs.keys()):
            pointLabel = point[1]
            if labelCapitalize:
                pointLabel = point[1].upper()
            if labelColor=='random':
                point_name = dwg.text(pointLabel, x=[graphInputs[point[1]][0][0]], y=[graphInputs[point[1]][0][1]], profile='full', alignment_baseline="middle", text_anchor="middle", style='fill:' + randomColors[random.randint(0, 146)] + ';  font-size: ' + str(7*CircularGraphPointRadius/10) + 'px; font-family: Arial, system-ui; opacity: '+str(globalOpacity)+';')
            elif labelColor=='linkedrandom':
                point_name = dwg.text(pointLabel, x=[graphInputs[point[1]][0][0]], y=[graphInputs[point[1]][0][1]], profile='full', alignment_baseline="middle", text_anchor="middle", style='fill:' + graphInputs[point[1]][1] + ';  font-size: ' + str(7*CircularGraphPointRadius/10) + 'px; font-family: Arial, system-ui; opacity: '+str(globalOpacity)+';')
            else:
                point_name = dwg.text(pointLabel, x=[graphInputs[point[1]][0][0]], y=[graphInputs[point[1]][0][1]], profile='full', alignment_baseline="middle", text_anchor="middle", style='fill:' + labelColor + ';  font-size: ' + str(7*CircularGraphPointRadius/10) + 'px; font-family: Arial, system-ui; opacity: '+str(globalOpacity)+';')
            dwg.add(point_name)

    
    dwg.save()
    print("Bridge SVG generated !")

    intertime = time.time()

    if 'svg' in fileType.lower():
        print("Converted to SVG (Vectors)", end=" ")
        cairosvg.svg2svg(url="Maths2SVG/gengraph.svg", write_to="Maths2SVG/results/graph.svg", output_width=outputSize+addLoopRad, output_height=outputSize+addLoopRad)
        print("in "+str(round((time.time()-intertime)*10000)/10)+" ms")
        intertime = time.time()
    if 'png' in fileType.lower():
        print("Converted to PNG ("+str(outputSize)+"x"+str(outputSize)+" px)", end=" ")
        cairosvg.svg2png(url="Maths2SVG/gengraph.svg", write_to="Maths2SVG/results/graph.png", output_width=outputSize+addLoopRad, output_height=outputSize+addLoopRad)
        print("in "+str(round((time.time()-intertime)*10000)/10)+" ms")
        intertime = time.time()
    if 'ps' in fileType.lower():
        print("Converted to PS (Vectors)", end=" ")
        cairosvg.svg2ps(url="Maths2SVG/gengraph.svg", write_to="Maths2SVG/results/graph.ps", output_width=outputSize+addLoopRad, output_height=outputSize+addLoopRad)
        print("in "+str(round((time.time()-intertime)*10000)/10)+" ms")
        intertime = time.time()
    if 'pdf' in fileType.lower(): 
        print("Converted to PDF (Vectors)", end=" ")
        cairosvg.svg2pdf(url="Maths2SVG/gengraph.svg", write_to="Maths2SVG/results/graph.pdf", output_width=outputSize+addLoopRad, output_height=outputSize+addLoopRad)
        print("in "+str(round((time.time()-intertime)*10000)/10)+" ms")
        intertime = time.time()
    
    print("Circular graph : operation terminated after "+str(round((time.time()-startTime)*10000)/10)+" ms")
    return True



if __name__== "__main__":
    circularGraph(
        fileType='png', # Or a list
        allowLoops=True,
        label=False,
        globalOpacity=1,
        oriented=True,
        outputSize=16,
        bgColor='transparent',
        pointColor='linkedrandom',
        labelColor='linkedrandom',
        mainColor='linkedrandom',
        graphInputs={
        "aa":["ab"],
        "ab":["ac"],
        "ac":["ad"],
        "ad":["aa"],
        # "ae":["aa", "ae"],
        # "af":["aa", "af"],
        # "ag":["aa", "ag"],
        # "ah":["aa", "ah"],
        # "ai":["aa", "ai"],
        # "aj":["aa", "aj"],
        # "ak":["aa", "ak"],
        # "al":["aa", "al"],
        # "am":["aa", "am"],
        # "an":["aa", "an"],
        # "ao":["aa", "ao"],
        # "ap":["aa", "ap"],
        # "aq":["aa", "aq"],
        # "ar":["aa", "ar"],
        # "as":["aa", "as"],
        # "at":["aa", "at"],
        # "au":["aa", "au"],
        # "av":["aa", "av"],
        # "aw":["aa", "aw"],
        # "ax":["aa", "ax"],
        # "ay":["aa", "ay"],
        # "az":["aa", "az"],
        # "ba":["aa"],
        # "bb":["aa"],
        # "bc":["aa"],
        # "bd":["aa"],
        # "be":["aa"],
        # "bf":["aa"],
        # "bg":["aa"],
        # "bh":["aa"],
        # "bi":["aa"],
        # "bj":["aa"],
        # "bk":["aa"],
        # "bl":["aa"],
        # "bm":["aa"],
        # "bn":["aa"],
        # "bo":["aa"],
        # "bp":["aa"],
        # "bq":["aa"],
        # "br":["aa"],
        # "bs":["aa"],
        # "bt":["aa"],
        # "bu":["aa"],
        # "bv":["aa"],
        # "bw":["aa"],
        # "bx":["aa"],
        # "by":["aa"],
        # "bz":["aa"],
        # "ca":["aa"],
        # "cb":["aa"],
        # "cc":["aa"],
        # "cd":["aa"],
        # "ce":["aa"],
        # "cf":["aa"],
        # "cg":["aa"],
        # "ch":["aa"],
        # "ci":["aa"],
        # "cj":["aa"],
        # "ck":["aa"],
        # "cl":["aa"],
        # "cm":["aa"],
        # "cn":["aa"],
        # "co":["aa"],
        # "cp":["aa"],
        # "cq":["aa"],
        # "cr":["aa"],
        # "cs":["aa"],
        # "ct":["aa"],
        # "cu":["aa"],
        # "cv":["aa"],
        # "cw":["aa"],
        # "cx":["aa"],
        # "cy":["aa"],
        # "cz":["aa"],
        # "da":["aa"],
        # "db":["aa"],
        # "dc":["aa"],
        # "dd":["aa"],
        # "de":["aa"],
        # "df":["aa"],
        # "dg":["aa"],
        # "dh":["aa"],
        # "di":["aa"],
        # "dj":["aa"],
        # "dk":["aa"],
        # "dl":["aa"],
        # "dm":["aa"],
        # "dn":["aa"],
        # "do":["aa"],
        # "dp":["aa"],
        # "dq":["aa"],
        # "dr":["aa"],
        # "ds":["aa"],
        # "dt":["aa"],
        # "du":["aa"],
        # "dv":["aa"],
        # "dw":["aa"],
        # "dx":["aa"],
        # "dy":["aa"],
        # "dz":["aa"],
        # "ea":["aa"],
        # "eb":["aa"],
        # "ec":["aa"],
        # "ed":["aa"],
        # "ee":["aa"],
        # "ef":["aa"],
        # "eg":["aa"],
        # "eh":["aa"],
        # "ei":["aa"],
        # "ej":["aa"],
        # "ek":["aa"],
        # "el":["aa"],
        # "em":["aa"],
        # "en":["aa"],
        # "eo":["aa"],
        # "ep":["aa"],
        # "eq":["aa"],
        # "er":["aa"],
        # "es":["aa"],
        # "et":["aa"],
        # "eu":["aa"],
        # "ev":["aa"],
        # "ew":["aa"],
        # "ex":["aa"],
        # "ey":["aa"],
        # "ez":["aa"],
        # "fa":["aa"],
        # "fb":["aa"],
        # "fc":["aa"],
        # "fd":["aa"],
        # "fe":["aa"],
        # "ff":["aa"],
        # "fg":["aa"],
        # "fh":["aa"],
        # "fi":["aa"],
        # "fj":["aa"],
        # "fk":["aa"],
        # "fl":["aa"],
        # "fm":["aa"],
        # "fn":["aa"],
        # "fo":["aa"],
        # "fp":["aa"],
        # "fq":["aa"],
        # "fr":["aa"],
        # "fs":["aa"],
        # "ft":["aa"],
        # "fu":["aa"],
        # "fv":["aa"],
        # "fw":["aa"],
        # "fx":["aa"],
        # "fy":["aa"],
        # "fz":["aa"],
        # "ga":["aa"],
        # "gb":["aa"],
        # "gc":["aa"],
        # "gd":["aa"],
        # "ge":["aa"],
        # "gf":["aa"],
        # "gg":["aa"],
        # "gh":["aa"],
        # "gi":["aa"],
        # "gj":["aa"],
        # "gk":["aa"],
        # "gl":["aa"],
        # "gm":["aa"],
        # "gn":["aa"],
        # "go":["aa"],
        # "gp":["aa"],
        # "gq":["aa"],
        # "gr":["aa"],
        # "gs":["aa"],
        # "gt":["aa"],
        # "gu":["aa"],
        # "gv":["aa"],
        # "gw":["aa"],
        # "gx":["aa"],
        # "gy":["aa"],
        # "gz":["aa"],
        # "ha":["aa"],
        # "hb":["aa"],
        # "hc":["aa"],
        # "hd":["aa"],
        # "he":["aa"],
        # "hf":["aa"],
        # "hg":["aa"],
        # "hh":["aa"],
        # "hi":["aa"],
        # "hj":["aa"],
        # "hk":["aa"],
        # "hl":["aa"],
        # "hm":["aa"],
        # "hn":["aa"],
        # "ho":["aa"],
        # "hp":["aa"],
        # "hq":["aa"],
        # "hr":["aa"],
        # "hs":["aa"],
        # "ht":["aa"],
        # "hu":["aa"],
        # "hv":["aa"],
        # "hw":["aa"],
        # "hx":["aa"],
        # "hy":["aa"],
        # "hz":["aa"],
        # "ia":["aa"],
        # "ib":["aa"],
        # "ic":["aa"],
        # "id":["aa"],
        # "ie":["aa"],
        # "if":["aa"],
        # "ig":["aa"],
        # "ih":["aa"],
        # "ii":["aa"],
        # "ij":["aa"],
        # "ik":["aa"],
        # "il":["aa"],
        # "im":["aa"],
        # "in":["aa"],
        # "io":["aa"],
        # "ip":["aa"],
        # "iq":["aa"],
        # "ir":["aa"],
        # "is":["aa"],
        # "it":["aa"],
        # "iu":["aa"],
        # "iv":["aa"],
        # "iw":["aa"],
        # "ix":["aa"],
        # "iy":["aa"],
        # "iz":["aa"],
        # "ja":["aa"],
        # "jb":["aa"],
        # "jc":["aa"],
        # "jd":["aa"],
        # "je":["aa"],
        # "jf":["aa"],
        # "jg":["aa"],
        # "jh":["aa"],
        # "ji":["aa"],
        # "jj":["aa"],
        # "jk":["aa"],
        # "jl":["aa"],
        # "jm":["aa"],
        # "jn":["aa"],
        # "jo":["aa"],
        # "jp":["aa"],
        # "jq":["aa"],
        # "jr":["aa"],
        # "js":["aa"],
        # "jt":["aa"],
        # "ju":["aa"],
        # "jv":["aa"],
        # "jw":["aa"],
        # "jx":["aa"],
        # "jy":["aa"],
        # "jz":["aa"],
        # "ka":["aa"],
        # "kb":["aa"],
        # "kc":["aa"],
        # "kd":["aa"],
        # "ke":["aa"],
        # "kf":["aa"],
        # "kg":["aa"],
        # "kh":["aa"],
        # "ki":["aa"],
        # "kj":["aa"],
        # "kk":["aa"],
        # "kl":["aa"],
        # "km":["aa"],
        # "kn":["aa"],
        # "ko":["aa"],
        # "kp":["aa"],
        # "kq":["aa"],
        # "kr":["aa"],
        # "ks":["aa"],
        # "kt":["aa"],
        # "ku":["aa"],
        # "kv":["aa"],
        # "kw":["aa"],
        # "kx":["aa"],
        # "ky":["aa"],
        # "kz":["aa"],
        # "la":["aa"],
        # "lb":["aa"],
        # "lc":["aa"],
        # "ld":["aa"],
        # "le":["aa"],
        # "lf":["aa"],
        # "lg":["aa"],
        # "lh":["aa"],
        # "li":["aa"],
        # "lj":["aa"],
        # "lk":["aa"],
        # "ll":["aa"],
        # "lm":["aa"],
        # "ln":["aa"],
        # "lo":["aa"],
        # "lp":["aa"],
        # "lq":["aa"],
        # "lr":["aa"],
        # "ls":["aa"],
        # "lt":["aa"],
        # "lu":["aa"],
        # "lv":["aa"],
        # "lw":["aa"],
        # "lx":["aa"],
        # "ly":["aa"],
        # "lz":["aa"],
        # "ma":["aa"],
        # "mb":["aa"],
        # "mc":["aa"],
        # "md":["aa"],
        # "me":["aa"],
        # "mf":["aa"],
        # "mg":["aa"],
        # "mh":["aa"],
        # "mi":["aa"],
        # "mj":["aa"],
        # "mk":["aa"],
        # "ml":["aa"],
        # "mm":["aa"],
        # "mn":["aa"],
        # "mo":["aa"],
        # "mp":["aa"],
        # "mq":["aa"],
        # "mr":["aa"],
        # "ms":["aa"],
        # "mt":["aa"],
        # "mu":["aa"],
        # "mv":["aa"],
        # "mw":["aa"],
        # "mx":["aa"],
        # "my":["aa"],
        # "mz":["aa"],
        # "na":["aa"],
        # "nb":["aa"],
        # "nc":["aa"],
        # "nd":["aa"],
        # "ne":["aa"],
        # "nf":["aa"],
        # "ng":["aa"],
        # "nh":["aa"],
        # "ni":["aa"],
        # "nj":["aa"],
        # "nk":["aa"],
        # "nl":["aa"],
        # "nm":["aa"],
        # "nn":["aa"],
        # "no":["aa"],
        # "np":["aa"],
        # "nq":["aa"],
        # "nr":["aa"],
        # "ns":["aa"],
        # "nt":["aa"],
        # "nu":["aa"],
        # "nv":["aa"],
        # "nw":["aa"],
        # "nx":["aa"],
        # "ny":["aa"],
        # "nz":["aa"],
        # "oa":["aa"],
        # "ob":["aa"],
        # "oc":["aa"],
        # "od":["aa"],
        # "oe":["aa"],
        # "of":["aa"],
        # "og":["aa"],
        # "oh":["aa"],
        # "oi":["aa"],
        # "oj":["aa"],
        # "ok":["aa"],
        # "ol":["aa"],
        # "om":["aa"],
        # "on":["aa"],
        # "oo":["aa"],
        # "op":["aa"],
        # "oq":["aa"],
        # "or":["aa"],
        # "os":["aa"],
        # "ot":["aa"],
        # "ou":["aa"],
        # "ov":["aa"],
        # "ow":["aa"],
        # "ox":["aa"],
        # "oy":["aa"],
        # "oz":["aa"],
        # "pa":["aa"],
        # "pb":["aa"],
        # "pc":["aa"],
        # "pd":["aa"],
        # "pe":["aa"],
        # "pf":["aa"],
        # "pg":["aa"],
        # "ph":["aa"],
        # "pi":["aa"],
        # "pj":["aa"],
        # "pk":["aa"],
        # "pl":["aa"],
        # "pm":["aa"],
        # "pn":["aa"],
        # "po":["aa"],
        # "pp":["aa"],
        # "pq":["aa"],
        # "pr":["aa"],
        # "ps":["aa"],
        # "pt":["aa"],
        # "pu":["aa"],
        # "pv":["aa"],
        # "pw":["aa"],
        # "px":["aa"],
        # "py":["aa"],
        # "pz":["aa"],
        # "qa":["aa"],
        # "qb":["aa"],
        # "qc":["aa"],
        # "qd":["aa"],
        # "qe":["aa"],
        # "qf":["aa"],
        # "qg":["aa"],
        # "qh":["aa"],
        # "qi":["aa"],
        # "qj":["aa"],
        # "qk":["aa"],
        # "ql":["aa"],
        # "qm":["aa"],
        # "qn":["aa"],
        # "qo":["aa"],
        # "qp":["aa"],
        # "qq":["aa"],
        # "qr":["aa"],
        # "qs":["aa"],
        # "qt":["aa"],
        # "qu":["aa"],
        # "qv":["aa"],
        # "qw":["aa"],
        # "qx":["aa"],
        # "qy":["aa"],
        # "qz":["aa"],
        # "ra":["aa"],
        # "rb":["aa"],
        # "rc":["aa"],
        # "rd":["aa"],
        # "re":["aa"],
        # "rf":["aa"],
        # "rg":["aa"],
        # "rh":["aa"],
        # "ri":["aa"],
        # "rj":["aa"],
        # "rk":["aa"],
        # "rl":["aa"],
        # "rm":["aa"],
        # "rn":["aa"],
        # "ro":["aa"],
        # "rp":["aa"],
        # "rq":["aa"],
        # "rr":["aa"],
        # "rs":["aa"],
        # "rt":["aa"],
        # "ru":["aa"],
        # "rv":["aa"],
        # "rw":["aa"],
        # "rx":["aa"],
        # "ry":["aa"],
        # "rz":["aa"],
        # "sa":["aa"],
        # "sb":["aa"],
        # "sc":["aa"],
        # "sd":["aa"],
        # "se":["aa"],
        # "sf":["aa"],
        # "sg":["aa"],
        # "sh":["aa"],
        # "si":["aa"],
        # "sj":["aa"],
        # "sk":["aa"],
        # "sl":["aa"],
        # "sm":["aa"],
        # "sn":["aa"],
        # "so":["aa"],
        # "sp":["aa"],
        # "sq":["aa"],
        # "sr":["aa"],
        # "ss":["aa"],
        # "st":["aa"],
        # "su":["aa"],
        # "sv":["aa"],
        # "sw":["aa"],
        # "sx":["aa"],
        # "sy":["aa"],
        # "sz":["aa"],
        # "ta":["aa"],
        # "tb":["aa"],
        # "tc":["aa"],
        # "td":["aa"],
        # "te":["aa"],
        # "tf":["aa"],
        # "tg":["aa"],
        # "th":["aa"],
        # "ti":["aa"],
        # "tj":["aa"],
        # "tk":["aa"],
        # "tl":["aa"],
        # "tm":["aa"],
        # "tn":["aa"],
        # "to":["aa"],
        # "tp":["aa"],
        # "tq":["aa"],
        # "tr":["aa"],
        # "ts":["aa"],
        # "tt":["aa"],
        # "tu":["aa"],
        # "tv":["aa"],
        # "tw":["aa"],
        # "tx":["aa"],
        # "ty":["aa"],
        # "tz":["aa"],
        # "ua":["aa"],
        # "ub":["aa"],
        # "uc":["aa"],
        # "ud":["aa"],
        # "ue":["aa"],
        # "uf":["aa"],
        # "ug":["aa"],
        # "uh":["aa"],
        # "ui":["aa"],
        # "uj":["aa"],
        # "uk":["aa"],
        # "ul":["aa"],
        # "um":["aa"],
        # "un":["aa"],
        # "uo":["aa"],
        # "up":["aa"],
        # "uq":["aa"],
        # "ur":["aa"],
        # "us":["aa"],
        # "ut":["aa"],
        # "uu":["aa"],
        # "uv":["aa"],
        # "uw":["aa"],
        # "ux":["aa"],
        # "uy":["aa"],
        # "uz":["aa"],
        # "va":["aa"],
        # "vb":["aa"],
        # "vc":["aa"],
        # "vd":["aa"],
        # "ve":["aa"],
        # "vf":["aa"],
        # "vg":["aa"],
        # "vh":["aa"],
        # "vi":["aa"],
        # "vj":["aa"],
        # "vk":["aa"],
        # "vl":["aa"],
        # "vm":["aa"],
        # "vn":["aa"],
        # "vo":["aa"],
        # "vp":["aa"],
        # "vq":["aa"],
        # "vr":["aa"],
        # "vs":["aa"],
        # "vt":["aa"],
        # "vu":["aa"],
        # "vv":["aa"],
        # "vw":["aa"],
        # "vx":["aa"],
        # "vy":["aa"],
        # "vz":["aa"],
        # "wa":["aa"],
        # "wb":["aa"],
        # "wc":["aa"],
        # "wd":["aa"],
        # "we":["aa"],
        # "wf":["aa"],
        # "wg":["aa"],
        # "wh":["aa"],
        # "wi":["aa"],
        # "wj":["aa"],
        # "wk":["aa"],
        # "wl":["aa"],
        # "wm":["aa"],
        # "wn":["aa"],
        # "wo":["aa"],
        # "wp":["aa"],
        # "wq":["aa"],
        # "wr":["aa"],
        # "ws":["aa"],
        # "wt":["aa"],
        # "wu":["aa"],
        # "wv":["aa"],
        # "ww":["aa"],
        # "wx":["aa"],
        # "wy":["aa"],
        # "wz":["aa"],
        # "xa":["aa"],
        # "xb":["aa"],
        # "xc":["aa"],
        # "xd":["aa"],
        # "xe":["aa"],
        # "xf":["aa"],
        # "xg":["aa"],
        # "xh":["aa"],
        # "xi":["aa"],
        # "xj":["aa"],
        # "xk":["aa"],
        # "xl":["aa"],
        # "xm":["aa"],
        # "xn":["aa"],
        # "xo":["aa"],
        # "xp":["aa"],
        # "xq":["aa"],
        # "xr":["aa"],
        # "xs":["aa"],
        # "xt":["aa"],
        # "xu":["aa"],
        # "xv":["aa"],
        # "xw":["aa"],
        # "xx":["aa"],
        # "xy":["aa"],
        # "xz":["aa"],
        # "ya":["aa"],
        # "yb":["aa"],
        # "yc":["aa"],
        # "yd":["aa"],
        # "ye":["aa"],
        # "yf":["aa"],
        # "yg":["aa"],
        # "yh":["aa"],
        # "yi":["aa"],
        # "yj":["aa"],
        # "yk":["aa"],
        # "yl":["aa"],
        # "ym":["aa"],
        # "yn":["aa"],
        # "yo":["aa"],
        # "yp":["aa"],
        # "yq":["aa"],
        # "yr":["aa"],
        # "ys":["aa"],
        # "yt":["aa"],
        # "yu":["aa"],
        # "yv":["aa"],
        # "yw":["aa"],
        # "yx":["aa"],
        # "yy":["aa"],
        # "yz":["aa"],
        # "za":["aa"],
        # "zb":["aa"],
        # "zc":["aa"],
        # "zd":["aa"],
        # "ze":["aa"],
        # "zf":["aa"],
        # "zg":["aa"],
        # "zh":["aa"],
        # "zi":["aa"],
        # "zj":["aa"],
        # "zk":["aa"],
        # "zl":["aa"],
        # "zm":["aa"],
        # "zn":["aa"],
        # "zo":["aa"],
        # "zp":["aa"],
        # "zq":["aa"],
        # "zr":["aa"],
        # "zs":["aa"],
        # "zt":["aa"],
        # "zu":["aa"],
        # "zv":["aa"],
        # "zw":["aa"],
        # "zx":["aa"],
        # "zy":["aa"],
        # "zz":["aa"],
        }
    )