import re

def nba_cup(result_sheet, to_find):
    games = result_sheet.split(',')
    
    match_list = [re.split(r'(?<=\d) (?=\w)', i) for i in games]
    
    
    
    return "testing"