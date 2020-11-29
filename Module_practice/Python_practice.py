counties = ["Arapahoe", "Denver", "Jefferson"]

counties_dict = {"Arapahoe":422829, "Denver":463353,"Jefferson":432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": f'{422829:,}'},
                {"county":"Denver", "registered_voters": f'{463353:,}'},
                {"county":"Jefferson", "registered_voters": f'{432438:,}'}] 

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
