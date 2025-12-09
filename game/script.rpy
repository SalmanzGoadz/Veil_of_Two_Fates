#==== CHARACTER DEFINITIONS =====
define c = Character("Carissa", color="#e8a5c7")
define n = Character("Narator", color="#ffffff", what_italic=True)
define suara = Character("Suara Bisikan", color="#666666", what_italic=True)
define a = Character("Aksara", color="#7fb3d5")
define d = Character("Dewa", color="#f4d03f")
define nenek = Character("Nenek", color="#d7bde2")
define guru = Character("Guru", color="#85929e")
define p = Character("Pemandu", color="#5fe09b")
define siswa1 = Character("Siswa 1", color="#aab7b8")
define siswa2 = Character("Siswa 2", color="#aab7b8")
define siswa3 = Character("Siswa 3", color="#aab7b8")
define k = Character("Kakek", color="#ff3725")
# ===== POINT SYSTEM =====
default aksara_points = 0
default dewa_points = 0
default talked_to_nenek = False

#gui
image bg blck = "images/blck.png"
image splash = "images/splash.jpg" 

# ===== BACKGROUNDS =====
image bg rumah_tua_malam = "rumah_tua_malam.png"
image bg rumah_tua_siang = "rumah_tua_siang.jpg"
image bg ruang_tamu_temaram = "ruang_tamu_temaram.png"
image bg ruang_tamu_terang = "ruang_tamu_terang.png"
image bg kamar_carissa = "kamarCarissa.png"
image bg halaman_sekolah = "halaman_sekolah.png"
image bg kelas = "kelas.png"
image bg perpustakaan = "perpustakaan.png"
image bg halaman_belakang = "halaman_belakang.png"
image bg atap_sekolah = "atap_sekolah.png"
image bg kantin = "kantin.png"
image bg langit_jingga = "langit_jingga.png"
image bg jalan_kota = "jalan_kota.png"
image bg candi_gerbang = "candi_gerbang.png"
image bg dalam_bus = "dalam_bus.png"
image bg kuil = "kuil.png"
image bg cafe = "cafe.png"
image bg koridor_sekolah = "lorong.png"
image bg ruang_makan = "ruang_makan.png"  
image bg candi_reruntuhan = "candi_reruntuhan.png" 


# ===== CHARACTER SPRITES - CARISSA =====
image carissa normal = "carissa_normal.png"
image carissa sedih = "carissa_sedih.png"
image carissa takut = "carissa_takut.png"
image carissa kaget = "carissa_kaget.png"
image carissa bingung = "carissa_bingung.png"
image carissa senyum = "carissa_senyum.png"
image carissa corrupted = "carissa_corrupted.png"  
image carissa marah = "carissa_marah.png"  
image carissa khawatir = "carissa_khawatir.png"  

# ===== CHARACTER SPRITES - AKSARA =====
image aksara normal = "aksara_normal.png"
image aksara serius = "aksara_serius.png"
image aksara khawatir = "aksara_khawatir.png"
image aksara sedih = "aksara_sedih.png"
image aksara marah = "aksara_marah.png"
image aksara senyum = "aksara_senyum.png"
image aksara kaget = "aksara_kaget.png"
image aksara guardian = "aksara_guardian.png"  # Mode penjaga#belum

# ===== CHARACTER SPRITES - DEWA =====
image dewa normal = "dewa_normal.png"
image dewa senyum = "dewa_senyum.png"
image dewa misterius = "dewa_misterius.png"
image dewa marah = "dewa_marah.png"
image dewa sedih = "dewa_sedih.png"#belum
image dewa serius = "dewa_serius.png"#belum
image dewa wujud_asli = "dewa_wujud_asli.png"  # Wujud roh

# ===== CHARACTER SPRITES - NENEK & KAKEK =====
image nenek normal = "nenek_normal.png"
image nenek khawatir = "nenek_khawatir.png"
image nenek senyum = "nenek_senyum.png"
image nenek serius = "nenek_serius.png"

image kakek normal = "kakek_normal.png"
image kakek khawatir = "kakek_khawatir.png"
image kakek senyum = "kakek_senyum.png"
image kakek serius = "kakek_serius.png"


# ===== NPC SPRITES =====
image npc generic = "npc_generic.png"
image guru = "guru.png"
image pemandu = "pemandu.png"

# ===== SPECIAL EFFECTS & ENTITIES =====
image hantu weak = "hantu_weak.png"
image hantu medium = "hantu_medium.png"
image hantu strong = "hantu_strong.png"
image bayangan = "bayangan.png"#sudah
image roh_kecil = "roh_kecil.png"#gaguna bjir
image cermin_bergetar = "cermin_bergetar.png"#sudah
image lilin = "lilin.png"#dah
image mata_biru = "mata_biru_glow.png"#sudah ini cuma aura karena mata biru dah ada
image aura_merah = "aura_merah.png"#sudah
image aura_biru = "aura_biru.png"#sudah
image jimat_glow = "jimat_glow.png"#sudah
image kalung_glow = "kalung_glow.png"#dah

# ===== CUSTOM TRANSITIONS =====
define slow_dissolve = Dissolve(2.0)
define flash_red = Fade(0.1, 0.0, 0.3, color="#8b0000")
define flash_white = Fade(0.1, 0.0, 0.5, color="#ffffff")
define flash_blue = Fade(0.1, 0.0, 0.5, color="#4169e1")
define nightmare_transition = ImageDissolve("nightmare_mask.png", 1.5)

# ===== AUDIO DEFINITIONS =====
define audio.rain = "audio/rain.ogg"
define audio.heartbeat = "audio/heartbeat.ogg"
define audio.wind = "audio/wind.ogg"
define audio.tension = "audio/tension.ogg"
define audio.school_bell = "audio/school_bell.ogg"
define audio.mystery_theme = "audio/mystery.ogg"
define audio.footsteps = "audio/footsteps.ogg"
define audio.classroom_chatter = "audio/classroom_chatter.ogg"
define audio.door_open = "audio/door_open.ogg"
define audio.book_flip = "audio/book_flip.ogg"
define audio.book_open = "audio/book_open.ogg"
define audio.magic = "audio/magic.ogg"
define audio.success = "audio/success.ogg"
define audio.running = "audio/running.ogg"
define audio.phone_vibrate = "audio/phone_vibrate.ogg"
define audio.bus_engine = "audio/bus_engine.ogg"
define audio.bus_stop = "audio/bus_stop.ogg"
define audio.thing_open = "audio/thing_open.ogg"
define audio.flame_flicker = "audio/flame_flicker.ogg"
define audio.alarm_clock = "audio/alarm_clock.ogg"  
define audio.dark_power = "audio/dark_power.ogg"  
define audio.holy_power = "audio/holy_power.ogg" 
define audio.light_explosion = "audio/light_explosion.ogg"  
define audio.sfx_combat = "audio/sfx_combat.ogg" 


#gui dan splash screen
# Animasi dengan transisi yang sangat smooth (RECOMMENDED)
transform logo_smooth:
    xalign 0.5 yalign 0.52
    alpha 0.0 zoom 1.12 blur 8.0
    
    # Fase 1: Fade in dengan kurva yang konsisten
    parallel:
        easein_cubic 1.8 alpha 1.0
    parallel:
        # Gunakan easing yang sama untuk zoom dan blur agar sinkron
        easein_cubic 1.8 zoom 1.0 blur 0.0
    parallel:
        easein_cubic 1.8 yalign 0.5
    
    # Fase 2: Hold stabil tanpa movement (lebih clean)
    pause 2.0
    
    # Fase 3: Fade out smooth
    parallel:
        easeout_cubic 1.2 alpha 0.0
    parallel:
        easeout_cubic 1.2 zoom 1.05 blur 4.0

# Alternatif: Animasi dengan breathing subtle
transform logo_breathing:
    xalign 0.5 yalign 0.5
    alpha 0.0 zoom 1.1 blur 6.0
    
    # Entrance smooth & sinkron
    parallel:
        ease 2.0 alpha 1.0
    parallel:
        ease 2.0 zoom 1.0 blur 0.0
    
    # Breathing effect yang sangat halus
    block:
        linear 2.5 zoom 1.01
        linear 2.5 zoom 1.0
    
    # Exit clean
    parallel:
        ease 1.0 alpha 0.0
    parallel:
        ease 1.0 zoom 1.03 blur 3.0

# Animasi minimalis tanpa zoom (paling stabil)
transform logo_minimal:
    xalign 0.5 yalign 0.5
    alpha 0.0 blur 10.0
    
    # Hanya fade dan deblur, tanpa zoom
    parallel:
        ease 2.0 alpha 1.0
    parallel:
        ease 2.0 blur 0.0
    
    # Hold
    pause 2.5
    
    # Exit
    parallel:
        ease 1.0 alpha 0.0
    parallel:
        ease 1.0 blur 5.0

# Premium: Slow motion cinematic
transform logo_cinematic_pro:
    xalign 0.5 yalign 0.5
    alpha 0.0 zoom 1.08 blur 5.0
    
    # Entrance sangat lambat dan smooth
    parallel:
        easein_quint 2.5 alpha 1.0
    parallel:
        easein_quint 2.5 zoom 1.0 blur 0.0
    
    # Micro movement sangat subtle
    block:
        linear 3.0 yalign 0.502
        linear 3.0 yalign 0.498
    
    # Exit gentle
    parallel:
        easeout_quint 1.5 alpha 0.0
    parallel:
        easeout_quint 1.5 zoom 1.04 blur 3.0

# --- SPLASH SCREEN LABEL ---
label splashscreen:
    scene black
    with Pause(0.3)
    
    # PILIH SALAH SATU:
    
    # OPSI 1: Paling smooth & recommended
    show splash at logo_smooth
    with Pause(5.0)
    
    # OPSI 2: Dengan breathing subtle
    # show splash at logo_breathing
    # with Pause(7.0)
    
    # OPSI 3: Minimal tanpa zoom (paling stabil)
    # show splash at logo_minimal
    # with Pause(5.5)
    
    # OPSI 4: Cinematic slow-motion
    # show splash at logo_cinematic_pro
    # with Pause(7.5)
    
    scene black
    with Dissolve(0.5)
    
    return 

# --- BONUS: Audio enhancement (optional) ---
# Uncomment jika punya audio
# label splashscreen:
#     scene black
#     with Pause(0.3)
#     
#     play sound "audio/splash_whoosh.ogg" fadein 0.5
#     show splash at logo_cinematic
#     with Pause(5.5)
#     
#     scene black
#     with Dissolve(0.5)
#     return


# ================================================
# CHAPTER 1 - AWAL TAKDIR
# ================================================

label start:
    scene black
    with Dissolve(1.0)
    
    play music audio.rain1 fadein 1.0 volume 0.3
    
    centered "{color=#fff}Di suatu tempat, garis antara dua dunia mulai memudar...{/color}"
    pause 1.0
    centered "{color=#888}Dan seorang gadis berdiri tepat di tengahnya.{/color}"
    pause 1.0
    
    scene bg rumah_tua_malam
    with slow_dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    play sound audio.wind3 volume 2.0 
    n "Malam itu, udara menggantung begitu pekat."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bukan karena hujan yang mengetuk jendela dengan ritme lambat..."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Melainkan karena sesuatu yang menunggu di balik sunyi, mulai bangkit dari kegelapan."
    stop sound
    
    jump scene1_rumah_tua

# ===== SCENE 1: Rumah Tua =====
label scene1_rumah_tua:
    scene bg ruang_tamu_temaram
    with slow_dissolve
    
    play sound audio.wind1 volume 1.0 fadeout 0.3
    
    show carissa sedih at center
    with dissolve
    pause 1.0

    stop sound fadeout 1.0
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa duduk sendirian di ruang tamu yang remang-remang."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Hujan mengetuk jendela dengan ritme menenangkan, namun entah mengapa, hatinya justru terasa gelisah."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di tangannya, sebuah foto lama—wajah ibunya tersenyum lembut di samping neneknya."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    play sound audio.ngomongdewek volume 2.0 fadein 0.2
    c "(berbisik) Ibu... kenapa sih aku harus warisi semua ini?"
    
    play sound audio.heartbeat1 fadein 1.0
    n "Tiba-tiba, suara langkah kaki terdengar dari luar kamar."
    stop sound
    
    show carissa kaget
    with vpunch
    
    play sound audio.hit volume 2.0 fadeout 1.0
    c "Nek?"
    
    pause 1.0
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tidak ada jawaban."
    stop sound
    play sound audio.wind2 volume 2.0 fadeout 1.0
    n "Angin berhembus lembut ke arahnya, membawa dingin yang menusuk hingga ke tulang."
    stop sound
    
    show carissa takut

    play sound audio.gulp volume 1.5
    
    c "(menelan ludah) H-hiii!~"
    
    play sound audio.wind2 

    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sunyi yang mencekam membuat bulu kuduknya berdiri."
    stop sound
    
    stop music fadeout 2.0

    play sound audio.keyyi volume 1.0 fadeout 1.0
    play sound audio.bisikan volume 2.0 fadeout 1.0
    suara "Carissa..."
    stop sound

    show carissa takut at right
    with move
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(suara bergetar) Siapa?!"
    stop sound

    show cermin_bergetar at left
    with flash_white
    
    play sound audio.heartbeat1
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Cermin di meja rias bergetar pelan."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di pantulannya, sosok perempuan bergaun putih muncul—berdiri tepat di belakang Carissa."
    stop sound
    
    show hantu medium at center behind carissa
    with dissolve
    
    play sound audio.shock volume 2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

    show carissa kaget
    with vpunch
    

    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa berbalik dengan cepat—"
    stop sound
    
    hide hantu medium
    with flash_red
    play sound audio.nengok volume 2.0 fadeout 1.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "—kosong."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tidak ada siapa pun."
    stop sound
    
    show carissa sedih
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berbisik, hampir menangis) Ibu... Nenek..."
    stop sound
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(memejamkan mata kuat-kuat) Ini cuma mimpi... mimpi..."
    stop sound

    pause 1.0
   
    # show lilin at center with dissolve
    play sound audio.transisi volume 7.0
    c "(membuka mata) ...?!."
    stop sound
    
    play music audio.tensionh volume 1.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "(bergema) Gerbang mulai terbuka..."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "Kau... kuncinya..."
    stop sound
    
    show carissa takut
    with hpunch
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menutup telinga) Pergi... jangan ganggu aku!"
    stop sound
    
    hide lilin
    with flash_red
    
    play sound audio.wind3 volume 5.0
    
    n "Lilin padam seketika."
    
    scene black
    with Dissolve(2.0)
    
    stop music fadeout 3.0
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kegelapan menyelimuti segalanya dalam sekejap mata."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sepanjang malam, Carissa menatap langit-langit kamarnya tanpa tidur."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setiap kali memejamkan mata, suara dari cermin itu terpantul kembali di pikirannya."
    stop sound
    
    pause 1.0
    
    jump scene2_sekolah_pagi

# ===== SCENE 2: Sekolah Pagi =====
label scene2_sekolah_pagi:


    scene bg halaman_sekolah
    with slow_dissolve
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pagi berikutnya, matahari terasa redup meski waktu sudah menunjukkan pukul tujuh."
    stop souund
    
    show carissa bingung at center
    with dissolve
    
    play sound audio.footstep1x loop volume 1.0 
    n "Carissa berjalan dengan langkah terburu-buru menuju gerbang sekolah."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kantung matanya menghitam—jelas ia tak tidur semalaman."
    stop sound 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Siapa sih wanita yang muncul tadi malam..?"
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setiap kali memejamkan mata, wajah perempuan bergaun putih itu muncul kembali."
    stop sound
    
    play sound audio.foostephskl volume 4.0
    n "Suara langkah kaki terdengar di belakangnya."
    stop sound
    
    show carissa kaget 
    with hpunch
    
    play sound audio.noleh volume 3.0
    n "Carissa menoleh dengan cepat—"
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "—tidak ada siapa pun."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(gemetar) Aku yakin tadi ada yang ngikutin deh..."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa!"
    stop sound
    
    show carissa kaget at right
    with move
    
    show aksara normal at left
    with easeinleft
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa terlonjak kaget."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di bawah pohon besar, Aksara berdiri dengan payung dan tas selempang."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Wajahnya tenang, namun matanya menatap dengan dalam ke arah Carissa."
    stop sound
    
    show carissa normal 
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berusaha tersenyum) Jangan nakutin gitu dong! Kaget tau."
    stop sound
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu keliatan pucat. Ada sesuatu yang ganggu kamu?"
    stop sound
    
    show carissa bingung
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ih, sok tau!"
    stop sound
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap Carissa lama) ...Kamu beneran tidur nyenyak kan tadi malam?"
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Hah? emangnya napa?"
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Matamu... ada yang beda."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Jangan mulai hal aneh lagi deh, Aksara."
    stop sound
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu tau kan aku tinggal di kuil. Aku bisa ngerasain kalau ada roh yang ngikutin seseorang."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Senyum Carissa perlahan memudar, menatap Aksara dengan ekspresi campur aduk antara takut dan bingung."
    stop sound
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(ragu) Jadi... kamu ngerasa ada yang... ngikutin aku?"
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(diam sejenak) Bukan cuma ngikutin. Lebih ke... ada sesuatu yang kebuka, dan kayaknya lagi ngincar kamu."
    stop sound
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kebuka? Maksudnya?"
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengalihkan pandangan) Susah buat dijelasin. Tapi intinya... jangan anggep ini enteng."
    stop sound

    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menggenggam tas) ..."
    stop sound
    
    play sound audio.school_bell1
    
    n "Bel sekolah tiba-tiba berbunyi keras, memecah ketegangan di antara mereka berdua."
    n "Suara ramai siswa mengalir di halaman, namun bagi Carissa, semuanya terasa semakin tak nyaman."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ehhh, sampai jumpa Aks-."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggenggam tangan Carissa) Tunggu dulu."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatapnya lama, seperti menimbang sesuatu yang ia tahu namun enggan diucapkan."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Akhirnya ia menunduk dengan pasrah."
    stop sound
    
    play sound audio.menghela volume 2.0 fadeout 1.0
    a "(menghela napas) Tapi ingat satu hal—"
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Jangan percaya siapa pun yang bilang tau soal kamu... kecuali aku."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Oh iya, jangan lupa selalu bawa jimat ini kemana-mana."
    stop sound
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara memberi Carissa sebuah jimat yang tampak kecil—terbuat dari logam hitam dengan guratan simbol kuno di permukaannya."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di tengahnya tertanam pecahan batu merah gelap yang memantulkan cahaya samar."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatap Carissa lama. Matanya menajam, seperti sedang menimbang sesuatu yang bahkan ia takut akui."
    stop sound
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berkata pelan) Aku cuma nggak mau kehilangan orang lagi..."
    stop sound
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengerutkan kening, bingung dengan maksud kata-kata Aksara."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kata-kata itu menggantung di kepalanya, terasa seperti peringatan—atau sesuatu yang lebih dari yang terlihat."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun, Carissa mengenggam erat jimat itu di telapak tangannya saat mendengar nada ketakutan dari Aksara."
    stop sound
    
    scene black
    with Dissolve(1.0)
    
    jump scene3_kelas

# ===== SCENE 3: Kelas - Murid Baru =====
label scene3_kelas:
    scene bg kelas
    with dissolve
    
    play sound audio.schoolchatter1 volume 2.0
    n "Kelas sudah ramai dengan suara obrolan siswa. Ruangan itu dipenuhi canda tawa yang menggema di dinding."
    
    show carissa normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa duduk di bangkunya, masih memikirkan percakapan dengan Aksara tadi."
   
    play sound audio.dooropen1
    n "Pintu kelas terbuka."

    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Guru masuk bersama seseorang yang belum pernah Carissa lihat."
    stop sound
    
    show guru at left
    with easeinleft
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    guru "Anak-anak, perhatian sebentar!"
    
    stop sound fadeout 1.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kelas mulai hening."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    guru "Hari ini kita kedatangan murid baru. Perkenalkan, Dewa Abinaya."
    stop sound
    
    show dewa senyum at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Seorang pemuda berdiri dengan percaya diri."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Rambut pirangnya mencolok, matanya tajam namun entah kenapa terasa... menenangkan?"
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Senyumnya membuat setengah dari siswa di kelas terpana akan ketampanan yang tidak biasa dari siswa baru ini."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum ramah) Senang bertemu kalian. Semoga kita bisa akrab ya."
    stop sound
    
    hide dewa senyum
    show npc generic at center
    with dissolve
    
    play sound audio.berbucara volume 2.0 fadein 0.5 loop
    siswa1 "(berbisik) Ganteng banget..."
    siswa2 "(berbisik) Kayak misterius gitu ya."
    siswa3 "(berbisik) Namanya Dewa, cocok sih."
    stop sound
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa menatap pemuda itu tanpa sadar."
    stop sound
    
    show dewa misterius
    
    play sound audio.tensionh volume 2.0 fadeout 1.0
    n "Saat mata mereka bertemu, seolah waktu berhenti."
    stop sound
    
    show mata_biru at center
    with flash_white
    
    play sound audio.tensionh volume 2.0 fadeout 1.0
    n "Sekilas, Carissa melihat bayangan api biru berpendar di balik mata Dewa."
    stop sound
    
    hide mata_biru
    with dissolve
    
    show carissa kaget
    with vpunch
    
    play sound audio.hit volume 1.0
    c "(dalam hati, terkejut) Apa itu...? Kenapa matanya kayak bercahaya?"
    stop sound
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dewa tersenyum lembut ke arah Carissa... seolah-olah ia bisa menembus pikiran Carissa."
    stop sound
    
    hide dewa senyum
    with easeoutright
    
    show carissa bingung at right
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Kenapa dia natap aku kayak gitu? Ngeri ah..."
    stop sound
    
    hide guru
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Guru mempersilakan Dewa duduk."
    stop sound 
    play sound audio.footstep1x loop volume 2.0 fadeout 1.0
    n "Ia berjalan melewati bangku Carissa."
    stop sound
    with hpunch

    show carissa normal
    play sound audio.heartbeat3 volume 2.0 fadeout 1.0
    c "(dalam hati) Kenapa dadaku—"
    stop sound

    
    show carissa bingung
    play sound audio.winddah volume 1.0 fadeout 0.5
    c "(memeluk diri sendiri) Dingin..."
    stop sound
    
    scene black
    with Dissolve(1.0)
    
    jump scene4_perpustakaan

