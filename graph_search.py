def search(G, s):
	foundHandled = []
	foundNotHandled = [s]
	while foundNotHandled != []:
		u = foundNotHandled[0]
		for each v connected to u:
			if foundNotHandled[v] == 0:
				foundNotHandled.append(v)
		x = foundNotHandled.pop()
		foundHandled.append(x)
	return foundHandled

