# The data we need to retrieve 
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# Add our dependencies
import csv
import os

#Open the election results and read the file
#assign a variable for the file to load
file_to_load=os.path.join("Resources/election_results.csv")
open("election_results.csv","a+")
#create a filename variable to a direct path to the file
file_to_save=os.path.join("Analysis/election_analysis.txt")

#initialize a total vote counter
total_votes=0

#candidate options & candidate votes
candidate_options=[]
candidate_votes={}

#Track Winning: Candidate, vote Count, and percentage
winning_candidate=""
winning_count=0
winning_percentage=0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    
    #Read the header row
    headers = next(file_reader)
    
    #Loop/Print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        #Get the candidate name from each row which is located on the 3rd column (item 2 in python)
        candidate_name=row[2]
        #If the candidate does NOT match any existing candidate, add it to the candidate to list
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)       
            #And begin tracking that candidate's voter count
            candidate_votes[candidate_name]=0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1       

#Save the results to the text file
with open(file_to_save,"w") as txt_file:
    #Print the final vote count to the terminal
    election_results=(
        f"\nElection Results\n"
        f"---------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------------\n")
    print(election_results,end="")
    #Save the final vote count to the text file ####not doing this#####
    txt_file.write(election_results)
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    