import sys
import os,re
import datefinder
import mysql.connector

hostname = 'localhost'
username = 'root'
password = 'saitest'
database = 'Trade'

def priceUnit(data):
	try:
		cursor.execute("INSERT INTO TRADE1 ('PriceUnitField') VALUES (%s,data);")
		record = cursor.fetchone()
		print("priceUnit:",record)
	except Exception as e:
		print("the Exception is:",e)

def invoiceQuantity(data):
	try:
		cursor.execute("INSERT INTO TRADE1 ('InvoiceQuantity') VALUES (%s,data);")
		record = cursor.fetchone()
		print("invoiceQuantity:",record)
	except Exception as e:
		print("the Exception is:",e)

def pricingBasic(data):
	try:
		cursor.execute("INSERT INTO TRADE1 ('PricingBasics') VALUES (%s,data);")
		record = cursor.fetchone()
		print("PricingBasics:",record)
	except Exception as e:
		print("the Exception is:",e)

def pricingBasicQuotaion(data):
	try:
	cursor.execute("SELECT PricingBasicQuotaion FROM TRADE1 WHERE LOWER(pricingBasicQuotaion) = data;")
		print("PricingBasicQuation:",record)
	except Exception as e:
		print("the Exception is:",e)

def premium_discount(data):
	try:
		cursor.execute("INSERT INTO TRADE1 ('PremiumDiscounr') VALUES (%s,data);")
		record = cursor.fetchone()
		print("PremiumDiscounr:",record)
	except Exception as e:
		print("the Exception is:",e)

def PricingBasics(data):
	try:
		cursor.execute("INSERT INTO TRADE1 ('PricingBasics') VALUES (%s,data);")
		record = cursor.fetchone()
		print("PricingBasics:",record)
	except Exception as e:
		print("the Exception is:",e)

def PaymentTerms(data):
	try:
		cursor.execute("SELECT PaymentTerms FROM TRADE1 WHERE LOWER(PaymentTerms) = data;")
		record = cursor.fetchone()
		print("PaymentTerms:",record)
	except Exception as e:
		print("the Exception is:",e)

def LCissuedbyfield(data):
	try:
		cursor.execute("SELECT LCissuedbyfield FROM TRADE1 WHERE LOWER(LCissuedbyfield) = data;")
		record = cursor.fetchone()
		print("LCissuedbyfield:",record)
	except Exception as e:
		print("the Exception is:",e)

def LCtobeIssued(data):
	try:
		cursor.execute("SELECT LCtobeIssued FROM TRADE1 WHERE LOWER(LCtobeIssued) = data;")
		record = cursor.fetchone()
		print("LCtobeIssued:",record)
	except Exception as e:
		print("the Exception is:",e)

def CreditFieldto(data):
	try:
		cursor.execute("INSERT INTO TRADE1 ('CreditFieldto') VALUES (%s,data);")
		record = cursor.fetchone()
		print("CreditFieldto:",record)
	except Exception as e:
		print("the Exception is:",e)

def CreditFieldfrom(data):
	try:
		cursor.execute("INSERT INTO TRADE1 ('CreditFieldfrom') VALUES (%s,data);")
		record = cursor.fetchone()
		print("CreditFieldfrom:",record)
	except Exception as e:
		print("the Exception is:",e)


