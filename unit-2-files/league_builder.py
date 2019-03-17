import csv

if __name__ == '__main__':

    # empty lists
    experience_yes = []
    experience_no = []

    # function which splits two lists above into three groups
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))]
                for i in range(n)]

    # reads csv file
    with open('soccer_players.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # creats text file and writes data into it.
        with open('teams.txt', 'w', newline='') as new_file:

            # iterates over csv lines
            for line in csv_reader:
                del line[1]  # deletes Height columns
                if line[1] == 'YES':
                    experience_yes.append(line)  # appends data to empty list
                elif line[1] == 'NO':
                    experience_no.append(line)

            group1 = []
            group1.append(partition(experience_no, 3)[0])
            group1.append(partition(experience_yes, 3)[0])

            group2 = []
            group2.append(partition(experience_no, 3)[1])
            group2.append(partition(experience_yes, 3)[1])

            group3 = []
            group3.append(partition(experience_no, 3)[2])
            group3.append(partition(experience_yes, 3)[2])

            new_file.write('%s\n' % 'Sharks')
            new_file.write('%s\n' % '=======')
            new_file.write('%s\n' % ', '.join(group1[0][0]))
            new_file.write('%s\n' % ', '.join(group1[0][1]))
            new_file.write('%s\n' % ', '.join(group1[0][2]))
            new_file.write('%s\n' % ', '.join(group1[1][0]))
            new_file.write('%s\n' % ', '.join(group1[1][1]))
            new_file.write('%s\n' % ', '.join(group1[1][2]))

            new_file.write('%s\n' % ' ')
            new_file.write('%s\n' % ' ')

            new_file.write('%s\n' % 'Dragons')
            new_file.write('%s\n' % '=======')
            new_file.write('%s\n' % ', '.join(group2[0][0]))
            new_file.write('%s\n' % ', '.join(group2[0][1]))
            new_file.write('%s\n' % ', '.join(group2[0][2]))
            new_file.write('%s\n' % ', '.join(group2[1][0]))
            new_file.write('%s\n' % ', '.join(group2[1][1]))
            new_file.write('%s\n' % ', '.join(group2[1][2]))

            new_file.write('%s\n' % ' ')
            new_file.write('%s\n' % ' ')

            new_file.write('%s\n' % 'Raptors')
            new_file.write('%s\n' % '=======')
            new_file.write('%s\n' % ', '.join(group3[0][0]))
            new_file.write('%s\n' % ', '.join(group3[0][1]))
            new_file.write('%s\n' % ', '.join(group3[0][2]))
            new_file.write('%s\n' % ', '.join(group3[1][0]))
            new_file.write('%s\n' % ', '.join(group3[1][1]))
            new_file.write('%s\n' % ', '.join(group3[1][2]))
