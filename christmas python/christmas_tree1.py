from colorama import Fore, Style
import numpy as np

tree = np.column_stack((np.arange(15, 6, -1), np.arange(1, 18, 2)))
[print(Fore.GREEN + ' '*i + Fore.GREEN + '*'*j + Style.RESET_ALL) for i,j in tree]
[print(Fore.RED + ' '*13 + ' || ' + Style.RESET_ALL) for _ in range(3)]
print(Fore.BLUE + ' '*11 + r'\======/' + Style.RESET_ALL)