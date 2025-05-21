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


# Ví dụ sử dụng
if __name__ == "__main__":
    # Ví dụ danh sách điểm
    test_scores = [9.5, 8.0, 7.5, 6.0, 11.0, -1.0]
    
    # Đếm học sinh Giỏi
    excellent_count = count_excellent_students(test_scores)
    print(f"Số học sinh đạt loại Giỏi: {excellent_count}")  # Kết quả: 2
    
    # Thử nghiệm với danh sách rỗng
    empty_test = []
    print(f"Danh sách rỗng: {count_excellent_students(empty_test)}")  # Kết quả: 0
    
    # Thử nghiệm với danh sách None
    print(f"Danh sách None: {count_excellent_students(None)}")  # Kết quả: 0