import sys
import os,re
import datefinder


def main():
	count = 0
	filepath = sys.argv[1]

	if not os.path.isfile(filepath):
		print("File path does not exist... !")
		sys.exit()

	line_count = 0

	with open(filepath) as fp:
		
		for line in fp:
			line_count += 1
			if ("thanks" in line.lower()):
				print("End of File...")
				sys.exit()
			
			if ("buyer" in line.lower()):
				print("--------buyer----------")
				Buyer = line.partition(':')
				print("Buyer:",Buyer[2])
			
			if ("cargo" in line.lower()):
				print("--------cargo----------")
				Cargo = line.partition(':')
				print("Cargo:",Cargo[2]) 
			
			if ("quantity" in line.lower()):
				print("--------quantity----------")
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
				print("--------terms----------")
				method = line.partition(':')
				terms_data = method[2].split(" ")
				terms_data1 =terms_data[1].lower()
				print("CFR") if "cfr" in terms_data1 else print("FOB") 
				terms_data2 = terms_data[2]
				print("Port name:",terms_data2)

			
			if ('delivery' in line.lower()) and count == 0:
				print("--------delivery----------")
				count += 1
				deleivery = line.partition(':')
				
				date_data = deleivery[2].split("to")
				#print(date_data)
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


			if ('price' in line.lower()):
				print("--------price---------")
				pri = line.partition(":")
				pric = (pri[2].lower()).replace(" ","")
				if('mt' in pric):
					print("price unit field:mt")
				elif('bbl' in pric):
					print("price unit field:bbl")
				if('bl' in pric):
					print("invoice:BL")
				elif('out-turn' in pric):
					print("invoice:out-turn")
				else:
					print("invoice:BL")
				if('platts' in pric):
					print("Pricing basic:platts")
				elif('agurus' in pric):
					print("Pricing basic :agurus")
				elif('futures' in pric):
					print("Pricing basic : futures")
				else:
					print("Pricing basic:platts")

				discount = re.findall('\d+',pric)[0]

				if('plus' or '+' in pric):
					a="+"+str(discount)
					print("premium/discount :",a)

				elif('minus' or "-" in pric):
					a="-"+str(discount)
					print("premium/discount :",a)

				if('mean' in pric):
					tup = (pri[2].lower()).split(" ")
					inde = tup.index('mean')
					print("index:",inde)
					print("tup:",tup)
					for i in range(inde,0,-1):
						if(i == 4):
							check = str(tup[i-1])+" "+str(tup[inde])
							print(check)
							print("check with db if not break")
					for i in range(inde,0,-1):
						if (i == 4):
							check = str(tup[i-2])+" "+str(tup[i-1]+" "+str(tup[inde]))
							print(check)
							print("check with db")
						
			
			if ('pricing' in line.lower()):
				print("--------pricing----------")
				pricing_list=['after bl','around bl','before bl','after nor','around nor','before nor']
				price = str(line.lower())
				price_sp = price.partition(':')[2]
				string1 = (price_sp).replace(" ","")
				print('bl') if('bl' in string1) else('nor')
				if('after' in string1):
					print("after")
				elif('before' in string1):
					print("before")
				else:
					print("around")
				numbers = re.findall('\d+',price)
				price_list = price.split(' ')
				#print(price_list)
				print(numbers[0])

			
			if ('payment' in line.lower()):
				print("--------payment----------")
				print("line_count:",line_count)
				string2 = str(line.lower()).replace(" ","")
				if("standbylc" in string2):
					print("standby LC")
				elif( "documentary LC" in string2 ):
					print(" documentary LC")
				elif("open account" in string2):
					print("open account")
				n = string2.find("at")+2
				m=n
				#print("n:",n)
				for n in range(len(string2)):
					if string2[n].isdigit():
						m += 1
						break
				#print("m:",string2)
				credit = string2[n:m+1]
				print("credit:",credit)

				if ('bl' in string2):
					n = string2.find("bl")
					print(string2[n:n+2])
				else:
					n = string2.find("nor")
					print(string2[n:n+3])

				num = re.findall('\d+',string2)[1]
				string3 = "lctobeissued"
				str3_len =len(string3)
				issue = string2.find("lctobeissued")+str3_len
				m = issue+len(num)
				issued = string2[issue:m]
				print("issued:",issued)

				if("loading" in string2):
					print("loading")
				elif("delivery" in string2):
					print("delivery")
				elif("discharge" in string2):
					print("discharge")
				

			if ('delivery' in line.lower()):
				string = str(line.lower()).replace(" ","")

				if("loading" in string):
					print("loading")
				elif("delivery" in string):
					print("delivery")
				elif("discharge" in string):
					print("discharge")
				



			
	
			if ('demurrage' in line.lower()):
				print("--------demurrage----------")
				dem_list =[]
				dem = line.partition(':')
				demu = str(dem[2]).replace(' ',"")
				data_dem = demu.strip("\n")
				dem_list.append(data_dem)
				#print(dem_list)
				if ('charterparty' in dem_list) or('cp' in dem_list) or ('c/p' in dem_list):
					print("charter party")
			
			if ('laytime' in line.lower()):
				print("--------laytime----------")
				lay = line.partition(':')
				layt = str(lay[2])
				numbers = re.findall('\d+',layt)
				Laytime = numbers[0]
				print("Laytime:",Laytime)


				

				


				


if __name__ == '__main__':
	main()