# ===== SCENE 4: Perpustakaan =====
label scene4_perpustakaan:
    scene bg perpustakaan
    with dissolve
    
    play music audio.mysterysound1 fadein 2.0 volume 0.2
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sore hari pun tiba. Carissa berada di perpustakaan yang sepi dan tenang."
    stop sound
    
    show carissa normal at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ia sibuk mencari buku untuk tugas kelompok, berjalan di antara rak-rak tinggi yang berjejer—membuat Carissa sedikit kewalahan."
    stop sound
    
    play sound audio.footstepperpus volume 3.0
    n "Langkah kaki pelan terdengar di balik sunyinya perpustakaan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    play sound audio.noleh volume 4.0
    n "Carissa pun menoleh, namun tidak ada seorang pun yang terlihat di sekitarnya."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Aku yakin tadi ada suara kayaknya..."
    play sound audio.whisper volume 2.0 fadeout 6.0
    d "(suara pelan dari belakang) Kamu sering sendirian ya."
    
    show carissa kaget at right
    with move
    with vpunch
    
    show dewa normal at left
    with easeinleft
    play sound audio.kagetperpus volume 2.0
    c "(terkejut) Dewa! Ngapain kamu ada di sini?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum) Hehehe... aku cuman gabut aja."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tertawa gugup) Ooohhh~ haha..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mencoba menenangkan diri, namun tatapan Dewa terlalu lama padanya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(santai tapi lembut) Kamu keliatan capek. Kayak lagi mikirin sesuatu yang berat."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(cepat) Ng-nggak! Aku cuma... kurang tidur aja."
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(mencondongkan tubuh sedikit) Hmm? Kamu bohongnya jelek banget."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa tertegun. Nada bicara Dewa terdengar ringan, namun membuat udara terasa sesak di dada Carissa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mencoba bercanda) Kamu pura-pura jadi cenayang ya? Bisa baca pikiran gitu."
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 fadeout 1.0
    d "(pelan) Aku ga bisa baca pikiran. Tapi aku bisa liat dari tatapan aja."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa hanya bisa menelan ludah, mencoba membalas tatapannya namun gagal."
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum kecil) Tenang aja, aku nggak bakal bilang ke siapa-siapa. Rahasia kecilmu aman sama aku."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berusaha santai) Rahasia? Aku ga ada ngomong apa-apa loh!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(mengangkat bahu) Siapa tau kamu punya sesuatu yang disembunyiin. Semua orang punya kan?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa ingin menjawab, namun suaranya seperti tersangkut di tenggorokan. Tatapan Dewa terlihat sama seperti sebelumnya."
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 
    play sound audio.ambilbuku volume 4.0
    d "(mengambil buku dari rak atas yang gak keliatan Carissa) Ini yang kamu cari?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Loh, kok kamu tau—"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum) Beruntung aja sih. (menatap cover buku) ...Mitos lokal ya? Tertarik sama cerita rakyat?" 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Eh... iya sih."
    play sound audio.balikbuku loop volume 4.0 fadeout 1.0
    d "(membalik-balik halaman)"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ehhh, kamu udah belum liatnya?"

    show dewa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menyodorkan buku pada Carissa) Nih, udah."

    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Byeee!!"
    
    hide dewa senyum
    with easeoutleft
    play sound audio.footstep1x loop volume 2.0 fadeout 1.0
    n "Langkah Dewa perlahan menjauh di antara rak-rak buku, meninggalkan aroma samar parfum yang menenangkan namun anehnya... terasa mencekam."
    
    show carissa sedih at center
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa masih berdiri di tempatnya, tenggelam dalam renungan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Untuk pertama kalinya, ia tidak tahu apakah harus takut... atau justru penasaran."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Siapa sebenarnya... Dewa?"
    
    scene black
    with Dissolve(1.0)
    
    jump scene5_halaman_belakang

# ===== SCENE 5: Halaman Belakang Sekolah =====
label scene5_halaman_belakang:
    scene bg halaman_belakang
    with dissolve
    
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setelah Carissa mengambil buku yang diperlukan, ia pun keluar dari sekolah dengan tangan penuh buku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di halaman sekolah."
    
    show aksara serius at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara duduk santai di taman, menatap ke arah perpustakaan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ia melihat sosok berambut pirang keluar dari pintu samping."
    
    show dewa misterius at right
    with easeinright
    play sound audio.tensionh volume 2.0 fadeout 1.0
    play sound audio.foostephskl volume 2.0 fadeout 1.0
    n "Dewa berjalan dengan tenang, lalu sekilas menatap ke arah Carissa yang baru keluar."
    
    hide dewa
    with easeoutright
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(dalam hati) Aura gelap itu... kenapa familiar?"
    
    show carissa normal at right
    with easeinright
    play sound audio.foostephskl volume 2.0 fadeout 1.0
    n "Carissa berjalan keluar, menatap langit yang mulai berubah jingga."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aksara! Kamu dari tadi di sini?"
    
    show aksara normal
    play sound audio.noleh volume 3.0
    a "(menoleh) Aku tadi liat ada orang yang barusan keluar. Kamu kenal nggak?"
    
    show carissa normal at center
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Hah? Oh itu murid baru, namanya Dewa."
    
    show aksara serius
    with vpunch
    play sound audio.shockdikit volume 2.0 fadeout 1.0
    a "(mendadak tegang) Kamu bilang... Dewa?"
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa menangkap perubahan mendadak pada wajah Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tangannya yang tadi santai di sisi tubuh, kini mengepal."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Iya... kenapa emangnya?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara diam sejenak, menatap ke arah tempat Dewa menghilang."
    
    menu:
        "Aksara, kamu gapapa?":
            play sound audio.select1 volume 6.0
            jump accept_aksara
        
        "Mungkin kebetulan aja namanya.":
            play sound audio.select1 volume 6.0
            jump not_suspected

label accept_aksara:
    $ aksara_points += 2
    
    show carissa khawatir
    play sound audio.footstep1xx volume 1.0
    c "(melangkah lebih dekat) Aksara, kamu gapapa? Kamu keliatan..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "...nggak kayak biasanya."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatapnya lama, seperti sedang mempertimbangkan sesuatu."
    
    play sound audio.menghela volume 2.0 fadeout 1.0
    a "(menghela napas) Carissa... nama itu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dewa..."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kenapa? Ada masalah sama namanya?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku... pernah denger nama itu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Entahlah, tapi rasanya familiar—bukan buat hal baik."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa merinding mendengar nada bicara Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Maksudmu...?"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggeleng) Aku nggak yakin. Mungkin aku salah ingat aja."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tapi... perasaanku nggak pernah salah soal hal-hal kayak gini."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatapnya dengan intensitas yang membuat jantung Carissa berdetak cepat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Janji sama aku... jangan terlalu deket sama dia sampai aku yakin sendiri."
    
    show carissa normal
    play sound audio.gulp volume 3.0 fadeout 1.0
    n "Carissa menelan ludah, merasakan keseriusan dari kata-kata Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun ia pun melakukan pinky promise dengan Aksara—mereka masing-masing mengaitkan jari kelingking satu sama lain."
    
    jump after_choo

label not_suspected:
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berusaha santai) Mungkin kamu pernah denger nama yang sama?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kan nama Dewa lumayan umum juga..."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatapnya dengan ekspresi yang sulit dibaca."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(pelan) ...mungkin."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun Carissa bisa melihat Aksara masih tegang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ada sesuatu yang tidak ia katakan."
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa, aku cuma mau bilang..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Hati-hati sama orang yang baru kamu kenal. Apapun yang dia katain."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengerutkan dahi, merasa ada yang aneh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun sebelum ia bisa bertanya lebih lanjut—"
    
    jump after_choo

label after_choo:
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap langit yang mulai gelap) Aku harus ke kuil. Kakek butuh bantuanku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap Carissa) Ingat yang aku bilang tadi pagi."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengangguk pelan, masih memikirkan reaksi aneh Aksara."
    
    hide aksara
    with easeoutleft
    play sound audio.foostephskl volume 1.0 fadeout 5.0
    n "Aksara berjalan pergi, meninggalkan Carissa sendirian."
    
    show carissa bingung at center
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Kenapa Aksara terlihat begitu... ketakutan?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Apa yang sebenarnya dia tau tentang Dewa?"
    
    play sound audio.windrumput volume 3.0 fadeout 1.0
    n "Angin tiba-tiba berhembus kencang."
    
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Daun-daun beterbangan."
    play sound audio.bisikan volume 1.0 fadeout 1.0
    suara "(bergema dari arah pohon) Carissa..."
    play sound audio.whisperr volume 1.0 fadeout 1.0
    suara "Darahmu... kunci kami..."
    
    show carissa takut
    with vpunch
    play sound audio.menoleh volume 3.0 fadeout 2.0
    c "(menoleh cepat) Siapa itu?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun tidak ada siapa-siapa."
    play sound audio.wind21 loop fadein 0.5
    n "Hanya hembusan angin dan bisikan yang perlahan memudar."
    
    scene bg langit_jingga
    with slow_dissolve
    
    jump chapter1_ending

label chapter1_ending:
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dalam perjalanan pulang, Carissa terus memikirkan peringatan Aksara dan tatapan misterius Dewa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Langit jingga senja menyelimuti kota, menandai berakhirnya hari yang penuh teka-teki."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Apa yang sebenarnya terjadi padanya? Dan apa yang akan terjadi selanjutnya?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dengan jimat Aksara tergenggam erat di tangannya, Carissa bersiap menghadapi malam yang penuh rahasia dan bahaya yang mungkin menantinya."
    
    scene black
    with Dissolve(2.0)
    
    jump chapter2_start

# ================================================
# CHAPTER 2 - RETAKAN DUA DUNIA
# ================================================

label chapter2_start:
    scene black
    with Dissolve(2.0)
    
    centered "{color=#fff}Tiga hari kemudian...{/color}"
    pause 1.5

    # ===== SCENE BARU: Morning Routine =====
    scene bg kamar_carissa with dissolve
    play sound audio.alarm_clock volume 3.0

    show carissa normal at center with dissolve
    play sound audio.yawn volume 3.0 fadeout 1.0
    c "(menguap) Hmmm... pagi lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa melakukan rutinitas pagi seperti biasa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Gosok gigi, mandi, sarapan bersama Nenek..."

    scene bg ruang_makan with dissolve
    show nenek senyum at left
    show carissa normal at right with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Sarapan dulu, Nduk. Nenek buatin nasi goreng kesukaan kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersenyum) Wah, makasih Nek!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Semuanya terasa normal."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Terlalu normal."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Seperti ketenangan sebelum badai..."

    jump scene1_mimpi_buruk

# ===== SCENE 1: Mimpi Buruk & Minigame 1 =====
label scene1_mimpi_buruk:
    scene black
    with nightmare_transition
    
    play music audio.heartbeat2 fadein 2.0
    n "Sekarang malam hari, Carissa terlelap dalam tidur yang gelisah."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun tidurnya bukanlah tidur yang menenangkan."
    
    centered "{color=#8b0000}Dunia Mimpi{/color}"
    pause 2.0
    
    scene bg ruang_tamu_temaram
    with nightmare_transition
    
    play sound audio.wind2 volume 4.0
    
    show carissa bingung at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(melihat sekeliling) Ini... kamarku?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi kenapa... warnanya aneh?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Seluruh ruangan berwarna merah gelap dan ungu pucat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bayangan-bayangan bergerak di dinding tanpa sumber cahaya."
    play sound audio.bisikan volume 2.0
    suara "(bergema dari segala arah) Carissaaaa..."
    
    show carissa takut
    with vpunch
    play sound audio.ngengg volume 2.0 fadeout 1.0
    c "Ini mimpi! Ini pasti mimpi!"
    
    show hantu medium at left
    with flash_white
    
    play sound audio.heartbeat1 fadein 0.3 fadeout 1.0
    n "Sosok-sosok gelap mulai muncul dari balik pintu."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka mendekat dengan gerakan tidak wajar—meluncur tanpa kaki."
    play sound audio.whisperr volume 1.0 fadeout 1.0
    suara "Darahmu..."
    play sound audio.whisperr volume 1.0 fadeout 1.0
    suara "Beri kami..."
    
    show carissa kaget
    play sound audio.female volume 2.0 
    c "(berteriak) PERGI! JANGAN DEKATI AKU!"
    
    # MINIGAME 1: Dodge Game
    # NOTE: Simple dodge/avoid game menggunakan arrow keys
    # Tutorial Ren'Py: search "renpy dodge game tutorial" di YouTube
    # Konsep: Player gerakkan Carissa dengan arrow keys untuk hindari hantu
    # Durasi: 30 detik
    # Jika kena hantu 3x: game over, ulangi
    # Jika berhasil: lanjut ke dialog sukses
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengepal kedua tangannya dengan erat."
    play sound audio.larii2 volume 1.0 fadeout 1.0
    n "Ia berlari menghindari bayangan-bayangan yang mengejarnya."
    
    show hantu medium at right
    with dissolve
    play sound audio.larii2 volume 1.0 fadeout 0.2
    c "(berlari) AKU HARUS BANGUN!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Detik demi detik berlalu—bayangan semakin dekat dengan jumlah yang banyak."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka membentuk formasi lingkaran yang besar, mengepung Carissa secara perlahan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa semakin ketakutan, meringkuk dengan badannya yang mungil."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun tiba-tiba, secercah cahaya biru menyinari sekeliling Carissa."

    hide carissa_kaget with dissolve
    hide hantu_medium with dissolve
    scene none
    call minigame_dodge

    
    scene ruang_tamu_temaram
    hide hantu medium
    with flash_blue
    play sound audio.scream volume 2.0 fadeout 1.0
    n "Bayangan-bayangan itu menjerit dan menghilang satu per satu."
    
    show carissa_kaget at center
    play sound audio.breathcapek volume 2.0 fadeout 1.0
    c "(terengah-engah) A-apa itu tadi?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa masih terpana dengan kejadian barusan—tidak percaya dengan mata kepalanya sendiri."
    
    with flash_white
    
    scene bg kamar_carissa
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa terbangun dengan napas tersengal."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Keringat dingin membasahi dahinya."
    
    show carissa takut at center
    with vpunch
    play sound audio.huh volume 1.0 fadeout 1.0
    c "(terbangun) Hah... hah..."
    play sound audio.detikjam fadeout 1.0
    n "Jam di meja menunjukkan pukul 5 pagi."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(gemetar) Mimpi tadi..."
    
    play sound audio.phonevibrate volume 2.0 fadein 0.5 fadeout 1.0
    n "Alarm ponsel berbunyi—waktunya bersiap ke sekolah."
    stop sound
    
    scene black
    with Dissolve(1.0)
    
    jump scene2_perjalanan_pagi

# ===== SCENE 2: Perjalanan Pagi =====
label scene2_perjalanan_pagi:
    scene bg jalan_kota
    with slow_dissolve
    
    play music audio.mysterykripy loop fadein 0.5 volume 0.2
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pagi itu terasa berbeda. Udara lebih berat dari biasanya."
    
    show carissa sedih at center
    with dissolve
    play sound audio.footstep1x loop volume 1.0 fadeout 1.0
    n "Carissa berjalan menuju sekolah dengan langkah terburu-buru."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tidurnya semalam penuh mimpi buruk—sama seperti malam sebelumnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun, Carissa melupakan sesuatu—jimat."
    
    show carissa kaget
    with vpunch
    play sound audio.gasp volume 1.0 fadeout 1.0
    c "Astaga! Jimatnya ketinggalan!"
    
    play sound audio.windrumput volume 3.0 fadein 0.3 fadeout 1.0
    n "Tiba-tiba, angin bertiup kencang. Dedaunan kering beterbangan tak karuan."
    play sound audio.bisikan volume 3.0 fadeout 1.0
    suara "(bergema dari segala arah) Carissaaaa..."
    
    show carissa takut
    play sound audio.footstep1x volume 4.0 fadeout 1.0
    c "(mundur) Eh...?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bayangan-bayangan mulai muncul dari berbagai sudut jalan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sosok-sosok transparan dengan mata kosong mulai mendekat."
    play sound audio.whisper volume 1.0 fadeout 1.0
    suara "Tanpa pelindung..."
    play sound audio.whisperr volume 1.0 fadeout 1.0
    suara "Kau milik kami..."
    
    show carissa kaget
    play sound audio.female volume 1.0 fadeout 1.0
    c "(berteriak) JANGAN MENDEKAT PERGI SANAA!"
    
    hide carissa kaget
    with dissolve
    play sound audio.lariaspal volume 1.0 fadeout 4.0
    n "Carissa berlari sekuat tenaga menuju gerbang sekolah."
    play sound audio.lariaspal volume 1.0 fadein 1.0 fadeout 1.0
    n "Bayangan-bayangan itu mengejarnya dengan kecepatan tidak wajar."
    
    play sound audio.lariaspal fadein 0.4 fadeout 0.2 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun tepat saat ia hampir tersudut—"
    
    with flash_blue
    play sound audio.tensionh volume 1.0 fadeout 1.0
    n "Lagi-lagi cahaya biru yang sama terpancar dari tubuh Carissa."
    stop sound
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bayangan-bayangan itu menjerit dan menghilang satu per satu."
    
    show carissa normal at center
    play sound audio.breathcapek volume 1.0 fadeout 1.0
    c "(terengah-engah) Hah... hah... aman..."
    play sound audio.heartbeat1 volume 1.0 fadeout 2.0
    n "Carissa merasakan jantungnya berdegup kencang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Aku harus lebih hati-hati... tapi cahaya biru tadi... darimana asalnya?"
    
    scene black
    with Dissolve(1.0)
    
    jump scene3_praktik_lapangan

# ===== SCENE 3: Praktik Lapangan - Interaksi dengan Dewa =====
label scene3_praktik_lapangan:
    scene bg halaman_belakang
    with dissolve
    
    play music audio.mysterysound2 volume 0.4 fadein 1.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Jam pelajaran ketiga. Praktik Biologi di luar kelas."
    
    show guru at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    guru "Baik anak-anak, hari ini kita akan belajar tentang ekosistem taman sekolah."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    guru "Kalian sudah dibagi kelompok berpasangan. Silakan cari area masing-masing."
    
    show carissa normal at center
    with easeinright
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa melihat daftar kelompok di papan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Kelompok 5... Carissa dan..."
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dewa?"
    
    show dewa senyum at right
    with easeinright
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum ramah) Sepertinya kita satu kelompok nih!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Mohon kerjasamanya Carissa."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c " Mohon kerjasamanya juga Dewa. Ayo kita mulai saja."
    
    hide guru
    with dissolve
    
    scene bg halaman_belakang
    with dissolve
    
    show carissa normal at left
    show dewa normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka berjalan ke area yang lebih sepi di belakang taman."
    play sound audio.windrumput volume 1.0 fadeout 1.0
    n "Hanya terdengar suara angin dan dedaunan yang bergesek."
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kamu tau nggak, aku perhatiin kamu dari hari pertama aku masuk."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(melirik) Kamu stalker ya?!"
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 fadeout 1.0
    d "Haha, bukan gitu maksudku..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Ada sesuatu yang kamu miiki... yang nggak ada di orang lain."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menegang) M-maksudnya?"
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tertawa kecil) Hahaha, kenapa? Emang ga boleh ya aku bilang gitu?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dewa berjongkok, mengambil sampel tanah dengan tenang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa memperhatikan dalam diam. Gerakannya anggun namun... terasa janggal."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Kenapa setiap kali dia di dekatku, ada hawa aneh tapi terasa nyaman untukku?"
    
    play sound audio.wind3 volume 3.0
    n "Angin tiba-tiba berhembus kencang."
    
    show dewa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Carissa, kamu... percaya sama hal-hal gaib?"
    
    show carissa kaget
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "K-kenapa tiba-tiba nanya gitu?"
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 fadeout 1.0
    d "(menatap langit) Yah... cuma penasaran aja sih."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum tipis) Kan jawaban orang beda-beda."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(pelan) A-aku... sebenernya pernah ngalamin hal-hal yang nggak bisa dijelasin sih."
    
    show dewa senyum
    play sound audio.nengok volume 1.0 fadeout 4.0
    d "(menoleh cepat, matanya berbinar) Oh iya?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Ceritain dong, kepo nih sama pengalamanmu."
    
    menu:
        "Ceritakan sedikit tentang pengalaman mistis":
            jump tell_dewa
        
        "Hindari topik, alihkan pembicaraan":
            jump avoid_dewa_talk

label tell_dewa:
    $ dewa_points += 2
    
    show carissa sedih
    play sound audio.menghela volume 1.0 fadeout 1.0
    c "(menghela napas) Sejak kecil, aku sering liat... bayangan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Sosok-sosok yang nggak bisa dilihat sama orang biasa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kadang ada yang cuma lewat, tapi ada juga yang sampe natap aku lama banget."
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 fadeout 1.0
    n "Mata Dewa berubah. Ada kilauan biru samar di dalamnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(serius) Kamu takut?"
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Iya sih, soalnya ini baru pertama kalinya..."
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum lembut) Mungkin kamu nggak harus takut."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Mungkin... mereka cuma butuh dimengerti."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Dewa) Kamu ngomong seolah kamu paham mereka."
    
    show dewa normal
    play sound audio.noleh volume 1.0 fadeout 1.0
    d "(mengangkat bahu) Siapa tau?"
    
    jump after_dewa_choice_scene3

label avoid_dewa_talk:
    $ aksara_points += 1
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tertawa gugup) Hahahha, buat apa coba? Menurutku itu cuma efek halusinasi aja tau."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Udah yuk kita selesain praktiknya. Nanti dikumpulin lho."
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 fadeout 1.0
    n "Dewa menatapnya lama. Ada kekecewaan samar di wajahnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(pelan) Hmm... baiklah."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Nada suaranya membuat Carissa merinding."
    
    jump after_dewa_choice_scene3

label after_dewa_choice_scene3:
    play sound audio.windrumput fadein 0.5 volume 3.0
    n "Angin berhembus pelan. Dedaunan kering beterbangan di mana-mana."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Dewa melanjutkan praktik yang tercantum di kertas ilmiah tersebut."
    
    show dewa senyum at center
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Ya ampun... kamu fokus banget sih."
    
    show carissa bingung
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "O-oiya?"
    
    show dewa senyum at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Iya. Jarang liat orang segitu seriusnya waktu praktik."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Senyum Dewa tampak ramah, namun tatapannya... sulit ditebak."
    
    scene black
    with Dissolve(1.0)
    
    jump scene4_kantin_siang

# ===== SCENE 4: Kantin Siang - Konflik Pertama =====
label scene4_kantin_siang:
    scene bg kantin
    with dissolve
    
    play music audio.mysterysound4 volume 0.5 fadein 1.0
    play sound audio.schoolchatter1 volume 3.0 fadeout 1.0
    n "Jam istirahat tiba. Kantin ramai dipenuhi lautan siswa yang sedang mengantri makanan."
    
    show carissa normal at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa duduk sendirian di sudut, memakan soto ayamnya dengan pelan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Hari ini aneh banget... apalagi si Dewa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Saat Carissa sedang berkecamuk dengan pikirannya sendiri, datang seseorang dari arah kirinya."
    
    show aksara khawatir at left
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(duduk di sebelah Carissa) Kamu gapapa?"
    
    show carissa normal
    play sound audio.noleh volume 3.0
    c "(menoleh) Iya, aku gapapa kok."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu yakin?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatapnya dengan serius."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa, aku mau nanya. Kamu... lagi deket sama Dewa?"
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kamu tau dari mana?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku lihat dari lantai 3 pas kamu ada pelajaran di luar kelas tadi..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kalian ngobrolin apa?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ga perlu khawatir Aksara, dia nggak ngapa-ngapain aku kok."
    
    show aksara serius
    play sound audio.menghela volume 3.0 fadeout 1.0
    a "(menghela napas) Aku nggak yakin kamu bilang gitu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Feeling-ku bilang kalo dia berbahaya buat kamu. Kemarin aku sudah bilang kan kalo jangan deket-deket si Dewa itu."
    
    show dewa senyum at right
    with easeinright
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum) Lagi pada ngomongin aku ya?"
    
    show aksara serius at left
    show carissa kaget at center
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara dan Carissa tersentak."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap tajam) Kenapa kepo?"
    
    show dewa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Aku kan punya telinga~ kebetulan juga aku lewat kok."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap Aksara) Tapi kayaknya kamu nggak suka sama aku ya?"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(dingin) Aku cuma mau melindungi temanku."
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 fadeout 1.0
    d "(senyum tipis) Melindungi? Dari apa?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Atau... dari siapa?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ketegangan di antara mereka membuat atmosfer sekitar terasa mencekam."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(cemas) Sudah, jangan berantem..."
    
    menu:
        "Bela Aksara - 'Aksara cuma khawatir sama aku'":
            jump defend_aksara_scene4
        
        "Bela Dewa - 'Dewa nggak berbahaya kok, Aksara'":
            jump defend_dewa_scene4
        
        "Netral - 'Kalian berdua kenapa sih? Jangan kayak gini'":
            jump neutral_scene4

