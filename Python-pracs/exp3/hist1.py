def histogram(l):
    s = list(set(l))
    count_s = []
    for i in s:
        count_s.append((i,l.count(i)))
    hist = sorted(count_s,key=lambda x:x[1])
    return hist
print(f"Histogram implemenation : ",histogram([13,12,14,15,11,13,7,12,7,13,14,12]))