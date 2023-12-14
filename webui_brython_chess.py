# run html with Brython without web server
from webui import webui
w = webui.window()
w.show("brython_chess.html")
webui.wait()
