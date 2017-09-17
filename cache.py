#cache.py


def solution(cacheSize, cities):
    answer = 0
    
    #If cache is empty, add items to the cacheSize
    cache=[]
    hit = 0
    cacheHit = False
    LRU = 0
    raw = cities
    cities = []

    #make all letter to upper letter
    for i in raw:
    	cities.append(i.upper())

    # initialize cache
    if not (cacheSize!=0):
	    for i in range(cacheSize):
	    	cache.append(cities[i])
	    	hit=hit+5 # cahe miss

    #check whether cities are hit in the cache
    for i in range (cacheSize, len(cities)):
    	#check whether the city is in the cache
    	for j in range (cacheSize):
    		if (cache[j]==cities[i]):
    			print("hit")
    			hit = hit +1
    			LRU = cache.pop(j)
    			cache.append(LRU)
    			cacheHit = True
    			break
    	if (cacheHit!=True):
    		print ("not hit!")
    		hit = hit +5
    		if not (cacheSize==0):
    			del cache[0]
    			cache.append(cities[i])
    	cacheHit = False			
    answer = hit
    print answer)
    return answer
solution (0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])

