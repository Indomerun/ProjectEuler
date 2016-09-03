print(sum([(position+1)*nameScore for position, nameScore in enumerate([sum([ord(char)-64 for char in name]) for name in sorted([string for string in open("../Data/data_022.txt").read().replace('"', "").split(',')])])]))

