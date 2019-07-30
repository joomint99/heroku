from faker import Faker

myfake=Faker()
#어떤 종류의 가짜 데이터를 뽑아낼지?




print(myfake.name())
print(myfake.address())
print(myfake.sentence())
print(myfake.random_number())
print(myfake.text())
