from time import sleep


# --- Display a bold line of green text with a black background:
#\033[ --- This is an escape character.
#1;    --- This implies that the text should be bold.
#32;   --- This implies that the text should be green.
#40m   --- This implies that the background should be black.
print("\033[1;32;40m\
Bold (1) green (32) TEXT ON A BLACK BACKGROUND(x)" +"\n")
 
 
sleep(2)


# --- Display a normal, underlined line of cyan text with a black background:
#\033[---This is an escape character.
#4;  --- This implies that the text should be underlined and normal.
#36; --- This implies that the text should be cyan.
#40m --- This implies that the background should be black.
print("\033[0;37;44m\
Normal, underlined (4) cyan text (37) on a black background (40)")

sleep(2)


# print terminal colour chart

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')
 
 
print_format_table()



