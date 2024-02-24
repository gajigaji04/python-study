from tqdm import tqdm
import time

# 총 반복 횟수
total_iterations = 100

# tqdm을 사용하여 상태 표시 바 생성
for i in tqdm(range(total_iterations), desc="Progress", unit="iteration"):
    # 작업 수행
    time.sleep(0.1)



print("Task completed!")
