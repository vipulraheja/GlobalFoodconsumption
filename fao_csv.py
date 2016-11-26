import csv
from collections import OrderedDict
import collections

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

					# print line[2]

					# if line[2] == "Alcoholic Beverages + (Total)":
					# 	if line[1] not in meat_list:
					# 		meat_list[line[1]] = {}
					# 		meat_list[line[1]][line[3]] = int(line[4])
					# 	else:
					# 		if line[3] not in meat_list[line[1]]:
					# 			meat_list[line[1]][line[3]] = int(line[4])

				else:
					if line[3] not in fao_list[line[1]]:
						fao_list[line[1]][line[3]] = int(line[4])

						# if line[2] == "Meat + (Total)":
						# 	meat_list[line[1]][line[3]] = int(line[4])

					else:
						fao_list[line[1]][line[3]] += int(line[4])

						# print line[2]

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

		print meat_list
		print fao_list['Afghanistan']

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
		# 		if meat_list[country][i] == 0:
		# 			meat_ratio[country][i] = 0
		# 			# print str(0) + ",", 
		# 		else:
		# 			meat_ratio[country][i] = fao_list[country][i]*1.0/meat_list[country][i] 
		# 			# print str(fao_list[country][i]*1.0/meat_list[country][i]) + ",", 

		# ordered_meat_ratio = {}
		# for country in meat_ratio:
		# 	temp_list = collections.OrderedDict(sorted(meat_ratio[country].items()))
		# 	dictlist = []
		# 	for key, value in temp_list.iteritems():
		# 		temp = [int(key),value]
		# 		dictlist.append(temp)
		# 	ordered_meat_ratio[country] = dictlist

		# print ordered_meat_ratio


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


		# print meat_list
# fao_strings = {}

# strings = {}
# cum = {}
# for key in fao_list:
# 	cum[key] = 0

# for key in fao_list:
# 	print fao_list[key]
# 	for i in range(0,19):
# 		# for key in fao_list:
# 		if key not in fao_strings:
# 			fao_strings[key] = ["{x: " + str((int)(key)-1970) + ", y: " + str(fao_list[key][i]) + ", y0: " + str(cum[key]) + "}"]
# 		else:
# 			fao_strings[key].append("{x: " + str((int)(key)-1970) + ", y: " + str(fao_list[key][i]) + ", y0: " + str(cum[key]) + "}")
# 		cum[key] += int(fao_list[key][i])

# fao_strings = collections.OrderedDict(sorted(fao_strings.items()))

# for j in range(0,len(fao_strings[str(key)])):
# 	print "[\n"
# 	for i in range(1970,2011):
# 		print fao_strings[str(i)][j] + ",\n"
# 	print "],\n"