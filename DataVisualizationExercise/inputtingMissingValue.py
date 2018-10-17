import csv
import matplotlib.pyplot as plt
import statistics as st

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)


    wr = open("newDataSet.csv", "w")

    wr.write(str(header[0]) + "," + str(header[1]) + "," + str(header[2]))
    wr.write("\n")

    n = 0
    for row in reader:
        if(row[0] == "NA"):
            row[0] = 0
            n += 1

        wr.write(str(row[0]) + "," + str(row[1]) + "," + str(row[2]))
        wr.write("\n")

    wr.close()

    print("The total numbers of missing values in dataset is : " + str(n))

    print()
    print("New dataset created successfully")



newfilename = 'newDataSet.csv'
with open(newfilename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dict = {}
    dictInterval = {}
    for row in reader:
        steps = row[0]

        if(steps != "NA"):
            date = row[1]

            interval = int(row[2])

            dict.setdefault(str(date), [])
            dict[str(date)].append(int(steps))

            dictInterval.setdefault(interval, [])
            dictInterval[interval].append(int(steps))


    # print(len(dict.keys()))

    listDate = []
    listTotal  = []
    listAvg = []
    # listMean = []
    # listMedian = []
    for i in dict.keys():
        listDate.append(i)
        listTotal.append(sum(dict.get(i)))
        listAvg.append(st.mean(dict.get(i)))

    plt.hist(listTotal)
    plt.title("Total Steps per day")
    plt.xlabel("Steps per day")
    plt.ylabel("Frequency")
    plt.yticks(range(0, 25, 5))
    plt.savefig('figure3(inputting missing values).svg')
    plt.close()
