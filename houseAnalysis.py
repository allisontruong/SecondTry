import os
import mock_datasql
import sqlite3
import matplotlib.pyplot as plt

dbInfo = {}  # db related info dictionary

def get_files(dir):
    # Get current working directory
    saved_path = os.getcwd()
    # Change directories to where the data is:
    os.chdir(dir)
    file_list = os.listdir(dir)
    #print(file_list)
    all_list = [f for f in os.listdir(dir) if f[-4:] == ".csv"]
    print(all_list)
    # List over files
    count = 1
    for data_file in all_list:
        #print(data_file)
        with open(data_file, mode='rt', encoding='utf-8') as fd:
            for recline in fd:
                # Record Map:
                #  0    1     2     3     4      5         6
                # id,number,street,city,state,postalCode,price
                # rec[0] -> id, rec[1] -> streetNumber
                # rec[2] -> streetName, rec[3] -> City
                # rec[4] -> State, rec[5] -> zipcode, rec[6] -> housePrice

                # Clean records from newlines
                rec = recline.strip().split(',')
                # Exclude header files
                if rec[0] == "id":
                    continue
                # Eliminate leading zeros from street Number rec[1]
                rec[1] = int(rec[1])
                # Remove $ from price
                rec[6] = float(rec[6].replace("$",""))

                # Update counter to have a unique record Id

                rec[0] = count
                count += 1
                #print(rec)
                # Insert data

                mock_datasql.dynamic_data_entry(dbInfo, rec)
                if rec[0] % 100 == 0:
                    dbInfo['con'].commit()
        #Last commit
        dbInfo['con'].commit()
    # Change back to original dir
    os.chdir(saved_path)


def display_state_info(data):
    """
    Displays the number of homes per state
    :param data: Data structure with home information
    :return: nothing
    """
    state = {} # rec[4] for state info
    for rec in data:
        if rec[4] in state:
            state[rec[4]] += 1
        else:
            state[rec[4]] = 1
    #print(state)

    # Sort the data
    #print(sorted(state, key=state.get, reverse=True))
    s_state = sorted(state.items(), key=state.get(1))
    #print(s_state)
    # s_state = tuple(state.items())
    # for s in s_state:
    #     print(s)
    sname = []
    scount = []

    #for st, count in state.items():
    for st, count in s_state:
        sname.append(st)
        scount.append(count)
        #print(st, count)
    print(sname)
    print(scount)
    plt.plot(scount, sname)
    plt.show()


def main():

    # Connect to db
    dbInfo['con'] = sqlite3.connect('tutorial.db')
    # Create a cursor (interact with DB)
    dbInfo['cur'] = dbInfo['con'].cursor()
  #  mock_datasql.create_table(dbInfo)
    # Path to data
   # data_dir = r"D:\SecondTry\data"
    #get_files(data_dir)
    data = mock_datasql.read_data(dbInfo)
    # for rec in data:
    #     print(rec)

    display_state_info(data)

    # Clean
    dbInfo['cur'].close()
    dbInfo['con'].close()

if __name__ == '__main__':
    main()
    exit(0)
