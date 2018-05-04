# Random 80 hospitals
# Put data in the individual hospitals
# Find similar features of patients and historical data

import random
def rand_rand(number):
    '''
    :param number: The number of data you wanted to randomize
    :return data: The data list of list returned as the data framework
    # stage of disease, age, comorbidity, bmi, wealth, gender, independency, smoke, race, education, death
    '''
    
    data = []

    for i in range(number):
        stage_of_disease = random.randint(0,100)
        age = random.randint(0,100)
        comorbidity = random.randint(0,100)
        bmi = random.randint(0,100)
        wealth = random.randint(1,100)
        gender = random.choice([0,100])
        independency = random.choice([0,50,100])
        smoke = random.choice([0,100])
        education = random.choice([0,20,40,60,80,100])
        race = random.choice([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
        death = random.choice([0,100])
        data.append([stage_of_disease, age, comorbidity, bmi, wealth, gender, independency, smoke, education, race, death])
    return data


def rand_hospital(number = 80):
    # Check and work
    hospital_data = []
    for i in range(number):
        hospital_data.append([])
    for i in range(number):
        for k in rand_rand(30000):
            hospital_data[i].append(k)
    return hospital_data


# Regarding to each feature in the patient
# Find the correlated historical data and compute the mortality rate of the data

def find_similar(patient, hospital, feature):
    similar = []
    if feature < 5:
        for sample in hospital:
            if abs(sample[feature]-patient[feature]) < 10:
                similar.append(sample)
    if feature >= 5:
        for sample in hospital:
            if sample[feature] == patient[feature]:
                similar.append(sample)
    return similar

def hospital_mortality(number = 80):
    hospital_mortality = []
    for i in range(number):
        hospital_mortality.append([0,0,0,0,0,0,0,0,0,0])
    return hospital_mortality

def compute_mortality(list_of_similar, hospital, feature):
    # Compute mortality regarding the feature
    sum_mortality = 0
    for sample in list_of_similar:
        sum_mortality += sample[-1]
    sum_mortality /= len(list_of_similar)
    return sum_mortality
    # Store
    #hospital_mortality[hospital][feature] = sum_mortality

# Constant
patient = [80, 65, 70, 94, 33, 100, 100, 0, 100, [0, 0, 1, 0]]
hospital_mortality = hospital_mortality()

#mian
hospital_data = rand_hospital()

for hospital in range(len(hospital_data)):
    for feature in range(0,10):
        similar = find_similar(patient, hospital_data[hospital], feature)
        sum_mortality = compute_mortality(similar,hospital,feature)
        hospital_mortality[hospital][feature] = sum_mortality

