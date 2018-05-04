import random


def data_interpret(data, feature):
    '''
    :param data: ALL OF THE DATA
    :param feature: The feature you want to consider (index)
    :return: The data interpret and given to the best hospital
    test age: 10-20
    '''

    hospital1 = []
    for sample in data:
        if 20 > sample[feature] > 10:
            hospital1.append(sample)

    for test in hospital1:
        if test[-1] == 0:
            pass
        else:
            hospital1.pop(hospital1.index(test))
    for i in range(600):
        hospital1.append(data[random.randint(1, len(data))])

    return hospital1


def compare_set(list1, data):
    hospital2 = []
    for i in range(len(list1)):
        hospital2.append(data[random.randint(1, len(data))])

    return hospital2


def generate_comb(exclude=None, death1=True):
    stage_of_disease = random.randint(1, 100) if exclude != 0 else None
    age = random.randint(0, 120) if exclude != 1 else None
    comorbidity = random.randint(1, 100) if exclude != 2 else None
    bmi = random.randint(1, 100) if exclude != 3 else None
    wealth = random.randint(1, 100) if exclude != 4 else None
    gender = random.choice([0, 100]) if exclude != 5 else None
    independency = random.choice([0, 50, 100]) if exclude != 6 else None
    smoke = random.choice([0, 100]) if exclude != 7 else None
    education = random.choice([0, 20, 40, 60, 80, 100]) if exclude != 8 else None
    race = random.choice([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) if exclude != 9 else None
    death = random.choice([0, 100])
    if death1:
        return [stage_of_disease, age, comorbidity, bmi, wealth, gender, independency, smoke, education, race, death]
    return [stage_of_disease, age, comorbidity, bmi, wealth, gender, independency, smoke, education, race]


def rand_data(number):
    '''
    :param number: The number of data you wanted to randomize
    :return data: The data list of list returned as the data framework


    # stage of disease, age, comorbidity, bmi, wealth, gender, independency, smoke, race, education, death
data = [\
    [23, 53, 26, 47, 10, 0, 50, 100, 0, [0,1,0,0], 1],
    [34, 23, 23, 16, 34, 0, 100, 100, 20, [1,0,0,0], 0],
    [75, 36, 84, 66, 30, 100, 50, 0, 40, [0,0,1,0], 1],
    [27, 72, 32, 84, 100, 100, 0, 100, 60, [0,0,0,1], 0],
    [84, 13, 75, 99, 30, 100, 100, 0, 100, [0,0,1,0], 0]]
    '''
    data = []
    for i in range(number):
        example = generate_comb()
        data.append(example)
    return data


def compare_hosp(feature_importance, hosp):
    index = 0
    ans = []
    for i in range(len(feature_importance)):
        if feature_importance[i] == max(feature_importance):
            index = i
    for hospital in hosp:
        ans.append(average(hospital)[index])

    return ans


def average(data):
    average = []
    for feature in range(9):
        feature_average = sum([sample[feature] for sample in data]) / len(data)
        average.append(feature_average)
    return average


def compare(A, B, no_feature):
    # compare current patient (A) and a sample patient in dataset (B) without given feature

    for feature in range(9):
        if feature != no_feature and abs(A[feature] - B[feature]) > 19:
            return False
    if no_feature != 9 and A[9] != B[9]:
        return False
    return True


def compare2(A, B, no_feature):
    for feature in range(9):
        if abs(A[no_feature] - B[no_feature]) > 1.1 and abs(A[feature] - B[feature]) > 19:
            return False
    if no_feature != 9 and A[9] != B[9]:
        return False
    return True


def calc_variance(dictionary):
    values = dictionary.values()
    mean = sum(values) / len(values)
    errors = [value - mean for value in values]
    variance = sum([i ** 2 for i in errors])
    return variance


patient = [80, 16, 70, 94, 33, 100, 100, 0, 100, [0, 0, 1, 0]]

data = rand_data(10000)
hospital1 = data_interpret(data, 1)
hospital2 = compare_set(hospital1, data)


##similar_1 = []
##similar_2 = []
##mortality_1 = 0
##mortality_2 = 0
##for i in range(len(data)):
##    if (compare2(patient, data[i], 1)):
##        similar_2.append(data[i])
##    if (compare(patient, data[i], 1)):
##        similar_1.append(data[i])
##
##for i in range(len(similar_1)):
##    mortality_1 += similar_1[i][-1]
##for j in range(len(similar_2)):
##    mortality_2 += similar_2[j][-1]
##
##mortality_1 /= len(similar_1)
##mortality_2 /= len(similar_2)
##
##rate_of_mort = mortality_1 / mortality_2
##if (rate_of_mort > 1.2):
##    print("Weak performance")
##elif (rate_of_mort < 0.8):
##    print("good performance")
##else:
##    print("Normal")


# calculate the importance of each feature for general patients
feature_importance = []
for feature in range(0, 10):
    combs = [generate_comb(exclude=feature, death1=False) for i in range(300)]
    mortality_age = {}
    for comb in combs:
        similar_m = []
        similar_age = []
        for sample in data:
            if compare(comb, sample, feature):
                similar_m.append(sample[-1])
                similar_age.append(sample[1])
        for i in range(len(similar_m)):
            mortality_age[similar_age[i]] = mortality_age.get(similar_age[i], 0) + 1
        # calculate the variance
    variance = calc_variance(mortality_age)
    feature_importance.append(variance)

            # BILL YOU WRITES HERE

            ##for feature in range(10):
            ##
            ##    # find similar patients in the dataset
            ##    similar = []
            ##    for sample in data:
            ##        if compare(patient, sample, feature):
            ##            similar.append(sample)
            ##
            ##    # calculate average mortality rate of this feature
            ##    total_mortality = 0
            ##    for sample in similar:
            ##        total_mortality += sample[-1]
            ##    total_mortality /= len(similar)
            ##
            ##    feature_importance.append(total_mortality)
            ##
            ##print(feature_importance)

