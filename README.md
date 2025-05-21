# 🎓 Quản Lý Điểm Học Sinh

## 📘 Mô tả bài toán

Ứng dụng Python này hỗ trợ xử lý điểm số học sinh với 2 chức năng chính:

- ✅ **Đếm số học sinh đạt loại Giỏi**  
  Học sinh có điểm hợp lệ (0–10) và điểm ≥ 8.0 được tính là học sinh giỏi.

- ✅ **Tính điểm trung bình hợp lệ**  
  Tính trung bình các điểm trong khoảng [0, 10]. Nếu không có điểm hợp lệ, trả về `0.0`.

> ⚠️ Các điểm không hợp lệ (âm, >10, hoặc `None`) sẽ bị bỏ qua trong mọi tính toán.

---

## 📂 Cấu trúc thư mục
- project_root/
  - src/
    - module.py          (chứa các hàm xử lý điểm)
    - module1.py
    - module2.py
  - test/
    - test_module.py     (chứa bộ test unittest)
  - README.md            (file mô tả dự án)


---

## 🚀 Cách chạy chương trình

### 1. Yêu cầu hệ thống

- Python 3.6 trở lên
- Đã cài đặt `unittest` (mặc định có sẵn trong Python)

### 2. Chạy chương trình chính

```bash
cd uni-test-NguyenTuanLinh
python3 src/module.py

Sau đó nhập danh sách điểm (cách nhau bằng dấu ,), ví dụ:
(9.5,8,7,-1,11)

3. Chạy bộ kiểm thử unittest

cd uni-test-NguyenTuanLinh
python3 -m unittest -v test.test_module

Nếu chạy thành công, bạn sẽ thấy kết quả:
test_average_all_valid (test.test_module.TestScoreFunctions) ... ok
test_excellent_all_valid (test.test_module.TestScoreFunctions) ... ok
...
----------------------------------------------------------------------
Ran 14 tests in 0.002s

OK

🧪 Danh sách kiểm thử (test/test_module.py)
Kiểm thử học sinh giỏi với tất cả điểm hợp lệ

Kiểm thử với điểm không hợp lệ (< 0, > 10, None)

Kiểm thử với danh sách rỗng

Kiểm thử với chỉ 1 điểm hợp lệ

Kiểm thử tính trung bình với các tình huống khác nhau
