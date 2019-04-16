from users import users

def manhattan(rating1, rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key])
	return distance

def computeNearestNeighbor(username, users):
	distances = []
	for user in users:
		if user != username:
			distance = manhattan(users[user], users[username])
			distances.append((distance, user))
	distances.sort()
	return distances

print computeNearestNeighbor("Hailey", users)
print computeNearestNeighbor('Angelica', users)

