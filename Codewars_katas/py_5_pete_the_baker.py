def cakes(recipe, available):
    # TODO: insert code
    x = []
    
    for key,val in recipe.items():
        if key in available:
            for i,j in available.items():
                if key == i:
                    x.append(j/val)
        elif key not in available:
            return 0
    return(int(min(x)))