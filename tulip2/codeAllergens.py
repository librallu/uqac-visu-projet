# Powered by Python 2.7

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + I : indent selected lines.
#   * Ctrl + Shift + I  : unindent selected lines.
#   * Ctrl + Return  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.
#   * Ctrl + Space  : show auto-completion dialog.

from tulip import *

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
	additives_fr = graph.getStringProperty("additives_fr")
	allergens = graph.getStringProperty("allergens")
	in_ = graph.getStringProperty("in")
	indice = graph.getStringProperty("indice")
	nutritionscore = graph.getIntegerProperty("nutrition-score")
	nutritionscorefr_100g = graph.getStringProperty("nutrition-score-fr_100g")
	out = graph.getStringProperty("out")
	packaging = graph.getStringProperty("packaging")
	product_name = graph.getStringProperty("product_name")
	type_ = graph.getBooleanProperty("type")
	viewBorderColor = graph.getColorProperty("viewBorderColor")
	viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
	viewColor = graph.getColorProperty("viewColor")
	viewFont = graph.getStringProperty("viewFont")
	viewFontAwesomeIcon = graph.getStringProperty("viewFontAwesomeIcon")
	viewFontSize = graph.getIntegerProperty("viewFontSize")
	viewLabel = graph.getStringProperty("viewLabel")
	viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
	viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
	viewLabelColor = graph.getColorProperty("viewLabelColor")
	viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")
	viewLayout = graph.getLayoutProperty("viewLayout")
	viewMetric = graph.getDoubleProperty("viewMetric")
	viewRotation = graph.getDoubleProperty("viewRotation")
	viewSelection = graph.getBooleanProperty("viewSelection")
	viewShape = graph.getIntegerProperty("viewShape")
	viewSize = graph.getSizeProperty("viewSize")
	viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture = graph.getStringProperty("viewTexture")
	viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")

	distToCenter = graph.getIntegerProperty("distanceToCenter")
	
	totX = 0
	totY = 0
	tot = 0

	for n in graph.getNodes():
		vect = viewLayout[n]
		totX += vect[0]
		totY += vect[1]
		tot += 1
	
	midX = totX / tot
	midY = totY / tot
	
	n = graph.addNode()
	viewLayout[n] = tlp.Vec3f(midX, midY, 0)
	viewColor[n] = tlp.Color(0, 255, 0, 255)
	viewSize[n] = tlp.Size(6, 6, 6)
	indice[n] = "center gravity"
	type_[n] = 0
	
	for n in graph.getNodes():
		if type_[n]:
			vect = viewLayout[n]
			valX = midX - vect[0]
			valY = midY - vect[1]
			distToCenter[n] = abs(valX) + abs(valY)
		elif(indice[n] != "center gravity"):
			graph.delNode(n)
	
