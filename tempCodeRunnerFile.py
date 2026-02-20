
    for csv_file, row_count in row_counts.items():
        print(f'{csv_file}: {row_count} rows')
    print(f'Total data: {total_data} rows\n')



# Specify the folder path
Yogesh = 'C:\\Users\\ayank\\OneDrive\\Desktop\\mini project\\Data Collection\\Yogesh'
Lalit = 'C:/Users/ayank/OneDrive/Desktop/mini project/Data Collection/Lalit'
Ayan = 'C:/Users/ayank/OneDrive/Desktop/mini project/Data Collection/Ayan'


# call get_count function for each folder
get_count(Yogesh)
get_count(Lalit)
