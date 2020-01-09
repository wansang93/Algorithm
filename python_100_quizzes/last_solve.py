page = 'BCBAEBCE'
frame = 3
time = 0

queue = []

for c in page:
    if c in queue:
        queue.remove(c)
        queue.append(c)
        time += 1
    else:
        if frame <= len(queue):
            queue.pop(0)
            queue.append(c)
        else:
            queue.append(c)
        time += 6

print(time)