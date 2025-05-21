from typing import List, Optional

def count_excellent_students(scores: Optional[List[float]]) -> int:
    """
    Phân tích điểm số và trả về số lượng học sinh đạt loại Giỏi.
    
    Args:
        scores: danh sách điểm số từ 0 đến 10
            
    Returns:
        số học sinh đạt loại Giỏi (>= 8.0)
        - Bỏ qua điểm âm hoặc lớn hơn 10 (coi là dữ liệu sai)
        - Nếu danh sách rỗng hoặc None, trả về 0
    """
    # Kiểm tra nếu danh sách rỗng hoặc None
    if scores is None or len(scores) == 0:
        return 0
    
    count = 0
    
    # Duyệt qua danh sách điểm
    for score in scores:
        # Kiểm tra điểm hợp lệ (từ 0 đến 10) và >= 8.0 (loại Giỏi)
        if score is not None and 0 <= score <= 10 and score >= 8.0:
            count += 1
    
    return count


def calculate_valid_average(scores: Optional[List[float]]) -> float:
    """
    Tính điểm trung bình hợp lệ (từ 0 đến 10)
    
    Args:
        scores: danh sách điểm số
            
    Returns:
        điểm trung bình của các điểm hợp lệ
        - Chỉ tính điểm hợp lệ (từ 0 đến 10)
        - Nếu danh sách rỗng hoặc None, trả về 0.0
        - Nếu không có điểm hợp lệ nào, trả về 0.0
    """
    # Kiểm tra nếu danh sách rỗng hoặc None
    if scores is None or len(scores) == 0:
        return 0.0
    
    sum_valid = 0.0
    count_valid = 0
    
    # Duyệt qua danh sách điểm
    for score in scores:
        # Chỉ tính điểm hợp lệ (từ 0 đến 10)
        if score is not None and 0 <= score <= 10:
            sum_valid += score
            count_valid += 1
    
    # Nếu không có điểm hợp lệ nào
    if count_valid == 0:
        return 0.0
    
    # Tính và trả về điểm trung bình
    return sum_valid / count_valid


# Đoạn mã kiểm thử
if __name__ == "__main__":
    # Ví dụ danh sách điểm
    test_scores = [9.5, 8.0, 7.5, 6.0, 11.0, -1.0]
    
    # Kiểm tra hàm count_excellent_students
    excellent_count = count_excellent_students(test_scores)
    print(f"Số học sinh đạt loại Giỏi: {excellent_count}")
    
    # Kiểm tra hàm calculate_valid_average
    avg_score = calculate_valid_average(test_scores)
    print(f"Điểm trung bình hợp lệ: {avg_score:.2f}")