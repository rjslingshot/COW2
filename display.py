import re

def output(text):
  ##------
  ## This formats output for provided text based on tags
  ##  and is used in the Methods.py
  ##
  ## Example: print(display.output("<Red>My Text<Reset>\n"))
  ##   "Red" defines the color and <Reset> changes the text   
  ##    color back. '\n' generates a carriage return
  ##------
  for i in range(50):
    # STYLES
    text = re.sub("<Bold>","\033[1m",text)
    text = re.sub("<Dim>","\033[2m",text)
    text = re.sub("<Underlined>","\033[4m",text)
    text = re.sub("<Blink>","\033[5m",text)
    text = re.sub("<Reverse>","\033[7m",text)
    text = re.sub("<Hidden>","\033[8m",text)
    # TEXT COLOR
    text = re.sub("<Default>","\033[39m",text)
    text = re.sub("<Black>","\033[30m",text)
    text = re.sub("<Red>","\033[31m",text)
    text = re.sub("<Green>","\033[32m",text)
    text = re.sub("<Yellow>","\033[33m",text)
    text = re.sub("<Blue>","\033[34m",text)
    text = re.sub("<Magenta>","\033[35m",text)
    text = re.sub("<Cyan>","\033[36m",text)
    text = re.sub("<LightGray>","\033[37m",text)
    text = re.sub("<DarkGray>","\033[90m",text)
    text = re.sub("<LightRed>","\033[91m",text)
    text = re.sub("<LightGreen>","\033[92m",text)
    text = re.sub("<LightYellow>","\033[93m",text)
    text = re.sub("<LightBlue>","\033[94m",text)
    text = re.sub("<LightMagenta>","\033[95m",text)
    text = re.sub("<LightCyan>","\033[96m",text)
    text = re.sub("<White>","\033[97m",text)
    # BACKGROUND COLOR
    text = re.sub("<BackgroundDefault>","\033[49m",text)
    text = re.sub("<BackgroundBlack>","\033[40m",text)
    text = re.sub("<BackgroundRed>","\033[41m",text)
    text = re.sub("<BackgroundGreen>","\033[42m",text)
    text = re.sub("<BackgroundYellow>","\033[43m",text)
    text = re.sub("<BackgroundBlue>","\033[44m",text)
    text = re.sub("<BackgroundMagenta>","\033[45m",text)
    text = re.sub("<BackgroundCyan>","\033[46m",text)
    text = re.sub("<BackgroundLightGray>","\033[47m",text)
    text = re.sub("<BackgroundDarkGray>","\033[100m",text)
    text = re.sub("<BackgroundLightRed>","\033[101m",text)
    text = re.sub("<BackgroundLightGreen>","\033[102m",text)
    text = re.sub("<BackgroundLightYellow>","\033[103m",text)
    text = re.sub("<BackgroundLightBlue>","\033[104m",text)
    text = re.sub("<BackgroundLightMagenta>","\033[105m",text)
    text = re.sub("<BackgroundLightCyan>","\033[106m",text)
    text = re.sub("<BackgroundWhite>","\033[107m",text)
    # RESETS
    text = re.sub("<Reset>","\033[0m",text)
    text = re.sub("<ResetBold>","\033[21m",text)
    text = re.sub("<ResetDim>","\033[22m",text)
    text = re.sub("<ResetUnderlined>","\033[24m",text)
    text = re.sub("<ResetBlink>","\033[25m",text)
    text = re.sub("<ResetReverse>","\033[27m",text)
    text = re.sub("<ResetHidden>","\033[28m",text)

  return text