import random

from lab.draw import Color


class Palette:
    BLACK = Color.from_hexstr("000000")
    MAROON = Color.from_hexstr("800000")
    GREEN = Color.from_hexstr("008000")
    OLIVE = Color.from_hexstr("808000")
    NAVY = Color.from_hexstr("000080")
    PURPLE = Color.from_hexstr("800080")
    TEAL = Color.from_hexstr("008080")
    SILVER = Color.from_hexstr("c0c0c0")
    GREY = Color.from_hexstr("808080")
    RED = Color.from_hexstr("ff0000")
    LIME = Color.from_hexstr("00ff00")
    YELLOW = Color.from_hexstr("ffff00")
    BLUE = Color.from_hexstr("0000ff")
    FUCHSIA = Color.from_hexstr("ff00ff")
    AQUA = Color.from_hexstr("00ffff")
    WHITE = Color.from_hexstr("ffffff")
    GREY0 = Color.from_hexstr("000000")
    NAVYBLUE = Color.from_hexstr("00005f")
    DARKBLUE = Color.from_hexstr("000087")
    BLUE3 = Color.from_hexstr("0000af")
    BLUE3 = Color.from_hexstr("0000d7")
    BLUE1 = Color.from_hexstr("0000ff")
    DARKGREEN = Color.from_hexstr("005f00")
    DEEPSKYBLUE4 = Color.from_hexstr("005f5f")
    DEEPSKYBLUE4 = Color.from_hexstr("005f87")
    DEEPSKYBLUE4 = Color.from_hexstr("005faf")
    DODGERBLUE3 = Color.from_hexstr("005fd7")
    DODGERBLUE2 = Color.from_hexstr("005fff")
    GREEN4 = Color.from_hexstr("008700")
    SPRINGGREEN4 = Color.from_hexstr("00875f")
    TURQUOISE4 = Color.from_hexstr("008787")
    DEEPSKYBLUE3 = Color.from_hexstr("0087af")
    DEEPSKYBLUE3 = Color.from_hexstr("0087d7")
    DODGERBLUE1 = Color.from_hexstr("0087ff")
    GREEN3 = Color.from_hexstr("00af00")
    SPRINGGREEN3 = Color.from_hexstr("00af5f")
    DARKCYAN = Color.from_hexstr("00af87")
    LIGHTSEAGREEN = Color.from_hexstr("00afaf")
    DEEPSKYBLUE2 = Color.from_hexstr("00afd7")
    DEEPSKYBLUE1 = Color.from_hexstr("00afff")
    GREEN3 = Color.from_hexstr("00d700")
    SPRINGGREEN3 = Color.from_hexstr("00d75f")
    SPRINGGREEN2 = Color.from_hexstr("00d787")
    CYAN3 = Color.from_hexstr("00d7af")
    DARKTURQUOISE = Color.from_hexstr("00d7d7")
    TURQUOISE2 = Color.from_hexstr("00d7ff")
    GREEN1 = Color.from_hexstr("00ff00")
    SPRINGGREEN2 = Color.from_hexstr("00ff5f")
    SPRINGGREEN1 = Color.from_hexstr("00ff87")
    MEDIUMSPRINGGREEN = Color.from_hexstr("00ffaf")
    CYAN2 = Color.from_hexstr("00ffd7")
    CYAN1 = Color.from_hexstr("00ffff")
    DARKRED = Color.from_hexstr("5f0000")
    DEEPPINK4 = Color.from_hexstr("5f005f")
    PURPLE4 = Color.from_hexstr("5f0087")
    PURPLE4 = Color.from_hexstr("5f00af")
    PURPLE3 = Color.from_hexstr("5f00d7")
    BLUEVIOLET = Color.from_hexstr("5f00ff")
    ORANGE4 = Color.from_hexstr("5f5f00")
    GREY37 = Color.from_hexstr("5f5f5f")
    MEDIUMPURPLE4 = Color.from_hexstr("5f5f87")
    SLATEBLUE3 = Color.from_hexstr("5f5faf")
    SLATEBLUE3 = Color.from_hexstr("5f5fd7")
    ROYALBLUE1 = Color.from_hexstr("5f5fff")
    CHARTREUSE4 = Color.from_hexstr("5f8700")
    DARKSEAGREEN4 = Color.from_hexstr("5f875f")
    PALETURQUOISE4 = Color.from_hexstr("5f8787")
    STEELBLUE = Color.from_hexstr("5f87af")
    STEELBLUE3 = Color.from_hexstr("5f87d7")
    CORNFLOWERBLUE = Color.from_hexstr("5f87ff")
    CHARTREUSE3 = Color.from_hexstr("5faf00")
    DARKSEAGREEN4 = Color.from_hexstr("5faf5f")
    CADETBLUE = Color.from_hexstr("5faf87")
    CADETBLUE = Color.from_hexstr("5fafaf")
    SKYBLUE3 = Color.from_hexstr("5fafd7")
    STEELBLUE1 = Color.from_hexstr("5fafff")
    CHARTREUSE3 = Color.from_hexstr("5fd700")
    PALEGREEN3 = Color.from_hexstr("5fd75f")
    SEAGREEN3 = Color.from_hexstr("5fd787")
    AQUAMARINE3 = Color.from_hexstr("5fd7af")
    MEDIUMTURQUOISE = Color.from_hexstr("5fd7d7")
    STEELBLUE1 = Color.from_hexstr("5fd7ff")
    CHARTREUSE2 = Color.from_hexstr("5fff00")
    SEAGREEN2 = Color.from_hexstr("5fff5f")
    SEAGREEN1 = Color.from_hexstr("5fff87")
    SEAGREEN1 = Color.from_hexstr("5fffaf")
    AQUAMARINE1 = Color.from_hexstr("5fffd7")
    DARKSLATEGRAY2 = Color.from_hexstr("5fffff")
    DARKRED = Color.from_hexstr("870000")
    DEEPPINK4 = Color.from_hexstr("87005f")
    DARKMAGENTA = Color.from_hexstr("870087")
    DARKMAGENTA = Color.from_hexstr("8700af")
    DARKVIOLET = Color.from_hexstr("8700d7")
    PURPLE = Color.from_hexstr("8700ff")
    ORANGE4 = Color.from_hexstr("875f00")
    LIGHTPINK4 = Color.from_hexstr("875f5f")
    PLUM4 = Color.from_hexstr("875f87")
    MEDIUMPURPLE3 = Color.from_hexstr("875faf")
    MEDIUMPURPLE3 = Color.from_hexstr("875fd7")
    SLATEBLUE1 = Color.from_hexstr("875fff")
    YELLOW4 = Color.from_hexstr("878700")
    WHEAT4 = Color.from_hexstr("87875f")
    GREY53 = Color.from_hexstr("878787")
    LIGHTSLATEGREY = Color.from_hexstr("8787af")
    MEDIUMPURPLE = Color.from_hexstr("8787d7")
    LIGHTSLATEBLUE = Color.from_hexstr("8787ff")
    YELLOW4 = Color.from_hexstr("87af00")
    DARKOLIVEGREEN3 = Color.from_hexstr("87af5f")
    DARKSEAGREEN = Color.from_hexstr("87af87")
    LIGHTSKYBLUE3 = Color.from_hexstr("87afaf")
    LIGHTSKYBLUE3 = Color.from_hexstr("87afd7")
    SKYBLUE2 = Color.from_hexstr("87afff")
    CHARTREUSE2 = Color.from_hexstr("87d700")
    DARKOLIVEGREEN3 = Color.from_hexstr("87d75f")
    PALEGREEN3 = Color.from_hexstr("87d787")
    DARKSEAGREEN3 = Color.from_hexstr("87d7af")
    DARKSLATEGRAY3 = Color.from_hexstr("87d7d7")
    SKYBLUE1 = Color.from_hexstr("87d7ff")
    CHARTREUSE1 = Color.from_hexstr("87ff00")
    LIGHTGREEN = Color.from_hexstr("87ff5f")
    LIGHTGREEN = Color.from_hexstr("87ff87")
    PALEGREEN1 = Color.from_hexstr("87ffaf")
    AQUAMARINE1 = Color.from_hexstr("87ffd7")
    DARKSLATEGRAY1 = Color.from_hexstr("87ffff")
    RED3 = Color.from_hexstr("af0000")
    DEEPPINK4 = Color.from_hexstr("af005f")
    MEDIUMVIOLETRED = Color.from_hexstr("af0087")
    MAGENTA3 = Color.from_hexstr("af00af")
    DARKVIOLET = Color.from_hexstr("af00d7")
    PURPLE = Color.from_hexstr("af00ff")
    DARKORANGE3 = Color.from_hexstr("af5f00")
    INDIANRED = Color.from_hexstr("af5f5f")
    HOTPINK3 = Color.from_hexstr("af5f87")
    MEDIUMORCHID3 = Color.from_hexstr("af5faf")
    MEDIUMORCHID = Color.from_hexstr("af5fd7")
    MEDIUMPURPLE2 = Color.from_hexstr("af5fff")
    DARKGOLDENROD = Color.from_hexstr("af8700")
    LIGHTSALMON3 = Color.from_hexstr("af875f")
    ROSYBROWN = Color.from_hexstr("af8787")
    GREY63 = Color.from_hexstr("af87af")
    MEDIUMPURPLE2 = Color.from_hexstr("af87d7")
    MEDIUMPURPLE1 = Color.from_hexstr("af87ff")
    GOLD3 = Color.from_hexstr("afaf00")
    DARKKHAKI = Color.from_hexstr("afaf5f")
    NAVAJOWHITE3 = Color.from_hexstr("afaf87")
    GREY69 = Color.from_hexstr("afafaf")
    LIGHTSTEELBLUE3 = Color.from_hexstr("afafd7")
    LIGHTSTEELBLUE = Color.from_hexstr("afafff")
    YELLOW3 = Color.from_hexstr("afd700")
    DARKOLIVEGREEN3 = Color.from_hexstr("afd75f")
    DARKSEAGREEN3 = Color.from_hexstr("afd787")
    DARKSEAGREEN2 = Color.from_hexstr("afd7af")
    LIGHTCYAN3 = Color.from_hexstr("afd7d7")
    LIGHTSKYBLUE1 = Color.from_hexstr("afd7ff")
    GREENYELLOW = Color.from_hexstr("afff00")
    DARKOLIVEGREEN2 = Color.from_hexstr("afff5f")
    PALEGREEN1 = Color.from_hexstr("afff87")
    DARKSEAGREEN2 = Color.from_hexstr("afffaf")
    DARKSEAGREEN1 = Color.from_hexstr("afffd7")
    PALETURQUOISE1 = Color.from_hexstr("afffff")
    RED3 = Color.from_hexstr("d70000")
    DEEPPINK3 = Color.from_hexstr("d7005f")
    DEEPPINK3 = Color.from_hexstr("d70087")
    MAGENTA3 = Color.from_hexstr("d700af")
    MAGENTA3 = Color.from_hexstr("d700d7")
    MAGENTA2 = Color.from_hexstr("d700ff")
    DARKORANGE3 = Color.from_hexstr("d75f00")
    INDIANRED = Color.from_hexstr("d75f5f")
    HOTPINK3 = Color.from_hexstr("d75f87")
    HOTPINK2 = Color.from_hexstr("d75faf")
    ORCHID = Color.from_hexstr("d75fd7")
    MEDIUMORCHID1 = Color.from_hexstr("d75fff")
    ORANGE3 = Color.from_hexstr("d78700")
    LIGHTSALMON3 = Color.from_hexstr("d7875f")
    LIGHTPINK3 = Color.from_hexstr("d78787")
    PINK3 = Color.from_hexstr("d787af")
    PLUM3 = Color.from_hexstr("d787d7")
    VIOLET = Color.from_hexstr("d787ff")
    GOLD3 = Color.from_hexstr("d7af00")
    LIGHTGOLDENROD3 = Color.from_hexstr("d7af5f")
    TAN = Color.from_hexstr("d7af87")
    MISTYROSE3 = Color.from_hexstr("d7afaf")
    THISTLE3 = Color.from_hexstr("d7afd7")
    PLUM2 = Color.from_hexstr("d7afff")
    YELLOW3 = Color.from_hexstr("d7d700")
    KHAKI3 = Color.from_hexstr("d7d75f")
    LIGHTGOLDENROD2 = Color.from_hexstr("d7d787")
    LIGHTYELLOW3 = Color.from_hexstr("d7d7af")
    GREY84 = Color.from_hexstr("d7d7d7")
    LIGHTSTEELBLUE1 = Color.from_hexstr("d7d7ff")
    YELLOW2 = Color.from_hexstr("d7ff00")
    DARKOLIVEGREEN1 = Color.from_hexstr("d7ff5f")
    DARKOLIVEGREEN1 = Color.from_hexstr("d7ff87")
    DARKSEAGREEN1 = Color.from_hexstr("d7ffaf")
    HONEYDEW2 = Color.from_hexstr("d7ffd7")
    LIGHTCYAN1 = Color.from_hexstr("d7ffff")
    RED1 = Color.from_hexstr("ff0000")
    DEEPPINK2 = Color.from_hexstr("ff005f")
    DEEPPINK1 = Color.from_hexstr("ff0087")
    DEEPPINK1 = Color.from_hexstr("ff00af")
    MAGENTA2 = Color.from_hexstr("ff00d7")
    MAGENTA1 = Color.from_hexstr("ff00ff")
    ORANGERED1 = Color.from_hexstr("ff5f00")
    INDIANRED1 = Color.from_hexstr("ff5f5f")
    INDIANRED1 = Color.from_hexstr("ff5f87")
    HOTPINK = Color.from_hexstr("ff5faf")
    HOTPINK = Color.from_hexstr("ff5fd7")
    MEDIUMORCHID1 = Color.from_hexstr("ff5fff")
    DARKORANGE = Color.from_hexstr("ff8700")
    SALMON1 = Color.from_hexstr("ff875f")
    LIGHTCORAL = Color.from_hexstr("ff8787")
    PALEVIOLETRED1 = Color.from_hexstr("ff87af")
    ORCHID2 = Color.from_hexstr("ff87d7")
    ORCHID1 = Color.from_hexstr("ff87ff")
    ORANGE1 = Color.from_hexstr("ffaf00")
    SANDYBROWN = Color.from_hexstr("ffaf5f")
    LIGHTSALMON1 = Color.from_hexstr("ffaf87")
    LIGHTPINK1 = Color.from_hexstr("ffafaf")
    PINK1 = Color.from_hexstr("ffafd7")
    PLUM1 = Color.from_hexstr("ffafff")
    GOLD1 = Color.from_hexstr("ffd700")
    LIGHTGOLDENROD2 = Color.from_hexstr("ffd75f")
    LIGHTGOLDENROD2 = Color.from_hexstr("ffd787")
    NAVAJOWHITE1 = Color.from_hexstr("ffd7af")
    MISTYROSE1 = Color.from_hexstr("ffd7d7")
    THISTLE1 = Color.from_hexstr("ffd7ff")
    YELLOW1 = Color.from_hexstr("ffff00")
    LIGHTGOLDENROD1 = Color.from_hexstr("ffff5f")
    KHAKI1 = Color.from_hexstr("ffff87")
    WHEAT1 = Color.from_hexstr("ffffaf")
    CORNSILK1 = Color.from_hexstr("ffffd7")
    GREY100 = Color.from_hexstr("ffffff")
    GREY3 = Color.from_hexstr("080808")
    GREY7 = Color.from_hexstr("121212")
    GREY11 = Color.from_hexstr("1c1c1c")
    GREY15 = Color.from_hexstr("262626")
    GREY19 = Color.from_hexstr("303030")
    GREY23 = Color.from_hexstr("3a3a3a")
    GREY27 = Color.from_hexstr("444444")
    GREY30 = Color.from_hexstr("4e4e4e")
    GREY35 = Color.from_hexstr("585858")
    GREY39 = Color.from_hexstr("626262")
    GREY42 = Color.from_hexstr("6c6c6c")
    GREY46 = Color.from_hexstr("767676")
    GREY50 = Color.from_hexstr("808080")
    GREY54 = Color.from_hexstr("8a8a8a")
    GREY58 = Color.from_hexstr("949494")
    GREY62 = Color.from_hexstr("9e9e9e")
    GREY66 = Color.from_hexstr("a8a8a8")
    GREY70 = Color.from_hexstr("b2b2b2")
    GREY74 = Color.from_hexstr("bcbcbc")
    GREY78 = Color.from_hexstr("c6c6c6")
    GREY82 = Color.from_hexstr("d0d0d0")
    GREY85 = Color.from_hexstr("dadada")
    GREY89 = Color.from_hexstr("e4e4e4")
    GREY93 = Color.from_hexstr("eeeeee")

    @staticmethod
    def named_values():
        return {
            name: value for
            name, value in vars(Palette).items()
            if (type(value) is Color)
        }

    @staticmethod
    def values():
        return list(Palette.named_values().values())

    @staticmethod
    def random():
        return random.choice(Palette.values())
