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
	in_ = graph.getStringProperty("in")
	indice = graph.getStringProperty("indice")
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

	nutritionScore = graph.getIntegerProperty("nutrition-score")
	
	for n in graph.getNodes():
		if type_[n]:
			viewLabel[n] = indice[n]

	for n in graph.getNodes():
		try:
			nutritionScore[n] = int(nutritionscorefr_100g[n])
		except ValueError:
			nutritionScore[n] = -11
			
			
	for n in graph.getNodes():
		viewSize[n] = tlp.Vec3f(1, 1, 1)

	for n in graph.getNodes():
		if nutritionScore[n] == -11:
			viewColor[n] = tlp.Color(128,128,128,255)
			
	print(nutritionScore.getNodeMax())
	print(nutritionScore.getNodeMin())