label defend_aksara_scene4:
    $ aksara_points += 3
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aksara cuma khawatir sama aku, Dewa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dia udah ngebantu aku dari dulu."
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 fadeout 1.0
    n "Dewa terdiam. Ada kilatan kecewa di matanya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(pelan) Oke... kalau itu maumu."
    
    hide dewa misterius
    with easeoutright
    
    show aksara normal at center
    with move
    play sound audio.breathhus volume 3.0 fadeout 2.0
    a "(menghela napas lega) Makasih, Carissa."

    scene bg koridor_sekolah 
    with dissolve
    show dewa misterius at center with dissolve
    play sound audio.tensionh volume 2.0 fadeout 1.0
    d "(menatap dari jauh) ...Menarik."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Semakin kau melindunginya... semakin besar kekuatannya nanti."
    hide dewa with dissolve
    
    jump after_kantin_choice

label defend_dewa_scene4:
    $ dewa_points += 3
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dewa nggak berbahaya kok, Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dia baik sama aku."
    
    show aksara sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(kecewa) Carissa..."
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum ke arah Aksara) Tuh, dia sendiri yang ngomong."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap Carissa) Aku janji nggak bakal sakitin kamu."
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengepalkan tangan) ...aku harap kamu nggak menyesal, Carissa."
    
    hide aksara khawatir
    with easeoutleft
    
    jump after_kantin_choice

label neutral_scene4:
    $ aksara_points += 1
    $ dewa_points += 1
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kalian berdua kenapa sih?! Please, jangan kayak gini..."
    
    show aksara normal
    play sound audio.menghela volume 3.0 fadeout 1.0
    a "(menghela napas) Baiklah..."
    
    show dewa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Oke... aku ngerti."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suasana masih terasa tegang, namun setidaknya keadaan masih terkondisi dengan baik."
    
    jump after_kantin_choice

label after_kantin_choice:
    scene black
    with Dissolve(1.0)
    play sound audio.jampel volume 3.0 fadeout 1.0 #bell
    n "Bel masuk berbunyi. Ketegangan perlahan mulai mereda."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun Carissa tahu... ini baru permulaan."
    
    jump scene5_perpustakaan_sore

# ===== SCENE 5: Perpustakaan Sore - Minigame 2 =====
label scene5_perpustakaan_sore:
    scene bg perpustakaan
    with dissolve
    
    play music audio.mysterysound2 volume 0.5 fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sepulang sekolah, Carissa memutuskan mencari informasi di perpustakaan tua dekat rumahnya."
    
    show carissa normal at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Mungkin... ada buku soal hal-hal gaib?"
    
    play sound audio.ambilbuku volume 2.0
    n "Jari-jarinya menelusuri punggung buku yang berdebu."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Mitologi Mistis... Penjaga Gerbang... Segel Jimat Kuno..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengambil buku tebal berjudul 'Dua Dunia: Pengenalan'."
    
    play sound audio.bookopen volume 2.0
    c "(membaca) 'Dalam kepercayaan kuno, ada garis tipis antara dunia manusia dan dunia roh...'"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "'Gerbang ini dijaga oleh Penjaga yang ditakdirkan. Jika gerbang terbuka...'"
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dunia akan..."
    
    play sound audio.heartbeat1 fadeout 1.0
    
    with flash_white
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Lampu perpustakaan berkedip. Buku di tangannya melayang, berpencar menjadi tiga titik cahaya berwarna hitam."
    
    play sound audio.wind3 volume 1.0
    suara "(bergema) Jangan tahu terlalu banyak..."
    
    show hantu weak at left
    with flash_white
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(gemetar) A-apa ini?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Jimat Aksara di sakunya berkedip merah redup, membentuk tiga jalur cahaya menuju rak-rak berbeda."
    
    # MINIGAME 2: Point & Click / Hidden Object
    # NOTE: Puzzle mencari buku yang tepat
    # Tutorial Ren'Py: search "renpy point and click game" atau "renpy hidden object"
    # Konsep: Tampilkan beberapa rak buku, player klik buku yang bercahaya merah
    # Ada 3 buku khusus yang harus ditemukan:
    # 1. "Penjaga Gerbang"
    # 2. "Ritual Segel Kuno"
    # 3. "Rakta"
    # Buku yang benar: bercahaya merah samar
    # Buku salah: efek negatif (screen shake, suara bisikan)
    # Tidak ada time limit, tapi ada pressure dari efek visual/audio
    
   
    play sound audio.laridulu volume 2.0 fadeout 1.0
    n "Carissa berlari mengikuti jalur pertama."
    
    play sound audio.success
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Penjaga Gerbang..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Jalur kedua membawanya ke balik tumpukan buku."
    
    play sound audio.success
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ritual Segel Kuno..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Jalur terakhir mengarah ke rak tertinggi."
    
    play sound audio.success
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Rakta!"
    
    hide hantu weak
    with flash_white
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bayangan-bayangan lenyap begitu ketiga buku terkumpul."
    
    show carissa sedih at center
    play sound audio.capek volume 1.0 fadeout 1.0
    c "(terengah-engah) Akhirnya..."
    play sound audio.bookopen volume 1.0 fadeout 1.0
    n "Carissa membuka buku 'Rakta' dengan tangan gemetar."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(membaca) 'Dalam dua abad sekali, akan muncul seseorang dengan darah Rakta...'"
    play sound audio.bookflip1 volume 1.0 fadeout 1.0
    c "'Mereka memiliki kemampuan melihat dan berkomunikasi dengan dunia roh...'"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "'Darah mereka adalah kunci pembuka gerbang...'"

    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Maksudnya apa semua ini? Darah rakta? Kunci gerbang?"
    
    show aksara serius at right
    with easeinright
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa!"
    
    show carissa kaget at left
    with move
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aksara?! Dari mana kamu—"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku ngerasain jimatku bereaksi kuat. Kamu... kenapa cari tahu hal-hal kayak gini?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatap ketiga buku di pelukan Carissa dengan ekspresi cemas."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "A-aku cuma..."
    
    show aksara serius
    play sound audio.footstep1x volume 1.0
    a "(mendekat) Carissa, kenapa tiba-tiba kamu nyari tau hal ini?"
    
    menu:
        "Jujur - 'Iya, aku butuh tau apa yang terjadi sama aku'":
            jump honest_aksara
        
        "Bohong - 'Enggak kok, cuma penasaran aja'":
            jump lie_aksara

label honest_aksara:
    $ aksara_points += 3
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menunduk) Iya... aku butuh tau apa yang sebenarnya terjadi sama aku, Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Mimpi buruk terus, bayangan-bayangan yang ngikutin... aku takut."
    
    show aksara khawatir
    play sound audio.menghela volume 3.0 fadeout 1.0
    a "(menghela napas, duduk di sebelah Carissa) Makasih udah jujur."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku paham perasaan kamu. Tapi... ini berbahaya, Carissa."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Makanya aku harus tau! Aku ga bisa terus-terusan ketakutan kayak gini."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum tipis) Baiklahh..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(serius lagi) Tapi janji sama aku, kalau ada apa-apa langsung hubungi aku."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Janji."
    
    jump after_choice_scene5

label lie_aksara:
    $ aksara_points -= 1
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tertawa gugup) Enggak kok! Aku cuma... penasaran aja."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kan lagi tugas sejarah, butuh referensi mitos lokal."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatapnya lama. Matanya tajam, seolah bisa melihat kebohongan Carissa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(pelan) Kamu bohong."
    
    show carissa kaget
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "A-aku nggak—"
    
    show aksara sedih
    play sound audio.menghela volume 1.0 fadeout 1.0
    a "(menghela napas) Kita udah kenal dari kecil, Carissa. Aku tau kapan kamu bohong..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku takut kamu kenapa-kenapa cuma karena hal-hal yang kamu cari tau sendirian."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Maaf, Aksara..."
    
    jump after_choice_scene5

label after_choice_scene5:
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Yaudah, lagian dah sore nih. Ayo balik bareng..."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(senyum kecil) Oke!"
    
    hide carissa senyum
    hide aksara normal
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka berdua berjalan keluar dari perpustakaan."
    
    scene bg perpustakaan
    with dissolve
    
    play sound audio.wind
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Keheningan kembali menyelimuti ruangan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di balik rak buku paling belakang, sebuah bayangan gelap mengintip."
    
    show bayangan at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "(bergema pelan) Jadi, sudah dimulai..."
    
    show mata_biru at center behind bayangan
    with flash_blue
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "(tertawa pelan) Dia akan menjadi milikku..."
    
    hide bayangan
    hide mata_biru
    with flash_white
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bayangan itu menghilang, meninggalkan hawa dingin yang mencekam."
    
    scene black
    with Dissolve(2.0)
    
    jump scene6_hari_libur

# ===== SCENE 6: Hari Libur - Pagi di Rumah =====
label scene6_hari_libur:
    scene black
    with Dissolve(1.0)
    
    centered "{color=#fff}Hari Sabtu - Sekolah Diliburkan{/color}"
    pause 1.5
    
    scene bg kamar_carissa
    with dissolve
    
    play music audio.mysterysound4 fadein 3.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pagi yang tenang. Carissa terbangun dengan perasaan lega—hari ini libur."
    
    show carissa normal at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(meregangkan badan) Akhirnya bisa istirahat..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun ketenangan itu hanya sesaat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mimpi semalam masih membekas, wajah-wajah tanpa rupa serta bisikan-bisikan asing yang mengganggu."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menyentuh kalung di lehernya) Kalung ini..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sebuah kalung perak dengan liontin berbentuk bulan sabit."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pemberian ibunya saat Carissa masih kecil."
    
    show kalung_glow at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berbisik) Kenapa akhir-akhir ini sering hangat?"
    
    hide kalung_glow
    with dissolve
    
    play sound audio.dooropen1 volume 3.0
    nenek "(dari luar) Carissa, sarapan!"
    
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek normal at left
    show carissa normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa duduk di meja makan bersama neneknya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aroma nasi goreng dan teh hangat mengisi ruangan."
    
    show nenek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Kamu keliatan capek, Nduk. Sekolahmu berat ya?"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nek... aku mau tanya sesuatu."
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(berhenti mengunyah) ada apa, Nduk?"
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Soal... Ibu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nenek pernah cerita kalo Ibu sering ngalamin hal-hal aneh, kan?"
    
    show nenek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Nenek terdiam. Tangannya yang memegang cangkir sedikit bergetar."
    play sound audio.menghela volume 3.0 fadeout 1.0
    nenek "(menghela napas) Iya..."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku... akhir-akhir ini sering liat sesuatu, Nek."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Bayangan-bayangan sama suara-suara yang nggak ada orangnya."
    
    show nenek khawatir
    with vpunch
    play sound audio.kagetperpus volume 1.0 fadeout 1.0
    nenek "(terkejut) Carissa..."
    
    menu:
        "Tanya tentang orang tua - 'Kenapa Ibu juga bisa liat, Nek?'":
            jump ask_parents
        
        "Tanya tentang kalung - 'Kalung ini... ada hubungannya?'":
            jump ask_necklace

label ask_parents:
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kenapa Ibu juga bisa liat, Nek?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Itu sudah menjadi warisan nenek moyang kita, Nduk."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Tapi, kamu sama Ibumu itu berbeda dari yang lainnya."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Berbeda gimana?"
    
    show nenek normal
    play sound audio.ngaduk volume 3.0 fadeout 1.0
    nenek "(mengaduk tehnya pelan) Nenek, Ibu, sama kamu... kita semua itu bisa melihat 'mereka'."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Hanya saja... Ibumu dulu cepat mempelajari apa yang dilatih."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dilatih?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(mengangguk) Ibumu belajar cara melawan mereka, cara melindungi diri, cara bikin segel..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Dia kuat, Nduk. Sangat kuat."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(pelan) Terus kenapa... aku nggak diajarin juga?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Nenek terdiam lama. Matanya berkaca-kaca."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(suara bergetar) Karena Ibumu nggak mau kamu ngalamin hal yang sama."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Dia bilang... 'Biar aku saja yang terakhir, Mbok. Carissa harus hidup normal.'"
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi akhirnya... tetep aja aku ngalamin ini."
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(menggenggam tangan Carissa) Iya, Nduk... maafin Nenek."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Yang penting sekarang... kamu harus hati-hati."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi Nek—"
    
    show nenek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(memotong) Carissa, dengerin Nenek."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Kamu punya sesuatu yang istimewa. Lebih dari Nenek, bahkan lebih dari Ibumu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Makanya... 'mereka' tertarik sama kamu."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Istimewa apanya? Aku cuma bisa melihat doang, Nek. Aku nggak bisa apa-apa!"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(mengusap pipi Carissa) Justru itu yang bikin kamu berbahaya, Nduk."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berbisik) Nek..."
    
    show nenek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(memeluk Carissa) Tenang aja, Nduk. Kan ada Nenek sama Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Dan... kalung itu."

    hide nenek senyum
    hide carissa takut
    with dissolve 
    jump after_choice_scene6

label ask_necklace:
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menyentuh kalung) Kalung ini... ada hubungannya sama yang aku alami?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(menatap kalung) Itu... kalung untuk melindungmu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Ibumu sendiri yang memberikan waktu kamu masih bayi."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Bayi? Jadi... aku udah punya ini dari dulu?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(mengangguk) Itu pemberian terakhir Ibumu sebelum dia..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(terhenti) ...sebelum dia pergi."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Pelindung dari apa, Nek?"
    
    show nenek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "...yang penting kamu jangan lepas kalung itu ya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Apapun yang terjadi."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Baik, Nek..."
    
    hide nenek normal
    hide carissa normal 
    with dissolve
    jump after_choice_scene6

label after_choice_scene6:
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka melanjutkan sarapan dalam keadaan hening."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Meski begitu, pikiran Carissa masih berkecamuk tentang informasi yang baru saja dia dapatkan."
    
    scene black
    with Dissolve(2.0)
    
    jump scene7_siang

label scene7_siang:
    scene bg ruang_tamu_terang
    with dissolve
    
    stop music fadeout 2.0
    play music audio.mysterysound1 volume 0.5 fadein 0.5
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Siang itu, matahari bersinar cerah."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa duduk santai di ruang tamu, scrolling ponselnya tanpa tujuan."
    
    show carissa normal at center
    with dissolve
    play sound audio.gasp volume 1.0 fadeout 1.0
    c "(menguap) Bingung mau ngapain..."
    
    play sound audio.door_open
    
    show nenek senyum at left
    with easeinleft
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Carissa, bantuin Nenek yuk!"
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Oke! Bantuin apa emangnya, Nek?"
    
    show nenek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Nenek mau bikin kue lapis sama gulai ayam."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Carissa kan udah besar, harus bisa masak juga."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tertawa) Iya deh, Nek~"
    
    scene black
    with Dissolve(1.0)
    
    # MINIGAME 3: Cooking Game
    # NOTE: Memory/Pattern game - ikuti resep dengan benar
    # Tutorial Ren'Py: search "renpy cooking game" atau "renpy memory game"
    # Konsep:
    # - Nenek kasih instruksi bumbu/bahan yang harus dimasukkan
    # - Player pilih bahan yang benar dari 4-6 pilihan
    # - Ada 5 tahap memasak
    # - Jika salah: masakan gosong/hambar, retry
    # - Jika benar semua: dapat masakan sempurna, bonding moment
    
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek normal at left
    show carissa normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di dapur yang hangat, Carissa dan neneknya mulai memasak."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Oke, sekarang kita bikin gulai ayam dulu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Carissa, ambilkan bawang merah sama bawang putih."
    
    # Simulasi minigame
    centered "{color=#fff}=== MEMASAK BERSAMA NENEK ==={/color}"
    pause 1.0
    
    menu:
        nenek "Tahap 1: Bumbu dasar apa yang harus ditumis dulu?"
        
        "Bawang merah & bawang putih":
            jump cooking_correct1
        
        "Kunyit & jahe":
            jump cooking_wrong1
        
        "Kemiri & ketumbar":
            jump cooking_wrong1

label cooking_wrong1:
    show nenek khawatir
    
    nenek "Aduh, bukan itu sayang. Coba lagi ya."
    
    menu:
        nenek "Bumbu dasar yang ditumis pertama adalah..."
        
        "Bawang merah & bawang putih":
            jump cooking_correct1

label cooking_correct1:
    play sound audio.success
    
    show nenek senyum
    
    nenek "Nah, bener! Pinter!"
    
    show carissa senyum
    
    c "Hehe, aku kan pernah liatin Nenek masak~"
    
    n "Aroma bawang tumis mengisi seisi dapur."
    
    menu:
        nenek "Tahap 2: Sekarang masukkan rempah apa?"
        
        "Serai & daun jeruk":
            jump cooking_wrong2
        
        "Kunyit, ketumbar & kemiri":
            jump cooking_correct2
        
        "Cabai & tomat":
            jump cooking_wrong2

label cooking_wrong2:
    show nenek khawatir
    
    nenek "Hmm, belum tepat. Coba yang lain."
    
    menu:
        nenek "Rempah yang bikin gulai harum adalah..."
        
        "Kunyit, ketumbar & kemiri":
            jump cooking_correct2

label cooking_correct2:
    play sound audio.success
    
    show nenek senyum
    
    nenek "Bagus! Sekarang aduk rata ya."
    
    show carissa normal
    
    c "Wah, wanginya udah keluar nih!"
    
    menu:
        nenek "Tahap 3: Kapan kita masukkan ayamnya?"
        
        "Setelah bumbu harum":
            jump cooking_correct3
        
        "Sebelum bumbu mateng":
            jump cooking_wrong3
        
        "Bersamaan dengan santan":
            jump cooking_wrong3

label cooking_wrong3:
    show nenek khawatir
    
    nenek "Wah, nanti ayamnya nggak meresap bumbunya."
    
    menu:
        nenek "Ayam dimasukkan saat..."
        
        "Setelah bumbu harum":
            jump cooking_correct3

label cooking_correct3:
    play sound audio.success
    
    show nenek senyum
    
    nenek "Tepat sekali! Sekarang tumis ayamnya sampai berubah warna."
    
    show carissa senyum
    
    c "Aku yang aduk ya, Nek!"
    
    menu:
        nenek "Tahap 4: Setelah ayam setengah matang, kita tambahkan apa?"
        
        "Air & santan":
            jump cooking_correct4
        
        "Garam & gula":
            jump cooking_wrong4
        
        "Kecap & saus":
            jump cooking_wrong4

label cooking_wrong4:
    show nenek khawatir
    
    nenek "Belum waktunya, sayang. Coba lagi."
    
    menu:
        nenek "Yang ditambahkan setelah ayam setengah matang..."
        
        "Air & santan":
            jump cooking_correct4

label cooking_correct4:
    play sound audio.success
    
    show nenek senyum
    
    nenek "Iya! Sekarang tunggu sampai mendidih."
    
    show carissa normal
    
    n "Mereka menunggu sambil sesekali mengaduk gulai."
    
    menu:
        nenek "Tahap 5: Terakhir, bumbu penyedap apa yang ditambahin?"
        
        "Garam, gula & kaldu bubuk":
            jump cooking_correct5
        
        "Merica & pala":
            jump cooking_wrong5
        
        "Cuka & kecap":
            jump cooking_wrong5

label cooking_wrong5:
    show nenek khawatir
    
    nenek "Hmm, nanti rasanya jadi aneh loh."
    
    menu:
        nenek "Bumbu penyedap yang pas untuk gulai..."
        
        "Garam, gula & kaldu bubuk":
            jump cooking_correct5

label cooking_correct5:
    play sound audio.success
    
    show nenek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Sempurna! Carissa hebat!"
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Yeay! Aku berhasil!"
    
    centered "{color=#0f0}★ GULAI AYAM BERHASIL DIBUAT! ★{/color}"
    pause 1.5
    
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek senyum at left
    show carissa senyum at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setelah gulai matang, mereka berdua duduk santai sambil menunggu nasi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Carissa makin pinter masak nih!"
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Hehe, makasih Nek. Aku belajar dari yang terbaik!"
    
    show nenek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(tersenyum lembut) Ibumu juga dulu suka bantuin Nenek masak."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Dia jago bikin rendang, loh."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(pelan) Aku... pengen bisa kayak Ibu."
    
    show nenek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(mengelus kepala Carissa) Kamu pasti bisa, sayang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Kamu keturunan ibumu. Pasti bisa dan lebih enak rasanya."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Heheheh, makasih ya Nek udah jagain aku selama ini."
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(memeluk Carissa) Nenek yang harusnya makasih sama kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Kamu sudah menjadi cucu yang baik buat Nenek."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka berdua memeluk dalam keheningan yang hangat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Moment sederhana yang terasa begitu berharga."
    
    hide carissa senyum
    hide nenek khawatir
    scene black
    with Dissolve(2.0)
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Siang itu berlalu dengan hangat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun di balik kehangatan itu, bayangan ancaman mulai mendekat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa tidak tahu... Bahaya sedang menunggunya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Apakah besok akan jadi hari yang mengubah segalanya? atau hanya pikiranya saja?"
    pause 1.0

    centered "{color=#fff}Seminggu Kemudian...{/color}"
    pause 1.5
    
    scene bg halaman_sekolah
    with dissolve
    
    play music audio.mysteryfum loop volume 1.0 fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pagi yang cerah di sekolah."
    play sound audio.larii2 loop volume 2.0 fadeout 1.0
    n "Siswa berlalu-lalang di koridor dengan riuh."
    
    show carissa normal at right
    with easeinright
    play sound footstepperpus loop volume 3.0 fadeout 1.0
    n "Carissa berjalan menuju kelasnya sambil bermain ponsel."
    
    play sound audio.footsteps
    
    show aksara normal at left
    with easeinleft
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dari arah berlawanan, Aksara berjalan sambil membawa setumpuk buku tebal."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berseru) Aksaraa!"
    
    show aksara senyum
    play sound audio.menoleh volume 1.0 fadeout 1.0
    a "(menoleh) Hai, Carissa!"
    
    show carissa normal at center
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(melihat buku-buku) Wah, banyak banget. Kamu habis kemana?"
    
    show aksara normal
    play sound audio.ambilbuku volume 3.0
    a "(mengangkat buku) Ini habis ke perpus, buat ngembaliin buku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Udah telat seminggu, takut kena denda."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tertawa) Hahaha, kamu tuh jarang banget telat. Pasti sibuk di kuil ya?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Iya... Kakek lagi butuh bantuan lebih banyak akhir-akhir ini."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Oh iya, tadi aku denger dari Bu Retno kalau besok angkatan kita ada outing class."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Hah? Bukannya bulan depan ya?"
    
    show aksara kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Loh, emang belum dikasih tau sama wali kelas kamu?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aneh juga sih, kok kelasmu nggak dapet pemberitahuan."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Hmm, mungkin Bu Sari lupa ngasih tau kali. Biasa deh, suka telat update."
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tertawa kecil) Hahaha, iya juga sih."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Terus kemana emang outing class-nya?"

    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dari yang aku denger sih, kita bakal ke candi-candi gitu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Buat pelajaran sejarah."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengerutkan kening) Candi? Candi apa?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kalau nggak salah... Candi Reksana Sewu."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(pelan) Reksana Sewu..."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Aksara) Kamu kayaknya pernah ke sana kan?"
    
    show aksara serius
    play sound audio.menghela volume 3.0 fadeout 1.0
    a "(menghela napas) Iya... Cuma sekali aja sih."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggeleng) Ah, sudahlah..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Yang penting kamu jangan lupa bawa jimat yang aku kasih ya."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Iya iya, tenang aja. Aku selalu bawa kok."
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Baguslah."
    
    play sound audio.school_bell
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bel masuk berbunyi."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Keburu telat nih. Nanti kita ngobrol lagi ya!"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Oke. Hati-hati di jalan."
    
    hide carissa senyum
    with easeoutright
    
    hide aksara normal
    with easeoutleft
    scene black
    with Dissolve(1.0)
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara menatap punggung Carissa yang menjauh dengan tatapan tidak biasa."
    
    jump scene8_outing_class

