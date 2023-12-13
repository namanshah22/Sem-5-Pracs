allPageRequests = [4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
numPageFrames = 3
page_faults = 0
page_hits = 0

s = set()
indexes = {}

for i in allPageRequests:
    if len(s) < numPageFrames:
        if allPageRequests[i] not in s:
            s.add(allPageRequests[i])
            page_faults += 1
        else:
            page_hits += 1
        indexes[allPageRequests[i]] = i
    else:
        if allPageRequests[i] not in s:
            lru = 999
            val = -1
            for page in s:
                if indexes[page] < lru:
                    lru = indexes[page]
                    val = page
            s.remove(val)
            s.add(allPageRequests[i])
            page_faults += 1
        else:
            page_hits += 1
        indexes[allPageRequests[i]] = i

total_requests = len(allPageRequests)
hit_ratio = page_hits / total_requests
miss_ratio = page_faults / total_requests

print("Page Faults:", page_faults)
print("Hit Ratio:", hit_ratio)
print("Miss Ratio:", miss_ratio)
