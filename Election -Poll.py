#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PyPoll
#incoporte the dependencies
import csv
import os

#file to load and out put
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

#total vote counter
total_votes = 0

#Candidate Options and voet counter
candidate_options = []
candidate_votes = {}

#winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0

#Read the csv and convert it into a list
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    #Read the header
    header = next(reader)
    
    for row in reader:
     #Run the loader animation 
        print(". " , end="")
        
    #Add to totla vote count
    total_vote_count = total_votes + 1
    
    #Extract the candidate name from each row
    candidate_name = row(2)
    
    # If the candidate does not match any existing candidate 
    #( in a way our loop is discovering candidates as it goes)
    
    if candidate_name not in candidate_options:
            # Add it to the list of candidate in the running
            candidate_options.append(candidate_name)
            
            #begin tracking that candidate voter count 
            candidate_voters[candidate_name] = 0
        
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:
    # print the final vote count
    
    election_results = (
        f"\n\nElection Results\n"
        f"---------------------\n"
        f"Total Votes:{total_votes}\n"
        f"------------------------\n"  
    )
print(election_results, end="")

# Save the file voet count to text file
txt_file.write(election_results)

#Determine the winner by looping through the counts
for candidate in candidate_votes:
     #Retrieve vote count and percentage
     votes = candiddate_votes.get(candidate)
     vote_percentage = float(votes) / float(total_votes) *100
    
    #Determine winning vote count and candidate
     if(votex > winning_count):
            winning_count = votes
            winning_candidate = candidate
    # print each cndidate's voter count and percentage to terminal
            voter_output = f"{candidate} : {vote_percentage: .3f}% ({vote}\n)"
    
            print(voter_output, end="")
    
            txt_file.write(voter_ouput)
    
    #print the winning candidates
     winning_candidate_summary = (
        f"--------------------\n"
        f"winner: {winnding_candidate}\n"
        f"-----------------------------\n"
    )
        
    print(winning_candidate_summary)
    
    #save the winning candidate name to text file
        txt_file.write(winning_candidate_summary)
    


# In[ ]:





# In[ ]:




