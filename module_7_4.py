teams = ['team1', 'team2']
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / len(teams)
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print('В команде Мастера кода участников: %(team1_num)s!\n' % {'team1_num': team1_num})
print("Итого сегодня в командах участников: %(team1_num)s  и %(team2_num)s!\n" % {'team1_num': team1_num, 'team2_num': team2_num})
print("Команда Волшебники данных решила задач: {score_2}!\n".format(score_2 = score_2))
print("Волшебники данных решили задачи за {team1_time} с!\n".format(team1_time = team1_time))
print(f'Команды решили {score_1} и {score_2} задач.\n')
print(f'Результат битвы: {challenge_result}\n')
print(f'Сегодня было решено {tasks_total}, в среднем по {time_avg} секунды на задачу!')