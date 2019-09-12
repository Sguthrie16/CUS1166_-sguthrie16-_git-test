def average(roster):
    total=0
    for i in roster:
        total += i.get_grade()
    return total/len(roster)
