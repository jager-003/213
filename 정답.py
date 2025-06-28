# import random

# def pick_study_dates():
#     # 4번 중 1번은 온라인, 3번은 오프라인
#     study_dates = []

#     # 1~3일 제외, 4일부터 28일까지 중에서 4개 날짜를 무작위로 선택
#     possible_dates = list(range(4, 29))
#     selected_dates = random.sample(possible_dates, 4)

#     # 오름차순 정렬 (원하는 경우)
#     selected_dates.sort()

#     # 1개는 온라인, 3개는 오프라인 (무작위로 온라인 하나 고르기)
#     online_study = random.choice(selected_dates)
#     for date in selected_dates:
#         if date == online_study:
#             print(f"온라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")
#         else:
#             print(f"오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")

# pick_study_dates()


# import random

# def pick_study_dates():
#     # 4~28일 중 랜덤으로 4개의 날짜 선택
#     possible_dates = list(range(4, 29))
#     selected_dates = random.sample(possible_dates, 4)

#     # 이 중 1개를 무작위로 오프라인 스터디로 지정
#     offline_day = random.choice(selected_dates)

#     # 출력
#     for date in sorted(selected_dates):
#         if date == offline_day:
#             print(f"오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")
#         else:
#             print(f"온라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")

# # 실행
# pick_study_dates()

#////////////////////////////////////////////////////////////////////////////////////
#압축버전 

import random  # 랜덤 기능을 사용하기 위해 import

# 4일부터 28일까지 중에서 중복 없이 4개 날짜를 랜덤으로 선택

dates = random.sample(range(4, 29), 4)

# 그 중 하나를 오프라인 스터디 날짜로 랜덤 선택
offline = random.choice(dates)

# 선택된 날짜들을 오름차순으로 정렬해서 출력
for d in sorted(dates):
    # 오프라인이면 "오프라인", 아니면 "온라인"으로 표시
    kind = "오프라인" if d == offline else "온라인"
    # 형식에 맞게 출력
    print(f"{kind} 스터디 모임 날짜는 매월 {d}일로 선정되었습니다.")