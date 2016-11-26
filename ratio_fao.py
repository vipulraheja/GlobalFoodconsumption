from json import JSONEncoder
import json
import random
import csv
import collections

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


with open("FAO_data_raw.csv","rb") as f1:
		fao_data = csv.reader(f1, delimiter=" ", skipinitialspace=True)
		
		fao_list = {}
		meat_list = {}

		countries = 0
		count = 0

		for line in fao_data:
			# print line
			# print meat_list
			if count >= 1 and count < 50:
				if line[4] == 'NA':
					line[4] = 0
				if line[1] not in fao_list:
					fao_list[line[1]] = {}
					fao_list[line[1]][line[3]] = int(line[4])

					# if line[2] == "Meat + (Total)":
					# 	meat_list[line[1]] = {}
					# 	meat_list[line[1]][line[3]] = int(line[4])

				else:
					if line[3] not in fao_list[line[1]]:
						fao_list[line[1]][line[3]] = int(line[4])

						# if line[2] == "Meat + (Total)":
						# 	meat_list[line[1]][line[3]] = int(line[4])

					else:
						fao_list[line[1]][line[3]] += int(line[4])

						# if line[2] == "Alcoholic Beverages + (Total)":
						# 	if line[1] not in meat_list:
						# 		meat_list[line[1]] = {}
						# 		meat_list[line[1]][line[3]] = int(line[4])
						# 	else:
						# 		if line[3] not in meat_list[line[1]]:
						# 			meat_list[line[1]][line[3]] = int(line[4])

				# print str(count) + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4]
				count = count + 1

			else:
				# print count
				# print fao_list
				if count == 50:
					count = 0
				else:
					count = count + 1

		# fao_list = collections.OrderedDict(sorted(fao_list.items()))
		# for country in fao_list:
		# 	print '\n' + country + ",",
		# 	# print fao_list[country]
		# 	for i in collections.OrderedDict(sorted(fao_list[country].items())):
		# 		if meat_list[country][i] == 0:
		# 			print str(0) + ",", 
		# 		else:
		# 			print str(fao_list[country][i]*1.0/meat_list[country][i]) + ",", 


		# LIST = [REGION, SUBREGION, YEAR, VALUE]

		# fao_list = collections.OrderedDict(sorted(fao_list.items()))
		# meat_ratio = {}

		# for country in fao_list:
		# 	meat_ratio[country] = {}
		# 	# print "\n" + country
		# 	# print fao_list[country]
		# 	# print meat_list[country]
		# 	for i in collections.OrderedDict(sorted(fao_list[country].items())):
		# 		print fao_list[country][i]
		# 		if fao_list[country][i] == 0:
		# 			meat_ratio[country][i] = 0
		# 			# print str(0) + ",", 
		# 		else:
		# 			meat_ratio[country][i] = meat_list[country][i]*1.0/fao_list[country][i]*1.0
		# 			# print str(fao_list[country][i]*1.0/meat_list[country][i]) + ",", 

		# ordered_meat_ratio = {}
		# for country in meat_ratio:
		# 	temp_list = collections.OrderedDict(sorted(meat_ratio[country].items()))
		# 	dictlist = []
		# 	for key, value in temp_list.iteritems():
		# 		temp = [int(key),value]
		# 		dictlist.append(temp)
		# 	ordered_meat_ratio[country] = dictlist

		fao_list = collections.OrderedDict(sorted(fao_list.items()))
		meat_ratio = {}

		ordered_meat_ratio = {}
		for country in fao_list:
			temp_list = collections.OrderedDict(sorted(fao_list[country].items()))
			dictlist = []
			for key, value in temp_list.iteritems():
				temp = [int(key),value]
				dictlist.append(temp)
			ordered_meat_ratio[country] = dictlist

		print collections.OrderedDict(sorted(ordered_meat_ratio.items()))

		# print ordered_meat_ratio


with open("total_ratio.json", "w") as outfile:
	outfile.write("[")

	for food in food_metadata:
		print str(food_metadata[food])

		if food in json_data:
			print str(json_data[food][3])
			json_string = "{\"name\": \"" + food + "\", \"region\" : \"" + json_data[food][0] + "\", \"subregion\" : \"" + json_data[food][1] + "\", \"income\" : " + str(json_data[food][2][0:41]) + ", \"population\" : " + str(json_data[food][3][0:41]) + ", \"lifeExpectancy\" : " + str(ordered_meat_ratio[food]) + "}"
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
