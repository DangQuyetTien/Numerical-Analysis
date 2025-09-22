import sys
import pandas as pd

class Hoocne:
    def __init__(self):
        self.a = []  # Hệ số đa thức
        self.b = []  # Hệ số sau khi tính toán
        self.C = []  # Hệ số của đạo hàm

    def print_table_header(self):
        print(f"|   i  |", end=' ')
        for coeff in self.a:
            print(f"{coeff:>10} |", end=' ')
        print()

    def print_table(self):
        for i in range(len(self.a)):
            print(f"| {i:>5} |", end=' ')
            for j in range(len(self.a)):
                if j <= i:
                    print(f"{self.b[j]:>10.4f} |", end=' ')
                else:
                    print(f"{' ':>10} |", end=' ')
            print()

    def solve(self, c):
        self.b = [0] * (len(self.a))
        self.b[-1] = self.a[-1]

        print(f"Tính giá trị đa thức tại x = {c}:")
        self.print_table_header()
        
        for i in range(len(self.a) - 1, 0, -1):
            self.b[i - 1] = self.b[i] * c + self.a[i - 1]

        self.print_table()
        return self.b[0]

    def chia(self, c):
        self.b = [0] * (len(self.a))
        self.b[-1] = self.a[-1]

        print(f"Chia đa thức cho (x - {c}):")
        self.print_table_header()
        
        for i in range(len(self.a) - 1, 0, -1):
            self.b[i - 1] = self.b[i] * c + self.a[i - 1]

        self.print_table()
        
        print("(")
        for i in range(len(self.a) - 1, 1, -1):
            print(f"b{i - 1}x^{i - 2}", end=' ')
            if i > 2:
                print("+ ", end=' ')
        print(")")

        for i in range(len(self.a) - 1, 1, -1):
            print(f"b[{i - 1}] = {self.b[i]:.4f}")

        print(f"Phần dư: {self.b[1]:.4f}")

    def nhan(self, c):
        self.b = [0] * (len(self.a) + 1)  # Tăng kích thước lên 1 vì số bậc tăng lên
        print(f"Nhân đa thức với (x - {c}):")
        
        # Tính hệ số bậc cao nhất
        self.b[-1] = self.a[-1]

        self.print_table_header()
        
        for i in range(len(self.a) - 1, 0, -1):
            self.b[i] = self.a[i] + self.b[i + 1] * (-c)

        self.print_table()

        print("(")
        for i in range(len(self.b)):
            print(f"b{i + 1}x^{i}", end=' ')
            if i < len(self.b) - 1:
                print("+ ", end=' ')
        print(")")

        for i in range(len(self.b)):
            print(f"b[{i + 1}] = {self.b[i]:.4f}")

    def daoham(self, c):
        self.b = [0] * (len(self.a))
        self.b[-1] = self.a[-1]

        print(f"Tính giá trị đạo hàm tại x = {c}:")
        self.print_table_header()
        
        for i in range(len(self.a) - 1, 0, -1):
            self.b[i - 1] = self.b[i] * c + self.a[i - 1]

        self.C = [0] * (len(self.a) - 1)  # Đạo hàm có bậc thấp hơn 1
        self.C[-1] = self.b[-1]

        for i in range(len(self.a) - 1, 1, -1):
            self.C[i - 2] = self.C[i - 1] * c + self.b[i - 1]

        self.print_table()

        return self.C[0]  # Giá trị đạo hàm tại x

def main():
    # Đọc dữ liệu từ file input.xlsx
    df = pd.read_excel("input.xlsx", header=None)

    n = int(df.iloc[0, 0])  # Số lượng hệ số
    a = df.iloc[1, :n].tolist()  # Các hệ số của đa thức
    x = df.iloc[2, 0]  # Giá trị x

    # In hướng dẫn chọn loại thao tác
    print("Vui lòng chọn loại thao tác:")
    print("1: Tính giá trị đa thức tại điểm x")
    print("2: Thực hiện phép chia đa thức cho (x-c)")
    print("3: Nhân đa thức với (x-c)")
    print("4: Tính giá trị đạo hàm tại điểm x")

    # Lấy loại thao tác từ dòng lệnh
    if len(sys.argv) < 2:
        print("Vui lòng cung cấp loại thao tác (1, 2, 3 hoặc 4) qua dòng lệnh! Ví dụ: py udhoocne.py 1")
        return

    type_ = int(sys.argv[1])
    hoocne = Hoocne()
    hoocne.a = a

    print("Đa thức đã cho:")
    for i in range(len(a), 0, -1):
        print(f"a{i}.x^{i - 1}", end=' ')
        if i > 1:
            print("+ ", end=' ')
    print()

    for i in range(len(a)):
        print(f"a{i + 1} = {hoocne.a[i]:.4f}")

    print()

    if type_ == 1:
        result = hoocne.solve(x)
        print(f"Giá trị của đa thức tại điểm: x={x:.4f} là: {result:.4f}")
    elif type_ == 2:
        hoocne.chia(x)
    elif type_ == 3:
        hoocne.nhan(x)
    elif type_ == 4:
        result = hoocne.daoham(x)
        print(f"Giá trị của đạo hàm tại điểm: x={x:.4f} là: {result:.4f}")
    else:
        print("Loại thao tác không hợp lệ! Vui lòng chọn 1, 2, 3 hoặc 4.")

if __name__ == "__main__":
    main()
