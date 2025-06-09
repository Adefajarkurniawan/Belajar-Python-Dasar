class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, jumlah):
        if jumlah >= 0:
            self.__saldo = jumlah
        else:
            print("Saldo tidak boleh negatif!")

akun1 = BankAccount(1000)

akun1.set_saldo(2000)
print(akun1.get_saldo())  # Output: 2000

akun1.set_saldo(-500)    # Akan print "Saldo tidak boleh negatif!"







