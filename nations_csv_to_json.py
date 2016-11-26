from json import JSONEncoder
import json
import random
import csv

food_data = []
food_metadata = {}
# FOOD DATA - MEAT
with open("FAO_data_raw.csv","rb") as f1:
		f1.next()
		fao_data = csv.reader(f1, delimiter=" ", skipinitialspace=True)
		
		count = 0
		for line in fao_data:
			if count >= 111 and count < 152:
				print line[1]
				print (int)(line[3])

				food_val = line[4]
				if food_val == "NA":
					food_val = 0

				print food_val

				country = line[1]
				food_data.append([(int)(line[3]), (int)(food_val)])
				count = count + 1

			else:
				if count == 968:
					print country
					print food_data
					food_metadata[country] = food_data
					count = 0
					food_data = []
				else:
					count = count + 1


# GDP DATA
with open("GDP_urbanisation.csv", "rb") as f:
	f.next()
	data = csv.reader(f, delimiter="\t", skipinitialspace=True) 

	json_data = {}

	count = 0
	countries = 0
	gdps = []
	perurbs = []
	food = []

	# outfile.write("[")

	for line in data:
		if count == 0:
			name = line[1]
			region = line[2]
			subregion = line[3]
			gdps.append([(int)(line[4]), (float)(line[5])])
			perurbs.append([(int)(line[4]), (float)(line[6])])
			count = count + 1

		else:
			gdps.append([(int)(line[4]), (float)(line[5])])
			perurbs.append([(int)(line[4]), (float)(line[6])])
			count = count + 1

			if count == 46:
				count = 0
				countries = countries + 1

				json_data[name] = [region, subregion, gdps, perurbs]
				# json_data.append("{\"name\": \"" + name + "\", \"region\" : \"" + region + "\", \"subregion\" : \"" + subregion + "\", \"income\" : " + str(gdps) + ", \"population\" : " + str(perurbs) + ", \"lifeExpectancy\" : " + str(food) + "}")

				# json_data.append({'a_name': name, 'b_region' : region, 'c_subregion' : subregion, 'd_gdp' : gdps, 'e_perurb' : perurbs, 'f_food' : food})

				# json_data = "{\"name\": \"" + name + "\", \"region\" : \"" + region + "\", \"subregion\" : \"" + subregion + "\", \"income\" : " + str(gdps) + ", \"population\" : " + str(perurbs) + ", \"lifeExpectancy\" : " + str(food) + "}"
				# outfile.write(json_data + ",")

				# print countries
				# print gdps
				# print perurbs
				# print countries
				# print name
				# print len(gdps)
				# print "-------------------------------------"

				# print json_data

				gdps = []
				perurbs = []
				food = []

# print len(json_data)
print len(food_metadata)

# print food_metadata

with open("aquatic.json", "w") as outfile:
	outfile.write("[")

	for food in food_metadata:
		print str(food_metadata[food])

		if food in json_data:
			print str(json_data[food][3])
			json_string = "{\"name\": \"" + food + "\", \"region\" : \"" + json_data[food][0] + "\", \"subregion\" : \"" + json_data[food][1] + "\", \"income\" : " + str(json_data[food][2][0:41]) + ", \"population\" : " + str(json_data[food][3][0:41]) + ", \"lifeExpectancy\" : " + str(food_metadata[food]) + "}"
			print json_string + "\n"

# 				# json_data.append({'a_name': name, 'b_region' : region, 'c_subregion' : subregion, 'd_gdp' : gdps, 'e_perurb' : perurbs, 'f_food' : food})

# 				# json_data = "{\"name\": \"" + name + "\", \"region\" : \"" + region + "\", \"subregion\" : \"" + subregion + "\", \"income\" : " + str(gdps) + ", \"population\" : " + str(perurbs) + ", \"lifeExpectancy\" : " + str(food) + "}"
			outfile.write(json_string + ",")

# 				print countries
				
	outfile.write("]")

# with open("gdp_json.json", "w") as outfile:
#   json.dump(json_data, outfile)

# name
# region
# subregion
# gdp
# perurb
