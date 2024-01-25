
for row_number in range (1,10): # 9 rows, as 10 is excluded
    if row_number <= 5:
        number_of_stars = row_number # number of stars is ascending
    else:
        number_of_stars = 10 - row_number # number of stars is descending
    print("*" * number_of_stars)



  