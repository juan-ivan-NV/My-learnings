import re

def nba_cup(result_sheet, to_find):
    games = result_sheet.split(',')
    #print(games)
    
    print([re.split(r'\d[ \W]', i) for i in games])
    #words = re.split(r'(\d( )\w)', text)
    
    return "testing"