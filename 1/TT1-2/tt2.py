kwhAmount = float(input('How much your next month kWh will be?\n'))

baseFee = float(1.79)
energyFee = float(0.0629)
transmissionBaseFee = float(3.98)
transmissionEnergyFee = float(0.031868)
electricityTax = float(0.0279372)

finalAmount = baseFee + transmissionBaseFee + (energyFee * kwhAmount) + (transmissionEnergyFee * kwhAmount) + (electricityTax * kwhAmount)
print (f'Your next month electric bill will be about {finalAmount:.2f}€')