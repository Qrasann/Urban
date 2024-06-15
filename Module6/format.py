team1_num = 7
team2_num = 8
score_1 = 45
score_2 = 40
team1_time = 25000
team2_time = 30000

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды 1!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды 2!'
else:
    challenge_result = 'Ничья!'

team1_str = "В команде 1 участников: %d !" % team1_num
print(team1_str)

teams_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(teams_str)

score_2_str = "Команда 2 решила задач: {} !".format(score_2)
print(score_2_str)

time_2_str = "Команда 2 решила задачи за {:.1f} с !".format(team2_time)
print(time_2_str)

scores_str = f"Команды решили {score_1} и {score_2} задач."
print(scores_str)

result_str = f"Результат битвы: {challenge_result}"
print(result_str)

tasks_time_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!."
print(tasks_time_str)
