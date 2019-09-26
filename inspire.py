import os
import json
key = "helloworld"

picurl = os.popen('wget -qO- --tries=3 --timeout=5 "http://inspirobot.me/api?generate=true" | grep ".jpg"').readline().replace("\n","")
txtjson = os.popen('wget -qO- --tries=3 --timeout=5 "https://api.ocr.space/parse/imageurl?apikey=' + key + '&url=' + picurl + '&language=eng"').readline().replace("\n","")
txt = json.loads(txtjson)["ParsedResults"][0]["ParsedText"].replace("-\r\n","").replace("\r\n"," ")
print txt