# ===== SCENE 8: Outing Class di Candi - Hari H =====
label scene8_outing_class:
    scene black
    with Dissolve(2.0)
    
    centered "{color=#fff}Hari Outing Class pun tiba{/color}"
    pause 1.5
    
    scene bg dalam_bus
    with dissolve
    
    play sound audio.bus_engine fadein 2.0
    play music audio.mystery_theme fadein 3.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pagi itu, bus sekolah melaju meninggalkan kota."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suara mesin dan obrolan siswa memenuhi perjalanan."
    
    show carissa normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa duduk di dekat jendela, menatap pemandangan yang berlalu."
    
    show dewa senyum at center
    with easeinright
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(muncul dari bangku belakang) Hei! Ngapain ngelamun?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nggak lah, ini lagi nikmatin pemandangan aja kok."
    
    show dewa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(duduk di sandaran kursi) Hmm, masa sih?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap Carissa) Kamu excited nggak ke candinya?"
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Lumayan sih, aku belum pernah ke sana soalnya."
    
    show dewa misterius
    play sound audio.tensionh volume 2.0 fadeout 1.0
    d "(tersenyum aneh) Tempatnya keren loh!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kamu bakal ngerasain sesuatu yang berbeda di sana."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "emang kamu udah pernah ke sana?"
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Hmm... Yahh, bisa dibilang gitu."
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    guru "(dari depan bus) Anak-anak, kita sudah sampai!"
    
    scene bg candi_gerbang
    with slow_dissolve
    
    stop sound fadeout 2.0
    play sound audio.busstop volume 2.0 fadeout 1.0
    n "Bus berhenti di depan gerbang besar Candi Reksana Sewu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bangunan kuno menjulang tinggi dengan ukiran-ukiran yang rumit."
    
    show carissa bingung at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap candi) Wow... besar banget."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setelah Aksara turun dari busnya, ia menghampiri Carissa yang sibuk berselfi-selfi di sekitar candi."
    
    show aksara normal at left
    with easeinleft
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Gimana perjalanannya tadi?"

    show carissa normal 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Amann dongg."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Lagi-lagi aku ngerasain energi gelap yang kuat..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Seperti hembusan angin, Dewa berjalan menghampiri Carissa dan Aksara. Mereka berdua terkejut dengan kehadiran Dewa yang tiba-tiba."

    show dewa misterius at right
    with easeinright
    play sound audio.tensionh volume 2.0 fadeout 1.0
    d "(tersenyum sambil menatap kalung Carissa) Warnanya cantik... seperti bulan di malam kelahiranmu."
    
    show aksara serius
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menoleh tajam) Apa yang kamu bilang?"
    
    show dewa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tertawa) Haha, cuma becanda kok!"
    
    hide dewa senyum
    with easeoutright
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Aksara) Dia... aneh nggak sih?" 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(serius) Emang, kan aku dah bilang. Pokoknya jangan tinggalin aku ya. Apapun yang terjadi."
    
    show carissa takut
    play sound audio.gulp volume 3.0 fadeout 1.0
    c "(menelan ludah) K-kamu bikin aku takut..."

    hide aksara serius 
    with easeoutleft

    hide carissa takut
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    guru "Baiklah anak-anak! Kita akan dibagi menjadi beberapa kelompok."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    guru "Kelompok 1 akan explore bagian utara, kelompok 2 bagian selatan..."
    
    scene black
    with Dissolve(1.0)
    
    
    
    scene bg candi_gerbang
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setelah pembagian kelompok, Carissa dan Aksara berada di kelompok yang sama."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka bersama rombongan berjalan memasuki area dalam candi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Udara terasa lebih dingin saat mereka memasuki lorong batu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Cahaya matahari hampir tidak tembus masuk."
    
    show npc generic at center
    with dissolve    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    siswa2 "Kok gelap banget ya?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    siswa3 "(menyalakan senter ponsel) Iya, bikin merinding deh!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    siswa1 "Guys, kalian ngerasa dingin nggak sih?"
    

    play sound audio.wind4 loop volume 3.0 fadeout 1.0
    n "Angin tiba-tiba berhembus kencang dari dalam candi."
    
    show npc generic
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    siswa1 "Wah! Dari mana anginnya tuh?!" 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Para siswa mulai ketakutan dan bergaduh satu sama lain."
    
    show npc generic at left
    with dissolve

    show pemandu at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    p "Tenang semuanya!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    p "Struktur candinya memang buat aliran udara jadi terasa kencang."

    hide npc generic
    hide pemandu
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di sisi lain, Carissa mendengar samar-samar bisikan dari pantulan dinding-dinding."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suara itu berbeda dari keributan siswa lainnya."
    play sound audio.bisikan volume 3.0 fadeout 1.0
    suara "(bergema dari kedalaman candi) Carissaaaa..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "Akhirnya... kau datang..."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(gemetar) S-suara itu lagi!"
    
    show aksara serius at left
    with dissolve
    play sound audio.nengok volume 3.0 fadeout 1.0
    a "(menoleh cepat) Kamu dengar sesuatu?"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berbisik) Ada... ada yang manggil namaku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Jimat di saku Carissa bergetar makin kencang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kalung di lehernya mulai bersinar samar."

    show jimat_glow at Position(xpos=0.5, ypos=0.6)

    with dissolve
    
    show kalung_glow at Position(xpos=0.5, ypos=0.55)
 
    with flash_blue
    
    show aksara serius
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap kalung) Carissa, kalungmu—!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tiba-tiba lantai candi bergetar."
    with hpunch


    show npc generic at right behind aksara
    with dissolve
    play sound audio.gempa volume 3.0 fadeout 1.0
    siswa1 "(panik) GEMPA!"
    play sound audio.larii2 loop volume 4.0 fadeout 1.0
    siswa2 "KELUAR! KITA HARUS KELUAR!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    p "(berteriak) TENANG! JANGAN PANIK! IKUT AKU!"
    
    hide jimat_glow
    hide kalung_glow
    with dissolve
    play sound audio.larii2 volume 3.0 fadeout 1.0
    n "Semua siswa berlarian menuju pintu keluar."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun Carissa terpaku di tempat, menatap lorong dalam candi."
    
    show carissa takut at center
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Kenapa... kenapa aku ngerasa harus ke sana?"
    
    show aksara khawatir at left
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menarik tangan Carissa) Carissa! Kita harus keluar!"
    
    hide npc generic
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi Carissa tidak bergerak. Matanya seperti terhipnotis."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "(lebih keras) DATANGLAH KE SINI!"
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(pelan) Aku... harus ke sana..."
    
    show aksara serius
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggeleng) JANGAN! CARISSA, DENGAR AKU!"
    menu:
        "Apa yang harus dilakukan Carissa?"
        
        "Ikuti kata Aksara dan keluar dari candi":
            jump listen_aksara_ending
        
        "Ikuti suara yang memanggil ke dalam candi":
            jump follow_voice_ending
        
        "Tetap di tempat, tidak kemana-mana":
            jump stay_neutral_ending

# ===== GOOD ENDING ROUTE =====
label listen_aksara_ending:
    $ aksara_points += 5
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "O-oke!"
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Bagus! Ayo cepat!"
    
    hide carissa normal
    hide aksara senyum
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Aksara berlari menuju pintu keluar."
    
    play sound audio.running
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di belakang mereka, bayangan-bayangan mulai muncul dari kegelapan."
    
    show hantu weak at center
    with flash_red
    play sound audio.scream volume 1.0 fadeout 1.0
    suara "(menjerit) JANGAN PERGI!"
    
    show carissa kaget at right
    show aksara serius at left
    with dissolve
    play sound audio.menoleh volume 3.0 fadeout 1.0
    c "(menoleh) A-apa itu?!"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menarik Carissa lebih kencang) JANGAN LIHAT! TERUS LARI!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara mengeluarkan jimat berbentuk permata biru dari sakunya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Jimat itu bersinar terang, membentuk perisai di belakang mereka."
    
    show aura_biru at left
    with flash_blue
    
    play sound audio.magic
    play sound audio.keyyi volume 1.0 fadeout 1.0 
    n "Bayangan-bayangan itu terpental dan tidak bisa mendekat."
    
    hide hantu weak
    with flash_white
    
    hide aura_biru
    with dissolve
    
    scene bg candi_gerbang
    with Dissolve(1.0)
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka berhasil keluar tepat waktu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pintu candi tertutup dengan sendirinya di belakang mereka."
    
    show carissa sedih at right
    show aksara khawatir at left
    with dissolve
    play sound audio.breathcapek volume 3.0 fadeout 1.0
    c "(terengah-engah) Hah... hah... Itu tadi... apa?"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum lega) Yang penting kita selamat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu dengerin aku, dan itu yang paling penting."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Makasih, Aksara... Kalau nggak ada kamu..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Untuk itu aku ada, kan?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(serius lagi) Tapi kita harus hati-hati. "
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Iya... Aku ngerti kok."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di kejauhan, Dewa berdiri sambil menatap mereka."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ekspresinya tidak terbaca."
    
    show dewa misterius at center behind aksara
    with dissolve
    play sound audio.tensionh volume 2.0 fadeout 1.0
    d "(dalam hati) Hmm... menarik."

    hide aksara normal
    hide carissa sedih
    hide dewa misterius
    with dissolve
    
    jump good_ending_chapter2

# ===== BAD ENDING ROUTE =====
label follow_voice_ending:
    $ dewa_points += 3
    $ aksara_points -= 3
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(melepas tangan Aksara) A-aku... harus ke sana."
    
    show aksara kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "CARISSA! JANGAN!"
    
    hide carissa bingung
    with easeoutright
    play sound audio.runn volume 3.0 fadeout 4.0
    n "Carissa berlari ke dalam kegelapan candi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mengikuti suara yang terus memanggilnya."
    
    play sound audio.running
    
    show aksara sedih at center
    with move
    play sound audio.panic volume 1.0 fadeout 1.0
    a "(berteriak) CARISSA!"
    play sound audio.runn volume 2.0 fadeout 1.0
    n "Aksara mencoba mengejar, tapi..."
    
    with hpunch
    play sound audio.batu volume 3.0 fadeout 1.0
    n "Pintu batu besar jatuh, memblokir jalannya."
    play sound audio.mukul loop volume 4.0 fadeout 1.0
    a "(memukul pintu) CARISSA! JAWAB AKU!"
    
    scene black
    with Dissolve(1.0)
    play sound audio.footstep1x loop volume 3.0 fadeout 1.0
    n "Di dalam kegelapan, Carissa terus berjalan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suara itu semakin jelas."
    
    show carissa takut at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(ketakutan) H-halo? Siapa di sana?"
    
    show dewa wujud_asli at right
    with flash_red
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(suara berbeda, lebih dalam) Akhirnya... kau datang sendiri."
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "D-Dewa?! Kenapa wujudmu—"
    
    show dewa wujud_asli
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Ini wujud asliku, Carissa."
    
    show aura_merah at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aura merah gelap menyelimuti Dewa."
    
    show carissa takut
    play sound audio.footstep1x volume 3.0 fadeout 1.0
    c "(mundur) A-aku... aku harus balik!"
    
    show dewa wujud_asli
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(mengangkat tangan) Sudah terlambat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa merasakan tubuhnya tidak bisa bergerak."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "A-apa yang kamu lakukan?!"
    
    show dewa wujud_asli
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Tenang... aku tidak akan sakiti kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kamu terlalu berharga untuk dilukai."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di luar, Aksara masih berusaha membuka pintu."
    
    hide carissa kaget
    hide dewa wujud_asli
    hide aura_merah
    with dissolve
    
    show aksara sedih at center
    with dissolve
    play sound audio.nangis volume 1.0 fadeout 1.0
    a "(menangis) Carissa... Kenapa kamu nggak dengerin aku..."
    
    scene black
    with Dissolve(2.0)
    play sound audio.batugeser volume 1.0 fadeout 1.0
    n "Ketika pintu akhirnya terbuka, Aksara menemukan Carissa terbaring tidak sadarkan diri."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sedangkan Dewa sudah menghilang dalam kegelapan."
    
    jump bad_ending_chapter2

# ===== NEUTRAL ENDING ROUTE =====
label stay_neutral_ending:
    $ aksara_points += 1
    $ dewa_points += 1
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(bingung) A-aku... aku nggak tau harus gimana!"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa, fokus! Lihat aku!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara memegang kedua bahu Carissa dengan erat."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tarik napas... dan ikuti aku perlahan."
    
    show carissa normal
    play sound audio.menarik volume 3.0
    c "(menarik napas) H-huh... O-oke..."
    play sound audio.footstep1x loop volume 3.0 fadeout 1.0
    n "Perlahan, mereka berjalan mundur menuju pintu keluar."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suara itu masih terus memanggil, tapi Carissa berusaha mengabaikannya."
    play sound audio.bisikan volume 3.0 fadeout 1.0
    suara "(semakin lemah) Carissa... jangan pergi..."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menutup telinga) Pergi... pergi dari kepalaku!"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Hampir sampai... terus bergerak!"
    
    play sound audio.runn volume 2.0
    n "Mereka berdua akhirnya sampai di pintu keluar."
    
    scene bg candi_gerbang
    with Dissolve(1.0)
    
    show carissa sedih at right
    show aksara khawatir at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(terduduk) Huh... huh... kenapa... kenapa aku hampir ngikutin suara itu?"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengelus punggung Carissa) Karena mereka punya pengaruh ke kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tapi yang penting... kamu bertahan."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku... masih bingung, Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Apa sebenarnya yang terjadi sama aku?"
    
    show aksara khawatir
    play sound audio.menghela volume 3.0 fadeout 1.0
    a "(menghela napas) Aku juga belum yakin sepenuhnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tapi satu hal yang pasti... kamu istimewa, Carissa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dan itu yang bikin kamu jadi target."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Istimewa... atau dikutuk?"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tergantung gimana kamu ngeliatnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di antara gerombolan siswa yang sudah keluar dari dalam candi, Dewa muncul sambil mengamati mereka berdua di baliknya."
    
    show dewa normal at center
    with dissolve
    
    hide dewa normal
    hide aksara normal
    hide carissa sedih
    with dissolve
    
    jump neutral_ending_chapter2

# ===== GOOD ENDING CHAPTER 2 =====
label good_ending_chapter2:
    scene bg halaman_sekolah
    with slow_dissolve
    
    play music audio.mystery_theme fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kembali ke sekolah, suasana sudah lebih tenang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Rombongan kelompok Carissa serta Guru menganggap getaran tadi hanya gempa kecil biasa."
    
    show carissa normal at right
    show aksara normal at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu yakin gapapa?"
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Iya, aku oke kok. Makasih ya, Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kalau nggak ada kamu... aku nggak tau bakal gimana."
    
    play sound audio.phonevibrate

    show carissa bingung
    play sound audio.phonevibrate volume 2.0 fadeout 1.0
    c "(lihat HP) ...?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ada pesan dari nomor tidak dikenal."

    centered "{color=#8b0000}'Kamu lolos... untuk sekarang.'{/color}"
    pause 1.0
    centered "{color=#8b0000}'Tapi lain kali... kamu tidak akan seberuntung ini.'{/color}"
    pause 1.0

    show carissa takut with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "A-Aksara..."

    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Ada apa?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menunjukkan HP) Ini..."

    show aksara kaget with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dari siapa itu?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "A-aku gatau."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Keduanya pun hanya bisa terdiam lama mengetahui hal ini."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Siapa yang sedang mengancam mereka?"

scene black with Dissolve(2.0)

centered "{color=#0f0}★ GOOD ENDING - KEPERCAYAAN YANG KUAT ★{/color}"
centered "{color=#fff}Tapi... benarkah ini berakhir?{/color}"

# ===== BAD ENDING CHAPTER 2 =====
label bad_ending_chapter2:
    scene bg ruang_tamu_temaram
    with slow_dissolve
    
    play music audio.tension fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa terbangun di kamarnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ia tidak ingat bagaimana ia bisa pulang."
    
    show carissa bingung at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(memegang kepala) Kepalaku... sakit banget."
    
    show nenek khawatir at left
    with easeinleft
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Carissa! Syukurlah kamu udah bangun, Nduk."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Kamu pingsan di candi tadi. Aksara yang bawa kamu pulang."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aksara? Di mana dia?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Dia langsung pergi setelah nganterin kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Mukanya sedih banget, Nduk."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Aksara... maafin aku..."
    
    hide nenek khawatir
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengambil ponselnya, mencoba menghubungi Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi tidak ada jawaban."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dia... marah sama aku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di pojok kamar, bayangan Dewa muncul sekilas."
    
    show dewa misterius at right
    with dissolve
    play sound audio.tensionh volume 2.0 fadeout 1.0
    play sound audio.bisikan volume 5.0
    d "(berbisik) Baru sekarang menyesal?"
    
    hide dewa misterius
    with dissolve
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Siapa?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi tidak ada siapa-siapa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Hanya keheningan yang mencekam."
    
    scene bg langit_jingga
    with slow_dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Senja tiba dengan cepat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa menatap ponselnya, berharap Aksara akan membalas pesannya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi tidak ada balasan."
    
    centered "{color=#f00}★ BAD ENDING - KEPERCAYAAN YANG RAPUH ★{/color}"
    pause 2.0
    
    centered "{color=#fff}Chapter 2 - SELESAI{/color}"
    pause 2.0
    
    centered "{color=#888}Pilihanmu telah merenggangkan hubungan dengan Aksara...{/color}"
    centered "{color=#888}Akankah kalian bisa memperbaikinya?{/color}"
    pause 2.0
    

# ===== NEUTRAL ENDING CHAPTER 2 =====
label neutral_ending_chapter2:
    scene bg halaman_sekolah
    with slow_dissolve
    
    play music audio.mysterysound3 fadein 2.0 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Perjalanan pulang terasa sunyi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Aksara duduk berdampingan di bus, tapi tidak banyak bicara."
    
    show carissa sedih at right
    show aksara khawatir at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu... masih denger suara-suara aneh?"
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menggeleng) Nggak. Udah berkurang kok."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Syukurlah..."
    play sound audio.menghela volume 3.0 fadeout 1.0
    a "(menghela napas) Tapi aku khawatir ini cuma baru permulaannya aja."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Maksudnya?"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Mereka udah tau siapa kamu. Dan mereka nggak akan berhenti sampai dapet apa yang mereka mau."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ohhh..."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kita harus lebih hati-hati."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dan... kamu harus mulai belajar melindungi diri."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku... nggak yakin bisa."
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu bisa. Aku percaya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum tipis) Lagipula, kamu nggak sendirian."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Makasih, Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun di dalam hati Carissa, masih ada keraguan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suara itu... terasa begitu meyakinkan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bagian dirinya masih penasaran... apa yang sebenarnya ada di dalam candi?"
    
    scene bg langit_jingga
    with slow_dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Senja menyelimuti kota dengan warna oranye kemerahan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa berdiri di antara dua pilihan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Percaya sepenuhnya pada Aksara... atau mencari tahu sendiri kebenarannya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Jalan mana yang akan ia pilih?"
    
    centered "{color=#ffaa00}★ NEUTRAL ENDING - DI PERSIMPANGAN JALAN ★{/color}"
    pause 2.0
    
    centered "{color=#fff}Chapter 2 - SELESAI{/color}"
    pause 2.0
    
    centered "{color=#888}Kamu berdiri di tengah jalan...{/color}"
    centered "{color=#888}Pilihan selanjutnya akan menentukan nasibmu...{/color}"
    pause 2.0

    jump chapter3_start

# ================================================
# CHAPTER 3 - GERBANG YANG TERBUKA
# ================================================

# SCENE 1 - CHAPTER 3
label chapter3_start:
    scene black
    with Dissolve(2.0)
    
    play music audio.tension fadein 3.0
    
    centered "{color=#fff}Tiga hari setelah kejadian di candi...{/color}"
    pause 1.5
    
    if aksara_points > dewa_points + 3:
        jump chapter3_scene1_good_start
    elif dewa_points > aksara_points + 3:
        jump chapter3_scene1_bad_start
    else:
        jump chapter3_scene1_neutral_start


label chapter3_scene1_good_start:
    scene bg kamar_carissa
    with dissolve
    
    play music audio.mysterykripy loop fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pagi itu, Carissa bangun dengan perasaan lebih tenang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Meski kejadian di candi masih membayangi, ia merasa lebih siap menghadapinya."
    
    show carissa normal at center
    with dissolve

    show kalung_glow at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kalung ibunya bergetar lembut. Lebih hangat dari biasanya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(bingung) Aneh..."
    
    hide kalung_glow
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Matanya tertuju ke kotak kayu di atas lemari yang sedari dulu ia selalu penasaran akan isinya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bentuk kotak tersebut terlihat berdebu."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Hmmmm, aku kepo."
    
    jump chapter3_scene2

label chapter3_scene1_bad_start:
    scene bg kamar_carissa
    with dissolve
    
    play music audio.tension fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa terbangun dengan nafas tersengal."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mimpi buruk lagi. Kali ini lebih menyeramkan dari sebelumnya."
    
    show carissa sedih at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(memegang kepala) Kenapa... kenapa aku nggak dengerin Aksara waktu itu?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ia meraih ponselnya. 3 hari tanpa kontak dengan Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pesannya terlihat dibaca saja tapi tidak ada balasan."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(gemetar) Jangan-jangan..."
    
    play sound audio.bisikan volume 2.0 fadeout 1.0
    suara "(berbisik lembut) Carissa..."
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Suara itu lagi?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    show kalung_glow at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kalung di lehernya bersinar redup."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "Jangan takut... Aku cuma mau bantu kamu..."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(ragu) Bantu... aku?"
    
    hide kalung_glow
    with flash_white
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suara itu menghilang, meninggalkan Carissa dalam kebingungan."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Apa... apa yang harus aku lakukan?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dalam renungan penyesalan, Carissa tanpa sadar melihat seisi kamarnya secara seksama."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Lalu, ia cukup terkejut dengan adanya kotak kayu berdebu di atas lemarinya karena ia tidak pernah menyadari benda tersebut selama bertahun-tahun."

    show carissa bingung
    with hpunch 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Apa ya isi kotak itu?"
    
    jump chapter3_scene2

