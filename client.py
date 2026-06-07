import Pyro5.api

uri = input("Nhap URI Server: ")

try:

    calculator = Pyro5.api.Proxy(uri)

    while True:

        n = int(input("\nNhap n = "))

        ket_qua = calculator.tinh_tong(n)

        print("\n===== KET QUA =====")
        print("n =", ket_qua["n"])
        print("Tong =", ket_qua["tong"])

        tiep = input("\nTiep tuc? (y/n): ")

        if tiep.lower() == "n":
            break

except Exception as e:
    print("Loi ket noi:", e)