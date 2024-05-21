import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/main.csv'
with open(filename) as f:
    reader = csv.reader(f)      # it will read as list of strings, instead of directly read by f will result in whole as a single string
    header_row = next(reader)   # it consumes the first line as well.
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # Get high temperatures from the file
    highs,students,roll_num,dates,mins =[],[],[],[],[]
    for row in reader:
        current_date = datetime.strptime(row[-1],'%d/%m/%Y')
        try:
            high = int(row[5])
            low = int(row[3])
        except ValueError:
            print(f"Student {row[1]} with roll no. {row[2]} was absent in the exam.")
        else:
            students.append(row[1])
            roll_num.append(row[0])
            dates.append(current_date)
            highs.append(high)
            mins.append(low)

# Plot the high temperatures
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(roll_num,highs,c='red',alpha = 0.9)
ax.plot(roll_num,mins,c='blue',alpha = 0.9)
plt.fill_between(roll_num,highs,mins,facecolor='green',alpha=0.39)
                                        # The facecolor determines the color of shaded region, alpha is for transparency, 0=full
                                        # transparent and 1=fully opaque
plt.title("marks of students in "+header_row[5]+" and "+header_row[3]+" exam.", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Marks', fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()