label chapter3_scene1_neutral_start:
    scene bg kamar_carissa
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa duduk di tepi tempat tidur, menatap ponselnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ada pesan dari Aksara sejak semalam, tapi ia belum membalasnya."
    
    show carissa bingung at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(membaca pesan) 'Carissa, kita perlu ngobrol. Ada yang harus aku jelasin.'"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Jari-jarinya menggantung di atas keyboard."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ia ingin membalas, tapi tidak tahu harus bilang apa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Aku... masih bingung sama yang terjadi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi aku juga nggak bisa terus-terusan hindarin dia."
    

    show kalung_glow at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kalung ibunya bergetar pelan, seolah merespons kegelisahannya."
    
    hide kalung_glow
    with dissolve

    show carissa normal
    with dissolve
    play sound audio.menghela volume 3.0 fadeout 1.0
    c "(menghela napas) Mungkin... aku harus cari tau sendiri dulu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ia melirik ke arah atas lemarinya, disana terdapat kotak kayu berdebu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tiga hari yang lalu, Carissa sempat sadar ada kotak tersebut seusai pulang dari studi tour."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi, ia memilih abai saat itu karena mungkin isinya tidak terlalu penting."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun, saat ini Carissa berpikir ulang..."
    play sound audio.keyyi volume 1.0 fadeout 1.0 
    c "Mungkin, ada petunjuk disitu...?"

    jump chapter3_scene2

# SCENE 2 - CHAPTER 3
label chapter3_scene2:
    scene bg kamar_carissa
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa memutuskan untuk membuka kotak kayu tersebut."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sudah bertahun-tahun kotak itu tersimpan, tidak tersentuh."
    
    show carissa normal at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa berjinjit saat hendak mengambil kotak. Ia pun akhirnya berhasil menurunkannya dari lemari."

    
    play sound audio.bukakotak volume 3.0 fadeout 1.0
    n "Kotak terbuka dengan bunyi derit pelan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Debu beterbangan di udara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di dalamnya: sebuah buku catatan tua, beberapa foto, dan sepotong kain merah yang sudah pudar."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ini... buku catatan Ibu?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengambil foto-foto lama."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Foto pertama: Ibunya masih muda, berdiri di depan kuil dengan beberapa orang berpakaian tradisional."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(membaca tulisan di belakang foto) 'Pertemuan Nirantara, 2007...'"
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nirantara? Apa itu?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Foto kedua: Ibunya sedang hamil besar, berdiri di depan candi saat... gerhana bulan."
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ini... waktu Ibu lagi hamil?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ada tulisan di belakang: 'Malam kelahiran yang ditakdirkan. Semoga dia tidak menanggung beban ini.'"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(air mata menetes) Ibu..."
    
    hide carissa sedih
    with dissolve

    play sound audio.bookopen volume 3.0 
    n "Carissa membuka buku catatan dengan tangan gemetar."
    stop sound

    play sound audio.bookflip1 volume 1.0
    centered "{i}'16 Tahun yang lalu...'{/i}"
    stop sound
    pause 1.0
    play sound audio.bookflip1 volume 1.0
    centered "{i}'Hari ini aku melahirkan Carissa.'{/i}"
    pause 1.0
    play sound audio.bookflip1 volume 3.0
    centered "{i}'Tepat saat gerhana bulan.'{/i}"
    pause 1.0
    
    play sound audio.bookflip1 volume 3.0
    
    centered "{i}'Para tetua Nirantara bilang... Carissa adalah Pembawa Darah Rakta.'{/i}"
    pause 1.0
    play sound audio.bookflip1 volume 3.0
    centered "{i}'Aku takut. Sangat takut.'{/i}"
    pause 1.0
    play sound audio.bookflip1 volume 3.0
    centered "{i}'Tapi aku akan lindungi dia. Apapun yang terjadi.'{/i}"
    pause 1.5
    
    show carissa sedih
    with dissolve
    
    c "(menangis) Jadi... aku..."
    

    play sound audio.bookflip1 volume 3.0

    centered "{i}'2 tahun kemudian...'{/i}"
    pause 1.0
    play sound audio.bookflip1 volume 3.0
    centered "{i}'Dewa Abinaya mulai bergerak.'{/i}"
    pause 1.0
    play sound audio.bookflip1 volume 3.0
    centered "{i}'Dia tau tentang Carissa. Dia akan datang.'{/i}"
    pause 1.5
    
    show carissa kaget
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dewa... Abinaya?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(terkejut) Nama itu... sama kayak—"
    
    
    show kalung_glow at center
    with flash_red
    
    play sound audio.heartbeat3 volume 2.0
    n "Kalung di leher Carissa tiba-tiba menyala merah terang!"
    
    show carissa takut
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "A-apaan ini?!"
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pandangan Carissa kabur. Ruangan berputar."
    
    scene black
    with flash_white
    

    play music audio.tensionmusic loop volume 2.0 fadein 2.0
    
    centered "{color=#8b0000}Pecahan Memori{/color}"
    pause 1.0
    
    scene bg candi_gerbang
    with nightmare_transition
    play sound audio.transisi volume 3.0 
    n "Carissa menemukan dirinya berdiri di depan gerbang besar."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi ini bukan dirinya. Dia... melihat dari mata orang lain."
    
    show carissa bingung at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(suara bergema) Di mana... ini?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Di depannya, gerbang batu besar bergetar hebat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Retakan mulai muncul di permukaannya."
    
    show dewa wujud_asli at right
    with dissolve
    
    show aura_merah at right
    with flash_red
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(suara bergema, marah) BUKA GERBANG INI!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "BIARKAN AKU LEWAT!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dari balik gerbang, sosok besar dengan aura merah menyeramkan mencoba menembus."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tangan di depan Carissa (tangan ibunya) terangkat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Energi biru bersinar, membentuk segel."
    
    show aura_biru at left
    with flash_blue
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ibunya berbisik mantra yang Carissa tidak pahami."
    
    show dewa marah
    play sound audio.mandewa volume 2.0 fadeout 1.0
    d "(menjerit) KAU PIKIR KAU BISA TAHAN AKU?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "ANAKMU! ANAKMU ADALAH DARAH RAKTA!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "AKU AKAN KEMBALI UNTUKNYA!"
    
    show aura_biru at center
    with flash_blue
    
    play sound audio.magic
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Segel menguat. Gerbang mulai tertutup."
    
    show dewa serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(suara melemah) Tunggu saja..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Aku akan kembali untuk anak itu!"
    
    hide dewa wujud_asli
    hide aura_merah
    with flash_white
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sosok itu tersedot kembali ke dalam gerbang."
    

    hide aura_biru
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tubuh ibunya perlahan melemah."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Energi terkuras habis."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pandangan mengabur... lalu gelap."
    
    scene black
    with flash_white
    
    scene bg kamar_carissa
    with dissolve
    
    show carissa takut at center
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(terbangun) HAH!"
    play sound audio.huh volume 2.0 fadeout 1.0
    n "Carissa terengah-engah, keringat dingin membasahi dahinya."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(gemetar) Itu... itu memori Ibu?"
    play sound audio.kagetperpus volume 3.0 fadeout 1.0
    c "(terkejut) Jadi murid baru... Dewa yang sama?!"
    

    show carissa takut
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dia bilang... akan kembali lagi..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Gimana bisa dia keluar sekarang?!"
    

    menu:
        "Apa yang harus Carissa lakukan?"
        
        "Langsung hubungi Aksara":
            $ aksara_points += 3
            jump call_aksara
        
        "Cari tau lebih lanjut dulu sendiri":
            $ dewa_points += 1
            jump investigate_more
        
        "Pergi menemui Dewa langsung":
            $ dewa_points += 2
            $ aksara_points -= 1
            jump confront_dewa


label call_aksara:
    play sound audio.phonevibrate volume 3.0
    n "Carissa menghubungi Aksara dengan tangan gemetar."

    if aksara_points > dewa_points + 3:
        play sound audio.keyyi volume 1.0 fadeout 1.0
        n "Telepon diangkat setelah nada pertama."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Carissa? Ada apa?"
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(bergetar) Aksara... aku... aku nemuin sesuatu."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Bisa kamu ke rumahku sekarang?"
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(tanpa ragu) Aku segera ke sana!"
        
    elif dewa_points > aksara_points + 3:
        play sound audio.keyyi volume 1.0 fadeout 1.0
        n "Telepon berdering beberapa kali sebelum diangkat."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "...Halo?"
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(gugup) Aksara... maaf ganggu."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Tapi aku... aku perlu bantuan kamu."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        n "Hening sejenak."
        play sound audio.menghela volume 2.0 fadeout 1.0
        a "(menghela napas) ...Oke. Aku ke sana."
        
    else:
        play sound audio.keyyi volume 1.0 fadeout 1.0
        n "Telepon diangkat setelah beberapa nada berdering."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Carissa?"
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Aksara, aku nemu catatan Ibu."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Dan... aku lihat sesuatu yang—"
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(memotong) Jangan kemana-mana. Aku datang sekarang."
    
    scene black
    with Dissolve(1.0)
    
    jump aksara_arrives


label investigate_more:
    show carissa bingung
    play sound audio.bookopen volume 3.0 fadeout 1.0
    c "(membuka lagi buku catatan) Mungkin ada info lain..."
    
    play sound audio.bookflip1 loop volume 2.0 
    n "Carissa membolak-balik halaman dengan cepat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sampai ia menemukan halaman yang berbeda—ditulis dengan tinta merah."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    centered "{color=#8b0000}{i}'KALAU KAMU MEMBACA INI, CARISSA...'{/i}{/color}"
    pause 1.5
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ini... pesan untuk aku?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    centered "{color=#8b0000}{i}'Maafkan Ibu. Ibu tidak bisa lindungi kamu selamanya.'{/i}{/color}"
    pause 1.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    centered "{color=#8b0000}{i}'Tapi ingat ini...'{/i}{/color}"
    pause 1.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    centered "{color=#8b0000}{i}'Kamu punya pilihan. Kamu yang tentukan jalanmu sendiri.'{/i}{/color}"
    pause 1.5
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    centered "{color=#8b0000}{i}'Percayalah pada seseorang yang kamu yakini saat ini.'{/i}{/color}"
    pause 1.0
    
    show carissa bingung
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Maksudnya... apa?"
    
    
    menu:
        "Carissa tetap bingung, Siapa yang harus dihubungi?"
        
        "Hubungi Aksara sekarang juga":
            $ aksara_points += 2
            jump call_aksara_path
        
        "Hubungi Nenek dulu":
            $ aksara_points += 1
            jump call_nenek_path


label confront_dewa:
    show carissa serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa segera berkemas-kemas dan hendak keluar dari rumah."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Aku harus dapet jawaban sekarang!"
    
    play sound audio.dooropen1 volume 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun, tepat Carissa melangkah keluar..."

    show nenek khawatir at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Carissa?! Mau kemana jam segini?"
    
    show carissa kaget at right
    with move 
    play sound audio.kagetperpus volume 3.0
    c "Nek, aku—"
    
    show nenek serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(melihat buku di tangan Carissa) Kamu... udah buka kotak itu?"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Iya, Nek. aku jadi tahu dan yakin sekarang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kalo aku... Darah Rakta."
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Carissa..."
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Duduk dulu, Nduk. Nenek mau cerita semuanya."
    
    jump nenek_explains

label call_nenek_path:
    $ talked_to_nenek = True
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek khawatir at left
    show carissa sedih at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nek... aku nemu catatan Ibu."
    
    show nenek khawatir
    play sound audio.menghela volume 3.0 fadeout 1.0
    nenek "(menghela napas panjang) Akhirnya... hari ini juga tiba."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nenek tahu soal ini?"
    
    show nenek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(mengangguk) Nenek tau sejak kamu lahir, Nduk."
    
    jump nenek_explains

label nenek_explains:
    $ talked_to_nenek = True
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek normal at left
    show carissa normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Carissa... kamu itu lahir pas gerhana bulan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Tepat 200 tahun setelah Darah Rakta terakhir."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Jadi... aku emang ditakdirkan buat ini?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Para tetua Nirantara bilang begitu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Tapi Ibumu... dia menolak takdir itu."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nolak?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Dia bilang: 'Carissa itu bukan alat, Mbok. Dia punya hak untuk hidup normal.'"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Makanya dia rela berkorban."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Dia menahan roh kuat namanya Dewa Abinaya."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi... sekarang Dewa itu kembali lagi, Nek."
    
    show nenek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(mengangguk) Iya. Nenek juga sebenernya udah ngerasain kalo segel Gerbang Roh agak melemah."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Makanya dia bisa muncul lagi, tapi belum bisa dalam wujud penuhnya."
    
    menu:
        "Apa yang Carissa tanyakan?"
        
        "Dewa belum dalam wujud penuh?":
            show carissa normal
            
            c "Gimana bisa, Nek?"
            
            show nenek normal
            
            nenek "Roh itu juga bisa menyamar seseorang, Nduk."
            nenek "Nenek yakin itu cuma masih setengah jiwa dari rohnya yang baru keluar."
            nenek "Tapi, kita juga harus hati-hati."
            
        "Apa yang sebenarnya Dewa mau dari aku?":
            show carissa bingung
            
            c "Dewa itu... sebenernya mau apa?"
            
            show nenek serius
            
            nenek "Dia mau buka Gerbang Roh sepenuhnya, Nduk."
            nenek "Buat menyatukan dunia manusia dan roh."
            nenek "Dan... cuma Darah Rakta yang bisa bantu dia mewujudkan itu."
            
        "Aku harus gimana sekarang?":
            show carissa takut
            
            c "Terus... aku harus gimana?"
            
            show nenek normal
            
            nenek "Kamu harus belajar mengendalikan kekuatan kamu, Nduk."
            nenek "Dan cari bantuan juga."
            nenek "Maaf kalo Nenek ga bisa bantu, Nenek juga sudah makin renta."
    

    show nenek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Hubungi Aksara, Nduk. Dia juga Nirantara sama kayak kita."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Dia bisa bantu kamu."
    
    $ aksara_points += 1
    
    show carissa normal
    
    c "(mengangguk) Oke, Nek."
    
    jump call_aksara_path

label call_aksara_path:
    play sound audio.phonevibrate loop volume 3.0 fadeout 1.0
    n "Carissa menghubungi Aksara dengan tangan gemetar."

    if aksara_points > dewa_points + 3:
        n "Telepon diangkat setelah nada pertama."
        
        a "Carissa? Ada apa?"
        
        c "(bergetar) Aksara... aku perlu ngobrol."
        c "Bisa kamu ke rumahku?"
        
        a "(tanpa ragu) Aku segera ke sana!"
        
    elif dewa_points > aksara_points + 3:
        n "Telepon berdering beberapa kali sebelum diangkat."
        
        a "...Halo?"
        
        c "(gugup) Aksara... maaf ganggu."
        c "Tapi aku... aku perlu bantuan kamu."
        
        n "Hening sejenak."
        
        a "(menghela napas) ...Oke. Aku ke sana."
        
    else:
        n "Telepon diangkat setelah beberapa nada berdering."
        
        a "Carissa?"
        
        c "Aksara, aku perlu ngobrol sama kamu."
        c "Ini penting."
        
        a "(serius) Oke. Aku datang sekarang."
    
    scene black
    with Dissolve(1.0)
    
    jump aksara_arrives

label aksara_arrives:
    scene bg ruang_tamu_terang
    with dissolve
    
    play sound audio.door_open
    
    show aksara khawatir at left
    with easeinleft
    
    
    if aksara_points > dewa_points + 3:
        # Good relationship
        show carissa normal at right
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(langsung menghampiri) Carissa, kamu gapapa?"
        
        show carissa sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(memeluk Aksara) Aksara... aku takut."
        
        show aksara normal
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(mengelus punggung Carissa) Tenang, aku di sini."
        
    elif dewa_points > aksara_points + 3:
        # Bad relationship
        show carissa sedih at right
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(berdiri agak jauh) ...Jadi, ada apa?"
        
        show carissa takut
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Aksara... aku tau sekarang. Tentang Darah Rakta."
        
        show aksara kaget
        with vpunch
        play sound audio.kagetperpus volume 3.0 fadeout 1.0
        a "Kamu... gimana bisa—"
        
        show carissa serius
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Aku nemu catatan Ibu. Dan aku... lihat memori dia sekilas."
        
        show aksara sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(menunduk) Maafin aku. Aku harusnya ngomong dari awal."
        
    else:
        # Neutral
        show carissa normal at left
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Kamu bilang nemu sesuatu?"
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(menyerahkan buku) Ini. Catatan Ibu."
        
        show aksara kaget at right
        with vpunch
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(membaca cepat) ..."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(menutup buku) Carissa... kita perlu ngobrol serius."
    
    jump chapter3_scene3  

# SCENE 3 - CHAPTER 3
label chapter3_scene3:
    scene bg ruang_tamu_terang
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    if talked_to_nenek:
        jump scene3_with_nenek_knowledge
    else:
        jump scene3_without_nenek_knowledge

label scene3_without_nenek_knowledge:
    if aksara_points > dewa_points + 3:
        show aksara normal at left
        show carissa normal at right
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(duduk di sebelah Carissa) Kamu bilang nemu sesuatu?"
        
        show carissa sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(menyerahkan buku catatan) Ini... catatan Ibu."
        
        show aksara khawatir
        play sound audio.bookopen volume 3.0
        a "(membuka buku, membaca)"
        play sound audio.keyyi volume 1.0 fadeout 1.0
        n "Aksara membaca dalam diam. Ekspresinya berubah."
        
        show aksara sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Carissa... kamu udah baca semuanya?"
        
        show carissa normal
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(mengangguk) Iya. Dan aku... lihat sesuatu."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Kayak memori Ibu waktu dia lawan... Dewa."
        
        show aksara kaget
        with vpunch
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Kamu... masuk ke memori ibumu?"
        
        show carissa bingung
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Iya. Itu... gimana bisa?"
        
        show aksara serius
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(menunjuk kalung) Mungkin... dari kalung itu, Carissa."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Aku bisa rasain ada sisa-sisa memori jiwa di dalamnya."
        
        
    elif dewa_points > aksara_points + 3:
        show aksara khawatir at left
        show carissa sedih at right
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(berdiri agak jauh) Carissa..."
        
        show carissa takut
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Aku tau sekarang, Aksara."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Tentang aku. Tentang... Darah Rakta."
        
        show aksara sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(menunduk) ..."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Aku harusnya ngomong dari awal."
        
        show carissa bingung
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Kenapa kamu nggak pernah bilang?"
        
        show aksara khawatir
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Karena... aku takut kamu kenapa-napa."

        show aksara sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Aku udah kehilangan orang tuaku dulu."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(suara bergetar) Mereka juga Nirantara. Mereka juga... melindungi orang-orang."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Dan aku... aku nggak bisa ngelakuin apa-apa."

        show carissa normal
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(terharu) Aksara..."

        show aksara khawatir
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Jadi sekarang, aku ga mau kehilangan lagi."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Orang yang penting bagiku."
        
    else:
        show aksara serius at left
        show carissa normal at right
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Jadi... kamu tau sekarang?"
        
        show carissa bingung
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(mengangguk) Iya. Dari catatan Ibu."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Tapi... aku masih bingung banyak hal."
        
        show aksara normal
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(duduk) Oke. Tanya aja. Aku jawab sejujurnya."
        
        show carissa sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Aku... kenapa aku Darah Rakta?"
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Apa... apa itu kutukan?"
        
        show aksara khawatir
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(menggeleng) Bukan kutukan. Itu... takdir."
    
        show aksara normal
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Carissa, aku mau jelasin dari awal."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Tapi janji... dengerin sampai selesai ya?"
    
    menu:
        "Apa respon Carissa?"
        
        "Iya, aku dengerin":
            $ aksara_points += 2
            
            show carissa normal
            
            c "(mengangguk) Iya. Aku janji."
            
            show aksara senyum
            
            a "(tersenyum tipis) Makasih."
            
        "Aku... takut dengernya":
            show carissa sedih
            
            c "Aku... takut dengernya."
            c "Takut makin bingung."
            
            show aksara khawatir
            
            a "Aku ngerti. Tapi... kamu harus tau."
            a "Biar kamu bisa lindungi diri kamu sendiri."
            
        "Kenapa baru sekarang ngomong?":
            $ aksara_points -= 1
            
            show carissa serius
            
            c "Kenapa baru sekarang kamu ngomong?"
            c "Kenapa nggak dari dulu?!"
            
            show aksara sedih
            
            a "(menunduk) Karena... aku pengecut."
            a "Aku takut kehilangan kamu."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Oke. Jadi... kamu tau tentang Gerbang Roh?"
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Yang... di candi itu?"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengangguk) Iya. Gerbang yang misahin dunia manusia sama dunia roh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Selama ini, gerbang itu... setengah terbuka."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Setengah terbuka?!"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Iya. Makanya kamu bisa liat roh. Makanya mereka bisa ganggu kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dan... makanya Dewa bisa 'menyusup' ke dunia manusia."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dewa... dia bukan manusia?"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggeleng) Dia roh. Roh yang sangat kuat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku curiga, Dewa yang ada di sekolah kita beneran roh kuno itu."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Gimana bisa dia wujudnya manusia? Terus apa tujuan dia?"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Roh itu bisa manipulasi wujud mereka, Carissa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Terus... Aku dengar dari cerita Kakek, tujuan dia itu mau buka gerbang sepenuhnya."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Buat apa?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Buat menyatukan dunia manusia sama dunia roh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dia bilang itu 'dunia sempurna'. Tapi sebenarnya..."
    
    menu:
        "Apa yang Carissa pikir?"
        
        "Itu... berbahaya ya?":
            $ aksara_points += 2
            
            show carissa normal
            
            c "Itu... berbahaya kan?"
            c "Kalau dua dunia nyatu... pasti bakal kacau."
            
            show aksara senyum
            
            a "(tersenyum) Iya. Kamu benar."
            a "Manusia dan roh itu dua hal yang berbeda jadi butuh waktu lama buat adaptasi."
            
        "Kenapa nggak boleh nyatu?":
            $ dewa_points += 1
            
            show carissa bingung
            
            c "Tapi... kenapa nggak boleh nyatu?"
            c "Bukannya jadi lebih transparan?"
            
            show aksara serius
            
            a "Karena nggak semua orang cepat adaptasi, Carissa."
            a "Bayangkan: semua orang tiba-tiba bisa liat roh."
            a "Yang pengecut bakal terus merasa ketakutan. Yang dendam terhadap manusia lain bisa nyuruh roh untuk membalasnya."
            a "Bakal jadi perang dimana-mana."
            
        "Aku... nggak ngerti":
            show carissa sedih
            
            c "Aku... masih nggak ngerti."
            c "Kenapa ini jadi tanggung jawab aku?"
            
            show aksara khawatir
            
            a "Karena cuma kamu yang bisa buka atau tutup gerbang."
            a "Cuma... Darah Rakta."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa, Darah Rakta itu... kemampuan langka."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Muncul cuma sekali dalam 200 tahun."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "200 tahun?!"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Iya. Dan kamu... lahir tepat 200 tahun setelah Darah Rakta terakhir."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Apalagi tepat gerhana bulan. Waktu yang... sempurna."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Jadi... aku ditakdirkan buat ini?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Bukan takdir. Waktu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap Carissa) Tapi... apa yang kamu lakukan dengan kekuatan itu?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Itu pilihan kamu."
    
    jump scene3_common_part

