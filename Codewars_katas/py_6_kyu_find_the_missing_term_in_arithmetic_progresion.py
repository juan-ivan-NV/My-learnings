def find_missing(sequence):

    step = (sequence[-1] - sequence[0])/len(sequence)
    
    for i in range(len(sequence)):
        if (sequence[i] + step) != sequence[i+1]:
            print(sequence[i])
            return sequence[i] + step