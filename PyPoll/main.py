import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

# Set variables 
count = 0
candidate_name = []
unique_candidate = []
vote_count = []
vote_percent = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    for row in csvreader:
        # Total number of votes
        count += 1
      
        candidate_name.append(row[2])       
    for x in set(candidate_name):
        unique_candidate.append(x)
        # i = total number of votes per candidate
        i = candidate_name.count(x)
        vote_count.append(i)
        # a = percent of total votes per candidate
        a = (i/count)*100
        vote_percent.append(a)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

    print("""
Election Results
    ---------------------
        """)
    print("Total Votes :" + str(count))    
    print("---------------------")
    for x in range(len(unique_candidate)):
                print(unique_candidate[x] + ": " + str(vote_percent[x]) +"% (" + str(vote_count[x])+ ")")
    print("---------------------")
    print("The winner is: " + winner)
    print("---------------------")

with open('PyPoll.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------\n")
    for x in range(len(set(unique_candidate))):
        text.write(unique_candidate[x] + ": " + str(vote_percent[x]) +"% (" + str(vote_count[x]) + ")\n")
    text.write("---------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------\n")



