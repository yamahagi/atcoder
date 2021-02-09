import heapq

N,K = map(int,input().split())
al = []
bl = []
for _ in range(N):
    a,b = map(int,input().split())
    al.append(a)
    bl.append(b)

present = 0
cura = 0
nexta = 0
cl = [(a,b) for a,b in zip(al,bl)]
heapq.heapify(cl)
time = 0
if len(cl) == 1:
    a = cl[0][0]
    b = cl[0][1]
    time = a * K + 1/2 *K * (K-1) * b
    present = K
while present < K:
    if cura == 0 and nexta == 0:
        cura,b = heapq.heappop(cl)
        nexta,nextb = heapq.heappop(cl)
    #nextmを超えるまでpresentを作る
    if b != 0:
        kosuu = min(K-present,(nexta-cura)//b+1)
        present += kosuu
        time += kosuu*cura + 1/2*kosuu*(kosuu-1)*b
        cura += kosuu*b
    else:
        time += (K-present) * cura
        break
    heapq.heappush(cl, (cura,b))
    cura = nexta
    b = nextb
    #nextmをcurmに変更し次のnextmを探す
    nexta,nextb = heapq.heappop(cl)
print(int(time))
