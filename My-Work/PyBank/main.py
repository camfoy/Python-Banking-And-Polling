import os
import csv

pybankCSV = os.path.join('Resources', 'budget_data.csv')

with open(pybankCSV, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    nMonths = 0
    
    totalProfit = 0
    
    previousProfit = 0
    change = 0
    greatestIncrease = 0
    greatestDecrease = 0
    
    for row in csvreader:
        
        nMonths += 1

        totalProfit += int(row[1])

        if previousProfit == 0:
            previousProfit = int(row[1])

        diffProfit = int(row[1]) - previousProfit
        
        if diffProfit > greatestIncrease:
            
            greatestIncrease = diffProfit
            greatestIncreaseDate = str(row[0])
            
        elif diffProfit < greatestDecrease:
            
            greatestDecrease = diffProfit
            greatestDecreaseDate = str(row[0])
            
        change += diffProfit
            
        previousProfit = int(row[1])
        
    averageChange = (change)/(nMonths - 1)

print('Financial Analysis')
print('------------------')
print(f'Total months: {nMonths}')
print(f'Total: ${totalProfit}')
print(f'Average Change: ${averageChange}')
print(f'Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})')
print(f'Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})')

file = open('Financial Analysis.txt', 'w')

file.write('Financial Analysis\n')
file.write('------------------\n')
file.write(f'Total months: {nMonths}\n')
file.write(f'Total: ${totalProfit}\n')
file.write(f'Average Change: ${averageChange}\n')
file.write(f'Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})\n')
file.write(f'Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})\n')

file.close()