import re

def nba_cup(result_sheet, to_find):
    games = result_sheet.split(',')
    match_list = [re.split(r'(?<=\d) (?=\w)', i) for i in games]
    print(match_list)
    
    match_dicts = []
    
    for match in match_list:
        matchd = []
        for team in match:
            
            for word in match.strip().split(' '):
                if word.isdigit():
                    
    return "testing"