import string
import random
import pandas as pd
import csv
import operator


# 1.1 , 1.2, 1.3 

for i in string.ascii_uppercase:
    with open(f'{i}.txt', mode='w+') as file, open('summary.txt', mode='a') as f:
        a = str(random.randint(1, 100))
        file.write(a)
        f.write(f'{i}.txt : {a}\n')

# 2.1, 2.2
content = [
    'Тому що ніколи тебе не вирвеш\n',
    'ніколи не забереш,\n',
    'тому що вся твоя свобода\n',
    'складається з меж,\n',
    'тому що в тебе немає\n',
    'жодного вантажу,\n',
    'тому що ти ніколи не слухаєш,\n',
    'оскільки знаєш і так,\n',
    'що я скажу.\n']

for i in content:
    with open('content_file.txt', mode="w", encoding="utf-8") as file, open('copy_content.txt', mode='a', encoding="utf-8") as f:
        file.writelines(content)
        f.writelines(i.upper())



# 3. Write a program that will simulate user score in a game. Create a list with 5 player's names. After that simulate 100 games for each player. As a result of the game create a list with player's name and his score(0-1000 range). And save it to a CSV file. File should looks like this:
#     ```
#     Player name, Score
#     Josh, 56
#     Luke, 784
#     Kate, 90
#     Mark, 125
#     Mary, 877
#     Josh, 345
#     ...
#     ```

fields = ['Player', 'Score']
players = ['Josh', 'Luke', 'Kate', 'Yaroslava', 'Lena']
players_simulated = []
score_of_players_simulated = []
for iter in range(1,101):
    # print(f'\n{iter} game:\n')
    for i in players:
        score = random.randint(0, 1000)
        players_simulated.append(i)
        score_of_players_simulated.append(score)
        
        # print((f'{i}:{score}'))


dict_to_frame = pd.DataFrame({'Player': players_simulated, 'score': score_of_players_simulated})

# # saving the dataframe
dict_to_frame.to_csv('Score_table.csv', index=False)
yaroslava_tmp_array, kate_tmp_array, lena_tmp_array, luke_tmp_array, josh_tmp_array = [], [], [], [], []

with open('Score_table.csv', mode='r') as file, open('high_scores.csv', mode='w+', newline="") as f:
    reader = csv.reader(file)
    writer = csv.writer(f)
    read = csv.reader(f)
    for row in reader:
        if row[0] == 'Yaroslava':
            yaroslava_tmp_array.append(row[1])
        if row[0] == 'Josh':
            josh_tmp_array.append(row[1])
        if row[0] == 'Lena':
            lena_tmp_array.append(row[1])
        if row[0] == 'Kate':
            kate_tmp_array.append(row[1])
        if row[0] == 'Luke':
            luke_tmp_array.append(row[1])
    writer.writerow(['Player', 'Score'])
    writer.writerow(['Yaroslava', max(yaroslava_tmp_array)])
    writer.writerow(['Josh', max(josh_tmp_array)])
    writer.writerow(['Lena', max(lena_tmp_array)])
    writer.writerow(['Kate', max(kate_tmp_array)])
    writer.writerow(['Luke', max(luke_tmp_array)])
        
    sortedlist = sorted(reader, key=lambda row: row[1], reverse=True) # Не вышел сортинг

# result = dict_to_frame.groupby('Player')['score'].max()
# print(result)




    
        
