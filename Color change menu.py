def selectDialog(list, heading=addonInfo('name')):
	dialog = xbmcgui.Dialog()
	return dialog.select(heading, list)


def menu(ret):
	dialog = xbmcgui.Dialog()
	items = [
			( '[B][COLOR aliceblue]aliceblue [/COLOR][/B]' , 'aliceblue' ) ,
			( '[B][COLOR antiquewhite]antiquewhite [/COLOR][/B]' , 'antiquewhite' ) ,
			( '[B][COLOR aqua]aqua [/COLOR][/B]' , 'aqua' ) ,
			( '[B][COLOR aquamarine]aquamarine [/COLOR][/B]' , 'aquamarine' ) ,
			( '[B][COLOR azure]azure [/COLOR][/B]' , 'azure' ) ,
			( '[B][COLOR beige]beige [/COLOR][/B]' , 'beige' ) ,
			( '[B][COLOR bisque]bisque [/COLOR][/B]' , 'bisque' ) ,
			( '[B][COLOR blanchedalmond]blanchedalmond [/COLOR][/B]' , 'blanchedalmond' ) ,
			( '[B][COLOR blue]blue [/COLOR][/B]' , 'blue' ) ,
			( '[B][COLOR blueviolet]blueviolet [/COLOR][/B]' , 'blueviolet' ) ,
			( '[B][COLOR brown]brown [/COLOR][/B]' , 'brown' ) ,
			( '[B][COLOR burlywood]burlywood [/COLOR][/B]' , 'burlywood' ) ,
			( '[B][COLOR cadetblue]cadetblue [/COLOR][/B]' , 'cadetblue' ) ,
			( '[B][COLOR chartreuse]chartreuse [/COLOR][/B]' , 'chartreuse' ) ,
			( '[B][COLOR chocolate]chocolate [/COLOR][/B]' , 'chocolate' ) ,
			( '[B][COLOR coral]coral [/COLOR][/B]' , 'coral' ) ,
			( '[B][COLOR cornflowerblue]cornflowerblue [/COLOR][/B]' , 'cornflowerblue' ) ,
			( '[B][COLOR cornsilk]cornsilk [/COLOR][/B]' , 'cornsilk' ) ,
			( '[B][COLOR crimson]crimson [/COLOR][/B]' , 'crimson' ) ,
			( '[B][COLOR cyan]cyan [/COLOR][/B]' , 'cyan' ) ,
			( '[B][COLOR darkblue]darkblue [/COLOR][/B]' , 'darkblue' ) ,
			( '[B][COLOR darkcyan]darkcyan [/COLOR][/B]' , 'darkcyan' ) ,
			( '[B][COLOR darkgoldenrod]darkgoldenrod [/COLOR][/B]' , 'darkgoldenrod' ) ,
			( '[B][COLOR darkgray]darkgray [/COLOR][/B]' , 'darkgray' ) ,
			( '[B][COLOR darkgreen]darkgreen [/COLOR][/B]' , 'darkgreen' ) ,
			( '[B][COLOR darkgrey]darkgrey [/COLOR][/B]' , 'darkgrey' ) ,
			( '[B][COLOR darkkhaki]darkkhaki [/COLOR][/B]' , 'darkkhaki' ) ,
			( '[B][COLOR darkmagenta]darkmagenta [/COLOR][/B]' , 'darkmagenta' ) ,
			( '[B][COLOR darkolivegreen]darkolivegreen [/COLOR][/B]' , 'darkolivegreen' ) ,
			( '[B][COLOR darkorange]darkorange [/COLOR][/B]' , 'darkorange' ) ,
			( '[B][COLOR darkorchid]darkorchid [/COLOR][/B]' , 'darkorchid' ) ,
			( '[B][COLOR darkred]darkred [/COLOR][/B]' , 'darkred' ) ,
			( '[B][COLOR darksalmon]darksalmon [/COLOR][/B]' , 'darksalmon' ) ,
			( '[B][COLOR darkseagreen]darkseagreen [/COLOR][/B]' , 'darkseagreen' ) ,
			( '[B][COLOR darkslateblue]darkslateblue [/COLOR][/B]' , 'darkslateblue' ) ,
			( '[B][COLOR darkslategray]darkslategray [/COLOR][/B]' , 'darkslategray' ) ,
			( '[B][COLOR darkturquoise]darkturquoise [/COLOR][/B]' , 'darkturquoise' ) ,
			( '[B][COLOR darkviolet]darkviolet [/COLOR][/B]' , 'darkviolet' ) ,
			( '[B][COLOR deeppink]deeppink [/COLOR][/B]' , 'deeppink' ) ,
			( '[B][COLOR deepskyblue]deepskyblue [/COLOR][/B]' , 'deepskyblue' ) ,
			( '[B][COLOR dimgray]dimgray [/COLOR][/B]' , 'dimgray' ) ,
			( '[B][COLOR dimgrey]dimgrey [/COLOR][/B]' , 'dimgrey' ) ,
			( '[B][COLOR dodgerblue]dodgerblue [/COLOR][/B]' , 'dodgerblue' ) ,
			( '[B][COLOR firebrick]firebrick [/COLOR][/B]' , 'firebrick' ) ,
			( '[B][COLOR floralwhite]floralwhite [/COLOR][/B]' , 'floralwhite' ) ,
			( '[B][COLOR forestgreen]forestgreen [/COLOR][/B]' , 'forestgreen' ) ,
			( '[B][COLOR fuchsia]fuchsia [/COLOR][/B]' , 'fuchsia' ) ,
			( '[B][COLOR gainsboro]gainsboro [/COLOR][/B]' , 'gainsboro' ) ,
			( '[B][COLOR ghostwhite]ghostwhite [/COLOR][/B]' , 'ghostwhite' ) ,
			( '[B][COLOR gold]gold [/COLOR][/B]' , '' ) ,
			( '[B][COLOR goldenrod]goldenrod [/COLOR][/B]' , 'goldenrod' ) ,
			( '[B][COLOR gray]gray [/COLOR][/B]' , 'gray' ) ,
			( '[B][COLOR green]green [/COLOR][/B]' , 'green' ) ,
			( '[B][COLOR greenyellow]greenyellow [/COLOR][/B]' , 'greenyellow' ) ,
			( '[B][COLOR grey]grey [/COLOR][/B]' , 'grey' ) ,
			( '[B][COLOR honeydew]honeydew [/COLOR][/B]' , 'honeydew' ) ,
			( '[B][COLOR hotpink]hotpink [/COLOR][/B]' , 'hotpink' ) ,
			( '[B][COLOR indianred]indianred [/COLOR][/B]' , 'indianred' ) ,
			( '[B][COLOR indigo]indigo [/COLOR][/B]' , 'indigo' ) ,
			( '[B][COLOR ivory]ivory [/COLOR][/B]' , 'ivory' ) ,
			( '[B][COLOR khaki]khaki [/COLOR][/B]' , 'khaki' ) ,
			( '[B][COLOR lavender]lavender [/COLOR][/B]' , 'lavender' ) ,
			( '[B][COLOR lavenderblush]lavenderblush [/COLOR][/B]' , '' ) ,
			( '[B][COLOR lawngreen]lawngreen [/COLOR][/B]' , 'lawngreen' ) ,
			( '[B][COLOR lemonchiffon]lemonchiffon [/COLOR][/B]' , 'lemonchiffon' ) ,
			( '[B][COLOR lightblue]lightblue [/COLOR][/B]' , 'lightblue' ) ,
			( '[B][COLOR lightcoral]lightcoral [/COLOR][/B]' , 'lightcoral' ) ,
			( '[B][COLOR lightcyan]lightcyan [/COLOR][/B]' , 'lightcyan' ) ,
			( '[B][COLOR lightgoldenrodyellow]lightgoldenrodyellow [/COLOR][/B]' , 'lightgoldenrodyellow' ) ,
			( '[B][COLOR lightgray]lightgray [/COLOR][/B]' , 'lightgray' ) ,
			( '[B][COLOR lightgreen]lightgreen [/COLOR][/B]' , '' ) ,
			( '[B][COLOR lightgrey]lightgrey [/COLOR][/B]' , '' ) ,
			( '[B][COLOR lightpink]lightpink [/COLOR][/B]' , '' ) ,
			( '[B][COLOR lightsalmon]lightsalmon [/COLOR][/B]' , '' ) ,
			( '[B][COLOR lightseagreen]lightseagreen [/COLOR][/B]' , 'lightseagreen' ) ,
			( '[B][COLOR lightskyblue]lightskyblue [/COLOR][/B]' , 'lightskyblue' ) ,
			( '[B][COLOR lightslategray]lightslategray [/COLOR][/B]' , 'lightslategray' ) ,
			( '[B][COLOR lightslategrey]lightslategrey [/COLOR][/B]' , 'lightslategrey' ) ,
			( '[B][COLOR lightsteelblue]lightsteelblue [/COLOR][/B]' , 'lightsteelblue' ) ,
			( '[B][COLOR lightyellow]lightyellow [/COLOR][/B]' , 'lightyellow' ) ,
			( '[B][COLOR lime]lime [/COLOR][/B]' , 'lime' ) ,
			( '[B][COLOR limegreen]limegreen [/COLOR][/B]' , 'limegreen' ) ,
			( '[B][COLOR linen]linen [/COLOR][/B]' , 'linen' ) ,
			( '[B][COLOR magenta]magenta [/COLOR][/B]' , 'magenta' ) ,
			( '[B][COLOR maroon]maroon [/COLOR][/B]' , 'maroon' ) ,
			( '[B][COLOR mediumaquamarine]mediumaquamarine [/COLOR][/B]' , 'mediumaquamarine' ) ,
			( '[B][COLOR mediumblue]mediumblue [/COLOR][/B]' , 'mediumblue' ) ,
			( '[B][COLOR mediumorchid]mediumorchid [/COLOR][/B]' , 'mediumorchid' ) ,
			( '[B][COLOR mediumpurple]mediumpurple [/COLOR][/B]' , 'mediumpurple' ) ,
			( '[B][COLOR mediumseagreen]mediumseagreen [/COLOR][/B]' , 'mediumseagreen' ) ,
			( '[B][COLOR mediumslateblue]mediumslateblue [/COLOR][/B]' , 'mediumslateblue' ) ,
			( '[B][COLOR mediumspringgreen]mediumspringgreen [/COLOR][/B]' , '' ) ,
			( '[B][COLOR mediumturquoise]mediumturquoise [/COLOR][/B]' , 'mediumspringgreen' ) ,
			( '[B][COLOR mediumvioletred]mediumvioletred [/COLOR][/B]' , 'mediumvioletred' ) ,
			( '[B][COLOR midnightblue]midnightblue [/COLOR][/B]' , '' ) ,
			( '[B][COLOR mintcream]mintcream [/COLOR][/B]' , 'mintcream' ) ,
			( '[B][COLOR mistyrose]mistyrose [/COLOR][/B]' , 'mistyrose' ) ,
			( '[B][COLOR moccasin]moccasin [/COLOR][/B]' , 'moccasin' ) ,
			( '[B][COLOR navajowhite]navajowhite [/COLOR][/B]' , 'navajowhite' ) ,
			( '[B][COLOR navy]navy [/COLOR][/B]' , 'navy' ) ,
			( '[B][COLOR none]none [/COLOR][/B]' , 'none' ) ,
			( '[B][COLOR oldlace]oldlace [/COLOR][/B]' , 'oldlace' ) ,
			( '[B][COLOR olive]olive [/COLOR][/B]' , 'olive' ) ,
			( '[B][COLOR olivedrab]olivedrab [/COLOR][/B]' , 'olivedrab' ) ,
			( '[B][COLOR orange]orange [/COLOR][/B]' , 'orange' ) ,
			( '[B][COLOR orangered]orangered [/COLOR][/B]' , 'orangered' ) ,
			( '[B][COLOR orchid]orchid [/COLOR][/B]' , 'orchid' ) ,
			( '[B][COLOR palegoldenrod]palegoldenrod [/COLOR][/B]' , 'palegoldenrod' ) ,
			( '[B][COLOR palegreen]palegreen [/COLOR][/B]' , 'palegreen' ) ,
			( '[B][COLOR paleturquoise]paleturquoise [/COLOR][/B]' , 'paleturquoise' ) ,
			( '[B][COLOR palevioletred]palevioletred [/COLOR][/B]' , 'palevioletred' ) ,
			( '[B][COLOR papayawhip]papayawhip [/COLOR][/B]' , 'papayawhip' ) ,
			( '[B][COLOR peachpuff]peachpuff [/COLOR][/B]' , 'peachpuff' ) ,
			( '[B][COLOR peru]peru [/COLOR][/B]' , 'peru' ) ,
			( '[B][COLOR pink]pink [/COLOR][/B]' , 'pink' ) ,
			( '[B][COLOR plum]plum [/COLOR][/B]' , 'plum' ) ,
			( '[B][COLOR powderblue]powderblue [/COLOR][/B]' , 'powderblue' ) ,
			( '[B][COLOR purple]purple [/COLOR][/B]' , 'purple' ) ,
			( '[B][COLOR red]red [/COLOR][/B]' , 'red' ) ,
			( '[B][COLOR rosybrown]rosybrown [/COLOR][/B]' , 'rosybrown' ) ,
			( '[B][COLOR royalblue]royalblue [/COLOR][/B]' , 'royalblue' ) ,
			( '[B][COLOR saddlebrown]saddlebrown [/COLOR][/B]' , 'saddlebrown' ) ,
			( '[B][COLOR salmon]salmon [/COLOR][/B]' , 'salmon' ) ,
			( '[B][COLOR sandybrown]sandybrown [/COLOR][/B]' , 'sandybrown' ) ,
			( '[B][COLOR seagreen]seagreen [/COLOR][/B]' , 'seagreen' ) ,
			( '[B][COLOR seashell]seashell [/COLOR][/B]' , 'seashell' ) ,
			( '[B][COLOR sienna]sienna [/COLOR][/B]' , 'sienna' ) ,
			( '[B][COLOR silver]silver [/COLOR][/B]' , 'silver' ) ,
			( '[B][COLOR skyblue]skyblue [/COLOR][/B]' , 'skyblue' ) ,
			( '[B][COLOR slateblue]slateblue [/COLOR][/B]' , 'slateblue' ) ,
			( '[B][COLOR slategray]slategray [/COLOR][/B]' , 'slategray' ) ,
			( '[B][COLOR slategrey]slategrey [/COLOR][/B]' , 'slategrey' ) ,
			( '[B][COLOR snow]snow [/COLOR][/B]' , 'snow' ) ,
			( '[B][COLOR springgreen]springgreen [/COLOR][/B]' , 'springgreen' ) ,
			( '[B][COLOR steelblue]steelblue [/COLOR][/B]' , 'steelblue' ) ,
			( '[B][COLOR tan]tan [/COLOR][/B]' , 'tan' ) ,
			( '[B][COLOR teal]teal [/COLOR][/B]' , 'teal' ) ,
			( '[B][COLOR thistle]thistle [/COLOR][/B]' , 'thistle' ) ,
			( '[B][COLOR tomato]tomato [/COLOR][/B]' , 'tomato' ) ,
			( '[B][COLOR transparent]transparent [/COLOR][/B]' , 'transparent' ) ,
			( '[B][COLOR turquoise]turquoise [/COLOR][/B]' , 'turquoise' ) ,
			( '[B][COLOR violet]violet [/COLOR][/B]' , 'violet' ) ,
			( '[B][COLOR wheat]wheat [/COLOR][/B]' , 'wheat' ) ,
			( '[B][COLOR white]white [/COLOR][/B]' , 'white' ) ,
			( '[B][COLOR whitesmoke]whitesmoke [/COLOR][/B]' , 'whitesmoke' ) ,
			( '[B][COLOR yellow]yellow [/COLOR][/B]' , 'yellow' ) ,
			( '[B][COLOR yellowgreen]yellowgreen [/COLOR][/B]' , 'yellowgreen' )
			]
 	select = selectDialog([i[0] for i in items], 'Select Color')
	if select == -1: return
	items =  items[select][1]
	if ret = 'Make call'
		DoSomthing(items)
	elif ret = 'Make call'
		DoSomthing(items)
	return
	
