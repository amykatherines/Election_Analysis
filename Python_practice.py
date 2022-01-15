


# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")



# # what is the score?
# score = int(input("What is your test score? "))

# #grade
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# counties = ["Arapahoe", "Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])



# d = {'1':'a','2':'b','3':'c','4':'d'}
# print(d.values(),type(d.values()))


# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# voting_data.insert(2,{"county":"El Paso", "registered_voters": 461149})
# print(voting_data)
# print(len(voting_data))
# voting_data[0] = voting_data[0]
# voting_data.append({"count":"Arapahoe", "registered_voters":422829})
# print(voting_data)


# # county_index = voting_data.index("county":"Arapahoe")
# county_index = voting_data.index("Arapahoe")
# print (county_index)
# num_rows = len(voting_data)
# print(num_rows)

#counties.insert(2, 'Denver')



# print(voting_data)
#dictionaries
# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353

# counties_dict["Jefferson"] = 432438
# print (len(counties_dict))

# print(counties_dict.items())
# print(counties_dict.keys())
# print(counties_dict.values())
# print(counties_dict.get("Denver"))
# print (counties_dict)
# print (counties_dict["Arapahoe"])


# counties_tuple = ("Arapahoe","Denver","Jefferson")

# # length of tuple
# print (len(counties_tuple))
# print (counties_tuple[1])

# counties = ["Arapahoe","Denver","Jefferson"]
# counties.insert(1, "El Paso")
# counties.remove("Arapahoe")
# counties.remove('Denver')
# counties.insert(2, 'Denver')
# counties.append("Arapahoe")
# print(counties)


# print (counties [-1])
# print (len(counties))
# counties.append("El Paso")


# counties.insert(2, "El Paso")

# counties.remove("El Paso")
# print(counties)

# print(counties.pop(3))
# print(counties)

# counties[2] = "El Paso"
# print(counties)

# print("Hello World")

# #practice determining the data type
# result=type(2019)
# print (result)

# #tuple type
# ballots = 1,341
# print (type(ballots))

# print(type(''))

# print (type(True))

# print("5 + 2 * 3")
# print(5+2*3)

# print("8 // 5 - 3")
# print(8 // 5 - 3)

# print("8 + 22 * 2 - 4")
# print(8 + 22 * 2 - 4)

# print("16 - 3 / 2 + 7 - 1")
# print(16 - 3 / 2 + 7 - 1)

# print("3 ** 3 % 5")
# print(3 ** 3 % 5)

# print("5 + 9 * 3 / 2 - 4")
# print(5 + 9 * 3 / 2 - 4)


# # for loops
# counties = ["Arapahoe", "Denver","Jefferson"]
# for county in counties:
#     print(county)

# numbers = [0,1,2,3,4]
# for num in numbers:
#     print(num)

# # for loop to loop throuh a set number of times
# for num in range(5):
#     print(num)

# # while loop
# x = 0
# while x <=5:
#     print(x)
#     x=x+1


# # for loop to lop through the list for the number of values in it 
# counties = ["Arapahoe", "Denver","Jefferson"]
# for i in range(len(counties)):
#     print(counties[i])


# # # iterate through  dictionary keys and values for loops

# counties_dict = {"Arapahoe":422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# # When using the keys() method, it doesn't matter what variable name we use in the for loop. The keys() method will print each key in order.

# print("returns the key")
# for county in counties_dict.keys():
#     print(county)

# print ("Values Method")
# for voters in counties_dict.values():
#     print(voters)

# # Or
# print ("Key Index Method")
# for county in counties_dict:
#     print(counties_dict[county])

# # or
# print ("Get Method")
# for county in counties_dict:
#     print(counties_dict.get(county))


# # Get the Key-Value pair from a dictionary with a for loop
# # print variables and strings concatenated together
# counties_dict = {"Arapahoe":422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")



# # Iterating through a list of dictionaries with a FOR LOOP
# voting_data = [{"county":"Arapahoe","registered_voters":442829},
#              {"county":"Denver","registered_voters":463353},
#              {"county":"Jefferson","registered_voters":432438}]

# # prints the LIST OF DICTIONARIES
# for county_dict in voting_data:
#     print(county_dict)

# # prints all the dictionaries in the list using the range function
# for i in range(len(voting_data)):
#     print(voting_data[i])


# # prints only the counties in dictionaries using the range function 
# for i in range(len(voting_data)):
#     print(voting_data[i]["county"])


# # prints only the counties in dictionaries using the range function
# for i in range(len(voting_data)):
#     print(voting_data[i]['registered_voters'])


# Iterating through a list of dictionaries with a FOR LOOP
# voting_data = [{"county":"Arapahoe","registered_voters":442829},
#              {"county":"Denver","registered_voters":463353},
#              {"county":"Jefferson","registered_voters":432438}]

# # Nested For loop to print the values in the list of Dictionaries
# # prints VALUES only
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# # Loop to print just the values for the key "registered_voters" for all the dictionaries
# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

#     # prints the voter counts in dictionaries using the range function
# for i in range(len(voting_data)):
#     print(voting_data[i]['registered_voters'])


# # Loop to print just the values for the key "county" for all the dictionaries
# for county_dict in voting_data:
#     print(county_dict['county'])


# voting_data = [{"county":"Arapahoe","registered_voters":442829},
#              {"county":"Denver","registered_voters":463353},
#              {"county":"Jefferson","registered_voters":432438}]

# # dictionary 
# counties_dict = {"Arapahoe":422829, "Denver": 463353, "Jefferson": 432438}

# # print with concatenation
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# # print using the f-strings command
# for county, voters in counties_dict.items():
#     print(f"{county} count has {voters} registered voters.")

# write multiple sentences, calculation in an f-string, print to screen
# include precision for the numbers and commas for thousands seperators
# f'{value:{width},.{precision}}'
# candidate_votes = int(input("how many votes received?"))
# total_votes = int(input("how many total in election?"))
# message_to_candidate = (
#     f"you received {candidate_votes:,} votes. " # thousand separator
#     f"The total in election was {total_votes:,} . "
#     f"You received {candidate_votes / total_votes *100:.2f}% of the total votes")

# print(message_to_candidate)



#  # read from dictionary, print out formatted message 
# counties_dict = {"Arapahoe":422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")


voting_data = [{"county":"Arapahoe","registered_voters":442829},
             {"county":"Denver","registered_voters":463353},
             {"county":"Jefferson","registered_voters":432438}]


# Loop through the list of dictionaries and print the values for the named keys
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")
