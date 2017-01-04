from evdev import uinput, ecodes as e



# moves = "fFbBlLrRuUdD"
# moves = list(moves)



def wail(moves):
    if moves is not '':
        moves = list(reversed(list(moves.swapcase())))
        for move in moves:
            with uinput.UInput() as ui:
                if move == 'f':
                    ui.write(e.EV_KEY, e.KEY_F, 1)
                    ui.write(e.EV_KEY, e.KEY_F, 0)
                elif move == 'F':
                    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
                    ui.write(e.EV_KEY, e.KEY_F, 1)

                elif move == 'b':
                    ui.write(e.EV_KEY, e.KEY_B, 1)
                    ui.write(e.EV_KEY, e.KEY_B, 0)
                elif move == 'B':
                    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
                    ui.write(e.EV_KEY, e.KEY_B, 1)

                elif move == 'l':
                    ui.write(e.EV_KEY, e.KEY_L, 1)
                    ui.write(e.EV_KEY, e.KEY_L, 0)
                elif move == 'L':
                    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
                    ui.write(e.EV_KEY, e.KEY_L, 1)

                elif move == 'r':
                    ui.write(e.EV_KEY, e.KEY_R, 1)
                    ui.write(e.EV_KEY, e.KEY_R, 0)
                elif move == 'R':
                    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
                    ui.write(e.EV_KEY, e.KEY_R, 1)

                elif move == 'u':
                    ui.write(e.EV_KEY, e.KEY_U, 1)
                    ui.write(e.EV_KEY, e.KEY_U, 0)
                elif move == 'U':
                    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
                    ui.write(e.EV_KEY, e.KEY_U, 1)

                elif move == 'd':
                    ui.write(e.EV_KEY, e.KEY_D, 1)
                    ui.write(e.EV_KEY, e.KEY_D, 0)
                elif move == 'D':
                    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
                    ui.write(e.EV_KEY, e.KEY_D, 1)

                ui.syn()
