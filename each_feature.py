import random
import matplotlib.pyplot as plt

a = [74, 13, 75, 99, 30, 100, 100, 0, 100, [0,0,1,0], 100]

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
        stage_of_disease = random.randint(1,100)
        age = random.randint(0,120)
        comorbidity = random.randint(1,100)
        bmi = random.randint(1,100)
        wealth = random.randint(1,100)
        gender = random.choice([0,100])
        independency = random.choice([0,50,100])
        smoke = random.choice([0,100])
        education = random.choice([0,20,40,60,80,100])
        race = random.choice([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
        death = random.random()
        if 0 <= age < 10:
            death = 100 if death < 0.11 else 0
        elif 10 <= age < 30:
            death = 100 if death < 0.03 else 0
        elif 30 <= age < 45:
            death = 100 if death < 0.08 else 0
        elif 45 <= age < 60:
            death = 100 if death < 0.13 else 0
        elif 60 <= age < 80:
            death = 100 if death < 0.17 else 0
        else:
            death = 100 if death < 0.23 else 0
    
            
        data.append([stage_of_disease, age, comorbidity, bmi, wealth, gender, independency, smoke, education, race, death])
    return data

data = rand_data(10000)
ages = [i for i in range(121)]
mortalities = [0 for i in range(121)]
number_age = [0 for i in range(121)]

for sample in data:
    age = sample[1]
    mortalities[age] += sample[10]
    number_age[age] += 1

for i in range(121):
    mortalities[i] /= number_age[i]
    
plt.plot(ages, mortalities)
new_mortalities = [12, 12.49925007, 11.80120358, 12.03797448, 12.70313866, 12.51826138, 11.95412935, 11.23023544, 11.82224334, 12.0969651, 11.05374861, 10.51643673, 9.555552175, 8.739765691, 8.052234375, 7.465747821, 7.096172115, 6.49447581, 6.233059664, 5.940591088, 5.679522923, 5.386996783, 5.067100992, 5.065439423, 4.805515957, 4.45570381, 4.366615799, 4.452412402, 4.27769792, 4.07017446, 4.756736392, 4.864045345, 5.391547926, 5.999088398, 5.836128814, 6.103360794, 6.649919001, 6.161305626, 6.325921418, 6.897553351, 6.763565049, 7.547509944, 7.229878727, 7.162325299, 7.040305352, 7.601659705, 8.176179008, 8.220307657, 8.510450933, 8.49328354, 8.497727866, 9.486369626, 9.843456397, 9.782244432, 9.932334782, 10.72928768, 10.69701203, 11.00645959, 11.60799754, 11.62245699, 12.32425432, 12.89365397, 14.30307001, 15.17412848, 15.70738968, 15.68575915, 16.17035032, 16.1122906, 16.2442967, 17.012499, 17.2966853, 16.87084034, 17.18847802, 17.61668536, 18.74803688, 18.09281249, 18.11347244, 17.85345098, 17.67333654, 18.00215148, 18.8961213, 19.00112769, 19.24073526, 19.28822779, 19.99707711, 19.86418025, 20.08827744, 20.94266314, 21.5445506, 21.68014637, 22.33554318, 21.69102014, 21.90495418, 21.13301979, 21.31822613, 21.39164106, 21.50468361, 21.81054033, 21.49752794, 21.35507571, 21.24710172, 21.28257364, 21.28708507, 22.23480658, 23.06764367, 23.06881907, 23.17071507, 23.17635454, 23.08538139, 22.63112361, 23.1465938, 23.21635901, 23.4145652, 23.00414252, 23.54976551, 23.62683901, 23.88302574, 23.98927783, 23.33488706, 23.01765619, 23.6818511]
plt.plot(ages, new_mortalities)

plt.show()