label scene3_with_nenek_knowledge:
    if aksara_points > dewa_points + 3:
        show aksara normal at left
        show carissa normal at right
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(duduk) Jadi... Nenek udah cerita?"
        
        show carissa sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(mengangguk) Iya. Tentang Darah Rakta, gerbang, Dewa..."
        
        show aksara khawatir
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Dan... gimana perasaan kamu?"
        
        show carissa bingung
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Aku... bener-bener kelebihan info. Tapi setidaknya aku paham kenapa."
        
        show aksara normal
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(tersenyum tipis) Aku tau ini berat."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Tapi aku janji... aku bakal bantu kamu."
        
    elif dewa_points > aksara_points + 3:
        show aksara sedih at left
        show carissa sedih at right
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "(berdiri agak jauh) Kamu... udah tau semuanya dari Nenek?"
        
        show carissa normal
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "(mengangguk) Iya."
        play sound audio.keyyi volume 1.0 fadeout 1.0
        n "Hening canggung."
        
        show aksara khawatir
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Maafin aku. Aku harusnya yang ngomong duluan."
        
        show carissa bingung
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Kenapa kamu nggak pernah bilang?"
        
        show aksara sedih
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Karena... aku takut kamu benci aku."
        
        show carissa normal
        
        c "..."
        
    else:
        show aksara serius at left
        show carissa normal at right
        with dissolve
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Jadi Nenek udah jelasin?"
        
        show carissa bingung
        play sound audio.keyyi volume 1.0 fadeout 1.0
        c "Iya. Tapi... aku masih bingung beberapa hal."
        
        show aksara normal
        play sound audio.keyyi volume 1.0 fadeout 1.0
        a "Oke. Tanya aja."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa, pasti Nenek udah bilang tentang pilihan kamu kan?"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengangguk) Tutup gerbangnya... atau buka seluruhnya."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Iya. Tapi ada yang Nenek mungkin belum tahu."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Apa?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tentang Dewa Abinaya, teman sekelasmu."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dewa... yang di sekolah?"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengangguk) Dia... bukan manusia."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0        
    c "Berarti, dia-"
            
    show aksara sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0      
    a "Ya... roh kuno yang udah diceritain sama nenekmu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dia nyoba nyamar jadi manusia biar ga dicurigain sama Nirantara yang lain."
            
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "APA?!"
            
    show aksara sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku juga baru tau abis kita selesai studi tournya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Soalnya aku bener-bener udah dilatih cara agar tau aura roh Dewa itu kayak gimana."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Terus... kenapa dia ga langsung ambil diriku?"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Karena, kuliat kamu ada semacam pelindung yang kuat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menunjuk kalung) kayaknya dari itu deh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Yah, intinya Dewa ga bisa sembarangan sih..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "jadi dia ngutus kroco-kroconya untuk nakutin kamu dulu untuk manfaatin ketakutanmu."
    
    show carissa takut
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Jadi... kalo aku takut—"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Pelindung itu bakal goyah dikit."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggenggam tangan Carissa) Makanya aku nggak mau kamu ambil risiko itu dan kasih kamu jimat untuk lapisan."
    
    jump scene3_common_part

label scene3_common_part:
    show aksara normal at left
    show carissa normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa, yang penting sekarang..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu harus belajar mengendalikan kekuatan kamu."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Mengendalikan? Caranya gimana?"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku bisa latih kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Biar kamu bisa lindungi diri sendiri."
    
    menu:
        "Apa respon Carissa?"
        
        "Iya, tolong latih aku":
            $ aksara_points += 3
            
            show carissa normal
            
            c "Iya. Tolong latih aku, Aksara."
            c "Aku nggak mau jadi beban lagi."
            
            show aksara senyum
            
            a "(tersenyum) Kamu nggak pernah jadi beban."
            a "Oke. Kita mulai besok."
            
        "Aku... takut":
            show carissa sedih
            
            c "Aku... takut."
            c "Takut nggak bisa."
            
            show aksara khawatir
            
            a "Kamu bisa. Aku percaya."
            a "(menggenggam tangan Carissa) Dan aku bakal temani kamu."
            
            $ aksara_points += 1
            
        "Aku butuh waktu mikir dulu":
            $ dewa_points += 1
            
            show carissa bingung
            
            c "Aku... butuh waktu mikir dulu."
            
            show aksara khawatir
            
            a "...Oke. Tapi jangan terlalu lama."
            a "Dewa... dia nggak akan sabar."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa, ada satu hal lagi."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Apa?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Konfrontasi terakhir... bakal terjadi di candi Reksana Sewu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tempat gerbang Roh berada."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kapan?"
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku nggak tau pasti. Tapi... segera terjadi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku takut Dewa makin agresif, makanya kita harus selangkah di depannya."
    
    if not talked_to_nenek:
        play sound audio.door_open
        
        show nenek khawatir at center behind aksara
        with dissolve
        
        nenek "Carissa, Aksara..."
        
        show carissa kaget at right
        show aksara normal at left
        
        c "Nek! Dari tadi dengerin?"
        
        show nenek khawatir
        
        nenek "(mengangguk) Iya, Nduk."
        nenek "Nenek harus tambahin sesuatu."
        
    else:
        show nenek normal at center behind aksara
        with dissolve
        
        nenek "Aksara bener, Nduk."
        nenek "Kamu harus berlatih."
    
    show nenek serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Apapun yang terjadi..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Keputusan semua ada di tangan kamu."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengangguk pelan)"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa, aku mau kamu tau satu hal."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Apa?"
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Apapun yang kamu pilih nanti..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku bakal selalu di sisi kamu."
    
    $ aksara_points += 1
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersenyum kecil) Makasih, Aksara."
    
    show nenek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mata Nenek terlihat berkaca-kaca."

    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nenek...?"
    
    show nenek khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(menggeleng) Nggak apa-apa, Nduk."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Nenek cuma... bangga sama kamu."

    hide nenek khawatir
    hide carissa normal
    hide aksara senyum
    with dissolve

    scene black
    with Dissolve(1.0)

    jump label_chapter3_scene4

# SCENE 4 - CHAPTER 3
label chapter3_scene4:
    scene black
    with Dissolve(1.0)
    
    centered "{color=#fff}Keesokan Harinya{/color}"
    pause 1.5
    
    # Branch berdasarkan relationship status
    if aksara_points > dewa_points + 3:
        jump scene4_good_relationship
    elif dewa_points > aksara_points + 3:
        jump scene4_bad_relationship
    else:
        jump scene4_neutral_relationship

# ===== GOOD RELATIONSHIP PATH =====
label scene4_good_relationship:
    scene bg kuil
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Aksara bertemu di kuil untuk berlatih."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pagi itu udara terasa sejuk dan menyegarkan."
    
    show carissa senyum at right
    show aksara senyum at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Pagi, Carissa! Udah sarapan?"
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Udah dong. Nenek masak bubur kesukaan aku."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum) Bagus. Kamu perlu energi buat latihan hari ini."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Emang latihannya berat?"
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Lumayan. Tapi aku yakin kamu bisa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menepuk bahu Carissa) Lagipula, aku bakal bantu kamu kok."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Makasih, Aksara."
    
    jump scene4_training_part1

# ===== BAD RELATIONSHIP PATH =====
label scene4_bad_relationship:
    scene bg kuil
    with dissolve
    
    play music audio.tension fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa tiba di kuil lebih awal."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suasana terasa... canggung."
    
    show carissa sedih at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Apa Aksara masih marah ya?"
    
    show aksara khawatir at left
    with easeinleft
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara datang, berdiri agak jauh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "...Kamu udah datang."
    
    show carissa bingung at right
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Iya..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Keadaan hening di sekitar membuat keduanya tampak canggung."
    
    show aksara serius
    play sound audio.menghela volume 3.0 fadeout 1.0
    a "(menghela napas) Oke. Kita mulai aja."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aksara... aku—"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggeleng) Nggak usah. Sekarang fokus ke latihan dulu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Urusan yang lain... nanti aja."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menunduk) ...Oke."
    
    jump scene4_training_part1

# ===== NEUTRAL RELATIONSHIP PATH =====
label scene4_neutral_relationship:
    scene bg candi_gerbang
    with dissolve
    
    play music audio.mysterysound2 fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Aksara bertemu di kuil seperti yang dijanjikan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tidak terlalu jauh, tapi juga tidak terlalu dekat."
    
    show carissa normal at right
    show aksara normal at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Siap?"
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Sejujurnya... nggak tau harus siap atau nggak."
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum tipis) Tenang. Kita mulai dari dasarnya ya."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengangguk) Oke."
    
    jump scene4_training_part1

# ===== TRAINING PART 1: Merasakan Energi =====
label scene4_training_part1:
    show kakek normal at center behind aksara
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Ah, kalian sudah datang."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kakek!"
    
    show kakek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Carissa, senang bertemu lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Aksara sudah cerita tentang... situasimu."
    
    if aksara_points > dewa_points + 3:
        show carissa normal
        
        c "(tersenyum) Iya, Kakek. Aku udah siap belajar."
        
        show kakek normal
        
        k "Bagus. Semangat yang positif akan bantu kamu."
        
    elif dewa_points > aksara_points + 3:
        show carissa sedih
        
        c "(menunduk) Maaf... aku jadi ngerepotin."
        
        show kakek khawatir
        
        k "Nggak perlu minta maaf, Nduk."
        k "Yang penting sekarang, kamu belajar melindungi diri sendiri."
        
    else:
        show carissa bingung
        
        c "Aku... aku nggak tau apakah bakal bisa."
        
        show kakek normal
        
        k "Percaya pada dirimu sendiri, Nduk. Itu langkah pertama."
    
    show kakek serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Baik, kita mulai."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Langkah pertama: merasakan energi spiritual di sekitarmu."
    
    show carissa normal at right
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Caranya?"
    
    show kakek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Tutup matamu. Tarik napas dalam-dalam."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Rasakan... aliran energi di dalam tubuhmu."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menutup mata)"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengikuti instruksi Kakek."
    
    if aksara_points > dewa_points + 3:
        show aksara normal at left
        
        a "(berbisik) Tenang aja. Aku di sini."
        
        n "Suara Aksara membuat Carissa lebih tenang."
        n "Perlahan, ia mulai merasakan sesuatu."
        
    elif dewa_points > aksara_points + 3:
        n "Carissa mencoba fokus, tapi pikirannya kacau."
        n "Rasa bersalah masih menghantuinya."
        
        show carissa sedih
        
        c "(dalam hati) Aku harus fokus... aku harus bisa..."
        
        n "Dengan susah payah, ia mulai merasakan sesuatu."
        
    else:
        n "Carissa mencoba fokus dengan sepenuh hati."
        n "Butuh beberapa saat, tapi akhirnya ia merasakan sesuatu."
    
    play sound audio.heartbeat
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Detak jantung. Aliran darah. Dan... sesuatu yang lebih."
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(membuka mata) Aku... aku ngerasain sesuatu!"
    
    if aksara_points > dewa_points + 3:
        show aksara senyum
        
        a "(tersenyum lebar) Keren! Aku tau kamu bisa, Carissa!"
        
    elif dewa_points > aksara_points + 3:
        show aksara normal
        
        a "(mengangguk) Bagus tuh."
        
    else:
        show aksara senyum
        
        a "(tersenyum tipis) Lihat? Kamu bisa kok."
    
    show kakek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Bagus! Itu energi spiritual kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Sekarang, coba fokuskan ke tanganmu."
    
    jump scene4_training_part2

# ===== TRAINING PART 2: Manifestasi Energi =====
label scene4_training_part2:
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menutup mata lagi)"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa mengangkat salah satu tangannya secara perlahan."
    
    if aksara_points > dewa_points + 3:
        n "Dengan kepercayaan diri yang lebih kuat, sebuah energi mengalir dengan lancar."
        n "Cahaya biru muncul secara stabil di telapak tangannya."
        
        show kalung_glow at right
        with flash_blue
        
        play sound audio.success
        
    elif dewa_points > aksara_points + 3:
        n "Carissa berusaha keras, tapi energinya tidak stabil."
        n "Cahaya berkelip-kelip, hampir padam."
        
        show carissa sedih
        
        c "(frustasi) Kenapa... kenapa nggak bisa—"
        
        show aksara khawatir
        
        a "Carissa, kamu terlalu tegang."
        
        show kakek serius
        
        k "Lepaskan beban di pikiranmu. Fokus hanya pada energi, Nduk. Bayangkan energi itu dengan sepenuh hatimu."
        
        n "Carissa menarik napas panjang, mencoba melupakan semuanya dan mulai memfokuskan dirinya."
        n "Perlahan, cahaya mulai stabil muncul di telapak tangannya."
        
        show kalung_glow at right
        with flash_blue
        
    else:
        n "Perlahan, cahaya biru samar muncul di telapak tangannya."
        n "Tidak terlalu terang, tapi cukup stabil."
        
        show kalung_glow at right
        with flash_blue
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(membuka mata) Cahaya ini—!"
    
    show kakek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Itu manifestasi dari Darah Raktamu, Nduk."

    hide kalung_glow
    with dissolve
    
    if aksara_points > dewa_points + 3:
        show aksara senyum
        
        a "(antusias) Carissa, kamu keren banget tau!"
        a "Aku dulu butuh berminggu-minggu buat bisa ngeluarin energi kayak gitu!"
        
        show carissa senyum
        
        c "(tersenyum) Beneran?"
        
        show aksara normal
        
        a "(mengangguk) Serius! Kamu natural banget!"
        
    elif dewa_points > aksara_points + 3:
        show aksara normal
        
        a "...Lumayan. Tapi masih perlu latihan lebih banyak."
        
        show carissa sedih
        
        c "(menunduk) Iya..."
        
        show kakek normal
        
        k "Aksara, jangan terlalu keras. Dia baru belajar."
        
    else:
        show aksara senyum
        
        a "(tersenyum) Bagus, Carissa. Kamu belajar cepet ya."
        
        show carissa senyum
        
        c "(tersenyum kecil) Makasih."
    
    jump scene4_training_part3


label scene4_training_part3:
    show kakek serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Sekarang, latihan kedua: membuat pelindung."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Ini penting buat melindungi diri dari serangan spiritual."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Sepenting itu ya?"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengeluarkan jimat) Iya, beneran penting."
    
    show aura_biru at left
    with flash_blue
    
    play sound audio.magic
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara mengeluarkan energi dari jimatnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Cahaya biru tua membentuk perisai di sekitarnya."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Wah..."
    
    show kakek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Sekarang giliran kamu, Nduk."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    k "Fokuskan energi ke benda yang jadi pelindungmu."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menyentuh kalung)"
    
    if aksara_points > dewa_points + 3:
        show aksara normal
        
        a "(berdiri di samping) Aku di sini kalau kamu butuh bantuan."
        
        n "Kehadiran Aksara membuat Carissa lebih percaya diri."
        n "Energi biru mengalir dengan lancar dari diri Carissa."
        
        show kalung_glow at right
        with flash_blue
        
        n "Dalam satu jam, muncul perisai biru berbentuk pentagon di sekitar Carissa."
        
        play sound audio.success
        
        show carissa senyum
        
        c "Aku... aku berhasil!"
        
        show aksara senyum
        
        a "(bertepuk tangan) Bagus, bagus"
        
    elif dewa_points > aksara_points + 3:
        n "Carissa berkonsentrasi keras."
        n "Tapi pikiran negatif terus mengganggunya."
        
        show carissa sedih
        
        c "(dalam hati) Aku harus bisa... aku harus buktikan..."
        
        n "Kalung mulai bersinar, tapi energinya cukup tidak stabil."
        n "Perisai tetap terbentuk tapi terus berkelip redup, menandakan ketidaksempurnaan."
        
        show kalung_glow at right
        with dissolve
        
        show carissa takut
        
        c "(panik) Kenapa nggak bisa—"
        
        show aksara khawatir
        
        a "(menggenggam tangan Carissa) Carissa, tenang!"
        
        n "Sentuhan Aksara membuat Carissa terkejut sekaligus tersentuh."
        
        show carissa normal
        
        n "Kumpulan energi mulai stabil. Perisai pentagon terbentuk lebih kuat dan bercahaya kuat."
        
        show aksara normal
        
        a "(melepas tangan) ...Bagus. Latihannya emang butuh fokus tingkat tinggi."
        
    else:
        n "Carissa mencoba dengan sepenuh hati."
        n "Energinya tidak terlalu kuat, tapi cukup stabil."
        
        show kalung_glow at right
        with flash_blue
        
        n "Perisai tipis terbentuk di sekitarnya."
        
        show carissa senyum
        
        c "Aku... berhasil!"
        
        show aksara senyum
        
        a "(tersenyum) Bagus."
    
    show kakek senyum
    
    k "Sangat bagus, Carissa. Gapapa nggak sempurna asalkan kamu udah paham."
    
    if aksara_points > dewa_points + 3:
        k "Kamu belajar lebih cepat dari yang kukira."
    elif dewa_points > aksara_points + 3:
        k "Kamu punya potensi. Tapi masih perlu latihan kontrol emosi."
    else:
        k "Dengan latihan lebih banyak, kamu akan semakin kuat."
    
    hide kalung_glow
    hide aura_biru
    with dissolve
    
    jump scene4_rest_time


label scene4_rest_time:
    scene bg kuil
    with Dissolve(1.0)
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setelah latihan, mereka istirahat sebentar."
    
    if aksara_points > dewa_points + 3:
        jump scene4_rest_good
    elif dewa_points > aksara_points + 3:
        jump scene4_rest_bad
    else:
        jump scene4_rest_neutral

label scene4_rest_good:
    show carissa senyum at right
    show aksara senyum at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Aksara duduk berdampingan di bawah pohon."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suasana hangat dan nyaman."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu hebat tadi."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tertawa kecil) Ah, berlebihan deh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku masih banyak yang harus belajar."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tapi kamu udah jauh lebih baik dari aku dulu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum) Aku bangga sama kamu."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersenyum) Makasih, Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Makasih udah selalu... ada buat aku."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menggenggam tangan Aksara) Aku janji nggak akan kemana-mana."
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum) Oke. Aku percaya sama kamu."
    
    jump scene4_shadow

label scene4_rest_bad:
    show carissa sedih at right
    show aksara khawatir at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Aksara duduk dengan jarak yang cukup jauh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Hening canggung menyelimuti mereka."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aksara..."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "..."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menunduk) Aku tau kamu masih... marah."
    
    show aksara sedih
    play sound audio.menghela volume 2.0 fadeout 1.0
    a "(menghela napas) Aku nggak marah."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap Carissa) Aku cuma... kecewa."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kecewa...?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kecewa sama diriku sendiri."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Karena nggak bisa lindungi kamu dengan lebih baik."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aksara, itu bukan salah kamu!"
    play sound audio.keyyi volume 1.0 fadeout 1.0                 
    c "Itu... itu salah aku yang nggak dengerin kamu waktu itu."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum sedih) Kita berdua sama-sama salah kayaknya."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Jadi... kita bisa mulai lagi?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Awal yang baru?"
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengulurkan tangan) Awal yang baru."
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa pun menjabat tangan Aksara."
    
    $ aksara_points += 2
    
    jump scene4_shadow

label scene4_rest_neutral:
    show carissa normal at right
    show aksara normal at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Aksara duduk sambil minum air."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Mereka hening dalam sunyinya kuil tua tersebut."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu... gimana perasaanmu?"
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Maksudnya?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tentang... ya semua ini."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Apa kamu udah bisa nerima dikit-dikit?"
    
    show carissa sedih
    play sound audio.menghela volume 3.0 fadeout 1.0
    c "(menghela napas) Yah, gimanapun juga aku harus ngelakuin ini kan?"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tenang, kamu nggak sendirian."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku bakal bantuin kamu sebisa aku, jadi semuanya jangan kamu bebankan ke diri sendiri ya?"
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersenyum tipis) Makasih, Aksara." 
    
    jump scene4_shadow

label scene4_shadow:
    scene black
    with Dissolve(1.0)
    
    centered "{color=#fff}Beberapa jam setelah berada di kuil, Carissa memutuskan pulang karena ia merasa lelah.{/color}"
    pause 1.0
    
    scene bg cafe
    with dissolve
    
    play music audio.tensionmusic fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dalam perjalanan pulang, Carissa mampir sebentar ke salah satu kafe yang ada di pinggir jalan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ia ingin membeli Iced Coffee kesukaannya."
    
    show carissa normal at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(melihat-lihat rak menu) Mmmm..."
    
    play sound audio.wind
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setelah membeli minuman favoritnya, ia berjalan menuju pintu keluar toko."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tepat ia keluarm tiba-tiba udara di sekelilingnya perlahan dingin yang menusuk kulit."
    
    show carissa bingung
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(merinding) Ada apa ini?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa tanpa sadar melihat sekelilingnya untuk memastikan bahwa itu hanya perasaannya sendiri."
    
    play sound audio.heartbeat
    
    scene bg cafe
    with flash_red
    
    show bayangan at center
    with dissolve
    
    play music audio.heartbeat fadein 1.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dari balik salah satu pohon, sosok bayangan hitam pekat muncul mengawasi Carissa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tanpa wajah dan bentuk yang jelas."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ia perlahan mendekati Carissa yang tepat di depan pintu kafe."
    
    show carissa takut at right
    with move
    play sound audio.footstep1x volume 1.0 fadeout 1.0
    c "(mundur) S-siapa?!"
    play sound audio.bisikan volume 3.0 fadeout 1.0
    suara "(bergema) Carissa..."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "K-kenapa kamu tau namaku?!"
    
    show bayangan
    play sound audio.whisperr volume 1.0 fadeout 1.0
    suara "Pesan... dari Tuan Dewa..."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dewa...?"
    
    # PESAN ULTIMATUM
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "Waktu... hampir habis..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "Ia... menunggu keputusanmu..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "Tiga hari lagi... datanglah ke candi..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "Sendirian..."
    
    show carissa takut
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kalau aku nggak datang?!"
    
    show bayangan
    play sound audio.whisperr volume 1.0 fadeout 1.0
    suara "(menyeringai) Maka... orang-orang terkasihmu..."
    play sound audio.scream volume 1.0 fadeout 1.0
    suara "Akan menjadi... korban pertama..."
    
    show carissa marah
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "JANGAN!"
    hide bayangan
    with flash_white
    
    play sound audio.wind
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Bayangan itu menghilang seperti asap."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tak ada yang tersisa dari bayangan tersebut."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dalam diam, Carissa merasakan tubuhnya bergetar hingga ia sampai mengepalkan tangannya."
    
    show carissa takut at center
    with move
    play sound audio.breathcapek volume 3.0 fadeout 1.0
    c "(terengah-engah) Hah... hah..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(gemetar) Tiga hari... aku harus... gimana?"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Kalau aku bilang ke Aksara... dia pasti ikut."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi kalau aku sendirian... apa aku bisa lindungi mereka?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Atau... aku cuma nyusahin aja?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa menggenggam erat kalung peninggalan ibunya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Keputusan besar menunggunya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi untuk saat ini... ia harus bersiap."

    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Bu... tolong bantu aku ya."
    
    scene black
    with Dissolve(2.0)
    
    jump chapter3_scene5

