def age_calculator(age, apples_ate, cig_smoked):
    answer = (100-age) + (apples_ate *3.5) + (cig_smoked *2)
    print(answer)

yash_data = [27, 20, 0]
#age_calculator(yash_data[0], yash_data[1], yash_data[2])

# Unpacking the arguments list
age_calculator(*yash_data)
