label minigame_dodge:

    $ player_x = 550
    $ player_y = 455

    # Jumlah musuh
    $ enemy_count = 5

    # List spawn unik untuk tiap index musuh
    $ ghost_x = []
    $ ghost_y = []

    python:
        for i in range(enemy_count):
            # tiap index musuh punya range spawn beda
            if i == 0:
                ghost_x.append(renpy.random.randint(0, 300))
            elif i == 1:
                ghost_x.append(renpy.random.randint(355, 600))
            elif i == 2:
                ghost_x.append(renpy.random.randint(656, 900))
            else:
                ghost_x.append(renpy.random.randint(945, 1080))

            ghost_y.append(renpy.random.randint(-500, -50))

    $ speed = 13
    $ hit = 0
    $ time_left = 10
    $ game_running = True

    window hide
    show screen dodge_ui

    while game_running:

        python:

            for i in range(enemy_count):

                ghost_y[i] += speed

                # respawn
                if ghost_y[i] > 900:
                    ghost_y[i] = renpy.random.randint(-350, -55)

                    if i == 0:
                        ghost_x[i] = renpy.random.randint(20, 300)
                    elif i == 1:
                        ghost_x[i] = renpy.random.randint(300, 695)
                    elif i == 2:
                        ghost_x[i] = renpy.random.randint(695, 1080)
                    else:
                        ghost_x[i] = renpy.random.randint(1050, 1080)

                # tabrakan
                if abs(player_x - ghost_x[i]) < 80 and abs(player_y - ghost_y[i]) < 120:
                    hit += 1
                    ghost_y[i] = -100
                    ghost_x[i] = renpy.random.randint(0, 1080)

                # batas kiri
                if player_x < 0:
                    player_x = 0

                # batas kanan
                if player_x > 1180:
                    player_x = 1180

                # batas atas
                if player_y < 0:
                    player_y = 0

                # batas bawah
                if player_y > 570:
                    player_y = 570

        if hit >= 3:
            $ game_running = False
            hide screen dodge_ui
            jump minigame_lose

        if time_left <= 0:
            $ game_running = False
            hide screen dodge_ui
            jump minigame_win

        $ time_left -= 0.02
        pause 0.02

    return

screen dodge_ui():
    
    #bg
    add "ruang_tamu_temaram.png"

    # Player
    add "carissa_mini.png" xpos player_x ypos player_y


    # Hantu
    for i in range(enemy_count):
        add "hantu_strong.png" xpos ghost_x[i] ypos ghost_y[i]


    # =========================
    # Tombol kiri
    # =========================
    frame:
        xalign 0.2
        yalign 0.9
        vbox:
            textbutton "←" action SetVariable("player_x", player_x - 225):
                xysize (200, 200)
                text_size 210
                


    # =========================
    # Tombol kanan
    # =========================
    frame:
        xalign 0.8
        yalign 0.9
        vbox:
            textbutton "→" action SetVariable("player_x", player_x + 225):
                xysize (200, 200)
                text_size 210
                

    # HUD
    text "Hit: [hit]/3" xpos 20 ypos 20
    text "Time: [int(time_left)]" xpos 500 ypos 20

label minigame_win:
    "Kamu berhasil menghindar!"
    with flash_blue
    return

label minigame_lose:
    "Kamu terkena 3 kali... Game over!"
    menu:
        "Ulangi mini game?"
        "Ya":
            jump minigame_dodge
        "Tidak":
            return