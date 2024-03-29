import re

def nba_cup(result_sheet, to_find):
    
    if not to_find: return ''
    
    win, draw, loss, points, conceded = 0,0,0,0,0
    
    for t1, s1, t2, s2 in re.findall(r'(.+?) (\b[\d.]+\b) (.+?) (\b[\d.]+\b)(?:,|$)', result_sheet):
        
        if '.' in s1 or '.' in s2: return f"Error(float number):{t1} {s1} {t2} {s2}"
        
        if to_find == t1 or to_find == t2:
            if to_find == t1: ps,cs = int(s1),int(s2)
            else: ps,cs = int(s2),int(s1)
            
            points += ps
            conceded += cs
            
            if s1 == s2: draw += 1
            elif ps < cs: loss += 1
            else: win += 1
    
    ranking = win * 3 + draw
    if not points and not conceded: return f"{to_find}:This team didn't play!"
    
    return f"{to_find}:W={win};D={draw};L={loss};Scored={points};Conceded={conceded};Points={ranking}"