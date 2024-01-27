import sys

def cat_shelter_data(datafile):
    '''Analyzing the cat's shelter log data and calculating the required statistics.
       
       Parameters:
       - datafile (str): Log file containing all the data about the cat's entry and exit time.
       
       Prints: 
       - Cat's visit
       - Other cat's visit
       - Our cat's total time in house
       - Average visit length
       - Longest visit
       - Shortest visit
    '''
    try:
        with open(datafile, 'rt') as file:
            lines = file.readlines()[:-1]

            our_cat_entries = 0
            their_cat_entries = 0
            our_cat_total_time = 0
            min_visit_time = float('inf') 
            max_visit_time = 0

            for line in lines:
                data = line.strip().split(',') #splits the line where 'comma' is present. (creates list)

                if len(data) != 3:
                    print(f"Skipping line with invalid number of data: {line}")
                    continue

                try:
                    type_of_cat, entry_time, exit_time = data #unpacking data


                    entry_time, exit_time = int(entry_time), int(exit_time) #type-casting (string to integer)
                    total_duration = exit_time - entry_time

                    if type_of_cat == 'OURS':
                        our_cat_entries += 1
                        our_cat_total_time += total_duration
                        min_visit_time = min(min_visit_time, total_duration)
                        max_visit_time = max(max_visit_time, total_duration)

                    elif type_of_cat == 'THEIRS':
                        their_cat_entries += 1

                except ValueError:
                    print(f"skipping non-numeric values: {line}") #skips the line with invalid data-type
                    continue

            if our_cat_entries == 0:
                print("No visits by our cat recorded.")
            else:
                avg_time = our_cat_total_time // our_cat_entries
                total_time_hour = our_cat_total_time // 60
                total_time_minutes = our_cat_total_time % 60
                
                #printing the data
                print(" Log File Analysis")   
                print("===================\n")
                print(f"Cat Visits: {our_cat_entries}")
                print(f"Other Cats: {their_cat_entries}")
                print(f"Total Time in House: {total_time_hour} Hours, {total_time_minutes} Minutes")
                print(f"Average Visit Length: {avg_time} Minutes")
                print(f"Longest Visit: {max_visit_time} Minutes")
                print(f"Shortest Visit: {min_visit_time} Minutes")

    except FileNotFoundError:
        print(f"Error!!! File '{datafile}' not found.")
    except:
        print("Error!!")

try:
    choice = sys.argv[1]
    cat_shelter_data(choice)
except IndexError:
    print("Error! Please provide the log file as a command-line argument.")
