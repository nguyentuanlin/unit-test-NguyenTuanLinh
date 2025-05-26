# 🎓 Quản Lý Điểm Học Sinh

Chào mừng bạn đến với dự án **Quản Lý Điểm Học Sinh** – một ứng dụng Python đơn giản nhưng mạnh mẽ giúp xử lý điểm số học sinh với các chức năng tự động và kiểm thử toàn diện!

---

## 📖 Giới thiệu

Dự án này được thiết kế để hỗ trợ giáo viên hoặc quản lý điểm số học sinh một cách hiệu quả. Ứng dụng cung cấp hai chức năng chính:

- ✅ Đếm số học sinh đạt loại Giỏi
- ✅ Tính điểm trung bình hợp lệ (loại bỏ điểm không hợp lệ)

---

## 📘 Mô tả bài toán

Ứng dụng Python này thực hiện hai chức năng cốt lõi:

### ✅ 1. Đếm số học sinh đạt loại Giỏi

- Học sinh được xếp loại Giỏi nếu điểm số hợp lệ (0 ≤ điểm ≤ 10) và đạt ≥ 8.0.
- Ví dụ: Điểm 9.5, 8.0 được tính; còn -1, 11 hoặc `None` sẽ bị bỏ qua.

### ✅ 2. Tính điểm trung bình hợp lệ

- Tính trung bình các điểm hợp lệ trong khoảng [0, 10].
- Nếu không có điểm nào hợp lệ, trả về `0.0`.
- Ví dụ: `(9.5, 8, 7, -1, 11)` → trung bình = `(9.5 + 8 + 7) / 3 = 8.17`

> ⚠️ **Lưu ý:** Mọi điểm không hợp lệ (âm, lớn hơn 10, hoặc `None`) sẽ bị loại bỏ khỏi các phép tính.

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


### Mô tả ngắn gọn:

- `src/module.py`: Chứa các hàm xử lý điểm.
- `test/test_module.py`: Các kiểm thử đơn vị.
- `README.md`: Tài liệu hướng dẫn sử dụng.

---

## 🚀 Hướng dẫn cài đặt và chạy chương trình

### 1. Yêu cầu hệ thống

- Python 3.6 trở lên (khuyến nghị 3.9+)
- `unittest` (có sẵn trong Python)
- Hỗ trợ: Windows, macOS, Linux

---

### 2. Cài đặt và chạy chương trình chính

git clone https://github.com/nguyentuanlin/unit-test-NguyenTuanLinh.git
cd unit-test-NguyenTuanLinh
python3 src/module.py


Sau khi chạy, chương trình sẽ yêu cầu bạn nhập danh sách điểm, cách nhau bằng dấu phẩy.

Ví dụ nhập:

                  9.5, 8, 7, -1, 11

Kết quả hiển thị:

                  Số học sinh Giỏi: 2
                 Điểm trung bình: 8.17


### 3. Chạy bộ kiểm thử đơn vị

### 📌 Lưu ý quan trọng:
- Luôn **bọc các đoạn lệnh/mã** trong khối ``` để đảm bảo hiển thị đúng (bắt đầu bằng ```bash hoặc ```python và kết thúc bằng ```).
- **Thêm một dòng trống** giữa các đoạn **text và code** để tránh bị dính dòng.

---
🧪 Đo Độ Bao Phủ (Code Coverage)
Để đảm bảo các kiểm thử của bạn bao phủ đủ phần mã nguồn, bạn có thể sử dụng công cụ coverage.py để đo độ bao phủ.

1. Cài đặt coverage
Bạn cài đặt coverage qua pip:

bash
Copy
Edit
pip install coverage
2. Chạy kiểm thử và đo độ bao phủ
Chạy kiểm thử cùng với đo độ bao phủ bằng lệnh:

bash
Copy
Edit
coverage run -m unittest discover -s test
-m unittest discover -s test tự động tìm và chạy các file test trong thư mục test.

3. Xem báo cáo độ bao phủ
Sau khi chạy xong, bạn xem báo cáo độ bao phủ dưới dạng text:

coverage report -m
Trong đó, -m hiện chi tiết dòng code nào chưa được kiểm thử.

kết quả kiểm thử 
<img width="715" alt="Ảnh màn hình 2025-05-26 lúc 17 35 09" src="https://github.com/user-attachments/assets/26915e5e-23b0-459d-9488-80950445af3a" />

