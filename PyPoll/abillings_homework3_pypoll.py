import pandas as pd

csv_path = "Resources/election_data.csv"

df = pd.read_csv(csv_path)

total_votes = df["Candidate"].count()

candidates = df["Candidate"].unique()

votes = df["Candidate"].value_counts()

votes_df = pd.DataFrame({"Candidate": candidates, "Total Votes": votes})

winner_df = votes_df.sort_values(["Total Votes"], ascending=False)

count_row = winner_df.shape[0]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for i in range (count_row):
    print(f"{winner_df.iloc[i,0]}: {round(winner_df.iloc[i, 1] / total_votes * 100, 3)}% ({winner_df.iloc[i, 1]})")

print("-------------------------")
print(f"Winner: {winner_df.iloc[0,0]}")
print("-------------------------")

output = open("electionResults.txt","w+")

output.write("Election Results \n")
output.write("------------------------- \n")
output.write(f"Total Votes: {total_votes} \n")
output.write("------------------------- \n")

for i in range (count_row):
    output.write(f"{winner_df.iloc[i,0]}: {round(winner_df.iloc[i, 1] / total_votes * 100, 3)}% ({winner_df.iloc[i, 1]}) \n")

output.write("------------------------- \n")
output.write(f"Winner: {winner_df.iloc[0,0]} \n")
output.write("-------------------------")

output.close()