import re

def nba_cup(result_sheet, to_find):
    games = result_sheet.split(',')
    match_list = [re.split(r'(?<=\d) (?=\w)', i) for i in games]
    #print(match_list)
    separate = lambda x: {re.sub('(?<=s) \d+', '', x).rstrip():re.findall('(?<=s )\d+', x)}
    match_dict = [[separate(i[0]), separate(i[1])] for i in match_list]
    #(?<=s )\w+
    print(match_dict)
    #team_1 ={re.sub('(?<=s )\w+', '', match_list[1][1]).rstrip():int(re.findall('(?<=s )\w+', match_list[1][0])[0])}
    #print(team_1)
    return "testing"