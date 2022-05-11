num0 = float(input('Digite o primeiro número: '))
num1 = float(input('Digite o segundo número: '))
if num0 > num1:
    print('O \033[;32mPRIMEIRO\033[m valor é maior que o segundo.')
elif num0 < num1:
    print('O \033[31mSEGUNDO\033[m valor é maior que o primeiro.')
else:
    print('Os dois valores são \033[36mIGUAIS\033[m.')
