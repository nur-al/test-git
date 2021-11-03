while True:
	s = input("Введите что-нибудь:")
	if s == "exit":
		break
	if len(s) < 3:
		print('Malo')
		continue
	print('norm')
