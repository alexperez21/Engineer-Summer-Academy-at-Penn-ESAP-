
#The intro credits 
def print_intro():
  print("Congrats, you are the newest ruler of ancient Samaria, elected for \n"
"a ten year term of office. Your duties are to distribute food, direct \n"
"farming, and buy and sell land as needed to support your people. Watch out \n"
"for rat infestations and the resultant plague! Grain is the general currency, \n" 
"measured in bushels. The following will help you in your decisions: \n")
  print("(a) Each person needs at least 20 bushels of grain per year to survive.\n"
"(b) Each person can farm at most 10 acres of land. \n"
"(c) It takes 2 bushels of grain to farm an acre of land."
"(d) The market price for land fluctuates yearly. \n")
  print("Rule wisely and you will be showered with appreciation at the end of \n"
"your term. Rule poorly and you will be kicked out of office!\n")

#from document
def ask_to_buy_land(bushels, cost):
	acres = int(input("How many acres will you buy? (Enter 0 if you don't want to buy any.) \n"))
	while (acres * cost > bushels):
		print ("O great Hammurabi, we have but " , bushels, " bushels of grain!")
		acres = int(input("How many acres will you buy? "))
	return acres

def ask_to_sell_land(acres):
	acre = int(input("How many acres will you sell?\n"))
	while (acre > acres):
		print ("O great Hammurabi, we have but " , acres, " acres of land!")
		acre = int(input("How many acres will you sell?\n "))
	return acre

def ask_to_feed(bushels):
	bushel = int(input("How many bushels will you use for feeding?\n"))
	while bushel > bushels:
		print ("O great Hammurabi, we have but" , bushels, " bushels of grain!\n")
		bushel = int(input("How many bushels will you use for feeding?\n"))
	return bushel

def ask_to_cultivate(acres, population, bushels):
	acre = int(input("How much land will you plant seed in?\n"))
	while (population * 10 < acre):
		print("O great Hammurabi, we have but ", population, " people who can farm!")
		acre = int(input("How much land will you plant seed in?\n"))
		while ((acre *2) > bushels):
			print("O great Hammurabi, we have but ", bushels, " bushels of grain!")
			acre = int(input("How much land will you plant seed in?\n"))
			while(acre > acres):
				print("O great Hammurabi, we have but ", acres, " acres of land!")
				acre = int(input("How much land will you plant seed in?\n"))
	return acre

def is_plague():
	chance = random.randint(1, 100)
	if chance <= 15:
		return True
	else:
		return False

def num_starving(population, bushels):
	people_survive = bushels // 20
	if (people_survive < population):
		return population - people_survive
	else:
		return 0

def num_immigrants(land, grainInStorage, population, num_starving):
	if (num_starving > 0):
		return 0
	else:
		return int((20 * land + grainInStorage) /((100 * population) + 1))

def get_harvest():
	number = random.randint(1, 8)
	return number

def do_rats_infest():
	possibility = random.randint(1, 100)
	if (possibility <= 40):
		return (random.randint(1, 3)) / 10
	else:
		return 0

def price_of_land():
	return random.randint(16, 22)

def Hammurabi():

	starved = 0
	immigrants = 5
	population = 100
	harvest = 3000          # total bushels harvested
	bushels_per_acre = 3    # amount harvested for each acre planted
	rats_ate = 200          # bushels destroyed by rats
	bushels_in_storage = 2800
	acres_owned = 1000
	cost_per_acre = 19      # each acre costs this many bushels
	plague_deaths = 0


	print_intro()

	for year in range(1, 11):
		print("O great Hammurabi!\nYou are in year " + str(year) + " of your ten year rule.In the previous year " + str(int(starved)) + " people starved to death.\nIn the previous year " + str(int(immigrants)) + " people entered the kingdom.\nThe population is now " + str(int(population)) + ".\nWe harvested "+str(int(harvest)) + " bushels at " + str(int(bushels_per_acre)) + " bushels per acre.\nRats destroyed " + str(int(rats_ate)) + " bushels, leaving " + str(int(bushels_in_storage)) + " bushels in storage.\nThe city owns " +str(int(acres_owned)) + " acres of land.Land is currently worth " + str(int(cost_per_acre)) + " bushels per acre.\nThere were " + str(int(plague_deaths)) + " deaths from the plague.")

		land_bought = ask_to_buy_land(bushels_in_storage, cost_per_acre)
		if (land_bought != 0):
			bushels_in_storage -= land_bought * cost_per_acre
			acres_owned += land_bought
		else:
			land_sold = ask_to_sell_land(acres_owned)
			bushels_in_storage += land_sold * cost_per_acre
			acres_owned -= land_sold

		bushel_to_feed = ask_to_feed(bushels_in_storage)
		bushels_in_storage -= bushel_to_feed

		bushels_per_acre = get_harvest()
		harvest = ask_to_cultivate(acres_owned, population, bushels_in_storage) *bushels_per_acre
		bushels_in_storage = bushels_in_storage + harvest 

		if(is_plague()):
			plague_deaths = int(population / 2)
			population -= plague_deaths

		starved = num_starving(population, bushel_to_feed)
		if (float(starved) > (population * 0.45)):
			print("Due to this extreme mismanagement, you have not only been impeached and thrown out of office, but you have also been declared 'National Fink'!!")
			break
		else:
			population = population - starved
		immigrants = num_immigrants(acres_owned, bushels_in_storage, population, starved)
		population += immigrants

		rats_ate = bushels_in_storage * do_rats_infest()
		bushels_in_storage -= rats_ate

		cost_per_acre = price_of_land()

		int(population)
		int(bushels_in_storage)
		int(acres_owned)
		
		if year==10:
			print("O great Hammurabi, YOU MADE IT! CONGRATS YOU WON")
			print("Your kingdom has " + population + "people, " + bushels_in_storage + " bushels in storage, and " + acres_owned + "acres owned. GOOD JOB!!")

Hammurabi()