# SCENE 5 - CHAPTER 3
label chapter3_scene5:
    scene black
    with Dissolve(1.0)
    
    centered "{color=#fff}Malamnya di hari yang sama.{/color}"
    pause 1.0
    

    menu:
        n "Apa yang harus Carissa lakukan dengan informasi ini?"
        
        "Langsung hubungi Aksara, ceritakan semuanya":
            $ aksara_points += 3
            jump scene5_told_aksara
        
        "Simpan dulu":
            $ dewa_points += 2
            jump scene5_keep_secret
        
        "Cerita ke Nenek dulu":
            $ aksara_points += 1
            jump scene5_tell_nenek


label scene5_told_aksara:
    scene bg ruang_tamu_terang
    with dissolve
    
    play music audio.mysterysound4 volume 0.5 fadeout 2.0
    play sound audio.phonevibrate volume 3.0 fadeout 1.0
    n "Carissa langsung menghubungi Aksara dan memintanya datang."
    
    show aksara khawatir at left
    show carissa sedih at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Ada apa lagi? Suaramu kayak ketakutan gitu."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Lalu, Carissa menyeritakan seluruh kejadian singkat tadi saat berada di kafe."
    
    show aksara serius
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Bayangan itu..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengepalkan tangan) Dia ngancam kamu?!"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengangguk) Dia bilang... tiga hari lagi aku harus datang ke candi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Sendirian."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu nggak akan sendirian."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku ikut."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi kalau aku nggak sendirian—"
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku nggak peduli apa maunya Dewa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap Carissa) Aku nggak akan biarkan kamu hadapi dia sendirian."
    
    $ aksara_points += 2
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersenyum sedih) Oke, Aksara..."
    
    jump scene5_preparation

label scene5_keep_secret:
    scene bg kamar_carissa
    with dissolve
    
    play music audio.tension fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa memutuskan untuk tidak memberitahu siapa pun."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Setidaknya... belum."
    
    show carissa sedih at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(duduk di tepi tempat tidur) Kalau aku bilang ke Aksara..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dia pasti ikut. Dan mungkin... dia yang kena bahaya."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap kalung) Tapi... apa aku kuat sendirian?"
    
    play sound audio.wind
    play sound audio.bisikan volume 2.0 fadeout 1.0
    suara "(berbisik lembut) Kamu... cukup kuat..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    suara "Percaya... pada dirimu sendiri..."
    
    show carissa takut
    with hpunch
    play sound audio.nengok volume 1.0 fadeout 1.0
    c "(menoleh cepat) ?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tidak ada siapa-siapa di dalam kamarnya."
    play sound audio.wind2 volume 3.0 fadeout 1.0
    n "Hanya angin malam yang berhembus pelan lewat jendelanya."
    
    show carissa sedih
    play sound audio.menghela volume 3.0 fadeout 1.0
    c "(menghela napas) Aku... harus mikir jernih."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tiga hari. Aku punya waktu tiga hari."
    
    jump scene5_preparation


label scene5_tell_nenek:
    scene bg ruang_tamu_terang
    with dissolve
    
    play music audio.mysterysound3 volume 0.5 fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa memutuskan untuk bercerita pada Nenek terlebih dulu."
    
    show nenek khawatir at left
    show carissa sedih at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nek... tadi aku didatengin satu bayangan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menceritakan kejadian)"
    
    show nenek khawatir
    play sound audio.breathhus volume 3.0 fadeout 1.0
    nenek "(menghela napas berat) Akhirnya... waktunya tiba."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Nenek... apa yang harus aku lakukan?"
    
    show nenek serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Kamu harus cerita ke Aksara, Nduk."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Jangan hadapi ini sendirian."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi kalau Aksara ikut... dia yang bahaya—"
    
    show nenek normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "(menggenggam tangan Carissa) Justru kalau kamu sendirian, itu lebih berbahaya dari apapun."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Aksara itu juga Nirantara yang terlatih, setidaknya ada orang yang bisa jagain kamu."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "..."
    
    show nenek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Percayalah sama orang-orang terdekatmu, Nduk."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Itulah kekuatan sejati."
    
    $ aksara_points += 1
    

    menu:
        "Apa yang Carissa lakukan?"
        
        "Ikuti saran Nenek":
            $ aksara_points += 2
            
            show carissa normal
            
            c "(mengangguk) Oke, Nek. Aku akan hubungi Aksara."
            
            jump scene5_aksara_from_nenek
        
        "Tetap rahasiakan dari Aksara":
            $ dewa_points += 2
            $ aksara_points -= 1
            
            show carissa sedih
            
            c "Maaf, Nek... tapi aku harus lindungi Aksara."
            c "Ini tanggung jawabku."
            
            show nenek khawatir
            
            nenek "(menggeleng sedih) Carissa..."
            
            jump scene5_preparation

label scene5_aksara_from_nenek:
    scene black
    with Dissolve(0.5)
    play sound audio.phonevibrate volume 1.0 fadeout 1.0
    n "Carissa menghubungi Aksara dan menceritakan semuanya."
    
    scene bg ruang_tamu_terang
    with dissolve
    
    show aksara serius at left
    show carissa normal at right
    show nenek normal at center 
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(datang dengan cepat) Carissa, kamu gapapa kan?"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Iya... Nenek yang nyaranin aku buat hubungi kamu."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap Nenek) Terima kasih, Nek."
    
    show nenek senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    nenek "Jaga dia baik-baik, Aksara."
    
    show aksara serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku janji." 

    $ aksara_points += 2
    
    jump scene5_preparation


label scene5_preparation:
    scene black
    with Dissolve(1.0)
    
    centered "{color=#fff}Dua Hari Kemudian{/color}"
    pause 1.0
    
    scene bg kuil
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa dan Aksara bertemu di kuil untuk persiapan terakhir."
    
    
    if aksara_points > dewa_points + 3:

        show aksara normal at left
        show carissa normal at right
        with dissolve
        
        a "Oke, kita punya satu hari lagi."
        a "Kita harus punya rencana."
        
        show carissa bingung
        
        c "Rencananya kayak gimana?"
        
        show aksara serius
        
        a "Pertama: kamu setidaknya harus sedikit ahli pelindungan diri."
        a "Kedua: kita perlu strategi kalau Dewa muncul."
        a "Ketiga: kita harus tau, pilihan apa yang mau kamu ambil."
        
        show carissa sedih
        
        c "Pilihan...?"
        
        show aksara normal
        
        a "Iya, apakah kamu bisa menghindari tipuan Dewa atau tidak."
        
    else:
        
        if dewa_points > aksara_points:
            show aksara normal at left
            show carissa sedih at right
            with dissolve
            
            a "Kamu... keliatan gelisah."
            
            show carissa bingung
            
            c "Aku... nggak apa-apa kok."
            
            show aksara khawatir
            
            a "(curiga) Carissa... ada yang kamu sembunyiin?"
            
            menu:
                "Apa yang Carissa lakukan?"
                
                "Akhirnya jujur ke Aksara":
                    $ aksara_points += 3
                    
                    show carissa sedih
                    
                    c "(menghela napas) Iya... ada yang belum aku ceritain."
                    c "(menceritakan ancaman bayangan)"
                    
                    show aksara serius
                    with vpunch
                    
                    a "KENAPA BARU SEKARANG BILANG?!"
                    
                    show carissa takut
                    
                    c "Aku... aku takut kamu kena bah—"
                    
                    show aksara sedih
                    
                    a "(menghela napas) Carissa..."
                    a "Kita itu tim. Kamu nggak harus tanggung semua sendirian, aku udah pernah bilang kan?"
                    
                    $ aksara_points += 1
                    
                "Tetap rahasiakan":
                    $ dewa_points += 3
                    $ aksara_points -= 2
                    
                    show carissa normal
                    
                    c "Nggak kok. Aku cuma... gugup aja hehehe."
                    
                    show aksara normal
                    
                    a "...Oke. Kalau ada apa-apa, bilang ya."
                    
                    show carissa sedih
                    
                    c "(dalam hati) Maafin aku, Aksara..."
        
        else:
            show aksara normal at left
            show carissa normal at right
            with dissolve
            
            a "Besok... kita ke candi Reksana Sewu."
            
            show carissa bingung
            
            c "Besok? Kenapa?"
            
            show aksara serius
            
            a "Aku ngerasa... waktunya udah deket."
            a "Jadi kita harus bersiap-siap."
    
    show kakek normal at center 
    with dissolve
    
    k "Kalian berdua... sudah siap?"
    
    if aksara_points > dewa_points + 3:
        show carissa senyum
        
        c "(mengangguk mantap) Iya, Kakek. Kami siap."
        
    else:
        show carissa sedih
        
        c "(mengangguk ragu) S-semoga..."
    
    show kakek serius
    
    k "(menyerahkan jimat berbentuk kepala rusa) Ini... jimat pelindung tambahan."
    k "Semoga kalian selamat."
    
    scene black
    with Dissolve(2.0)
    
    centered "{color=#fff}Hari Terakhir{/color}"
    pause 1.5
    centered "{color=#888}Apakah semuanya berjalan dengan baik atau berakhir dengan buruk?{/color}"
    pause 2.0
    
    jump chapter3_scene6

label chapter3_scene6:
    scene black
    with Dissolve(2.0)
    
    play music audio.tensionmusic volume 0.5 fadein 3.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    centered "{color=#fff}Candi Reksana Sewu{/color}"
    pause 1.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    centered "{color=#888}Matahari turun di ufuk barat...{/color}"
    pause 1.5
    
    scene bg candi_gerbang
    with dissolve
    
    play sound audio.wind21 volume 3.0 fadeout 1.0
    n "Langit berwarna jingga kemerahan, pertanda matahari akan segera tenggelam."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa berdiri di depan gerbang candi yang megah."
    
    
    if aksara_points > dewa_points + 3:
        jump scene6_with_aksara
    else:
        jump scene6_alone


label scene6_with_aksara:
    show carissa normal at right
    show aksara serius at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengamati sekeliling) Kamu ngerasa nggak?"
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ngerasa apa?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Energi di sini... nggak stabil."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku ngerasa gerbangnya perlahan-lahan kebuka."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menggunakan mata batinnya) iya... Nggak beraturan sama sekali."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggenggam tangan Carissa) Aku di sini."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Apapun yang terjadi, kita hadapi bareng."
    
    $ aksara_points += 1
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengangguk) Iya."
    
    jump scene6_dewa_appears


label scene6_alone:
    if dewa_points > aksara_points + 3:
        show carissa sedih at center
        with dissolve
        
        c "(dalam hati) Aku... datang sendirian."
        c "Semoga... ini keputusan yang benar."
        
        play sound audio.footsteps
        
        n "Tiba-tiba, terdengar langkah kaki dari belakang."
        
        show carissa kaget
        with vpunch
        play sound audio.noleh volume 3.0 
        c "(menoleh cepat) Siapa?!"
        
        show aksara serius at left
        with easeinleft
        play sound audio.breathcapek volume 3.0 
        a "(terengah-engah) Kamu pikir... aku bakal biarin kamu sendirian?"
        
        show carissa takut at right
        with move
        
        c "Aksara?! Kok kamu—"
        
        show aksara khawatir
        
        a "Nenekmu tadi telpon aku."
        a "(menatap Carissa) Harusnya aku nanya, kok kamu nekat?"
        
        show carissa sedih
        
        c "(menunduk) Maafin aku... aku cuma—"
        
        show aksara normal
        play sound audio.menghela volume 3.0 
        a "(menghela napas) Sudahlah. Yang penting kita harus hadapi bersama."
        
        $ aksara_points += 1
        
    else:
        show carissa normal at right
        show aksara normal at left
        with dissolve
        
        a "Sudah siap?"
        
        show carissa bingung
        
        c "Mmmm, iya..."
        
        show aksara serius
        
        a "Bagus, kalo ada apa-apa harus kasih tau ya."
        
        show carissa normal
        
        c "(mengangguk) Oke."
    
    jump scene6_dewa_appears

label scene6_dewa_appears:
    play sound audio.wind
    with hpunch
    play sound audio.wind4 volume 3.0 fadeout 1.0
    n "Angin tiba-tiba bertiup kencang."
    play sound audio.windrumput volume 3.0 fadeout 1.0
    n "Debu dan dedaunan beterbangan."
    
    show carissa takut
    show aksara serius
    
    play sound audio.heartbeat1 volume 3.0 fadeout 1.0
    n "Salah satu candi batu di depan mereka mulai bergetar hebat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Retakan-retakan bercahaya merah muncul di permukaannya."
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Gerbangnya—!"
    
    show dewa wujud_asli at center
    with flash_red
    
    
    play sound audio.transform volume 3.0 fadeout 1.0
    n "Sosok tinggi besar muncul dari balik gerbang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aura merah gelap menyelimutinya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Ini bukan lagi Dewa yang ramah di sekolah."

    show dewa wujud_asli at center 
    with dissolve
    play sound audio.bisikan volume 3.0 fadeout 1.0
    d "(suara bergema) Carissa... akhirnya kau datang."
    
    show aksara guardian at left
    with flash_blue
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara langsung berubah wujud menjadi sosok pucat biru kehijauan, aura biru tua menyelimutinya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berteriak) JANGAN DEKATI DIA!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tertawa) Nirantara... tetap setia seperti biasa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap Carissa) Tapi aku tidak datang untuk bertarung."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Aku datang... untuk memberikan pilihan, yah anggap saja sebagai kompromi."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Pilihan...?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Pilihan yang akan menentukan nasib dua dunia ini."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Tergantung kamu secara sukarela mau memberikannya atau tidak."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kalau tidak mau, maka... yah aku terpaksa sih harus mengambilnya secara paksa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Senang udah mengenalmu, Carissa."
    play sound audio.mandewa volume 2.0 fadeout 1.0
    a "(berteriak) CUKUP OMONG KOSONGMU!"
    
    play sound audio.magic
    
    show aura_biru at left
    with flash_blue
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara meluncurkan serangan energi biru ke arah Dewa!"
    play sound audio.block volume 3.0 fadeout 1.0
    d "(menangkis dengan mudah)"
    
    play sound audio.wind
    with flash_red
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara terpantul akibat tangkisan dari Dewa."
    
    show  aksara guardian 
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Ugh!"
    
    show carissa kaget
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "AKSARA!"
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menggeleng) Kau terlalu lemah untuk melawanku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap Aksara dengan tatapan tajam) Kau pikir dengan kekuatan kecil itu bisa mengalahkanku?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berdiri dengan susah payah) Selama... aku masih hidup..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku nggak akan membiarkanmu... sentuh dia!"
    
    play sound audio.menghela volume 3.0 fadeout 1.0
    d "(menghela napas) Kesetiaan yang bodoh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(mengangkat tangan)"
    
    show aura_merah at center
    with flash_red
    
    play sound audio.heartbeat
    
    show carissa takut
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "JANGAN!"
    
    show carissa normal at center
    with move
    play sound audio.runn volume 3.0 fadeout 1.0
    n "Carissa berlari ke depan Aksara, membentangkan tangannya."
    
    show kalung_glow at center
    with flash_blue
    
    play sound audio.transformibu volume 3.0 fadeout 1.0
    n "Kalung ibunya bersinar terang!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Pelindung biru muncul dan menahan serangan Dewa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kau... melindunginya?"
    
    show carissa serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(gemetar) Dia... temanku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku nggak akan biarkan kamu nyakitin dia!"
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum tipis) Menarik..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kau rela berkorban?"
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Bukan berkorban. Tapi melindungi orang yang penting untukku."
    
    hide aura_merah
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menurunkan tangan) Baiklah. Aku nggak akan nyerang dia lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap Carissa) Tapi kamu harus dengerin tawaranku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berbisik ke Carissa) Jangan percaya dia..."
    
    show carissa bingung at right
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tawaran apa?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Aku sudah hidup ribuan tahun, Carissa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Selama itu, aku melihat kebodohan yang sama berulang."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kebodohan?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Manusia takut dan membenci kami."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kedua ras selalu hidup dalam kewaspadaan yang tidak perlu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(merentangkan tangan) Tapi bayangkan... jika tidak ada perantara lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Jika manusia dan roh hidup bersama. Tidak ada lagi yang tersembunyi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berteriak) Itu cuma kebohongan! Kamu cuma mau kekuasaan!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum dingin) Kekuasaan?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Aku sudah punya kekuasaan, Penjaga."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Yang aku inginkan... adalah kebebasan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kebebasan untuk keluar dari sangkar ini."
    
    show carissa bingung
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Gimana bisa?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Candi ini... adalah penjara bagiku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Para penjaga berkali-kali mengurungku, termasuk Ibumu juga."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Aku berada tidak sepenuhnya di dunia roh dan tidak sepenuhnya di dunia manusia."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap Carissa) Aku lelah."
    
    # PILIHAN AWAL - Reaksi Carissa
    menu:
        "Bagaimana perasaan Carissa?"
        
        "Kasihan sama Dewa":
            $ dewa_points += 2
            
            show carissa sedih
            
            c "Kamu... terjebak selama ini?"
            
            d "Akhirnya ada yang mengerti."
            
            a "Carissa, jangan percaya—"

            jump scene6_three
            
        "Curiga sama Dewa":
            $ aksara_points += 2
            
            show carissa serius
            
            c "Terus kenapa kamu ganggu aku?"
            c "Kalau cuma mau bebas, kenapa harus melibatkan aku?"
                    
            d "(tersenyum tipis) Karena cuma kamu yang bisa membebaskanku."
            
            jump scene6_three

        "Bingung":
            show carissa bingung
            
            c "Aku... nggak ngerti."
            
            
            d "Kamu akan, makanya dengarkan dulu tawaranku."

            jump scene6_three

label scene6_three:
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Aku beri kamu tiga pilihan, Carissa."
    
    show carissa takut
    play sound audio.gulp volume 3.0 fadeout 1.0
    c "(menelan ludah)"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "PERTAMA: Buka gerbang dengan darah Raktamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Dunia manusia dan roh akan menyatu, tidak ada yang akan jadi penghalang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Ribuan roh yang terjebak seperti aku... akan bebas."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "KEDUA: Tutup gerbang selamanya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Dunia kembali terpisah. Roh kembali ke dimensi mereka."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Tapi... kau akan kehilangan semua kekuatanmu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Menjadi manusia biasa. Tidak bisa melihat kami lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Yah, bisa saja kamu memilih yang ini."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    
    d "KETIGA: Tidak memilih apapun."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Biarkan semuanya seperti sekarang. Gerbang setengah terbuka."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Tapi aku... dan roh lainnya... akan terus mengejarmu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Selamanya."
    
    # AKSARA MENCOBA MEMBERI TAHU KEBENARAN
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa! Jangan dengerin dia!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kalau gerbang dibuka, bukan cuma 'kebebasan' yang terjadi!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Bakalan ada kekacauan abadi juga!"
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap tajam ke Aksara) Diam, Penjaga!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kau hanya takut kehilangan posisimu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Tanpa gerbang, Nirantara tidak dibutuhkan lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "ITU NGGAK BENAR!"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menutup telinga) CUKUP!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Hening sesaat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Hanya suara angin yang berhembus pelan."
    
    show carissa normal
    play sound audio.breathhus volume 3.0 fadeout 1.0
    c "(napas berat) Aku... aku butuh waktu buat mikir."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Sayangnya, waktu adalah kemewahan yang tidak kita miliki."
    
    play sound audio.magic
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Gerbang bergetar lebih hebat!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Gerbang sudah tidak stabil."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Dalam beberapa menit, ia akan runtuh perlahan-lahan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Dan jika itu terjadi..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap Carissa) Tidak ada yang bisa mengendalikannya lagi, kecuali kalo kamu mau."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Maksudnya?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Maksudnya... gerbang akan terbuka secara paksa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dan energinya akan... meledak, hati-hati Carissa."

    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Jadi, Carissa..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Pilih sekarang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Atau biarkan takdir memilih."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa menatap Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Temannya yang selalu ada. Yang selalu melindungi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Lalu menatap Dewa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sosok yang mengaku terjebak sehingga menginginkan kebebasan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dan gerbang di belakangnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Yang menunggu keputusannya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Ibu... apa yang harus aku lakukan?"
    
    # FLASH MEMORY - Pesan Ibu
    play sound audio.heartbeat
    
    centered "{color= "#8b0000"}{i}'Percayalah pada seseorang yang kamu yakini.'{/i}{/color}"
    pause 1.5
    
    show carissa normal
    play sound audio.transisi volume 3.0
    c "(membuka mata) Aku... sudah tau jawabannya."
    
    jump scene6_final_choice

# ================================================
# FINAL CHOICE - Menentukan Ending
# ================================================

label scene6_final_choice:
    scene bg candi_gerbang
    with dissolve
    
    show carissa serius at center
    with dissolve
    
    play music audio.heartbeat fadein 2.0
    
    centered "{color="#fff"}PILIHAN TERAKHIR{/color}"
    pause 2.0
    
    menu:
        n "Apa keputusan Carissa?"
        
        "Tutup gerbang - Percaya Aksara":
            jump ending_good
        
        "Buka gerbang - Percaya Dewa":
            jump ending_bad
        
        "Cari jalan lain":
            jump ending_neutral

# ================================================
# GOOD ENDING - Close Gate
# ================================================

