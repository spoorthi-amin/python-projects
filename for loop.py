# fruits=['apple','banana','orange']
# for fruit in fruits:
#     print(fruit)
#     print(fruit +  ' pie')


students_score=[120,130,500,567,800,700,900,134]
# print(sum(students_score))
# 'OR'
# sum=0
# for score in students_score:
#     sum+=score
# print(sum)

max_score=0
for score in students_score:
    if score>max_score:
       max_score=score
print(max_score)
    
       