import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름": "최현수", "나이": 14, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()