from datetime import datetime, timedelta


def generate_schedule(days: int, work_days: int, rest_days: int, start_date: datetime) -> list[datetime]:
    schedule = []
    current_date = start_date
    total_work_days = 0
    
    while total_work_days < days:
        for _ in range(work_days):
            if total_work_days < days:
                schedule.append(current_date)
                current_date += timedelta(days=1)
                total_work_days += 1
            else:
                break

        if total_work_days < days:
            total_work_days += rest_days
            current_date += timedelta(days=rest_days)
    
    return schedule

print(generate_schedule(5, 2, 1, datetime(2020, 1, 30)))
