import sys
import os,re
import datefinder


def main():
	count = 0
	filepath = sys.argv[1]

	if not os.path.isfile(filepath):
		print("File path does not exist... !")
		sys.exit()

	with open(filepath) as fp:
		#count = 0
		for line in fp:
			if ("thanks" in line.lower()):
				print("End of File...")
				sys.exit()

			if ("buyer" in line.lower()):
				Buyer = line.partition(':')
				print("Buyer:",Buyer[2])
			
			if ("cargo" in line.lower()):
				Cargo = line.partition(':')
				print("Cargo:",Cargo[2]) 

			if ("quantity" in line.lower()):
				Quantity = line.partition(':')
				data = Quantity[2].lower()
				d=data.replace("'","")
				if 'bb' or 'mt' in d:
					s = d.split(' ')
					Type = s[2]
					print("Type:",Type)
					Quan = s[1]
					print("Quantity:",Quan)
					print('Option : seller') if "sellers" in s else print('Option : buyers')
					Tolerance = s[4]
					print("Tolerance:",Tolerance)

			if ('terms' in line.lower()):
				method = line.partition(':')
				terms_data = method[2].split(" ")
				terms_data1 =terms_data[1].lower()
				print("CFR") if "cfr" in terms_data1 else print("FOB") 
				terms_data2 = terms_data[2]
				print("Port name:",terms_data2)

			
			if ('delivery' in line.lower()) and count == 0:
				count += 1
				deleivery = line.partition(':')
				
				date_data = deleivery[2].split("to")
				print(date_data)
				laycan_from = date_data[1].replace(',',"")
				laycan_to = date_data[0].replace(',',"")

				print("laycan_to:",laycan_to)
				print("laycan_from",laycan_from)

				narrow = deleivery[2].split(" narrowed down")
				narrow_day = narrow[1]
				#print("s:",narrow_day)
				narr_date = narrow_day.split('by')[1]
				narr_down = re.findall("\d+", narrow_day)[0]
				
				print("narr_date:",narr_date)
				print("narr_down:",narr_down)
				


				

				


				


if __name__ == '__main__':
	main()