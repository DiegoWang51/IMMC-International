import csv
import random
import matplotlib.pyplot as plt

def compare(A, B, no_feature):
    # compare current patient (A) and a sample patient in dataset (B) without given feature

    for feature in range(9):
        if feature != no_feature and abs(A[feature] - B[feature]) > 10:
            return False
    if no_feature != 9 and A[9] != B[9]:
        return False
    return True
  
def rand_sample(number, patient):
    '''
    :param number: The number of data you wanted to randomize
    :param patient: Read the characteristics of the patient inorder to produce data 
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
        stage_of_disease = random.randint(patient[0]-5, patient[0]+5)
        age = random.randint(0, 100)
        comorbidity = random.randint(patient[2]-5, patient[2]+5)
        bmi = random.randint(patient[3]-5, patient[3]+5)
        wealth = random.randint(patient[4]-5, patient[4]+5)
        gender = patient[5]
        independency = patient[6]
        smoke = patient[7]
        education = patient[8]
        race = patient[9]
        death = random.random()
        if age < 10:
            death = 100 if death < 0.08 else 0
        elif age < 20:
            death = 100 if death < 0.03 else 0
        elif age < 30:
            death = 100 if death < 0.04 else 0
        elif age < 40:
            death = 100 if death < 0.06 else 0
        elif age < 50:
            death = 100 if death < 0.08 else 0
        elif age < 60:
            death = 100 if death < 0.11 else 0
        elif age < 70:
            death = 100 if death < 0.13 else 0
        elif age < 80:
            death = 100 if death < 0.16 else 0
        elif age < 90:
            death = 100 if death < 0.19 else 0
        elif age < 100:
            death = 100 if death < 0.26 else 0
        else:
            death = 100 if death < 0.33 else 0
        data.append([stage_of_disease, age, comorbidity, bmi, wealth, gender, independency, smoke, education, race, death])


    return data
  
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
        death = random.random()
        if age < 10:
            death = 100 if death < 0.08 else 0
        elif age < 20:
            death = 100 if death < 0.03 else 0
        elif age < 30:
            death = 100 if death < 0.04 else 0
        elif age < 40:
            death = 100 if death < 0.06 else 0
        elif age < 50:
            death = 100 if death < 0.08 else 0
        elif age < 60:
            death = 100 if death < 0.11 else 0
        elif age < 70:
            death = 100 if death < 0.13 else 0
        elif age < 80:
            death = 100 if death < 0.16 else 0
        elif age < 90:
            death = 100 if death < 0.19 else 0
        elif age < 100:
            death = 100 if death < 0.26 else 0
        else:
            death = 100 if death < 0.33 else 0
        data.append([stage_of_disease, age, comorbidity, bmi, wealth, gender, independency, smoke, education, race, death])
    return data


def rand_rand(number):
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


def calc_variance(l):
    mean = sum(l) / len(l)
    error = [i - mean for i in l]
    var = sum([err**2 for err in error])
    return var


print('start')
##patient = [80, 65, 70, 94, 33, 100, 100, 0, 100, [0, 0, 1, 0]]
##data = rand_sample(10000, patient)
##similar = []
##
##for i in range(len(data)):
##    if compare(patient,data[i],1):
##        similar.append(data[i])
##
##
####Graph 2
##mortality = [0 for i in range(101)]
##people = [0 for i in range(101)]
##
##for sample in similar:
##    mortality[sample[1]] += sample[-1]
##    people[sample[1]] += 1 # add a person
##
##ratio = [mortality[i] / people[i] for i in range(len(mortality))]
##plt.plot([i for i in range(0, 101)], ratio)
##plt.xlabel('age / year')
##plt.ylabel('mortality')
##
##plt.show()


print('3')
# Graph 3 嘿嘿
patients = rand_data(500)
similar1 = [rand_sample(random.randint(3000, 3600), patient) for patient in patients]
print('3.2')
similar2 = [rand_sample(random.randint(3000, 3600), patient) for patient in patients]
similar3 = [rand_sample(random.randint(3000, 3600), patient) for patient in patients]
similar4 = [rand_sample(random.randint(3000, 3600), patient) for patient in patients]
similar5 = [rand_rand(random.randint(3000, 3600)) for patient in patients]
similar6 = [rand_rand(random.randint(3000, 3600)) for patient in patients]
similar7 = [rand_sample(random.randint(3000, 3600), patient) for patient in patients]
similar8 = [rand_sample(random.randint(3000, 3600), patient) for patient in patients]
similar9 = [rand_rand(random.randint(3000, 3600)) for patient in patients]
similar10 = [rand_rand(random.randint(3000, 3600)) for patient in patients]

print('de')
# de_noise
rate_num = 0
all_var = []
similars = [similar1, similar2, similar3, similar4, similar5, similar6, similar7, similar8, similar9, similar10]
for similar in similars:
    ratios = []
    for i in range(500):

        mortality = [0 for i in range(101)]
        people = [0 for i in range(101)]

        for sample in similar[i]:
            mortality[sample[1]] += sample[-1]
            people[sample[1]] += 1 # add a person

        ratio = [mortality[i] / people[i] for i in range(len(mortality))]
        ratios.append(ratio)
##        plt.plot([i for i in range(101)], ratio)
##        plt.xlabel('age / year')
##        plt.ylabel('mortality')
##        plt.title('mortality-age before summation -- picture {}'.format(i))
##        plt.show()
    all_ratio = [0 for i in range(101)]
    for ratio in ratios:
        all_ratio = [all_ratio[i] + ratio[i] for i in range(101)]
        
    f = open('/Users/wlt/Desktop/mort_rate{}.csv'.format(rate_num), 'w')
    wter = csv.writer(f)
    wter.writerow(ratios)
    f.close()
    rate_num += 1
##    plt.plot([i for i in range(101)], all_ratio)
##    plt.xlabel('age / year')
##    plt.ylabel('total mortality')
##    plt.title('mortality-age after summation')
##    plt.show()
    var = calc_variance(all_ratio) / 10000
    all_var.append(var)

print('4')
# 4 ~ 7
all_lambda = []
patient = [80, 65, 70, 94, 33, 100, 100, 0, 100, [0, 0, 1, 0]]

for feature in range(10):
    pool = rand_sample(random.randint(3000, 3600), patient)
    similar_mortality = 0
    all_mortality = 0
    for sample in pool:
        if patient[1] - 5 < sample[1] < patient[1] + 5:
            similar_mortality += sample[-1]
        all_mortality += sample[-1]
    _lambda = similar_mortality / all_mortality
    all_lambda.append(_lambda)


f = open('/Users/wlt/Desktop/similar.csv', 'w')
wter = csv.writer(f)
for i in similar[0]:
    wter.writerow(i)
f.close()


print('hosp')
# Random 80 hospitals
# Put data in the individual hospitals
# Find similar features of patients and historical data


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

hospital_score = []
for mortality in hospital_mortality:
    hospital = sum([mortality[i] * all_lambda[i] * all_var[i] for i in range(len(mortality))])
    hospital_score.append([mortality, all_lambda, all_var, hospital])


f = open('/Users/wlt/Desktop/hosp_data.csv', 'w')
wter = csv.writer(f)
for line in hospital_score:
    wter.writerow(line)
f.close()

print('end')
