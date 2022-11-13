import svgwrite, svgwrite.utils, svgwrite.base
import cairosvg
import math
import random

# TODO Arrowheads
# TODO Auto-scale export + allow to choose size
# TODO Display Unicode

randomColors =  'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'grey', 'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'


def circularGraph(
    fileType: str='svg',
    graphInputs: dict={"Why": ["not"], "not": ["try"], "try": []},
    label: bool=True,
    labelCapitalize: bool=True,
    outputSize: int=1000,
    mainColor: str='random',
    bgColor: str='transparent',
    pointColor: str='transparent',
    labelColor: str='transparent',
    globalOpacity: float=0.5):

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
    \n - `labelCapitalize` : Make point names uppercase
    \n - `outputSize` : Output file width=height (pixels)
    \n - `mainColor` : Color of the arrows and point borders [can be 'random']
    \n - `bgColor` : Color behind the graph [can be 'transparent']
    \n - `pointColor` : Color of the points [can be 'transparent']
    \n - `labelColor` : Color of the point names [can be 'transparent']
    \n - `globalOpacity` : Opacity of the whole output
    \n Graph proportion is automatic.
    \n A maximum a 3 characters (Latin or Cyrillic) for each point will be properly displayed.
    \n The maximum export size is 32767x32767.
    """
    # Constants
    numberofpoints = len(graphInputs)
    insideAngle = 2*math.pi/numberofpoints
    centerxy = outputSize/2 # CircularGraphRadius+CircularGraphPointRadius+15/numberofpoints+0.5 # 
    CircularGraphPointRadius = math.pi*centerxy/numberofpoints/3 # 140/numberofpoints+20 # x = 
    CircularGraphRadius = centerxy - CircularGraphPointRadius-CircularGraphPointRadius/10 # numberofpoints*10+200 # 

    # Colors
    transparent = svgwrite.solidcolor.SolidColor(color='white', opacity=None, profile='tiny')
    if pointColor=='transparent':
        pointColor = transparent

    dwg = svgwrite.Drawing('./Maths2SVG/gengraph.svg')

    if mainColor=='random':
        for point in enumerate(graphInputs.keys()):
            graphInputs[point[1]].insert(0, ((math.cos(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius), (math.sin(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius)))
            graphInputs[point[1]].insert(1, (randomColors[random.randint(0, 146)]))
        slicefrom2 = 1
    else:
        for point in enumerate(graphInputs.keys()):
            graphInputs[point[1]].insert(0, ((math.cos(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius), (math.sin(point[0]*(insideAngle)-math.pi/2)*CircularGraphRadius)))
        slicefrom2 = 0

    if bgColor != 'transparent':
        dwg.add(dwg.rect((-centerxy, -centerxy), (centerxy*2, centerxy*2), fill=bgColor, opacity=globalOpacity))


    for point in enumerate(graphInputs.keys()):
        if mainColor == 'random':
            arrowColor = graphInputs[point[1]][1]
        else:
            arrowColor = mainColor
        for arrow in graphInputs[point[1]][1+slicefrom2:]:
            if arrow!=point[1]:
                angle = math.atan2((graphInputs[arrow][0][1]-graphInputs[point[1]][0][1]),(graphInputs[arrow][0][0]-graphInputs[point[1]][0][0]))
                drawn_arrow = dwg.line(
                    start=(graphInputs[point[1]][0][0]+CircularGraphPointRadius*math.cos(angle), graphInputs[point[1]][0][1]+CircularGraphPointRadius*math.sin(angle)), 
                    end=(graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)))
                drawn_arrow.stroke(arrowColor, opacity=globalOpacity, width=CircularGraphPointRadius/10)
                dwg.add(drawn_arrow)

                drawn_arrow_marker = dwg.polygon(points=[
                        (graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)), 
                        (graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle)*1.5-CircularGraphPointRadius*0.25*math.sin(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)*1.5+CircularGraphPointRadius*0.25*math.cos(angle)), 
                        (graphInputs[arrow][0][0]-CircularGraphPointRadius*math.cos(angle)*1.5+CircularGraphPointRadius*0.25*math.sin(angle), graphInputs[arrow][0][1]-CircularGraphPointRadius*math.sin(angle)*1.5-CircularGraphPointRadius*0.25*math.cos(angle))
                ])
                drawn_arrow_marker.fill(arrowColor, opacity=globalOpacity)
                dwg.add(drawn_arrow_marker)
            else:
                angle = math.atan2((graphInputs[arrow][0][1]),(graphInputs[arrow][0][0]))
                print(angle, point[1], arrow)
                dwg.C

    for point in enumerate(graphInputs.keys()):
        if mainColor == 'random':
            strokeColor = graphInputs[point[1]][1]
        else:
            strokeColor = mainColor
        small_circle = dwg.circle(center=graphInputs[point[1]][0], r=CircularGraphPointRadius)
        small_circle.fill(pointColor, opacity=globalOpacity).stroke(strokeColor, opacity=globalOpacity, width=CircularGraphPointRadius/5)
        dwg.add(small_circle)

    if label and labelColor != 'transparent':
        for point in enumerate(graphInputs.keys()):
            pointLabel = point[1]
            if labelCapitalize:
                pointLabel = point[1].upper()
            point_name = dwg.text(pointLabel, x=[graphInputs[point[1]][0][0]], y=[graphInputs[point[1]][0][1]+2], alignment_baseline="middle", text_anchor="middle", style='fill: ' + labelColor + ';  font-size: ' + str(7*CircularGraphPointRadius/10) + 'px; font-family: Arial, system-ui; opacity: '+str(globalOpacity)+';')
            dwg.add(point_name)
    
    dwg.save()
    print("Bridge SVG generated !")

    # Resize and scale svg

    if 'svg' in fileType:
        print("Converting to SVG…")
        cairosvg.svg2svg(url="./Maths2SVG/gengraph.svg", write_to="./doc/graph.svg", output_width=outputSize, output_height=outputSize)
    if 'png' in fileType:
        print("Converting to PNG…")
        cairosvg.svg2png(url="./Maths2SVG/gengraph.svg", write_to="./doc/graph.png", output_width=outputSize, output_height=outputSize)
    if 'ps' in fileType:
        print("Converting to PS…")
        cairosvg.svg2ps(url="./Maths2SVG/gengraph.svg", write_to="./doc/graph.ps", output_width=outputSize, output_height=outputSize)
    if 'pdf' in fileType: 
        print("Converting to PDF…")
        cairosvg.svg2pdf(url="./Maths2SVG/gengraph.svg", write_to="./doc/graph.pdf", output_width=outputSize, output_height=outputSize)
    
    print("Circular graph : operation terminated.")
    return True



if __name__== "__main__":
    circularGraph(
        fileType='png', # Or a list
        graphInputs={
        "aa":["aa"],
        "ab":["aa"],
        "ac":["aa"],
        "ad":["aa"],
        "ae":["aa"],
        "af":["aa"],
        "ag":["aa"],
        "ah":["aa"],
        "ai":["aa"],
        "aj":["aa"],
        "ak":["aa"],
        "al":["aa"],
        "am":["aa"],
        "an":["aa"],
        "ao":["aa"],
        "ap":["aa"],
        "aq":["aa"],
        "ar":["aa"],
        "as":["aa"],
        "at":["aa"],
        "au":["aa"],
        "av":["aa"],
        "aw":["aa"],
        "ax":["aa"],
        "ay":["aa"],
        "az":["aa"],
        "ba":["aa"],
        "bb":["aa"],
        "bc":["aa"],
        "bd":["aa"],
        "be":["aa"],
        "bf":["aa"],
        "bg":["aa"],
        "bh":["aa"],
        "bi":["aa"],
        "bj":["aa"],
        "bk":["aa"],
        "bl":["aa"],
        "bm":["aa"],
        "bn":["aa"],
        "bo":["aa"],
        "bp":["aa"],
        "bq":["aa"],
        "br":["aa"],
        "bs":["aa"],
        "bt":["aa"],
        "bu":["aa"],
        "bv":["aa"],
        "bw":["aa"],
        "bx":["aa"],
        "by":["aa"],
        "bz":["aa"],
        "ca":["aa"],
        "cb":["aa"],
        "cc":["aa"],
        "cd":["aa"],
        "ce":["aa"],
        "cf":["aa"],
        "cg":["aa"],
        "ch":["aa"],
        "ci":["aa"],
        "cj":["aa"],
        "ck":["aa"],
        "cl":["aa"],
        "cm":["aa"],
        "cn":["aa"],
        "co":["aa"],
        "cp":["aa"],
        "cq":["aa"],
        "cr":["aa"],
        "cs":["aa"],
        "ct":["aa"],
        "cu":["aa"],
        "cv":["aa"],
        "cw":["aa"],
        "cx":["aa"],
        "cy":["aa"],
        "cz":["aa"],
        "da":["aa"],
        "db":["aa"],
        "dc":["aa"],
        "dd":["aa"],
        "de":["aa"],
        "df":["aa"],
        "dg":["aa"],
        "dh":["aa"],
        "di":["aa"],
        "dj":["aa"],
        "dk":["aa"],
        "dl":["aa"],
        "dm":["aa"],
        "dn":["aa"],
        "do":["aa"],
        "dp":["aa"],
        "dq":["aa"],
        "dr":["aa"],
        "ds":["aa"],
        "dt":["aa"],
        "du":["aa"],
        "dv":["aa"],
        "dw":["aa"],
        "dx":["aa"],
        "dy":["aa"],
        "dz":["aa"],
        "ea":["aa"],
        "eb":["aa"],
        "ec":["aa"],
        "ed":["aa"],
        "ee":["aa"],
        "ef":["aa"],
        "eg":["aa"],
        "eh":["aa"],
        "ei":["aa"],
        "ej":["aa"],
        "ek":["aa"],
        "el":["aa"],
        "em":["aa"],
        "en":["aa"],
        "eo":["aa"],
        "ep":["aa"],
        "eq":["aa"],
        "er":["aa"],
        "es":["aa"],
        "et":["aa"],
        "eu":["aa"],
        "ev":["aa"],
        "ew":["aa"],
        "ex":["aa"],
        "ey":["aa"],
        "ez":["aa"],
        "fa":["aa"],
        "fb":["aa"],
        "fc":["aa"],
        "fd":["aa"],
        "fe":["aa"],
        "ff":["aa"],
        "fg":["aa"],
        "fh":["aa"],
        "fi":["aa"],
        "fj":["aa"],
        "fk":["aa"],
        "fl":["aa"],
        "fm":["aa"],
        "fn":["aa"],
        "fo":["aa"],
        "fp":["aa"],
        "fq":["aa"],
        "fr":["aa"],
        "fs":["aa"],
        "ft":["aa"],
        "fu":["aa"],
        "fv":["aa"],
        "fw":["aa"],
        "fx":["aa"],
        "fy":["aa"],
        "fz":["aa"],
        "ga":["aa"],
        "gb":["aa"],
        "gc":["aa"],
        "gd":["aa"],
        "ge":["aa"],
        "gf":["aa"],
        "gg":["aa"],
        "gh":["aa"],
        "gi":["aa"],
        "gj":["aa"],
        "gk":["aa"],
        "gl":["aa"],
        "gm":["aa"],
        "gn":["aa"],
        "go":["aa"],
        "gp":["aa"],
        "gq":["aa"],
        "gr":["aa"],
        "gs":["aa"],
        "gt":["aa"],
        "gu":["aa"],
        "gv":["aa"],
        "gw":["aa"],
        "gx":["aa"],
        "gy":["aa"],
        "gz":["aa"],
        "ha":["aa"],
        "hb":["aa"],
        "hc":["aa"],
        "hd":["aa"],
        "he":["aa"],
        "hf":["aa"],
        "hg":["aa"],
        "hh":["aa"],
        "hi":["aa"],
        "hj":["aa"],
        "hk":["aa"],
        "hl":["aa"],
        "hm":["aa"],
        "hn":["aa"],
        "ho":["aa"],
        "hp":["aa"],
        "hq":["aa"],
        "hr":["aa"],
        "hs":["aa"],
        "ht":["aa"],
        "hu":["aa"],
        "hv":["aa"],
        "hw":["aa"],
        "hx":["aa"],
        "hy":["aa"],
        "hz":["aa"],
        "ia":["aa"],
        "ib":["aa"],
        "ic":["aa"],
        "id":["aa"],
        "ie":["aa"],
        "if":["aa"],
        "ig":["aa"],
        "ih":["aa"],
        "ii":["aa"],
        "ij":["aa"],
        "ik":["aa"],
        "il":["aa"],
        "im":["aa"],
        "in":["aa"],
        "io":["aa"],
        "ip":["aa"],
        "iq":["aa"],
        "ir":["aa"],
        "is":["aa"],
        "it":["aa"],
        "iu":["aa"],
        "iv":["aa"],
        "iw":["aa"],
        "ix":["aa"],
        "iy":["aa"],
        "iz":["aa"],
        "ja":["aa"],
        "jb":["aa"],
        "jc":["aa"],
        "jd":["aa"],
        "je":["aa"],
        "jf":["aa"],
        "jg":["aa"],
        "jh":["aa"],
        "ji":["aa"],
        "jj":["aa"],
        "jk":["aa"],
        "jl":["aa"],
        "jm":["aa"],
        "jn":["aa"],
        "jo":["aa"],
        "jp":["aa"],
        "jq":["aa"],
        "jr":["aa"],
        "js":["aa"],
        "jt":["aa"],
        "ju":["aa"],
        "jv":["aa"],
        "jw":["aa"],
        "jx":["aa"],
        "jy":["aa"],
        "jz":["aa"],
        "ka":["aa"],
        "kb":["aa"],
        "kc":["aa"],
        "kd":["aa"],
        "ke":["aa"],
        "kf":["aa"],
        "kg":["aa"],
        "kh":["aa"],
        "ki":["aa"],
        "kj":["aa"],
        "kk":["aa"],
        "kl":["aa"],
        "km":["aa"],
        "kn":["aa"],
        "ko":["aa"],
        "kp":["aa"],
        "kq":["aa"],
        "kr":["aa"],
        "ks":["aa"],
        "kt":["aa"],
        "ku":["aa"],
        "kv":["aa"],
        "kw":["aa"],
        "kx":["aa"],
        "ky":["aa"],
        "kz":["aa"],
        "la":["aa"],
        "lb":["aa"],
        "lc":["aa"],
        "ld":["aa"],
        "le":["aa"],
        "lf":["aa"],
        "lg":["aa"],
        "lh":["aa"],
        "li":["aa"],
        "lj":["aa"],
        "lk":["aa"],
        "ll":["aa"],
        "lm":["aa"],
        "ln":["aa"],
        "lo":["aa"],
        "lp":["aa"],
        "lq":["aa"],
        "lr":["aa"],
        "ls":["aa"],
        "lt":["aa"],
        "lu":["aa"],
        "lv":["aa"],
        "lw":["aa"],
        "lx":["aa"],
        "ly":["aa"],
        "lz":["aa"],
        "ma":["aa"],
        "mb":["aa"],
        "mc":["aa"],
        "md":["aa"],
        "me":["aa"],
        "mf":["aa"],
        "mg":["aa"],
        "mh":["aa"],
        "mi":["aa"],
        "mj":["aa"],
        "mk":["aa"],
        "ml":["aa"],
        "mm":["aa"],
        "mn":["aa"],
        "mo":["aa"],
        "mp":["aa"],
        "mq":["aa"],
        "mr":["aa"],
        "ms":["aa"],
        "mt":["aa"],
        "mu":["aa"],
        "mv":["aa"],
        "mw":["aa"],
        "mx":["aa"],
        "my":["aa"],
        "mz":["aa"],
        "na":["aa"],
        "nb":["aa"],
        "nc":["aa"],
        "nd":["aa"],
        "ne":["aa"],
        "nf":["aa"],
        "ng":["aa"],
        "nh":["aa"],
        "ni":["aa"],
        "nj":["aa"],
        "nk":["aa"],
        "nl":["aa"],
        "nm":["aa"],
        "nn":["aa"],
        "no":["aa"],
        "np":["aa"],
        "nq":["aa"],
        "nr":["aa"],
        "ns":["aa"],
        "nt":["aa"],
        "nu":["aa"],
        "nv":["aa"],
        "nw":["aa"],
        "nx":["aa"],
        "ny":["aa"],
        "nz":["aa"],
        "oa":["aa"],
        "ob":["aa"],
        "oc":["aa"],
        "od":["aa"],
        "oe":["aa"],
        "of":["aa"],
        "og":["aa"],
        "oh":["aa"],
        "oi":["aa"],
        "oj":["aa"],
        "ok":["aa"],
        "ol":["aa"],
        "om":["aa"],
        "on":["aa"],
        "oo":["aa"],
        "op":["aa"],
        "oq":["aa"],
        "or":["aa"],
        "os":["aa"],
        "ot":["aa"],
        "ou":["aa"],
        "ov":["aa"],
        "ow":["aa"],
        "ox":["aa"],
        "oy":["aa"],
        "oz":["aa"],
        "pa":["aa"],
        "pb":["aa"],
        "pc":["aa"],
        "pd":["aa"],
        "pe":["aa"],
        "pf":["aa"],
        "pg":["aa"],
        "ph":["aa"],
        "pi":["aa"],
        "pj":["aa"],
        "pk":["aa"],
        "pl":["aa"],
        "pm":["aa"],
        "pn":["aa"],
        "po":["aa"],
        "pp":["aa"],
        "pq":["aa"],
        "pr":["aa"],
        "ps":["aa"],
        "pt":["aa"],
        "pu":["aa"],
        "pv":["aa"],
        "pw":["aa"],
        "px":["aa"],
        "py":["aa"],
        "pz":["aa"],
        "qa":["aa"],
        "qb":["aa"],
        "qc":["aa"],
        "qd":["aa"],
        "qe":["aa"],
        "qf":["aa"],
        "qg":["aa"],
        "qh":["aa"],
        "qi":["aa"],
        "qj":["aa"],
        "qk":["aa"],
        "ql":["aa"],
        "qm":["aa"],
        "qn":["aa"],
        "qo":["aa"],
        "qp":["aa"],
        "qq":["aa"],
        "qr":["aa"],
        "qs":["aa"],
        "qt":["aa"],
        "qu":["aa"],
        "qv":["aa"],
        "qw":["aa"],
        "qx":["aa"],
        "qy":["aa"],
        "qz":["aa"],
        "ra":["aa"],
        "rb":["aa"],
        "rc":["aa"],
        "rd":["aa"],
        "re":["aa"],
        "rf":["aa"],
        "rg":["aa"],
        "rh":["aa"],
        "ri":["aa"],
        "rj":["aa"],
        "rk":["aa"],
        "rl":["aa"],
        "rm":["aa"],
        "rn":["aa"],
        "ro":["aa"],
        "rp":["aa"],
        "rq":["aa"],
        "rr":["aa"],
        "rs":["aa"],
        "rt":["aa"],
        "ru":["aa"],
        "rv":["aa"],
        "rw":["aa"],
        "rx":["aa"],
        "ry":["aa"],
        "rz":["aa"],
        "sa":["aa"],
        "sb":["aa"],
        "sc":["aa"],
        "sd":["aa"],
        "se":["aa"],
        "sf":["aa"],
        "sg":["aa"],
        "sh":["aa"],
        "si":["aa"],
        "sj":["aa"],
        "sk":["aa"],
        "sl":["aa"],
        "sm":["aa"],
        "sn":["aa"],
        "so":["aa"],
        "sp":["aa"],
        "sq":["aa"],
        "sr":["aa"],
        "ss":["aa"],
        "st":["aa"],
        "su":["aa"],
        "sv":["aa"],
        "sw":["aa"],
        "sx":["aa"],
        "sy":["aa"],
        "sz":["aa"],
        "ta":["aa"],
        "tb":["aa"],
        "tc":["aa"],
        "td":["aa"],
        "te":["aa"],
        "tf":["aa"],
        "tg":["aa"],
        "th":["aa"],
        "ti":["aa"],
        "tj":["aa"],
        "tk":["aa"],
        "tl":["aa"],
        "tm":["aa"],
        "tn":["aa"],
        "to":["aa"],
        "tp":["aa"],
        "tq":["aa"],
        "tr":["aa"],
        "ts":["aa"],
        "tt":["aa"],
        "tu":["aa"],
        "tv":["aa"],
        "tw":["aa"],
        "tx":["aa"],
        "ty":["aa"],
        "tz":["aa"],
        "ua":["aa"],
        "ub":["aa"],
        "uc":["aa"],
        "ud":["aa"],
        "ue":["aa"],
        "uf":["aa"],
        "ug":["aa"],
        "uh":["aa"],
        "ui":["aa"],
        "uj":["aa"],
        "uk":["aa"],
        "ul":["aa"],
        "um":["aa"],
        "un":["aa"],
        "uo":["aa"],
        "up":["aa"],
        "uq":["aa"],
        "ur":["aa"],
        "us":["aa"],
        "ut":["aa"],
        "uu":["aa"],
        "uv":["aa"],
        "uw":["aa"],
        "ux":["aa"],
        "uy":["aa"],
        "uz":["aa"],
        "va":["aa"],
        "vb":["aa"],
        "vc":["aa"],
        "vd":["aa"],
        "ve":["aa"],
        "vf":["aa"],
        "vg":["aa"],
        "vh":["aa"],
        "vi":["aa"],
        "vj":["aa"],
        "vk":["aa"],
        "vl":["aa"],
        "vm":["aa"],
        "vn":["aa"],
        "vo":["aa"],
        "vp":["aa"],
        "vq":["aa"],
        "vr":["aa"],
        "vs":["aa"],
        "vt":["aa"],
        "vu":["aa"],
        "vv":["aa"],
        "vw":["aa"],
        "vx":["aa"],
        "vy":["aa"],
        "vz":["aa"],
        "wa":["aa"],
        "wb":["aa"],
        "wc":["aa"],
        "wd":["aa"],
        "we":["aa"],
        "wf":["aa"],
        "wg":["aa"],
        "wh":["aa"],
        "wi":["aa"],
        "wj":["aa"],
        "wk":["aa"],
        "wl":["aa"],
        "wm":["aa"],
        "wn":["aa"],
        "wo":["aa"],
        "wp":["aa"],
        "wq":["aa"],
        "wr":["aa"],
        "ws":["aa"],
        "wt":["aa"],
        "wu":["aa"],
        "wv":["aa"],
        "ww":["aa"],
        "wx":["aa"],
        "wy":["aa"],
        "wz":["aa"],
        "xa":["aa"],
        "xb":["aa"],
        "xc":["aa"],
        "xd":["aa"],
        "xe":["aa"],
        "xf":["aa"],
        "xg":["aa"],
        "xh":["aa"],
        "xi":["aa"],
        "xj":["aa"],
        "xk":["aa"],
        "xl":["aa"],
        "xm":["aa"],
        "xn":["aa"],
        "xo":["aa"],
        "xp":["aa"],
        "xq":["aa"],
        "xr":["aa"],
        "xs":["aa"],
        "xt":["aa"],
        "xu":["aa"],
        "xv":["aa"],
        "xw":["aa"],
        "xx":["aa"],
        "xy":["aa"],
        "xz":["aa"],
        "ya":["aa"],
        "yb":["aa"],
        "yc":["aa"],
        "yd":["aa"],
        "ye":["aa"],
        "yf":["aa"],
        "yg":["aa"],
        "yh":["aa"],
        "yi":["aa"],
        "yj":["aa"],
        "yk":["aa"],
        "yl":["aa"],
        "ym":["aa"],
        "yn":["aa"],
        "yo":["aa"],
        "yp":["aa"],
        "yq":["aa"],
        "yr":["aa"],
        "ys":["aa"],
        "yt":["aa"],
        "yu":["aa"],
        "yv":["aa"],
        "yw":["aa"],
        "yx":["aa"],
        "yy":["aa"],
        "yz":["aa"],
        "za":["aa"],
        "zb":["aa"],
        "zc":["aa"],
        "zd":["aa"],
        "ze":["aa"],
        "zf":["aa"],
        "zg":["aa"],
        "zh":["aa"],
        "zi":["aa"],
        "zj":["aa"],
        "zk":["aa"],
        "zl":["aa"],
        "zm":["aa"],
        "zn":["aa"],
        "zo":["aa"],
        "zp":["aa"],
        "zq":["aa"],
        "zr":["aa"],
        "zs":["aa"],
        "zt":["aa"],
        "zu":["aa"],
        "zv":["aa"],
        "zw":["aa"],
        "zx":["aa"],
        "zy":["aa"],
        "zz":["aa"],
        }
    )