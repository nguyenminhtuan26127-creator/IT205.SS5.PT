# =========================================================
# PHÂN TÍCH BÀI TOÁN
# =========================================================
# 1. Mục tiêu chương trình
# - Xây dựng hệ thống đánh giá sĩ số lớp học
# - Kiểm tra số lượng học viên đi học của từng lớp
# - In trạng thái lớp học sau khi nhập dữ liệu hợp lệ
#
# =========================================================
# INPUT
# =========================================================
# 1. branch_count
# - Ý nghĩa: Số lượng chi nhánh cần kiểm tra
# - Kiểu dữ liệu: int
#
# 2. student_count
# - Ý nghĩa: Số học viên đi học của từng lớp
# - Kiểu dữ liệu: int
#
# =========================================================
# OUTPUT
# =========================================================
# 1. Nếu số học viên >= 20
# -> "Lớp học ổn định"
#
# 2. Nếu số học viên từ 1 -> 19
# -> "Lớp cần được nhắc nhở theo dõi"
#
# 3. Nếu số học viên == 0
# -> "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
#
# 4. Nếu số học viên < 0
# -> "Số học viên không hợp lệ. Vui lòng nhập lại."
#
# =========================================================
# THUẬT TOÁN XỬ LÝ
# =========================================================
# Bước 1:
# - Nhập số lượng chi nhánh
#
# Bước 2:
# - Dùng vòng lặp for để duyệt từng chi nhánh
#
# Bước 3:
# - Mỗi chi nhánh có 2 lớp học
# - Dùng vòng lặp for để duyệt từng lớp
#
# Bước 4:
# - Nhập số học viên đi học
# - Nếu dữ liệu âm:
#   + Thông báo lỗi
#   + Yêu cầu nhập lại
#
# Bước 5:
# - Sau khi dữ liệu hợp lệ:
#   + Nếu == 0:
#       -> Lớp vắng toàn bộ
#   + Nếu >= 20:
#       -> Lớp học ổn định
#   + Ngược lại:
#       -> Lớp cần được nhắc nhở theo dõi
#
# =========================================================
# KỸ THUẬT ĐƯỢC SỬ DỤNG
# =========================================================
# - Vòng lặp for
# - Vòng lặp while True
# - Câu điều kiện if / elif / else
# - Kiểm tra dữ liệu hợp lệ
# - Xử lý Edge Cases
# =========================================================

# Nhập số lượng chi nhánh
branch_count = int(input("Nhập số lượng chi nhánh: "))

# Duyệt từng chi nhánh
for branch_index in range(1, branch_count + 1):

    print(f"\nChi nhánh {branch_index}:")

    # Mỗi chi nhánh có 2 lớp học
    for class_index in range(1, 3):

        # Kiểm tra dữ liệu hợp lệ
        while True:

            # Nhập số học viên đi học
            student_count = int(
                input(
                    f"Nhập số học viên đi học của lớp {class_index}: "
                )
            )

            # EDGE CASE 1: Số học viên âm
            if student_count < 0:

                print(
                    "Số học viên không hợp lệ. "
                    "Vui lòng nhập lại."
                )

            else:
                # Dữ liệu hợp lệ -> thoát vòng lặp
                break

        # EDGE CASE 2: Lớp vắng toàn bộ
        if student_count == 0:

            print(
                f"Chi nhánh {branch_index} - "
                f"Lớp {class_index}: "
                "Lớp vắng toàn bộ, "
                "bỏ qua kiểm tra trạng thái."
            )

        # Lớp học ổn định
        elif student_count >= 20:

            print(
                f"Chi nhánh {branch_index} - "
                f"Lớp {class_index}: "
                "Lớp học ổn định"
            )
              
        # Lớp cần được nhắc nhở
        else:

            print(
                f"Chi nhánh {branch_index} - "
                f"Lớp {class_index}: "
                "Lớp cần được nhắc nhở theo dõi"
            )

# Kết thúc chương trình
print("\nĐã hoàn tất đánh giá sĩ số lớp học.")
