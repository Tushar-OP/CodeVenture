# your code goes here

def find_mass(s):
	
	stack = []
	
	for i in range(len(s)):
		if s[i] == 'H':
			stack.append(1)
		if s[i] == 'C':
			stack.append(12)
		if s[i] == 'O':
			stack.append(16)
		if s[i] == '(':
			stack.append(-1)
		if s[i] >= '2' and s[i] <= '9':
			n = stack[-1]
			stack.pop()
			stack.append(n * int(s[i]))
		if s[i] == ')':
			total = 0
			while(stack[-1] != -1):
				total += stack[-1]
				stack.pop()
			stack.pop()
			stack.append(total)
	
	res = 0
	
	while(stack != []):
		res += stack[-1]
		stack.pop()
	
	print(res)
	
	
	


mol = input().strip()

find_mass(mol)

