f = open('cities.txt', 'r')
out = open('out.txt', 'w')
for line in f:
	out.write("{\n\"id\":null,\n\"name\": {\n\"value\":\"%s\",\n\"synonyms\":[]\n}\n}," % line.strip())