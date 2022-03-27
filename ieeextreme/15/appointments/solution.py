import heapq
from collections import defaultdict


END = 0
PATIENT_ID = 1

nof_tests = int(input())
for test in range(nof_tests):
    nof_patients = int(input())
    patients_by_day = defaultdict(list)
    for patient in range(nof_patients):
        start, end = map(int, input().split())
        patients_by_day[start].append((end, patient))
 
    is_possible = True
    schedule = [None] * nof_patients
    for day in range(1, nof_patients + 1):
        # Add patients with start = day to a min heap based on end
        if day == 1:
            possible_patients = patients_by_day[day]
            heapq.heapify(possible_patients)
        else:
            for patient in patients_by_day[day]:
                heapq.heappush(possible_patients, patient)

        if not possible_patients:
            is_possible = False
            break
        
        # Pick patient with valid start and smaller end
        patient = heapq.heappop(possible_patients)
        patient_id = patient[PATIENT_ID]
        end = patient[END]
        if end < day:
            is_possible = False
            break
        schedule[day - 1] = patient_id + 1

    if is_possible:
        print(" ".join(map(str, schedule)))
    else:
        print("impossible")
