import pandas as pd

csv_path = "Resources/election_data.csv"

df = pd.read_csv(csv_path)

total_votes = df["Candidate"].count()

candidates = df["Candidate"].unique()

votes = df["Candidate"].value_counts()

votes_df = pd.DataFrame({"Candidate": candidates, "Total Votes": votes})

winner_df = votes_df.sort_values(["Total Votes"], ascending=False)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {round(votes_df.iloc[0, 1] / total_votes * 100, 3)}% ({votes_df.iloc[0, 1]})")
print(f"Correy: {round(votes_df.iloc[1, 1] / total_votes * 100, 3)}% ({votes_df.iloc[1, 1]})")
print(f"Li: {round(votes_df.iloc[2, 1] / total_votes * 100, 3)}% ({votes_df.iloc[2, 1]})")
print(f"O'Tooley: {round(votes_df.iloc[3, 1] / total_votes * 100, 3)}% ({votes_df.iloc[3, 1]})")
print("-------------------------")
print(f"Winner: {winner_df.iloc[0,0]}")
print("-------------------------")

output = open("electionResults.txt","w+")

output.write("Election Results \n")
output.write("------------------------- \n")
output.write(f"Total Votes: {total_votes} \n")
output.write("------------------------- \n")
output.write(f"Khan: {round(votes_df.iloc[0, 1] / total_votes * 100, 3)}% ({votes_df.iloc[0, 1]}) \n")
output.write(f"Correy: {round(votes_df.iloc[1, 1] / total_votes * 100, 3)}% ({votes_df.iloc[1, 1]}) \n")
output.write(f"Li: {round(votes_df.iloc[2, 1] / total_votes * 100, 3)}% ({votes_df.iloc[2, 1]}) \n")
output.write(f"O'Tooley: {round(votes_df.iloc[3, 1] / total_votes * 100, 3)}% ({votes_df.iloc[3, 1]}) \n")
output.write("------------------------- \n")
output.write(f"Winner: {winner_df.iloc[0,0]} \n")
output.write("-------------------------")