def main():
	count = 0
	filepath = sys.argv[1]
	try:
		myConnection = mysql.connector.connect(host=hostname,user=username,passwd=password,db=database)
		if myConnection.is_connected():
			db_Info = myConnection.get_server_info()
			print("--------DATABASE INFO-----------")
			print("Connected to MySQL Server version ", db_Info)
			cursor = myConnection.cursor()
			cursor.execute("select database();")
			record = cursor.fetchone()
			print("You are connected to database: ", record)

	except Exception as e:
		print("Exception:",e)

	if not os.path.isfile(filepath):
		print("File path does not exist... !")
		sys.exit()

	line_count = 0

	with open(filepath) as fp:
		
		for line in fp:
			line_count += 1
			if ("thanks" in line.lower()):
				print("End of File...")
				myConnection.close()
				print("MySQL connection is closed")
				sys.exit()
			
			if ("buyer" in line.lower()):
				print("--------buyer----------")
				Buyer = line.partition(':')
				try:
					cursor.execute("SELECT Buyer FROM TRADE1 WHERE LOWER(Buyer) = Buyer[2];")
					record = cursor.fetchone()
					print("BUYER:",record)
				except Exception as e:
					print("the Exception is:",e)

				print("Buyer:",Buyer[2])
			
			if ("cargo" in line.lower()):
				print("--------cargo----------")
				Cargo = line.partition(':')
				try:
					cursor.execute("SELECT Cargo FROM TRADE1 WHERE LOWER(Cargo) = Cargo[2];")
					record = cursor.fetchone()
					print("Cargo:",record)
				except Exception as e:
					print("the Exception is:",e)
				print("Cargo:",Cargo[2]) 
			
			if ("quantity" in line.lower()):
				print("--------quantity----------")
				Quantity = line.partition(':')
				data = Quantity[2].lower()
				d=data.replace("'","")
				if 'bb' or 'mt' in d:
					s = d.split(' ')
					Type = s[2]
					Quan = s[1]
					Tolerance = s[4]
					print("Type:",Type)
					print("Quantity:",Quan)
					print("Tolerance:",Tolerance)
					if (Type == 'bb'):
						try:
							cursor.execute("INSERT INTO TRADE1 ('BBLQuantity') VALUES (%s,s[1]);")
							record = cursor.fetchone()
							print("Quantity:",record)
						except Exception as e:
							print("the Exception is:",e)

					elif(Type == 'mt'):
						try:
							cursor.execute("INSERT INTO TRADE1 ('SellerOption') VALUES ("sellers")") if "sellers" in s else cursor.execute("INSERT INTO TRADE1 ('BuyerOption') VALUES ("Buyers")")
						except Exception as e:
							print("the Exception is:",e)
					
					try:
						cursor.execute("INSERT INTO TRADE1 ('Tollerence') VALUES (%s,Tollerence);")
						record = cursor.fetchone()
						print("Tollerence:",record)
					except Exception as e:
						print("the Exception is:",e)

						
			
			if ('terms' in line.lower()):
				print("--------terms----------")
				method = line.partition(':')
				terms_data = method[2].split(" ")
				terms_data1 =terms_data[1].lower()
				try:	
					cursor.execute("INSERT INTO TRADE1 ('FOB') VALUES(%s,terms_data1);")if "cfr" in terms_data1 else cursor.execute("INSERT INTO TRADE1 ('CFR') VALUES(%s,terms_data1);") 
					record = cursor.fetchone()
					print("FOB/CFR:",record)
				except Exception as e:
						print("the Exception is:",e)
				terms_data2 = terms_data[2]
				try:	
					cursor.execute("INSERT INTO TRADE1 ('PortName') VALUES(%s,terms_data[2]);")
					record = cursor.fetchone()
					print("PortName:",record)
				except Exception as e:
						print("the Exception is:",e)
				print("Port name:",terms_data2)

			
			if ('delivery' in line.lower()) and count == 0:
				print("--------delivery----------")
				count += 1
				deleivery = line.partition(':')
				
				date_data = deleivery[2].split("to")
				#print(date_data)
				laycan_from = date_data[1].replace(',',"")
				laycan_to = date_data[0].replace(',',"")

				try:	
					cursor.execute("INSERT INTO TRADE1 ('LaycanFrom') VALUES(%s,laycan_from);")
				except Exception as e:
						print("the Exception is:",e)

				try:	
					cursor.execute("INSERT INTO TRADE1 ('LaycanTo') VALUES(%s,laycan_to);")
				except Exception as e:
						print("the Exception is:",e)
				print("laycan_to:",laycan_to)

				print("laycan_from",laycan_from)

				narrow = deleivery[2].split(" narrowed down")
				narrow_day = narrow[1]
				#print("s:",narrow_day)
				narr_date = narrow_day.split('by')[1]
				narr_down = re.findall("\d+", narrow_day)[0]

				try:	
					cursor.execute("INSERT INTO TRADE1 ('NarrowedDown') VALUES(%s,narr_down);")
				except Exception as e:
						print("the Exception is:",e)

				try:	
					cursor.execute("INSERT INTO TRADE1 ('NarrowedDownDate') VALUES(%s,narr_date);")
				except Exception as e:
						print("the Exception is:",e)
				
				print("narr_date:",narr_date)
				print("narr_down:",narr_down)


			if ('price' in line.lower()):
				print("--------price---------")
				pri = line.partition(":")
				pric = (pri[2].lower()).replace(" ","")
				if('mt' in pric):
					priceUnit(data=mt)
					print("price unit field:mt")
				elif('bbl' in pric):
					priceUnit(data=bbl)
					print("price unit field:bbl")
				if('bl' in pric):
					invoiceQuantity(data=bl)
					print("invoice:BL")
				elif('out-turn' in pric):
					invoiceQuantity(data=out-turn)
					print("invoice:out-turn")
				else:
					invoiceQuantity(data=bl)
					print("invoice:BL")
				if('platts' in pric):
					pricingBasic(data=platts)
					print("Pricing basic:platts")
				elif('agurus' in pric):
					pricingBasic(data=agurus)
					print("Pricing basic :agurus")
				elif('futures' in pric):
					pricingBasic(data=futures)
					print("Pricing basic : futures")
				else:
					pricingBasic(data=platts)
					print("Pricing basic:platts")

				discount = re.findall('\d+',pric)[0]

				if('plus' or '+' in pric):
					a="+"+str(discount)
					premium_discount(data=a)
					print("premium/discount :",a)

				elif('minus' or "-" in pric):
					a="-"+str(discount)
					premium_discount(data=a)
					print("premium/discount :",a)

				if('mean' in pric):
					tup = (pri[2].lower()).split(" ")
					inde = tup.index('mean')
					#print("index:",inde)
					print("pricing basic quotation bill")
					for i in range(inde,0,-1):
						if(i == 4):
							check = str(tup[i-1])+" "+str(tup[inde])
							print(check)
							pricingBasicQuotaion(data=check)
							print("check with db if not break")
					for i in range(inde,0,-1):
						if (i == 4):
							check = str(tup[i-2])+" "+str(tup[i-1]+" "+str(tup[inde]))
							print(check)
							pricingBasicQuotaion(data=check)
							print("check with db")
						
			
			if ('pricing' in line.lower()):
				print("--------pricing----------")
				pricing_list=['after bl','around bl','before bl','after nor','around nor','before nor']
				price = str(line.lower())
				price_sp = price.partition(':')[2]
				string1 = (price_sp).replace(" ","")
				print('bl') if('bl' in string1) else('nor')
				if('after' in string1):
					PricingBasics(data=string1)
					print("after")
				elif('before' in string1):
					PricingBasics(data=string1)
					print("before")
				else:
					PricingBasics(data="around")
					print("around")
				numbers = re.findall('\d+',price)
				price_list = price.split(' ')
				print(numbers[0])
				try:	
					cursor.execute("INSERT INTO TRADE1 ('PricingQuotes') VALUES(%s,price_list);") 
					record = cursor.fetchone()
					print("PricingQuotes:",record)
				except Exception as e:
						print("the Exception is:",e)


				

			
			if ('payment' in line.lower()):
				print("--------payment----------")
				print("line_count:",line_count)
				string2 = str(line.lower()).replace(" ","")
				if("standbylc" in string2):
					PaymentTerms(data=string2)
					print("standby LC")
				elif( "documentary LC" in string2 ):
					PaymentTerms(data=string2)
					print(" documentary LC")
				elif("open account" in string2):
					PaymentTerms(data=string2)
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
				CreditFieldto(data=credit)
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
				CreditFieldfrom(data=issued)
				print("issued:",issued)

				if("loading" in string2):
					LCissuedbyfield(data=delivery)
					print("loading")
				elif("delivery" in string2):
					LCissuedbyfield(data=delivery)
					print("delivery")
				elif("discharge" in string2):
					LCissuedbyfield(data=discharge)
					print("discharge")
				

			if ('delivery' in line.lower()):
				string = str(line.lower()).replace(" ","")

				if("loading" in string):
					LCissuedbyfield(data=loading)
					print("loading")
				elif("delivery" in string):
					LCissuedbyfield(data=delivery)
					print("delivery")
				elif("discharge" in string):
					LCissuedbyfield(data=discharge)
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
					try:	
						cursor.execute("INSERT INTO TRADE1 ('Demaurrage') VALUES(data_dem);")
					except Exception as e:
						print("the Exception is:",e)
			
			if ('laytime' in line.lower()):
				print("--------laytime----------")
				lay = line.partition(':')
				layt = str(lay[2])
				numbers = re.findall('\d+',layt)
				Laytime = numbers[0]
				try:	
					cursor.execute("INSERT INTO TRADE1 ('Laytime') VALUES(Laytime);")
				except Exception as e:
						print("the Exception is:",e)
				print("Laytime:",Laytime)

	

if __name__ == '__main__':
	main()