import sys
import pandas as pd

class Hoocne:
    def __init__(self):
        self.a = []  # Polynomial coefficients
        self.b = []  # Coefficients after calculations
        self.C = []  # Derivative coefficients

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
        self.b = [0] * len(self.a)
        self.b[0] = self.a[0]

        print(f"Tính giá trị đa thức tại x = {c}:")
        self.print_table_header()
        
        for i in range(1, len(self.a)):
            self.b[i] = self.b[i-1] * c + self.a[i]

        self.print_table()
        return self.b[-1]

    def chia(self, c):
        self.b = [0] * len(self.a)
        self.b[0] = self.a[0]

        print(f"Chia đa thức cho (x - {c}):")
        self.print_table_header()
        
        for i in range(1, len(self.a)):
            self.b[i] = self.b[i-1] * c + self.a[i]

        self.print_table()

        print("Đa thức thương:")
        for i in range(len(self.a) - 2, -1, -1):
            exponent = len(self.a) - 2 - i
            #print(self.b)
            print(f"{self.b[exponent]:.4f}x^{i}", end=' ')
            if i < len(self.b) - 1:
                print("+ ", end=' ')
        #print()

        print(f"Phần dư: {self.b[-1]:.4f}")

    def nhan(self, c):
        self.b = [0] * (len(self.a) + 1)  # Tăng kích thước lên 1 vì bậc cao nhất tăng lên
        self.b[0] = self.a[0]  # Hệ số bậc cao nhất của b vẫn là a[0]

        print(f"Nhân đa thức với (x - {c}):")
        self.print_table_header()

        # Tính các hệ số của đa thức sau khi nhân
        for i in range(1, len(self.b)-1):
            self.b[i] = self.a[i] - c * self.a[i-1]
        self.b[len(self.b)-1] = - c *self.a[-1] 
        
        for i in range(len(self.b)):
            print(f"{self.b[i]:>10.4f} |", end=' ')
        
        print("\nĐa thức nhân:")
        for i in range(len(self.a), -1, -1):
            exponent = len(self.a) - i
            #print(self.b)
            print(f"{self.b[exponent]:.4f}x^{i}", end=' ')
            if i < len(self.b) - 1:
                print("+ ", end=' ')


    def daoham(self, c):
        #Vui lòng nhập số cấp bạn muốn đạo hàm
        n=2
    
        # Kiểm tra xem đa thức có đủ hạng tử để tính đạo hàm
        if len(self.a) < 2:
            print("Đa thức không có đủ hạng tử để tính đạo hàm.")
            return 0

        current_coefficients = self.a[:]  # Hệ số hiện tại
        derivative_values = []  # Danh sách lưu các giá trị đạo hàm
        derivative_coefficients = []  # Danh sách lưu các hệ số của đạo hàm

        print(f"Tính giá trị đạo hàm bậc {n} tại x = {c}:")

        for degree in range(n):
            # Tính các hệ số của đạo hàm
            next_coefficients = [0] * (len(current_coefficients) - 1)  # Khởi tạo cho đạo hàm tiếp theo

            # Tính hệ số đạo hàm
            for i in range(len(current_coefficients) - 1):
                next_coefficients[i] = (len(current_coefficients) - 1 - i) * current_coefficients[i]  # Tính hệ số đạo hàm

            # Lưu hệ số đạo hàm vào danh sách
            derivative_coefficients.append(next_coefficients)

            # Tính giá trị đạo hàm tại c
            derivative_value = 0
            for coeff in next_coefficients:
                derivative_value = derivative_value * c + coeff

            derivative_values.append(derivative_value)  # Lưu giá trị đạo hàm tại c

            # Cập nhật hệ số hiện tại cho lần lặp tiếp theo
            current_coefficients = next_coefficients

            # In ra bảng hệ số của đạo hàm bậc hiện tại
            print(f"\nĐạo hàm bậc {degree + 1}:")
            print(f"Giá trị đạo hàm bậc {degree + 1} tại x = {c}: {derivative_value:.4f}")

        return derivative_values  # Trả về danh sách giá trị của các đạo hàm tại x



def main():
    # Read input from file input.xlsx
    df = pd.read_excel("input.xlsx", header=None)

    n = int(df.iloc[0, 0]) + 1  # Number of coefficients
    a = df.iloc[1, :n].tolist()  # Polynomial coefficients
    x = df.iloc[2, 0]  # Value of x

    # Display options for the operation
    print("Vui lòng chọn loại thao tác:")
    print("1: Tính giá trị đa thức tại điểm x")
    print("2: Thực hiện phép chia đa thức cho (x-c)")
    print("3: Nhân đa thức với (x-c)")
    print("4: Tính giá trị đạo hàm tại điểm x")

    # Get operation type from command-line argument
    if len(sys.argv) < 2:
        print("Vui lòng cung cấp loại thao tác (1, 2, 3 hoặc 4) qua dòng lệnh! Ví dụ: python udhoocne.py 1")
        return

    type_ = int(sys.argv[1])
    hoocne = Hoocne()
    hoocne.a = a

    print("Đa thức đã cho:")
    n = len(a)  # Độ dài của mảng a
    for i in range(n):
        exponent = n - 1 - i  # Chỉ số bậc x bắt đầu từ len(a)-1
        print(f"{a[i]}*x^{exponent}", end=' ')
        if i < n - 1:
            print("+ ", end=' ')
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
        print(f"Giá trị của đạo hàm tại điểm: x={x:.4f} là: {result}")
    else:
        print("Loại thao tác không hợp lệ! Vui lòng chọn 1, 2, 3 hoặc 4.")

if __name__ == "__main__":
    main()
