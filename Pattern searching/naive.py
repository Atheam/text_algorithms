


def naive_pattern(text,pattern):
	out = []
	for s in range(0,len(text)-len(pattern)+1):
		if pattern == text[s:s+len(pattern)]:
			out.append(s)
	return out




	



