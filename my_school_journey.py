# using python input variable i want say something about my education journey so far
primary_start = input("The year i enter primary school: ")
primary_grad = input("my graduation year: ")

# all about my secondary school 
secondary_start = input("The year i enter secondary school: ")
secondary_grad = input("year i graduate from secondary school: ")

# my university level 
tertiary_level = input("The year i started my higher eduation level: ")

# years i spent in my primary school
primary_duration =  int(primary_grad) - int(primary_start)

# my secondary school year duration 
secondary_duration = int(secondary_grad) - int(secondary_start)

# my expected year of graduation from tertiary level 
tertiary_grad = int(tertiary_level) + 5

print(f"i started my primary school education in year {primary_start}, i spent {primary_duration} year in my primary school; i was opportune to quickly further my education at secondary level in year {secondary_start} and graduated in year {secondary_grad} ; i was so luckey to start my engineering career in one of the best university in nigeria , in the year {tertiary_level} and i am expected to graduate in the year {tertiary_grad}, if everything go well as plan. ")