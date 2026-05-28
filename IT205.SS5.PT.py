      
"""
1.1 Phân tích Input/Output
Input:
Tên biến            Kiểu dữ liệu    Ràng buộc
total_room          int             ≥ 0,nếu < 0 → dừng chương trình
row                 int             ≥ 0, ≤ 10, nếu < 0 → bỏ qua phòng
col                 int             ≥ 0, ≤ 10, nếu > 10 → cảnh báo

Output:
Điều kiện                   Kết quả
total_room < 0              In lỗi → thoát
row < 0                     In lỗi → bỏ qua phòng đó
row > 10 hoặc col > 10      Cảnh báo phòng quá lớn
Hợp lệ                      In sơ đồ ghế bằng *

1.2 Pseudocode
Lặp vô hạn:
    Nhập total_room
    Nếu total_room < 0 → in lỗi, thoát

    Lặp từng phòng 1 → total_room:
        Nhập row, col
        Nếu row < 0 hoặc col < 0 → in lỗi, bỏ qua (continue)
        Nếu row > 10 hoặc col > 10 → in cảnh báo
        In sơ đồ ghế: lặp row lần, mỗi lần in "* " × col

    Thoát vòng while
"""

while True:
    total_room = int(input("Nhập số phòng học cần kiểm tra: "))
    if total_room < 0:
        print("Số lượng phòng không hợp lệ!\n")
        break 

    for room_index in range(1, total_room + 1):
        print(f"\n--- Phòng {room_index} ---")
        row = int(input(f"Nhập số hàng ghế của phòng {room_index}: "))
        col = int(input(f"Nhập số ghế trên 1 hàng của phòng {room_index}: "))
        if row < 0 or col < 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này.\n")
            continue
        if row > 10 or col > 10:
            print("Cảnh báo: Phòng quá lớn!\n")
        print(f"\nKết quả kiểm tra của phòng {room_index}:")
        for current_row in range(row):
            print("* " * col)
        print()
    break

    