def valid_parenthesis(string):
	temp_list = []
	for i in string:
		if i == '(':
			temp_list.append(i)
		elif i == ')':
			if len(temp_list) == 0:
				return False
			elif temp_list[-1] == '(':
				temp_list.pop()
			else:
				return False
	if len(temp_list) == 0:
		return True
	else:
		return False

print('изменение для теста git')