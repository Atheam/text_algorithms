



def finite_automata_search(text,pattern):
	delta = build_automata(pattern)
	out = []
	q = 0
	for s in range(0,len(text)):
		print(delta)
		q = delta[q].get(text[s])
		if not q:
			q = 0
			continue
		if q == len(delta) - 1:
			out.append(s + 1 - q)
	return out


def build_automata(pattern):
	result = []
	alphabet = list(set(pattern))
	for q in range(0, len(pattern) + 1):
		result.append({})
		for a in alphabet:
			k = min(len(pattern) + 1, q + 2)
			while True:
				k = k - 1
				if pattern[:k] == (pattern[:q]+a)[q-k+1:]:
					break
			result[q][a] = k    
	return result

    




	

 