# def profile(name, age, main_lang):
#     print("이름: {0}\t 나이: {1}\t 주 사용 언어: {2}".format(name, age, main_lang))
#
# profile("유재석", 20, "파이썬")
# profile("최지웅", 14, "자바")
#
# #같은 학교 같은 학년 같은 수업

def profile(name, age=14, main_lang="python"):
     print("이름: {0}\t 나이: {1}\t 주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석")
profile("최지웅")