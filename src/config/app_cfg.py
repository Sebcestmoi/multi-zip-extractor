from enum import Enum

class Theme_wp(Enum):
    BG_COLOR = "white"
    BT_COLOR = "purple"
    FG_COLOR = "purple"
    TXT_BG_COLOR = BG_COLOR
    TXT_FG_COLOR = FG_COLOR

class Theme_grey(Enum):
    BG_COLOR = "#606060"
    BT_COLOR = "#CACACA"
    FG_COLOR = "#CACACA"
    TXT_BG_COLOR = "black"
    TXT_FG_COLOR = "white"

class Theme_pink(Enum):
    BG_COLOR = "#FCEFFB"
    BT_COLOR = "#F986E2"
    FG_COLOR = "#F986E2"
    TXT_BG_COLOR = BG_COLOR
    TXT_FG_COLOR = FG_COLOR

class Theme_dark(Enum):
    BG_COLOR = "#000000"
    BT_COLOR = "#D00000"
    FG_COLOR = "#D00000"
    TXT_BG_COLOR = BG_COLOR
    TXT_FG_COLOR = FG_COLOR

class Theme_psycho(Enum):
    BG_COLOR = "#FF0000"
    BT_COLOR = "#00F7FF"
    FG_COLOR = "#00F7FF"
    TXT_BG_COLOR = BG_COLOR
    TXT_FG_COLOR = "black"

class Theme_style(Enum):
    BG_COLOR = "#E803E8"
    BT_COLOR = "#06E803"
    FG_COLOR = "#06E803"
    TXT_BG_COLOR = "black"
    TXT_FG_COLOR = "white"

class App_font(Enum):
    TXT_FONT_1 = "Arial 10 bold"
    TXT_FONT_2 = "Arial 14 bold"
