import csv
# 1. Open the file
# 2. Convert the file into a CSV
rows = []
with open("salary_survey.csv", "r") as f:
	data = csv.DictReader(f)
	for r in data:
		rows.append(r)


# 3. Go through each row in the CSV
# 	- For each row:
for row in rows:
	# 4. If the row has a mal-formed city and state pair, fix it
	# 		- Inspect each column
	# 		- If the column is for a state, check that the state is not empty
	if not row.get("State"):
		# - If the state is empty
		# check that the  city column has two values separated by a comma.
		# Split these values along the comma and treat the frist part 
		# as the city and the second part as the state
		pair = row.get("City").split(",")
		if len(pair) == 2 and len(pair[0]) > 0 and len(pair[1]) > 0:
			city = pair[0]
			state = pair[1]
			# Assign the values to their respective columns
			row["State"] = state
			row["City"] = city


	
# 5. After going through all the rows, save the data as a new file
with open("clean.csv", "w") as f:
	fieldnames = rows[0]
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(rows)




# (optional) If the state is abbreviated, replace with the full state name