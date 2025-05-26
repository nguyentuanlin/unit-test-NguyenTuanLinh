from typing import List, Optional

def count_excellent_students(scores: Optional[List[float]]) -> int:
    """
    Đếm số học sinh có điểm hợp lệ (0 <= điểm <= 10) và điểm >= 8.0
    """
    if scores is None or len(scores) == 0:
        return 0
    count = 0
    for score in scores:
        if score is not None and 0 <= score <= 10 and score >= 8.0:
            count += 1
    return count

def calculate_valid_average(scores: Optional[List[float]]) -> float:
    """
    Tính trung bình các điểm hợp lệ (0 <= điểm <= 10)
    Nếu không có điểm hợp lệ, trả về 0.0
    """
    if scores is None or len(scores) == 0:
        return 0.0
    sum_valid = 0.0
    count_valid = 0
    for score in scores:
        if score is not None and 0 <= score <= 10:
            sum_valid += score
            count_valid += 1
    if count_valid == 0:
        return 0.0
    return sum_valid / count_valid

def main():
    input_str = input("Nhập danh sách điểm cách nhau bởi dấu phẩy (ví dụ: 9.5,8,7,-1,11): ")

    try:
        test_scores = [float(x.strip()) for x in input_str.split(",") if x.strip() != '']
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số thực cách nhau bởi dấu phẩy.")
        return

    excellent_count = count_excellent_students(test_scores)
    avg_score = calculate_valid_average(test_scores)

    print(f"Số học sinh đạt loại Giỏi (>=8.0): {excellent_count}")
    print(f"Điểm trung bình hợp lệ (0-10): {avg_score:.2f}")

if __name__ == "__main__":
    main()
