from users import users

def minkowski(rating1, rating2, r):
	distance = 0
	commonRatings = False
	for key in rating1:
		if key in rating2:
			distance +=pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True
	if commonRatings:
		return pow(distance, 1/r)
	else:
		return -1 


distance = minkowski(users["Angelica"], users["Chan"], 2)
print distance
