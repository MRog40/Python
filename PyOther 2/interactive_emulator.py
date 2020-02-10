while True:
	cmd = input(">>> ")
	if "=" in cmd:
		_ = exec(cmd)
	else:
		_ = eval(cmd)
		print("    {}\n".format(_))