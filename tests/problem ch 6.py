Grade = float(input('input grade'))
if Grade >= 90.0:
	Grade = 'A'
elif Grade >= 80.0:
	Grade = 'B'
elif Grade >= 70.0:
	Grade = 'C'
elif Grade >= 60.0:
	Grade = 'D'
elif Grade < 60.0:
	Grade = 'F'
print(Grade)
