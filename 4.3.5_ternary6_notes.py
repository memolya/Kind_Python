m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
num_1, num_2, num_3 = map(int, input().split(' '))

res_1 = '#до' if (num_1 == 1) else 'ре' if (num_1 == 2) else 'ми' if (num_1 == 3) else '#фа' if (num_1 == 4) else 'соль' if (num_1 == 5) else 'ля' if (num_1 == 6) else 'си'
res_2 = '#до' if (num_2 == 1) else 'ре' if (num_2 == 2) else 'ми' if (num_2 == 3) else '#фа' if (num_2 == 4) else 'соль' if (num_2 == 5) else 'ля' if (num_2 == 6) else 'си'
res_3 = '#до' if (num_3 == 1) else 'ре' if (num_3 == 2) else 'ми' if (num_3 == 3) else '#фа' if (num_3 == 4) else 'соль' if (num_3 == 5) else 'ля' if (num_3 == 6) else 'си'

print(res_1, res_2, res_3, sep = ' ')

