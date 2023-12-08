allPageRequests = [4,7,6,1,7,6,1,2,7,2]
numPageFrames = 3
pageFaults = 0
pageFrames = []
for page in allPageRequests:
    if page not in pageFrames:
        if len(pageFrames) < numPageFrames:
            pageFrames.append(page)
        else:
            pageFrames = pageFrames[1:] + [page]
            pageFaults+=1
        print(f"Page input {page} : page frames - {pageFrames}, fault")
    else:
        print(f"Page input {page} : page frames - {pageFrames}, hit")

#print(f"\nPage Faults = {pageFaults}, Page Hits = {len(allPageRequests)-pageFaults}")
hits=len(allPageRequests)-pageFaults
hit_ratio = hits / len(allPageRequests)
miss_ratio = pageFaults / len(allPageRequests)

print(f"\n\nNo. of page hits = {hits}")
print(f"No. of page faults = {pageFaults}")
print(f"Hit ratio = {hit_ratio}")
print(f"Miss ratio = {miss_ratio}")
