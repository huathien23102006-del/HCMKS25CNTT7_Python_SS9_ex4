# 1. Phân tích Input / Output
# Input
# Danh sách đơn hàng ban đầu
# order_list = [
#     "GE001 - PENDING",
#     "GE002 - DELIVERING",
#     "GE003 - CANCELLED"
# ]

# Kiểu dữ liệu:

# list[str]
# Dữ liệu người dùng nhập
# Menu chính
# 1
# 2
# 3
# 4

# Kiểu dữ liệu:

# str -> int
# Menu cập nhật
# 1
# 2
# 3
# 4

# Kiểu dữ liệu:

# str -> int
# Mã đơn hàng

# Ví dụ:

# ge004

# Kiểu dữ liệu:

# str
# Trạng thái

# Ví dụ:

# pending

# Kiểu dữ liệu:

# str
# Vị trí sửa / xóa

# Ví dụ:

# 2

# Kiểu dữ liệu:

# str -> int
# Output
# Hiển thị danh sách
# Danh sách đơn hàng hiện tại:
# 1. GE001 - PENDING
# 2. GE002 - DELIVERING
# 3. GE003 - CANCELLED
# Thêm thành công
# Đã thêm đơn hàng thành công!
# Sửa thành công
# Đã cập nhật đơn hàng thành công!
# Xóa thành công
# Đã xóa: GE002 - DELIVERING
# Sai vị trí
# Không tồn tại đơn hàng ở vị trí này!
# Nhập chữ thay vì số
# Vị trí không hợp lệ!
# Thống kê
# ===== THỐNG KÊ ĐƠN HÀNG =====
# PENDING: 2
# DELIVERING: 1
# COMPLETED: 0
# CANCELLED: 1
# Tổng số đơn hàng: 4
# 2. Đề xuất giải pháp
# Hiển thị danh sách

# Dùng:

# for

# hoặc:

# enumerate()

# để đánh số thứ tự.

# Thêm đơn hàng

# Chuẩn hóa:

# order_code = input(...).strip().upper()
# status = input(...).strip().upper()

# Ghép chuỗi:

# new_order = f"{order_code} - {status}"

# Thêm vào cuối:

# order_list.append(new_order)
# Sửa đơn hàng

# Người dùng nhập vị trí bắt đầu từ 1.

# Đổi sang index:

# index = position - 1

# Kiểm tra:

# 0 <= index < len(order_list)

# Nếu hợp lệ:

# order_list[index] = updated_order
# Xóa đơn hàng

# Dùng:

# removed_order = order_list.pop(index)

# Để vừa xóa vừa lấy được dữ liệu hiển thị.

# Thống kê trạng thái

# Khởi tạo:

# pending_count = 0
# delivering_count = 0
# completed_count = 0
# cancelled_count = 0

# Tách trạng thái:

# parts = order.split(" - ")
# status = parts[1]

# Đếm theo trạng thái.

# Kiểm tra dữ liệu
# Menu
# choice.isdigit()
# Vị trí
# position.isdigit()

# Nếu sai:

# Vị trí không hợp lệ!
# 3. Thuật toán (Pseudocode)
# Khởi tạo danh sách đơn hàng

# Lặp vô hạn

#     Hiển thị menu chính

#     Nhập lựa chọn

#     Nếu lựa chọn không hợp lệ
#         Thông báo lỗi
#         quay lại menu

#     Nếu chọn 1
#         Hiển thị danh sách

#     Nếu chọn 2
#         Hiển thị menu cập nhật

#         Lặp menu cập nhật

#             Nếu chọn 1
#                 Nhập mã đơn hàng
#                 Nhập trạng thái
#                 Chuẩn hóa
#                 Thêm vào danh sách

#             Nếu chọn 2
#                 Nhập vị trí
#                 Kiểm tra hợp lệ
#                 Nhập dữ liệu mới
#                 Cập nhật đơn hàng

#             Nếu chọn 3
#                 Nhập vị trí
#                 Kiểm tra hợp lệ
#                 Xóa đơn hàng

#             Nếu chọn 4
#                 Quay lại menu chính

#     Nếu chọn 3
#         Thống kê số lượng từng trạng thái

#     Nếu chọn 4
#         Thoát chương trình
#         break
# (2) Source Code Python Hoàn Chỉnh
# ==========================
# Danh sách đơn hàng ban đầu
# ==========================
order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]


# ==========================
# Hiển thị danh sách
# ==========================
def show_orders():
    if len(order_list) == 0:
        print("Danh sách đơn hàng hiện đang trống.")
    else:
        print("\nDanh sách đơn hàng hiện tại:")
        for index, order in enumerate(order_list, start=1):
            print(f"{index}. {order}")


# ==========================
# Thống kê trạng thái
# ==========================
def statistics():
    pending = 0
    delivering = 0
    completed = 0
    cancelled = 0

    for order in order_list:
        parts = order.split(" - ")

        if len(parts) != 2:
            continue

        status = parts[1]

        if status == "PENDING":
            pending += 1
        elif status == "DELIVERING":
            delivering += 1
        elif status == "COMPLETED":
            completed += 1
        elif status == "CANCELLED":
            cancelled += 1

    print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
    print(f"PENDING: {pending}")
    print(f"DELIVERING: {delivering}")
    print(f"COMPLETED: {completed}")
    print(f"CANCELLED: {cancelled}")
    print(f"Tổng số đơn hàng: {len(order_list)}")


# ==========================
# Menu chính
# ==========================
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    # ==========================
    # Chức năng 1
    # ==========================
    if choice == 1:
        show_orders()

    # ==========================
    # Chức năng 2
    # ==========================
    elif choice == 2:

        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")

            sub_choice = input("Nhập lựa chọn: ").strip()

            if not sub_choice.isdigit():
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                continue

            sub_choice = int(sub_choice)

            # Thêm đơn hàng
            if sub_choice == 1:
                order_code = input(
                    "Nhập mã đơn hàng: "
                ).strip().upper()

                status = input(
                    "Nhập trạng thái: "
                ).strip().upper()

                new_order = f"{order_code} - {status}"

                order_list.append(new_order)

                print("Đã thêm đơn hàng thành công!")

            # Sửa đơn hàng
            elif sub_choice == 2:
                position = input(
                    "Nhập vị trí cần sửa: "
                ).strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                position = int(position)

                if position < 1 or position > len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue

                order_code = input(
                    "Nhập mã đơn hàng mới: "
                ).strip().upper()

                status = input(
                    "Nhập trạng thái mới: "
                ).strip().upper()

                order_list[position - 1] = (
                    f"{order_code} - {status}"
                )

                print("Đã cập nhật đơn hàng thành công!")

            # Xóa đơn hàng
            elif sub_choice == 3:
                position = input(
                    "Nhập vị trí cần xóa: "
                ).strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                position = int(position)

                if position < 1 or position > len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue

                removed_order = order_list.pop(position - 1)

                print(f"Đã xóa: {removed_order}")

            # Quay lại menu chính
            elif sub_choice == 4:
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

    # ==========================
    # Chức năng 3
    # ==========================
    elif choice == 3:
        statistics()

    # ==========================
    # Chức năng 4
    # ==========================
    elif choice == 4:
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")