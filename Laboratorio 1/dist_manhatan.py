from users import users


def manhattan(rating1, rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key])
	return distance


print users["Veronica"]
print manhattan(users['Hailey'], users['Veronica'])
print manhattan(users['Hailey'], users['Jordyn'])
