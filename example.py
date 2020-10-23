import term_updater as tu
from time  import sleep
from string import ascii_lowercase

upterm = tu.term_updater()
upterm.init_updater()
print("========================")
print("letters : ")
print("count :")
print("========================")


upterm.display_terminal()
sleep(1)

for i in range(1,27):
    upterm.update_terminal(f"letters : {ascii_lowercase[:i]}",1)
    upterm.update_terminal(f"count : {str(i)}",2)
    upterm.display_terminal()
    sleep(1)

upterm.end_updater()
