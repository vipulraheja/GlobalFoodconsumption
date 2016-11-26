import csv

with open("FAO_data_raw.csv","rb") as f1:
		f1.next()
		fao_data = csv.reader(f1, delimiter=" ", skipinitialspace=True)
		
		count = 0
		for line in fao_data:
			if count >= 111 and count < 152:
				print str(count) + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4]
				count = count + 1

			else:
				if count == 968:
					count = 0
				else:
					count = count + 1