def get_gender(sex= 'Unknown'): #default value
    if sex is 'm':
        sex ="Male"
    elif sex is 'f':
        sex ="Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()