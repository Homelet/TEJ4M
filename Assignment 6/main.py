class Bank:
	def __init__(self):
		self.balance = 0
	
	
	def deposit(self, number):
		self.balance += number
	
	
	def withdrawal(self, number):
		self.balance -= number
	
	
	def print_status(self):
		print(self.balance)


bank_action = {
	"D": Bank.deposit,
	"W": Bank.withdrawal
}

bank = Bank()

while True:
	deposit = input().split(" ")
	bank_action[deposit[0]](bank, int(deposit[1]))
	bank.print_status()
