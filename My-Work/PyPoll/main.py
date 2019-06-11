import os
import csv

pypollCSV = os.path.join('Resources', 'election_data.csv')

with open(pypollCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    totalVotesCast = 0
    
    candidates = []

    for row in csvreader:

        totalVotesCast += 1
        
        if row[2] not in candidates:
            
            candidates.append(row[2])
            
with open(pypollCSV, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    candidate_one = candidates[0]
    total_c1 = 0
    
    candidate_two = candidates[1]
    total_c2 = 0
    
    candidate_three = candidates[2]
    total_c3 = 0
    
    candidate_four = candidates[3]
    total_c4 = 0
    
    for row in csvreader:
        
        if row[2] == candidate_one:
            
            total_c1 += 1
            
        elif row[2] == candidate_two:
            
            total_c2 += 1
            
        elif row[2] == candidate_three:
            
            total_c3 += 1
            
        elif row[2] == candidate_four:
            
            total_c4 += 1
            
percent_c1 = round(total_c1/totalVotesCast*100, 3)
percent_c2 = round(total_c2/totalVotesCast*100, 3)
percent_c3 = round(total_c3/totalVotesCast*100, 3)
percent_c4 = round(total_c4/totalVotesCast*100, 3)

if percent_c1 > percent_c2 and percent_c3 and percent_c4:
    
    winning_candidate = candidate_one
    
elif percent_c2 > percent_c3 and percent_c4:
    
    winning_candidate = candidate_two
    
elif percent_c3 > percent_c4:
    
    winning_candidate = candidate_three
    
else:
    
    winning_candidate = candidate_four
    
print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalVotesCast}')
print('-------------------------')
print(f'{candidate_one}: {percent_c1}% ({total_c1})')
print(f'{candidate_two}: {percent_c2}% ({total_c2})')
print(f'{candidate_three}: {percent_c3}% ({total_c3})')
print(f'{candidate_four}: {percent_c4}% ({total_c4})')
print('-------------------------')
print(f'Winner: {winning_candidate}')
print('-------------------------')

file = open('Election Results.txt', 'w')

file.write('Election Results\n')
file.write('-------------------------\n')
file.write(f'Total Votes: {totalVotesCast}\n')
file.write('-------------------------\n')
file.write(f'{candidate_one}: {percent_c1}% ({total_c1})\n')
file.write(f'{candidate_two}: {percent_c2}% ({total_c2})\n')
file.write(f'{candidate_three}: {percent_c3}% ({total_c3})\n')
file.write(f'{candidate_four}: {percent_c4}% ({total_c4})\n')
file.write('-------------------------\n')
file.write(f'Winner: {winning_candidate}\n')
file.write('-------------------------\n')

file.close()