label ending_good:
    $ aksara_points += 5
    
    scene bg candi_gerbang
    with dissolve
    
    show carissa serius at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dengan suara tegas) Aku pilih... TUTUP GERBANG."
    
    show dewa wujud_asli at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Apa?!"
    
    show aksara guardian at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum lega)"
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Dewa) Maaf, Dewa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku paham kamu pengen bebas."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi... aku percaya sama Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Jadi kamu membuang kesempatan ini?"
    
    show carissa serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Bukan membuang. Tapi memilih jalan yang benar."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Dunia mungkin nggak sempurna, tapi itu bukan alasan untuk memaksa perubahan."
    
    show dewa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(terdiam lama)"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "...Kau mirip ibumu."
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ibu?"
    
    show dewa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Wanita yang kuat dan keras kepala."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(suara berubah gelap) TAPI SAYANGNYA..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "AKU TIDAK AKAN MEMBIARKANMU MENUTUP GERBANG!"
    
    show aura_merah at right
    with flash_red
    
    play sound audio.magic
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aura merah Dewa meledak dan energi gelap memenuhi udara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berteriak) CARISSA, MUNDUR!"
    
    play sound audio.wind
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dewa meluncurkan bola serangan energi berwarna merah ke arah Carissa."
    
    show carissa takut at center
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "KYAAA!"
    
    # AKSARA MELINDUNGI
    show aksara guardian at center
    with move
    with flash_blue
    
    play sound audio.magic
    
    show aura_biru at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara melompat ke depan Carissa dan membentuk perisai biru."
    play sound audio.block volume 1.0 fadeout 1.0
    a "(menahan serangan) UGHHH!"
    
    with hpunch
    play sound audio.elemen volume 3.0 fadeout 1.0
    n "Benturan kedua energi pun mengguncang di sekitar candi."
    

    show aksara guardian at left
    with move
    with hpunch
    play sound audio.pusg volume 1.0 fadeout 1.0
    a "(terpental) Akh!"
    
    show carissa kaget
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "AKSARA!"

    hide aksara guardian
    with dissolve
    
    show dewa wujud_asli at center
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "JIKA KAU TIDAK MAU MEMBUKA GERBANG..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "MAKA AKU AKAN MENGAMBIL DARAHMU DENGAN PAKSA!"
    
    show carissa serius at right
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menggenggam kalung) Aku... nggak akan kalah!"
    
    show kalung_glow at right
    with flash_blue
    
    play sound audio.magic
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kalung ibunya bersinar terang, dan mulai membentuk energi biru yang menyelimuti Carissa."
    
    show aura_biru at right
    with dissolve
    play sound audio.crem volume 1.0 fadeout 1.0
    c "(berteriak) INI UNTUK IBU!"
    
    play sound audio.magic
    with flash_blue
    
    show dewa wujud_asli at center
    with flash_red
    play sound audio.block volume 3.0 fadeout 1.0
    d "(menangkis) HAHAHA! LEMAH!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Serangan Carissa sukses membuat Dewa sedikit mundur dari tempatnya."
    

    show aksara guardian at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berdiri) Carissa... kita serang dia bersamaan!"
    
    show carissa normal at right
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengangguk) Oke!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara dan Carissa pun mengumpulkan energi mereka dengan fokus."
    
    show aura_biru at left
    show kalung_glow at right
    with dissolve
    
    play sound audio.heartbeat5 volume 2.0 
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Cahaya biru semakin terang!"
    
    show dewa wujud_asli at center
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "KAU PIKIR ITU CUKUP?!"
    
    show aura_merah at center
    with flash_red
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dewa juga mengumpulkan kekuatannya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berteriak) SEKARANG!"
    
    play sound audio.magic
    with flash_blue
    with flash_red
    
    with hpunch
    with vpunch
    play sound audio.boom2 volume 3.0
    n "Ledakan dahsyat benar-benar mengguncangkan seluruh wilayah candi."
    
    scene white
    with Dissolve(0.3)
    
    play sound audio.wind
    
    scene bg candi_gerbang
    with Dissolve(0.5)
    
    # HASIL PERTARUNGAN
    show dewa sedih at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Asap perlahan menghilang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Dewa berlutut, aura merahnya melemah."
    play sound audio.breathhus volume 2.0 fadeout 1.0
    d "(napas berat) Kalian... kuat."
    
    show aksara guardian at left
    show carissa normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara dan Carissa masih berdiri meski lelah."
    play sound audio.breathcapek volume 2.0 fadeout 1.0
    a "(terengah) Sekarang, Carissa!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tutup gerbangnya sebelum dia pulih!"
    
    show carissa serius
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengangguk)"
    
    hide aura_biru
    hide kalung_glow
    with dissolve

    
    show carissa normal at center
    with move
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Aksara) Aku harus gimana?"
    
    show aksara normal at left
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Sentuh gerbang. Alirkan darahmu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku akan bantu menstabilkan energimu."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku... bakal kehilangan kekuatan kan?"
    
    show aksara khawatir
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengangguk)"
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Gapapa. Selama semua orang selamat serta aku juga."
    
    # PROSES PENUTUPAN
    play sound audio.magic
    
    show kalung_glow at center
    with flash_blue
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa berjalan ke candi batu yang bergetar."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Menggunakan pecahan batu, ia melukai telapak tangannya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(meringis) Ssssh..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Darah merah segar menetes ke permukaan gerbang."
    
    show aura_biru at left
    with flash_blue
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara meletakkan tangannya di bahu Carissa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Menyalurkan energi biru untuk menstabilkan proses."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berbisik) Fokus, Carissa. Bayangkan gerbang tertutup rapat."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    
    c "(menutup mata untuk berkonsentrasi)"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Cahaya biru dari Aksara dan cahaya merah dari darah Carissa mulai bercampur."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Membentuk pola segel berbentuk pola candi di permukaan."
    
    show dewa sedih at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(menatap dengan tatapan lelah)"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Jadi... ini akhirnya... hahah."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(membuka mata sejenak) Dewa..."
    
    show dewa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum tipis) Sampaikan salamku... pada ibumu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Di kehidupan yang lain."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Sosok Dewa perlahan memudar seperti asap."
    
    hide dewa normal
    with flash_white
    
    play sound audio.wind
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tersedot kembali ke dalam gerbang yang mulai menutup."

    play sound audio.magic
    with flash_white
    
    hide kalung_glow
    hide aura_biru
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Segel bersinar terang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Retakan-retakan mulai menyatu satu per satu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Portal yang ada di candi batu pun tertutup rapat kembali."
    
    show carissa sedih at center
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa merasakan sesuatu hilang dari dalam dirinya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Seperti ada yang dicabut paksa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(membuka mata) Aku... aku nggak bisa ngerasain apa-apa lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kemampuan melihat roh... sudah lenyap."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tubuhnya sempoyongan karena kakinya kehilangan tenaga."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara telah kembali dalam wujud manusianya."
    
    show aksara normal at left
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menangkap) Carissa!"
    
    show carissa senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersenyum lemah) Makasih... Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Kita... berhasil kan?"
    
    show aksara senyum
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum) Iya. Kita berhasil."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu hebat."
    
    show carissa normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku cuma... ngikutin hatiku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Aksara) Dan percaya sama kamu."
    
    show aksara normal
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku juga percaya sama kamu. Dari awal."
    
    scene black
    with Dissolve(2.0)
    
    play music audio.mystery_theme fadein 2.0
    
    centered "{color="#0f0"}GOOD ENDING{/color}"
    pause 1.5
    centered "{color="#fff"}KEPERCAYAAN{/color}"
    pause 2.0
    
    scene bg halaman_sekolah
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Beberapa minggu kemudian..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Kehidupan kembali normal."
    
    show carissa senyum at right
    show aksara senyum at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Gimana rasanya jadi manusia normal?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tertawa) Enak ternyata. Kayak tenang gitu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku bisa tidur nyenyak tanpa mimpi buruk lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Nggak nyesel kehilangan kekuatan nih?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menggeleng) Nggak."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku lebih suka kehidupan yang damai."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Aksara) Lagipula... aku punya kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum) Selalu."
    
    hide carissa senyum at right
    hide aksara senyum at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Gerbang Roh memang sudah tertutup seperti yang sudah diketahui."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi... apakah Dewa benar-benar tertahan kali ini?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Atau hanya kehilangan sebagian kekuatannya dan telah menhilang?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Entahlah, untuk saat ini dunia telah aman."
    
    scene black
    with Dissolve(2.0)
    
    centered "{color="#fff"}TAMAT{/color}"
    pause 2.0
    centered "{color="#888"}Terima kasih telah bermain{/color}"
    centered "{color="#888"}'Veil of Two Fates'{/color}"
    pause 2.0
    

# ================================================
# BAD ENDING - Open Gate
# ================================================

label ending_bad:
    $ dewa_points += 5
    
    scene bg candi_gerbang
    with dissolve
    
    show carissa sedih at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dengan suara ragu) Aku... aku pilih BUKA GERBANG."
    
    show aksara guardian at left
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "CARISSA, JANGAN!"
    
    show dewa wujud_asli at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum lebar) Bijak."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Aksara) Maafin aku..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(bergetar) Kenapa...?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Lihat? Dia memilih dengan benar. Sekarang..."
    
    show aksara guardian at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Kau tidak bisa berbuat apa-apa lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggenggam senjata) Aku tidak akan membiarkanmu!"
    
    play sound "sfx_combat.ogg"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Aksara melesat maju, cahaya suci mengelilingi tubuhnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Namun kekuatan Dewa sudah terlalu kuat. Dari belakang gerbang batu terbuka, memberi energi gelap mengalir bebas."
    
    show aksara guardian at center
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(terjatuh, napas tersengal) Ngh...!"
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tertawa dingin) Sudah kubilang. Kau tidak bisa menang."
    
    show carissa sedih at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berbisik) Aksara..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengangkat kepala) Carissa... tolong... kita masih bisa—"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menggeleng pelan) Tidak, Aksara. Hentikan."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Apa...?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Menyerahlah. Kamu tidak bisa menang. Tidak ada gunanya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(dengan suara parau) Kenapa kamu bilang begitu...? Carissa, ini bukan dirimu!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(suara bergetar) Ini memang aku. Aku yang sebenarnya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berusaha berdiri) Tidak... kamu lebih kuat dari ini. Kamu punya nenekmu, kamu punya—"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(memotong) Nenek? Ya, kamu benar."
    
    show carissa marah
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi apa itu cukup? Aku tetap sendirian, Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Carissa..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Semua orang punya keluarga utuh. Ayah, ibu, kakak, adik. Tapi aku?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tertawa getir) Aku cuma punya nenek tua yang bahkan nggak bisa ngerti apa yang aku rasain."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menggeleng keras) Itu tidak benar! Nenekmu sayang sama—"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Sayang?! Dia bahkan nggak nenangin aku waktu susah tidur setiap malam!"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(suara melemah) Dia nggak ngerti kenapa aku selalu merasa... kosong."
    
    hide dewa wujud_asli
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Suara berbisik mulai terdengar di sekitar Carissa. Lembut tapi beracun."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(suara gaib) Ya... kau sendirian... selalu seperti itu..."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(memegang kepala) Hentikan..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Bahkan saat nenekmu memelukmu... kau masih merasa hampa, bukan?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(bergetar) A-aku..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(merangkak mendekati) Carissa!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Jangan dengarkan bisikan itu!"
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap kosong)"
    
    scene kamar_carissa
    with dissolve
    
    "FLASHBACK: Malam pertama Carissa tiba di rumah Nenek."
    
    show carissa sedih at center
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(monolog) Pertama kali aku datang ke sini... aku merasa aneh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Seperti ada yang memanggilku bilang... 'Aku mengerti kamu.'"
    play sound audio.bisikan volume 3.0 fadeout 1.0
    d "(suara bisikan) Tenang... aku di sini..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berbaring di tempat tidur) Siapa...?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Orang yang kau percayai..."
    
    scene bg candi_gerbang
    with dissolve
    
    show carissa bingung at left
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersadar) Apa itu tadi?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Semua itu..."
    
    show dewa wujud_asli at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(muncul kembali) Aku hanya membantumu melihat kebenaran."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Bahwa kau memang sendirian. Bahwa tidak ada yang benar-benar peduli."
    
    show aksara guardian at center
    with vpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berteriak) ITU BOHONG!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Nenekmu merawatmu! Dia benar-benar menyayangimu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dan aku... aku juga peduli padamu, Carissa!"
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Aksara dengan berkaca-kaca) Tapi... kenapa rasanya tetap sakit?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Karena dia yang bikin seolah-olah kamu merasa begitu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menunjuk Dewa) Dia memanfaatkanmu!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tertawa) Oh... Bukan aku."
    
    show carissa sedih
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berlutut) Aku... aku tidak tahu lagi..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Mana yang beneran... mana yang bukan..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(merangkak lebih dekat) Carissa, dengarkan aku."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Perasaanmu itu nyata. Kesedihanmu itu nyata. Tapi..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu tidak sendirian."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengangkat kepala) Aksara..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(nada dingin) Terlambat."
    
    show dewa wujud_asli at center
    with vpunch

    show carissa kaget 
    with hpunch

    show aksara guardian at right
    with dissolve

    play sound "dark_power.ogg"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Energi gelap dari gerbang mulai mengalir ke tubuh Carissa."
    
    show carissa takut
    with hpunch
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(berteriak) AKH! APA INI?!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "Ini hadiah untukmu, biar ga pernah merasa sakit lagi."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berusaha meraih Carissa) CARISSA, TIDAK!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Tapi sudah terlambat."
    
    scene bg black
    with fade
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Cahaya menelan segalanya."
    
    scene bg candi_reruntuhan
    with fade
    
    show aksara guardian at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(terbaring lemah) Carissa... di mana..."
    
    show carissa corrupted at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa berdiri di depannya. Tapi matanya kosong. Tidak ada kehangatan di sana."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dengan suara datar) Aku di sini, Aksara."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(bergetar) Carissa... kamu..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku tidak merasakan apa-apa lagi. Tidak sakit. Tidak sedih."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersenyum hambar) Tidak sendirian."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menangis) Ini bukan yang kamu inginkan..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Ini persis yang aku inginkan."
    
    show dewa wujud_asli at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(merangkul bahu Carissa) Sekarang dia milikku."
    play sound audio.keyyi volume 1.0 fadeout 1.0 
    d "Dan dunia ini... akan segera menyusul."
    
    scene black
    with fade
    
    centered "{color="#8B0000"}BAD ENDING{/color}"
    centered "{color="#8B0000"}TERTELAN KEGELAPAN{/color}"
     
    centered "Carissa memilih untuk membuka gerbang."
    centered "Kekuatan gelap Dewa yang telah lama membisikinya akhirnya mengambil alih sepenuhnya."
    centered "Aksara gagal menyelamatkan Carissa."

    centered "Dewa pun memanfaatkan Darah Rakta milik Carissa untuk membuka Gerbang Roh."
    centered "Dan kegelapan perlahan menyebar ke seluruh dunia..."
    
    centered "{color="#fff"}TAMAT{/color}"
    pause 2.0
    centered "{color="#888"}Terima kasih telah bermain{/color}"
    centered "{color="#888"}'Veil of Two Fates'{/color}"
    pause 2.0

# ================================================
# NEUTRAL ENDING - Aksara's Sacrifice
# ================================================

label ending_neutral:
    $ aksara_points += 3
    
    scene bg candi_gerbang
    with dissolve
    
    show carissa sedih at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dengan suara gemetar) Aku... aku tidak bisa memilih..."
    
    show aksara guardian at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap Carissa) Carissa..."
    
    show dewa wujud_asli at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tersenyum tipis) Tidak bisa memilih? Lemah."
    
    show carissa marah
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "BUKAN! Aku bukan lemah!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap Aksara) Aku hanya... tidak mau ada yang terluka lagi."
    play sound audio.footstep1x volume 3.0 fadeout 1.0
    a "(melangkah maju) Carissa, kamu tidak perlu menanggung ini sendirian."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Ada cara lain."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Cara lain?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap gerbang) Gerbang ini..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Butuh seseorang yang bisa mengunci Dewa selamanya, tapi tetap membiarkan roh-roh lain hidup bebas."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(tertawa mengejek) Kau pikir kau bisa menandingi kekuatanku?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap tajam) Aku tak perlu mengalahkanmu. Aku hanya perlu... menahanmu."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aksara, tunggu—kamu ngomong apa?"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum lembut) Aku adalah Nirantara. Ini tugasku sejak awal."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Melindungi keseimbangan dunia ini."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menggeleng keras) Tidak! Pasti ada cara lain!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tidak ada, Carissa. Jika gerbang ditutup sepenuhnya, semua roh akan terkurung termasuk yang tidak bersalah."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Jika gerbang terbuka... Dewa akan bebas merusak segalanya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Tapi jika ada penjaga yang mengunci gerbang dari dalam..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Dewa akan terkurung. Roh-roh lain tetap bisa hidup di dunia manusia, dunia akan tetap aman."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(air mata mulai jatuh) Tapi... kamu..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku akan baik-baik saja. Ini pilihan yang harus aku buat."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(murka) KAU PIKIR KAU SIAPA?!"
    
    show dewa wujud_asli at center
    with vpunch
    
    play sound audio.darkpower volume 2.0 fadeout 2.0
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Energi gelap meledak dari tubuh Dewa, membuat tanah berguncang."
    
    show aksara guardian at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(mengangkat tangan, cahaya suci pun muncul)"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku hanya perlu mengikatmu... selamanya."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    play sound "holy_power.ogg"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Cahaya biru tua memancar dari tubuh Aksara, membentuk rantai-rantai energi yang melilit Dewa."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    d "(berteriak) TIDAK! LEPASKAN!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(dengan tenang) Ini adalah pengorbananku."
    
    play sound audio.footstep1xx loop volume 3.0 fadeout 1.0
    n "Aksara berjalan mendekati gerbang, sementara rantai cahaya terus mengikat Dewa."
    
    show aksara guardian at center
    with dissolve
    
    show carissa sedih at left
    with dissolve
    play sound audio.runn loop volume 3.0 fadeout 1.0
    c "(berlari) AKSARA, JANGAN!"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(berbalik, tersenyum) Carissa... kamu kuat. Lebih kuat dari yang kamu kira."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menangis) Aku tidak mau kamu pergi..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Aku tidak pergi. Aku akan selalu di sini."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(menatap lembut) Dan kamu... harus hidup. Untuk nenekmu. Untuk dirimu sendiri."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tapi—"
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Jangan biarkan kesepianmu menang. Kamu punya orang yang sayang sama kamu."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "Kamu tidak sendirian, Carissa. Tidak pernah."
    
    show carissa takut
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(mengulurkan tangan) Aksara..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    a "(tersenyum terakhir kali) Terima kasih... sudah mengingatkanku kenapa aku menjadi Nirantara."
    
    play sound "light_explosion.ogg"
    
    scene bg white
    with flash
    play sound audio.light volume 3.0 fadeout 1.0
    n "Cahaya menyilaukan memenuhi sekitar candi."
    
    show carissa sedih at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(terjatuh) Aksara..."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Gerbang sekarang berkilauan dengan cahaya biru putih. Di permukaannya, terukir simbol rumit."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Carissa bisa merasakan—Aksara ada di sana."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menyentuh gerbang) Aku janji... aku akan hidup dengan baik."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Aku tidak akan menyia-nyiakan pengorbananmu."
    
    scene bg ruang_tamu_terang
    with fade
    play sound audio.transisi volume 3.0
    n "Beberapa hari kemudian..."
    
    show nenek normal at right
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    n "Carissa! Makan siang sudah siap!"
    
    show carissa normal at left
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(tersenyum kecil) Iya, Nek. Tunggu sebentar."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Carissa menatap ke arah luar jendela."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(dalam hati) Terima kasih, Aksara."
    
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Kehidupan Carissa berlanjut dengan damai."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Roh-roh masih ada dengan muncul dimana-mana."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Tapi mereka tidak berbahaya lagi. Tanpa iming-iming kekuatan dari Dewa, mereka hanya... ada."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Hidup berdampingan dengan manusia, seperti yang seharusnya."
    
    show carissa normal at center
    with dissolve
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "(menatap langit) Dunia ini... berbeda sekarang."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    c "Tidak sempurna. Tapi... lebih baik."
    
    scene bg candi_gerbang
    with fade
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Di dalam candi, gerbang masih berdiri kokoh."
    play sound audio.keyyi volume 1.0 fadeout 1.0
    "Cahaya biru berkilauan lembut di permukaannya."
    play sound audio.keyyi volume 1.0 fadeout 1.0 
    "Dan di balik gerbang itu, Aksara berdiri tanpa lelah menjaga agar kegelapan tidak pernah keluar lagi."
    
    show aksara guardian_spirit at center
    with dissolve
    
    a "(monolog internal) Ini adalah tempatku sekarang."
    
    scene bg black
    with fade
    
    centered "{color="#FFD700"}NEUTRAL ENDING{/color}"
    centered "{color="#FFD700"}PENJAGA ABADI{/color}"
    
    centered "Aksara memilih untuk menjadi penjaga gerbang selamanya."
    centered "Dewa terkurung, tidak bisa melarikan diri."
    centered "Roh-roh tetap hidup di dunia manusia,tanpa pengaruh jahat."
    
    centered "Carissa kehilangan Aksara, tapi dunia diselamatkan."
    centered "Keseimbangan tercapai dengan pengorbanan."

    centered "{color="#fff"}TAMAT{/color}"
    pause 2.0
    centered "{color="#888"}Terima kasih telah bermain{/color}"
    centered "{color="#888"}'Veil of Two Fates'{/color}
    pause 2.0
 
return   

#credit scene
# --- 4. PENGATURAN TAMPILAN CREDITS ---

# A. ANIMASI GERAK (Transform)
# Saya ubah ypos akhir menjadi -2.5 agar teks yang panjang bisa naik sampai hilang sepenuhnya
transform credits_scroll(waktu_scroll):
    ypos 1.1
    linear waktu_scroll ypos -2.5

# B. TAMPILAN LAYAR (Screen)
screen rolling_credits():
    # Memastikan screen ini ada di layer paling atas
    zorder 100
    
    # Background hitam
    add "#000"

    frame:
        background None
        xalign 0.5
        
        # Terapkan animasi gerak (Durasi diperlama jadi 25.0 detik agar terbaca)
        at credits_scroll(25.0)

        vbox:
            xalign 0.5
            spacing 25 # Jarak antar baris sedikit diperlebar

            # --- JUDUL ---
            text "CREDITS" size 65 bold True color "#ffffff" xalign 0.5
            null height 60 

            # --- BAGIAN GUI ---
            text "GUI & Interface Design" size 30 color "#cccccc" xalign 0.5
            text "Revano" size 45 bold True color "#ffffff" xalign 0.5
            null height 40

            # --- BAGIAN CODING SCRIPT ---
            text "Lead Programmer / Scripting" size 30 color "#cccccc" xalign 0.5
            text "Khanza" size 45 bold True color "#ffffff" xalign 0.5
            null height 40

            # --- BAGIAN NASKAH & ASET ---
            text "Story Writer & Asset Management" size 30 color "#cccccc" xalign 0.5
            text "Naswa" size 45 bold True color "#ffffff" xalign 0.5
            text "Syafira" size 45 bold True color "#ffffff" xalign 0.5
            null height 40

            # --- BAGIAN MINI GAME ---
            text "Mini Game Developers and Sound" size 30 color "#cccccc" xalign 0.5
            text "Fadly" size 45 bold True color "#ffffff" xalign 0.5
            text "Salman" size 45 bold True color "#ffffff" xalign 0.5
            null height 40

            #--- BAGIAN SPRITE---
            text "Ilusstator Character" size 30 color "#cccccc" xalign 0.5
            text "Alfi" size 45 bold True color "#ffffff" xalign 0.5
            text "Michele" size 45 bold True color "#ffffff" xalign 0.5
            text "Khanza" size 45 bold True color "#ffffff" xalign 0.5
            null height 60


            # --- PENUTUP ---
            text "Special Thanks" size 30 color "#cccccc" xalign 0.5
            text "Alfi & Michele" size 35 bold True color "#ffffff" xalign 0.5
            text "Our Teachers & Friends" size 35 bold True color "#ffffff" xalign 0.5
            null height 60

            text "Thanks for Playing!" size 55 bold True color "#ffff00" xalign 0.5
            # --- AKHIR TEKS ---