def hex_string_to_RGB(hex_string): 
    color = [int(hex_string.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)]
    return {'r':color[0],'g':color[1],'b':color[2]}