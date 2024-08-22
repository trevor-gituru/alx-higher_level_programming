def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for number in list_of_integers:
        if peak < number:
            peak = number
    return peak
