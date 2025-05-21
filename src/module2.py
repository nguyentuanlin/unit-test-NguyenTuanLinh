from typing import List, Optional

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
    
    valid_scores = []
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