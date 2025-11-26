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

# ===== BACKGROUNDS =====
image bg rumah_tua_malam = "rumah_tua_malam.png"
image bg rumah_tua_siang = "rumah_tua_siang.jpg"
image bg ruang_tamu_temaram = "ruang_tamu_temaram.png"
image bg ruang_tamu_terang = "ruang_tamu_terang.png"
image bg kamar_carissa = "kamar_carissa.png"
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


# ===== CHARACTER SPRITES - CARISSA =====
image carissa normal = "carissa_normal.png"
image carissa sedih = "carissa_sedih.png"
image carissa takut = "carissa_takut.png"
image carissa kaget = "carissa_kaget.png"
image carissa bingung = "carissa_bingung.png"
image carissa senyum = "carissa_senyum.png"

# ===== CHARACTER SPRITES - AKSARA =====
image aksara normal = "aksara_normal.png"
image aksara serius = "aksara_serius.png"
image aksara khawatir = "aksara_khawatir.png"
image aksara sedih = "aksara_sedih.png"
image aksara marah = "aksara_marah.png"
image aksara senyum = "aksara_senyum.png"
image aksara guardian = "aksara_guardian.png"  # Mode penjaga

# ===== CHARACTER SPRITES - DEWA =====
image dewa normal = "dewa_normal.png"
image dewa senyum = "dewa_senyum.png"
image dewa misterius = "dewa_misterius.png"
image dewa marah = "dewa_marah.png"
image dewa sedih = "dewa_sedih.png"
image dewa serius = "dewa_serius.png"
image dewa wujud_asli = "dewa_wujud_asli.png"  # Wujud roh

# ===== CHARACTER SPRITES - NENEK & KAKEK =====
image nenek normal = "nenek_normal.png"
image nenek khawatir = "nenek_khawatir.png"
image nenek senyum = "nenek_senyum.png"

image kakek normal = "kakek_normal.png"
image kakek khawatir = "kakek_khawatir.png"
image kakek senyum = "kakek_senyum.png"


# ===== NPC SPRITES =====
image npc generic = "npc_generic.png"
image guru = "guru.png"
image pemandu = "pemandu.png"

# ===== SPECIAL EFFECTS & ENTITIES =====
image hantu weak = "hantu_weak.png"
image hantu medium = "hantu_medium.png"
image hantu strong = "hantu_strong.png"
image bayangan = "bayangan.png"
image roh_kecil = "roh_kecil.png"
image cermin_bergetar = "cermin_bergetar.png"
image lilin = "lilin.png"
image mata_biru = "mata_biru_glow.png"
image aura_merah = "aura_merah.png"
image aura_biru = "aura_biru.png"
image jimat_glow = "jimat_glow.png"
image kalung_glow = "kalung_glow.png"

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
# ================================================
# CHAPTER 1 - AWAL TAKDIR
# ================================================

label start:
    scene black
    with Dissolve(1.0)
    
    play music audio.rain fadein 2.0
    
    centered "{color=#fff}Di suatu tempat, garis antara dua dunia mulai memudar...{/color}"
    pause 1.0
    centered "{color=#888}Dan seorang gadis berdiri tepat di tengahnya.{/color}"
    pause 1.0
    
    scene bg rumah_tua_malam
    with slow_dissolve
    
    n "Malam itu, udara menggantung begitu pekat."
    n "Bukan karena hujan yang mengetuk jendela dengan ritme lambat..."
    n "Melainkan karena sesuatu yang menunggu di balik sunyi, mulai bangkit dari kegelapan."
    
    jump scene1_rumah_tua

# ===== SCENE 1: Rumah Tua =====
label scene1_rumah_tua:
    scene bg ruang_tamu_temaram
    with slow_dissolve
    
    play sound audio.wind
    
    show carissa sedih at center
    with dissolve
    pause 1.0
    
    n "Carissa duduk sendirian di ruang tamu yang remang-remang."
    n "Hujan mengetuk jendela dengan ritme menenangkan, namun entah mengapa, hatinya justru terasa gelisah."
    n "Di tangannya, sebuah foto lama—wajah ibunya tersenyum lembut di samping neneknya."
    
    c "(berbisik) Ibu... kenapa sih aku harus warisi semua ini?"
    
    play sound audio.heartbeat
    
    n "Tiba-tiba, suara langkah kaki terdengar dari luar kamar."
    
    show carissa kaget
    with vpunch
    
    c "Nek?"
    
    pause 1.0
    
    n "Tidak ada jawaban."
    n "Angin berhembus lembut ke arahnya, membawa dingin yang menusuk hingga ke tulang."
    
    show carissa takut
    
    c "(menelan ludah) H-hiii!~"
    
    play sound audio.wind
    
    n "Sunyi yang mencekam membuat bulu kuduknya berdiri."
    
    stop music fadeout 2.0
    
    suara "Carissa..."
    
    show carissa takut at right
    with move
    
    c "(suara bergetar) Siapa?!"
    
    show cermin_bergetar at left
    with flash_white
    
    play sound audio.heartbeat
    
    n "Cermin di meja rias bergetar pelan."
    n "Di pantulannya, sosok perempuan bergaun putih muncul—berdiri tepat di belakang Carissa."
    
    show hantu medium at center behind carissa
    with dissolve
    
    show carissa kaget
    with vpunch
    
    n "Carissa berbalik dengan cepat—"
    
    hide hantu medium
    with flash_red
    
    n "—kosong."
    n "Tidak ada siapa pun."
    
    show carissa sedih
    
    c "(berbisik, hampir menangis) Ibu... Nenek..."
    
    n "Carissa menutup matanya erat, berharap semua ini hanya ilusi."
    
    show lilin at left
    with dissolve
    
    n "Namun lilin di altar kecil neneknya tiba-tiba bergoyang tampa angin."
    
    play music audio.tension
    
    suara "(bergema) Gerbang mulai terbuka..."
    suara "Kau... kuncinya..."
    
    show carissa takut
    with hpunch
    
    c "(menutup telinga) Pergi... jangan ganggu aku!"
    
    hide lilin
    with flash_red
    
    play sound audio.wind
    
    n "Lilin padam seketika."
    
    scene black
    with Dissolve(2.0)
    
    stop music fadeout 3.0
    
    n "Kegelapan menyelimuti segalanya dalam sekejap mata."
    n "Sepanjang malam, Carissa menatap langit-langit kamarnya tanpa tidur."
    n "Setiap kali memejamkan mata, suara dari cermin itu terpantul kembali di pikirannya."
    
    pause 2.0
    
    jump scene2_sekolah_pagi

# ===== SCENE 2: Sekolah Pagi =====
label scene2_sekolah_pagi:
    play music audio.mystery_theme fadein 3.0
    
    scene bg halaman_sekolah
    with slow_dissolve
    
    n "Pagi berikutnya, matahari terasa redup meski waktu sudah menunjukkan pukul tujuh."
    
    show carissa bingung at center
    with dissolve
    
    n "Carissa berjalan dengan langkah terburu-buru menuju gerbang sekolah."
    n "Kantung matanya menghitam—jelas ia tak tidur semalaman."
    
    c "(dalam hati) Siapa sih wanita yang muncul tadi malam..?"
    
    n "Setiap kali memejamkan mata, wajah perempuan bergaun putih itu muncul kembali."
    
    play sound audio.footsteps
    
    n "Suara langkah kaki terdengar di belakangnya."
    
    show carissa kaget
    with hpunch
    
    n "Carissa menoleh dengan cepat—"
    n "—tidak ada siapa pun."
    
    c "(gemetar) Aku yakin tadi ada yang ngikutin deh..."
    
    a "Carissa!"
    
    show carissa kaget at right
    with move
    
    show aksara normal at left
    with easeinleft
    
    n "Carissa terlonjak kaget."
    n "Di bawah pohon besar, Aksara berdiri dengan payung dan tas selempang."
    n "Wajahnya tenang, namun matanya menatap dengan dalam ke arah Carissa."
    
    show carissa normal
    
    c "(berusaha tersenyum) Jangan nakutin gitu dong! Kaget tau."
    
    show aksara serius
    
    a "Kamu keliatan pucat. Ada sesuatu yang ganggu kamu?"
    
    show carissa bingung
    
    c "Ih, sok tau! Maksudnya ganggu gimana?"
    
    show aksara khawatir
    
    a "(pelan tapi tegas) Aura kamu... beda. Nggak kayak biasanya."
    
    n "Carissa tertawa kecil, namun nada suaranya terdengar goyah. Matanya sesaat melirik sekeliling, seolah ada sesuatu yang mengawasinya."
    
    show carissa normal
    
    c "Aura? Kamu ngomong apaan sih!? Jangan mulai hal aneh lagi deh, Aksara."
    
    show aksara serius
    
    a "Kamu tau kan aku tinggal di kuil. Aku bisa ngerasain kalau ada roh yang ngikutin seseorang—bisa ganggu keseimbangan energi orang itu."
    
    n "Senyum Carissa perlahan memudar, menatap Aksara dengan ekspresi campur aduk antara takut dan bingung."
    
    show carissa takut
    
    c "(ragu) Jadi... kamu ngerasa ada yang... ngikutin aku?"
    
    a "(diam sejenak) Bukan cuma ngikutin. Lebih ke... ada sesuatu yang kebuka, dan kayaknya lagi ngincar kamu."
    
    show carissa kaget
    with vpunch
    
    c "Kebuka? Maksudnya?"
    
    a "(mengalihkan pandangan) Susah buat dijelasin. Tapi intinya... jangan anggep ini enteng."
    a "Kalau kamu terus ngeliat mereka tanpa perlindungan, mereka mungkin bakal nyerang kamu."
    
    show carissa sedih
    
    c "(menggenggam tas) Aksara..."
    
    show aksara khawatir
    
    a "Carissa, kamu harus percaya sama aku—"
    
    play sound audio.school_bell
    
    n "Bel sekolah tiba-tiba berbunyi keras, memecah ketegangan di antara mereka berdua."
    n "Suara ramai siswa mengalir di halaman, namun bagi Carissa, semuanya terasa semakin tak nyaman."
    
    show carissa normal
    
    c "(memotong) Nanti aja ya. Aku... takut dengerinnya."
    
    n "Aksara menatapnya lama, seperti menimbang sesuatu yang ia tahu namun enggan diucapkan."
    n "Akhirnya ia menunduk dengan pasrah."
    
    show aksara serius
    
    a "(menghela napas) Oke. Tapi ingat satu hal—"
    a "Jangan percaya siapa pun yang bilang tau soal kamu... kecuali aku."
    a "Oh iya, jangan lupa selalu bawa jimat ini kemana-mana."
    
    n "Aksara memberi Carissa sebuah jimat yang tampak kecil—terbuat dari logam hitam dengan guratan simbol kuno di permukaannya."
    n "Di tengahnya tertanam pecahan batu merah gelap yang memantulkan cahaya samar."
    n "Aksara menatap Carissa lama. Matanya menajam, seperti sedang menimbang sesuatu yang bahkan ia takut akui."
    
    a "(berkata pelan) Aku cuma nggak mau kehilangan orang lagi..."
    
    show carissa bingung
    
    n "Carissa mengerutkan kening, bingung dengan maksud kata-kata Aksara."
    n "Kata-kata itu menggantung di kepalanya, terasa seperti peringatan—atau sesuatu yang lebih dari yang terlihat."
    n "Namun, Carissa mengenggam erat jimat itu di telapak tangannya saat mendengar nada ketakutan dari Aksara."
    
    scene black
    with Dissolve(1.0)
    
    jump scene3_kelas

# ===== SCENE 3: Kelas - Murid Baru =====
label scene3_kelas:
    scene bg kelas
    with dissolve
    
    play sound audio.classroom_chatter
    
    n "Kelas sudah ramai dengan suara obrolan siswa. Ruangan itu dipenuhi canda tawa yang menggema di dinding."
    
    show carissa normal at right
    with dissolve
    
    n "Carissa duduk di bangkunya, masih memikirkan percakapan dengan Aksara tadi."
    
    play sound audio.door_open
    
    n "Pintu kelas terbuka."
    n "Guru masuk bersama seseorang yang belum pernah Carissa lihat."
    
    show guru at left
    with easeinleft
    
    guru "Anak-anak, perhatian sebentar!"
    
    stop sound fadeout 1.0
    
    n "Kelas mulai hening."
    
    guru "Hari ini kita kedatangan murid baru. Perkenalkan, Dewa Abinaya."
    
    show dewa senyum at center
    with dissolve
    
    n "Seorang pemuda berdiri dengan percaya diri."
    n "Rambut pirangnya mencolok, matanya tajam namun entah kenapa terasa... menenangkan?"
    n "Senyumnya membuat setengah dari siswa di kelas terpana akan ketampanan yang tidak biasa dari siswa baru ini."
    
    d "(tersenyum ramah) Senang bertemu kalian. Semoga kita bisa akrab ya."
    
    hide dewa senyum
    show npc generic at right
    with dissolve
    
    siswa1 "(berbisik) Ganteng banget..."
    siswa2 "(berbisik) Kayak misterius gitu ya."
    siswa3 "(berbisik) Namanya Dewa, cocok sih."
    
    n "Carissa menatap pemuda itu tanpa sadar."
    
    show dewa misterius
    
    n "Saat mata mereka bertemu, seolah waktu berhenti."
    
    show mata_biru at center
    with flash_white
    
    n "Sekilas, Carissa melihat bayangan api biru berpendar di balik mata Dewa."
    
    hide mata_biru
    with dissolve
    
    show carissa kaget
    with vpunch
    
    c "(dalam hati, terkejut) Apa itu...? Kenapa matanya kayak bercahaya?"
    
    show dewa senyum
    
    n "Dewa tersenyum lembut ke arah Carissa... seolah-olah ia bisa menembus pikiran Carissa."
    
    hide dewa senyum
    with easeoutright
    
    show carissa bingung at right
    
    c "(dalam hati) Kenapa dia natap aku kayak gitu? Ngeri ah..."
    
    hide guru
    with dissolve
    
    n "Guru mempersilakan Dewa duduk."
    n "Ia berjalan melewati bangku Carissa."
    n "Namun Carissa justru merasakan hawa dingin yang aneh terpancar dari pemuda pirang itu."
    
    show carissa takut
    
    c "(dalam hati) Dinginnyeee~"
    
    scene black
    with Dissolve(1.0)
    
    jump scene4_perpustakaan

# ===== SCENE 4: Perpustakaan =====
label scene4_perpustakaan:
    scene bg perpustakaan
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Sore hari pun tiba. Carissa berada di perpustakaan yang sepi dan tenang."
    
    show carissa normal at center
    with dissolve
    
    n "Ia sibuk mencari buku untuk tugas kelompok, berjalan di antara rak-rak tinggi yang berjejer—membuat Carissa sedikit kewalahan."
    
    play sound audio.footsteps
    
    n "Langkah kaki pelan terdengar di balik sunyinya perpustakaan."
    n "Carissa pun menoleh, namun tidak ada seorang pun yang terlihat di sekitarnya."
    
    show carissa bingung
    
    c "(dalam hati) Aku yakin tadi ada suara kayaknya..."
    
    d "(suara pelan dari belakang) Kamu sering sendirian ya."
    
    show carissa kaget at right
    with move
    with vpunch
    
    show dewa normal at left
    with easeinleft
    
    c "(terkejut) Dewa! Ngapain kamu ada di sini?"
    
    show dewa senyum
    
    d "(tersenyum) Hehehe... aku cuman gabut aja."
    
    show carissa normal
    
    c "(tertawa gugup) Ooohhh~ haha..."
    
    n "Carissa mencoba menenangkan diri, namun tatapan Dewa terlalu lama padanya."
    
    d "(santai tapi lembut) Kamu keliatan capek. Kayak lagi mikirin sesuatu yang berat."
    
    show carissa bingung
    
    c "(cepat) Ng-nggak! Aku cuma... kurang tidur aja."
    
    show dewa senyum
    
    d "(mencondongkan tubuh sedikit) Hmm? Kamu bohongnya jelek banget."
    
    n "Carissa tertegun. Nada bicara Dewa terdengar ringan, namun membuat udara terasa sesak di dada Carissa."
    
    show carissa kaget
    
    c "(mencoba bercanda) Kamu pura-pura jadi cenayang ya? Bisa baca pikiran gitu."
    
    show dewa misterius
    
    d "(pelan) Aku ga bisa baca pikiran. Tapi aku bisa liat dari tatapan aja."
    
    show carissa takut
    
    n "Carissa hanya bisa menelan ludah, mencoba membalas tatapannya namun gagal."
    
    show dewa senyum
    
    d "(tersenyum kecil) Tenang aja, aku nggak bakal bilang ke siapa-siapa. Rahasia kecilmu aman sama aku."
    
    show carissa normal
    
    c "(berusaha santai) Rahasia? Aku ga ada ngomong apa-apa loh!"
    
    d "(mengangkat bahu) Siapa tau kamu punya sesuatu yang disembunyiin. Semua orang punya kan?"
    
    n "Carissa ingin menjawab, namun suaranya seperti tersangkut di tenggorokan. Tatapan Dewa terlihat sama seperti sebelumnya."
    
    show dewa misterius
    
    d "(berbisik pelan) Tapi hati-hati, Carissa... beberapa hal emang lebih baik nggak diketahui."
    
    show carissa kaget
    with vpunch
    
    n "Carissa membeku. Entah kenapa, kalimat itu terdengar seperti lebih dari sekadar saran."
    
    show dewa senyum
    
    d "(tersenyum tipis) Udah ah, nanti kamu mimpi buruk gara-gara aku."
    
    hide dewa senyum
    with easeoutleft
    
    n "Langkah Dewa perlahan menjauh di antara rak-rak buku, meninggalkan aroma samar parfum yang menenangkan namun anehnya... terasa mencekam."
    
    show carissa sedih at center
    with move
    
    n "Carissa masih berdiri di tempatnya, tenggelam dalam renungan."
    n "Untuk pertama kalinya, ia tidak tahu apakah harus takut... atau justru penasaran."
    
    c "(dalam hati) Siapa sebenarnya... Dewa?"
    
    scene black
    with Dissolve(1.0)
    
    jump scene5_halaman_belakang

# ===== SCENE 5: Halaman Belakang Sekolah =====
label scene5_halaman_belakang:
    scene bg halaman_belakang
    with dissolve
    
    play music audio.tension fadein 2.0
    
    n "Setelah Carissa mengambil buku yang diperlukan, ia pun keluar dari sekolah dengan tangan penuh buku."
    n "Di halaman sekolah."
    
    show aksara serius at left
    with dissolve
    
    n "Aksara duduk santai di taman, menatap ke arah perpustakaan."
    n "Ia melihat sosok berambut pirang keluar dari pintu samping."
    
    show dewa misterius at right
    with easeinright
    
    n "Dewa berjalan dengan tenang, lalu sekilas menatap ke arah Carissa yang baru keluar."
    
    hide dewa
    with easeoutright
    
    show aksara khawatir
    
    a "(dalam hati) Aura gelap itu... kenapa familiar?"
    
    show carissa normal at right
    with easeinright
    
    n "Carissa berjalan keluar, menatap langit yang mulai berubah jingga."
    
    c "Aksara! Kamu dari tadi di sini?"
    
    show aksara normal
    
    a "(menoleh) Aku tadi liat ada orang yang barusan keluar. Kamu kenal nggak?"
    
    show carissa normal at center
    with move
    
    c "Hah? Oh itu murid baru, namanya Dewa."
    
    show aksara serius
    with vpunch
    
    a "(mendadak tegang) Kamu bilang... Dewa?"
    
    show carissa bingung
    
    n "Carissa menangkap perubahan mendadak pada wajah Aksara."
    n "Tangannya yang tadi santai di sisi tubuh, kini mengepal."
    
    c "Iya... kenapa emangnya?"
    
    show aksara khawatir
    
    n "Aksara diam sejenak, menatap ke arah tempat Dewa menghilang."
    
    menu:
        "Aksara, kamu gapapa?":
            jump accept_aksara
        
        "Mungkin kebetulan aja namanya.":
            jump not_suspected

label accept_aksara:
    $ aksara_points += 2
    
    show carissa khawatir
    
    c "(melangkah lebih dekat) Aksara, kamu gapapa? Kamu keliatan..."
    c "...nggak kayak biasanya."
    
    show aksara serius
    
    n "Aksara menatapnya lama, seperti sedang mempertimbangkan sesuatu."
    
    a "(menghela napas) Carissa... nama itu."
    a "Dewa..."
    
    show carissa kaget
    
    c "Kenapa? Ada masalah sama namanya?"
    
    show aksara khawatir
    
    a "Aku... pernah denger nama itu."
    a "Entahlah, tapi rasanya familiar—bukan buat hal baik."
    
    show carissa bingung
    
    n "Carissa merinding mendengar nada bicara Aksara."
    
    c "Maksudmu...?"
    
    show aksara serius
    
    a "(menggeleng) Aku nggak yakin. Mungkin aku salah ingat aja."
    a "Tapi... perasaanku nggak pernah salah soal hal-hal kayak gini."
    
    n "Aksara menatapnya dengan intensitas yang membuat jantung Carissa berdetak cepat."
    
    a "Janji sama aku... jangan terlalu deket sama dia sampai aku yakin sendiri."
    
    show carissa normal
    
    n "Carissa menelan ludah, merasakan keseriusan dari kata-kata Aksara."
    n "Namun ia pun melakukan pinky promise dengan Aksara—mereka masing-masing mengaitkan jari kelingking satu sama lain."
    
    jump after_choo

label not_suspected:
    show carissa normal
    
    c "(berusaha santai) Mungkin kamu pernah denger nama yang sama?"
    c "Kan nama Dewa lumayan umum juga..."
    
    show aksara serius
    
    n "Aksara menatapnya dengan ekspresi yang sulit dibaca."
    
    a "(pelan) ...mungkin."
    
    n "Namun Carissa bisa melihat Aksara masih tegang."
    n "Ada sesuatu yang tidak ia katakan."
    
    show aksara khawatir
    
    a "Carissa, aku cuma mau bilang..."
    a "Hati-hati sama orang yang baru kamu kenal. Apapun yang dia katain."
    
    show carissa bingung
    
    n "Carissa mengerutkan dahi, merasa ada yang aneh."
    n "Namun sebelum ia bisa bertanya lebih lanjut—"
    
    jump after_choo

label after_choo:
    show aksara khawatir
    
    a "(menatap langit yang mulai gelap) Aku harus ke kuil. Kakek butuh bantuanku."
    a "(menatap Carissa) Ingat yang aku bilang tadi pagi."
    
    show carissa normal
    
    n "Carissa mengangguk pelan, masih memikirkan reaksi aneh Aksara."
    
    hide aksara
    with easeoutleft
    
    n "Aksara berjalan pergi, meninggalkan Carissa sendirian."
    
    show carissa bingung at center
    
    c "(dalam hati) Kenapa Aksara terlihat begitu... ketakutan?"
    c "Apa yang sebenarnya dia tau tentang Dewa?"
    
    play sound audio.wind
    
    n "Angin tiba-tiba berhembus kencang."
    
    with hpunch
    
    n "Daun-daun beterbangan."
    
    suara "(bergema dari arah pohon) Carissa..."
    suara "Darahmu... kunci kami..."
    
    show carissa takut
    with vpunch
    
    c "(menoleh cepat) Siapa itu?!"
    
    n "Namun tidak ada siapa-siapa."
    n "Hanya hembusan angin dan bisikan yang perlahan memudar."
    
    scene bg langit_jingga
    with slow_dissolve
    
    jump chapter1_ending

label chapter1_ending:
    n "Dalam perjalanan pulang, Carissa terus memikirkan peringatan Aksara dan tatapan misterius Dewa."
    n "Langit jingga senja menyelimuti kota, menandai berakhirnya hari yang penuh teka-teki."
    n "Apa yang sebenarnya terjadi padanya? Dan apa yang akan terjadi selanjutnya?"
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
    
    play music audio.tension fadein 3.0
    
    centered "{color=#fff}Tiga hari kemudian...{/color}"
    pause 1.5
    centered "{color=#888}Bayangan semakin mendekat.{/color}"
    centered "{color=#888}Dan sebuah pilihan akan mengubah segalanya.{/color}"
    pause 2.0
    
    jump scene1_mimpi_buruk

# ===== SCENE 1: Mimpi Buruk & Minigame 1 =====
label scene1_mimpi_buruk:
    scene black
    with nightmare_transition
    
    play music audio.heartbeat fadein 2.0
    
    n "Malam itu, Carissa terlelap dalam tidur yang gelisah."
    n "Namun tidurnya bukanlah tidur yang menenangkan."
    
    centered "{color=#8b0000}Dunia Mimpi{/color}"
    pause 2.0
    
    scene bg ruang_tamu_temaram
    with nightmare_transition
    
    play sound audio.wind
    
    show carissa bingung at center
    with dissolve
    
    c "(melihat sekeliling) Ini... kamarku?"
    c "Tapi kenapa... warnanya aneh?"
    
    n "Seluruh ruangan berwarna merah gelap dan ungu pucat."
    n "Bayangan-bayangan bergerak di dinding tanpa sumber cahaya."
    
    suara "(bergema dari segala arah) Carissaaaa..."
    
    show carissa takut
    with vpunch
    
    c "Ini mimpi! Ini pasti mimpi!"
    
    show hantu medium at left
    with flash_white
    
    play sound audio.heartbeat
    
    n "Sosok-sosok gelap mulai muncul dari balik pintu."
    n "Mereka mendekat dengan gerakan tidak wajar—meluncur tanpa kaki."
    
    suara "Darahmu..."
    suara "Beri kami..."
    
    show carissa kaget
    
    c "(berteriak) PERGI! JANGAN DEKATI AKU!"
    
    # MINIGAME 1: Dodge Game
    # NOTE: Simple dodge/avoid game menggunakan arrow keys
    # Tutorial Ren'Py: search "renpy dodge game tutorial" di YouTube
    # Konsep: Player gerakkan Carissa dengan arrow keys untuk hindari hantu
    # Durasi: 30 detik
    # Jika kena hantu 3x: game over, ulangi
    # Jika berhasil: lanjut ke dialog sukses
    
    n "Carissa mengepal kedua tangannya dengan erat."
    n "Ia berlari menghindari bayangan-bayangan yang mengejarnya."
    
    play sound audio.running
    
    show hantu medium at right
    with dissolve
    
    c "(berlari) AKU HARUS BANGUN!"
    
    n "Detik demi detik berlalu—bayangan semakin dekat dengan jumlah yang banyak."
    n "Mereka membentuk formasi lingkaran yang besar, mengepung Carissa secara perlahan."
    n "Carissa semakin ketakutan, meringkuk dengan badannya yang mungil."
    n "Namun tiba-tiba, secercah cahaya biru menyinari sekeliling Carissa."
    
    hide hantu medium
    with flash_blue
    
    n "Bayangan-bayangan itu menjerit dan menghilang satu per satu."
    
    show carissa normal at center
    
    c "(terengah-engah) A-apa itu tadi?"
    
    n "Carissa masih terpana dengan kejadian barusan—tidak percaya dengan mata kepalanya sendiri."
    
    with flash_white
    
    scene bg kamar_carissa
    with dissolve
    
    n "Carissa terbangun dengan napas tersengal."
    n "Keringat dingin membasahi dahinya."
    
    show carissa takut at center
    with vpunch
    
    c "(terbangun) Hah... hah..."
    
    n "Jam di meja menunjukkan pukul 5 pagi."
    
    show carissa sedih
    
    c "(gemetar) Mimpi tadi..."
    
    play sound audio.phone_vibrate
    
    n "Alarm ponsel berbunyi—waktunya bersiap ke sekolah."
    
    scene black
    with Dissolve(1.0)
    
    jump scene2_perjalanan_pagi

# ===== SCENE 2: Perjalanan Pagi =====
label scene2_perjalanan_pagi:
    scene bg jalan_kota
    with slow_dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Pagi itu terasa berbeda. Udara lebih berat dari biasanya."
    
    show carissa sedih at center
    with dissolve
    
    n "Carissa berjalan menuju sekolah dengan langkah terburu-buru."
    n "Tidurnya semalam penuh mimpi buruk—sama seperti malam sebelumnya."
    n "Namun, Carissa melupakan sesuatu—jimat."
    
    show carissa kaget
    with vpunch
    
    c "Astaga! Jimatnya ketinggalan!"
    
    play sound audio.wind
    
    n "Tiba-tiba, angin bertiup kencang. Dedaunan kering beterbangan tak karuan."
    
    suara "(bergema dari segala arah) Carissaaaa..."
    
    show carissa takut
    
    c "(mundur) Eh...?!"
    
    n "Bayangan-bayangan mulai muncul dari berbagai sudut jalan."
    n "Sosok-sosok transparan dengan mata kosong mulai mendekat."
    
    suara "Tanpa pelindung..."
    suara "Kau milik kami..."
    
    show carissa kaget
    
    c "(berteriak) JANGAN MENDEKAT PERGI SANAA!"
    
    hide carissa kaget
    with dissolve
    
    n "Carissa berlari sekuat tenaga menuju gerbang sekolah."
    n "Bayangan-bayangan itu mengejarnya dengan kecepatan tidak wajar."
    
    play sound audio.running
    
    n "Namun tepat saat ia hampir tersudut—"
    
    with flash_blue
    
    n "Lagi-lagi cahaya biru yang sama terpancar dari tubuh Carissa."
    n "Bayangan-bayangan itu menjerit dan menghilang satu per satu."
    
    show carissa normal at center
    
    c "(terengah-engah) Hah... hah... aman..."
    
    n "Carissa merasakan jantungnya berdegup kencang."
    
    c "(dalam hati) Aku harus lebih hati-hati... tapi cahaya biru tadi... darimana asalnya?"
    
    scene black
    with Dissolve(1.0)
    
    jump scene3_praktik_lapangan

# ===== SCENE 3: Praktik Lapangan - Interaksi dengan Dewa =====
label scene3_praktik_lapangan:
    scene bg halaman_belakang
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Jam pelajaran ketiga. Praktik Biologi di luar kelas."
    
    show guru at left
    with dissolve
    
    guru "Baik anak-anak, hari ini kita akan belajar tentang ekosistem taman sekolah."
    guru "Kalian sudah dibagi kelompok berpasangan. Silakan cari area masing-masing."
    
    show carissa normal at center
    with easeinright
    
    n "Carissa melihat daftar kelompok di papan."
    
    c "(dalam hati) Kelompok 5... Carissa dan..."
    
    show carissa kaget
    with vpunch
    
    c "Dewa?"
    
    show dewa senyum at right
    with easeinright
    
    d "(tersenyum ramah) Sepertinya kita satu kelompok nih!"
    d "Mohon kerjasamanya Carissa."
    
    show carissa normal
    
    c " Mohon kerjasamanya juga Dewa. Ayo kita mulai saja."
    
    hide guru
    with dissolve
    
    scene bg halaman_belakang
    with dissolve
    
    show carissa normal at left
    show dewa normal at right
    with dissolve
    
    n "Mereka berjalan ke area yang lebih sepi di belakang taman."
    n "Hanya terdengar suara angin dan dedaunan yang bergesek."
    
    show dewa senyum
    
    d "Kamu tau nggak, aku perhatiin kamu dari hari pertama aku masuk."
    
    show carissa bingung
    
    c "(melirik) Kamu stalker ya?!"
    
    show dewa misterius
    
    d "Haha, bukan gitu maksudku..."
    d "Aura yang kamu miiki... nggak seperti milik orang lain."
    
    show carissa takut
    
    c "(menegang) K-Kenapa bisa kamu tau hal kayak gitu?"
    
    show dewa senyum
    
    d "(tertawa kecil) Hahaha, emang ga boleh ya?"
    
    n "Dewa berjongkok, mengambil sampel tanah dengan tenang."
    n "Carissa memperhatikan dalam diam. Gerakannya anggun namun... terasa janggal."
    
    show carissa bingung
    
    c "(dalam hati) Kenapa setiap kali dia di dekatku, ada hawa aneh tapi terasa nyaman untukku?"
    
    play sound audio.wind
    
    n "Angin tiba-tiba berhembus kencang."
    
    show dewa normal
    
    d "Carissa, kamu... percaya sama hal-hal gaib?"
    
    show carissa kaget
    with hpunch
    
    c "K-kenapa tiba-tiba nanya gitu?"
    
    show dewa misterius
    
    d "(menatap langit) Yah... cuma penasaran aja sih."
    d "(tersenyum tipis) Kan jawaban orang beda-beda."
    
    show carissa sedih
    
    c "(pelan) A-aku... sebenernya pernah ngalamin hal-hal yang nggak bisa dijelasin sih."
    
    show dewa senyum
    
    d "(menoleh cepat, matanya berbinar) Oh iya?"
    d "Ceritain dong, kepo nih sama pengalamanmu."
    
    menu:
        "Ceritakan sedikit tentang pengalaman mistis":
            jump tell_dewa
        
        "Hindari topik, alihkan pembicaraan":
            jump avoid_dewa_talk

label tell_dewa:
    $ dewa_points += 2
    
    show carissa sedih
    
    c "(menghela napas) Sejak kecil, aku sering liat... bayangan."
    c "Sosok-sosok yang nggak bisa dilihat sama orang biasa."
    c "Kadang ada yang cuma lewat, tapi ada juga yang sampe natap aku lama banget."
    
    show dewa misterius
    
    n "Mata Dewa berubah. Ada kilauan biru samar di dalamnya."
    
    d "(serius) Kamu takut?"
    
    show carissa normal
    
    c "Iya sih, soalnya ini baru pertama kalinya..."
    
    show dewa senyum
    
    d "(tersenyum lembut) Mungkin kamu nggak harus takut."
    d "Mungkin... mereka cuma butuh dimengerti."
    
    show carissa bingung
    
    c "(menatap Dewa) Kamu ngomong seolah kamu paham mereka."
    
    show dewa normal
    
    d "(mengangkat bahu) Siapa tau?"
    
    jump after_dewa_choice_scene3

label avoid_dewa_talk:
    $ aksara_points += 1
    
    show carissa normal
    
    c "(tertawa gugup) Hahahha, buat apa coba? Menurutku itu cuma efek halusinasi aja tau."
    c "Udah yuk kita selesain praktiknya. Nanti dikumpulin lho."
    
    show dewa misterius
    
    n "Dewa menatapnya lama. Ada kekecewaan samar di wajahnya."
    
    d "(pelan) Hmm... baiklah."
    
    show carissa takut
    
    n "Nada suaranya membuat Carissa merinding."
    
    jump after_dewa_choice_scene3

label after_dewa_choice_scene3:
    play sound audio.wind
    
    n "Angin berhembus pelan. Dedaunan kering beterbangan di mana-mana."
    n "Carissa dan Dewa melanjutkan praktik yang tercantum di kertas ilmiah tersebut."
    
    show dewa senyum at center
    with move
    
    d "Ya ampun... kamu fokus banget sih."
    
    show carissa bingung
    with vpunch
    
    c "O-oiya?"
    
    show dewa senyum at left
    with dissolve
    
    d "Iya. Jarang liat orang segitu seriusnya waktu praktik."
    
    n "Senyum Dewa tampak ramah, namun tatapannya... sulit ditebak."
    
    scene black
    with Dissolve(1.0)
    
    jump scene4_kantin_siang

# ===== SCENE 4: Kantin Siang - Konflik Pertama =====
label scene4_kantin_siang:
    scene bg kantin
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Jam istirahat tiba. Kantin ramai dipenuhi lautan siswa yang sedang mengantri makanan."
    
    show carissa normal at center
    with dissolve
    
    n "Carissa duduk sendirian di sudut, memakan soto ayamnya dengan pelan."
    
    c "(dalam hati) Hari ini aneh banget... apalagi si Dewa."
    
    n "Saat Carissa sedang berkecamuk dengan pikirannya sendiri, datang seseorang dari arah kirinya."
    
    show aksara khawatir at left
    with move
    
    a "(duduk di sebelah Carissa) Kamu gapapa?"
    
    show carissa normal
    
    c "(menoleh) Iya, aku gapapa kok."
    
    show aksara serius
    
    a "Kamu yakin?"
    
    n "Aksara menatapnya dengan serius."
    
    a "Carissa, aku mau nanya. Kamu... lagi deket sama Dewa?"
    
    show carissa bingung
    
    c "Kamu tau dari mana?"
    
    show aksara khawatir
    
    a "Aku lihat dari lantai 3 pas kamu ada pelajaran di luar kelas tadi..."
    a "Kalian ngobrolin apa?"
    
    c "Ga perlu khawatir Aksara, dia nggak ngapa-ngapain aku kok."
    
    show aksara serius
    
    a "(menghela napas) Aku nggak yakin kamu bilang gitu."
    a "Feeling-ku bilang kalo dia berbahaya buat kamu. Kemarin aku sudah bilang kan kalo jangan deket-deket si Dewa itu."
    
    show dewa senyum at right
    with easeinright
    
    d "(tersenyum) Lagi pada ngomongin aku ya?"
    
    show aksara serius at left
    show carissa kaget at center
    with vpunch
    
    n "Aksara dan Carissa tersentak."
    
    a "(menatap tajam) Kenapa kepo?"
    
    show dewa normal
    
    d "Aku kan punya telinga~ kebetulan juga aku lewat kok."
    d "(menatap Aksara) Tapi kayaknya kamu nggak suka sama aku ya?"
    
    show aksara serius
    
    a "(dingin) Aku cuma mau melindungi teman aku."
    
    show dewa misterius
    
    d "(senyum tipis) Melindungi? Dari apa?"
    d "Atau... dari siapa?"
    
    n "Ketegangan di antara mereka membuat atmosfer sekitar terasa mencekam."
    
    show carissa sedih
    
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
    
    c "Aksara cuma khawatir sama aku, Dewa."
    c "Dia udah ngebantu aku dari dulu."
    
    show dewa misterius
    
    n "Dewa terdiam. Ada kilatan kecewa di matanya."
    
    d "(pelan) Oke... kalau itu maumu."
    
    hide dewa misterius
    with easeoutright
    
    show aksara normal at center
    with move
    
    a "(menghela napas lega) Makasih, Carissa."
    a "Aku cuma nggak mau kamu kenapa-kenapa."
    
    jump after_kantin_choice

label defend_dewa_scene4:
    $ dewa_points += 3
    
    show carissa normal
    
    c "Dewa nggak berbahaya kok, Aksara."
    c "Dia baik sama aku."
    
    show aksara sedih
    
    a "(kecewa) Carissa..."
    
    show dewa senyum
    
    d "(tersenyum ke arah Aksara) Tuh, dia sendiri yang ngomong."
    d "(menatap Carissa) Aku janji nggak bakal sakitin kamu."
    
    show aksara khawatir
    
    a "(mengepalkan tangan) ...aku harap kamu nggak menyesal, Carissa."
    
    hide aksara khawatir
    with easeoutleft
    
    jump after_kantin_choice

label neutral_scene4:
    $ aksara_points += 1
    $ dewa_points += 1
    
    show carissa sedih
    
    c "Kalian berdua kenapa sih?! Please, jangan kayak gini..."
    
    show aksara normal
    
    a "(menghela napas) Baiklah..."
    
    show dewa normal
    
    d "Oke... aku ngerti."
    
    n "Suasana masih terasa tegang, namun setidaknya keadaan masih terkondisi dengan baik."
    
    jump after_kantin_choice

label after_kantin_choice:
    scene black
    with Dissolve(1.0)
    
    n "Bel masuk berbunyi. Ketegangan perlahan mulai mereda."
    n "Namun Carissa tahu... ini baru permulaan."
    
    jump scene5_perpustakaan_sore

# ===== SCENE 5: Perpustakaan Sore - Minigame 2 =====
label scene5_perpustakaan_sore:
    scene bg perpustakaan
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Sepulang sekolah, Carissa memutuskan mencari informasi di perpustakaan tua dekat rumahnya."
    
    show carissa normal at center
    with dissolve
    
    c "(dalam hati) Mungkin... ada buku soal hal-hal gaib?"
    
    play sound audio.book_flip
    
    n "Jari-jarinya menelusuri punggung buku yang berdebu."
    
    show carissa bingung
    
    c "Mitologi Mistis... Penjaga Gerbang... Segel Jimat Kuno..."
    
    n "Carissa mengambil buku tebal berjudul 'Dua Dunia: Pengenalan'."
    
    play sound audio.book_open
    
    c "(membaca) 'Dalam kepercayaan kuno, ada garis tipis antara dunia manusia dan dunia roh...'"
    c "'Gerbang ini dijaga oleh Penjaga yang ditakdirkan. Jika gerbang terbuka...'"
    
    show carissa kaget
    with vpunch
    
    c "Dunia akan..."
    
    play sound audio.heartbeat
    
    with flash_white
    
    show carissa takut
    
    n "Lampu perpustakaan berkedip. Buku di tangannya melayang, berpencar menjadi tiga titik cahaya berwarna hitam."
    
    play sound audio.wind
    
    suara "(bergema) Jangan tahu terlalu banyak..."
    
    show hantu weak at left
    with flash_white
    
    c "(gemetar) A-apa ini?!"
    
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
    
    play sound audio.running
    
    n "Carissa berlari mengikuti jalur pertama."
    
    play sound audio.success
    
    c "Penjaga Gerbang..."
    
    n "Jalur kedua membawanya ke balik tumpukan buku."
    
    play sound audio.success
    
    c "Ritual Segel Kuno..."
    
    n "Jalur terakhir mengarah ke rak tertinggi."
    
    play sound audio.success
    
    c "Rakta!"
    
    hide hantu weak
    with flash_white
    
    n "Bayangan-bayangan lenyap begitu ketiga buku terkumpul."
    
    show carissa sedih at center
    
    c "(terengah-engah) Akhirnya..."
    
    n "Carissa membuka buku 'Rakta' dengan tangan gemetar."
    
    c "(membaca) 'Dalam dua abad sekali, akan muncul seseorang dengan darah Rakta...'"
    c "'Mereka memiliki kemampuan melihat dan berkomunikasi dengan dunia roh...'"
    c "'Darah mereka adalah kunci pembuka gerbang...'"
    
    show carissa kaget
    with vpunch
    
    c "Maksudnya apa semua ini? Darah rakta? Kunci gerbang?"
    
    show aksara serius at right
    with easeinright
    
    a "Carissa!"
    
    show carissa kaget at left
    with move
    with vpunch
    
    c "Aksara?! Dari mana kamu—"
    
    show aksara khawatir
    
    a "Aku ngerasain jimatku bereaksi kuat. Kamu... kenapa cari tahu hal-hal kayak gini?"
    
    n "Aksara menatap ketiga buku di pelukan Carissa dengan ekspresi cemas."
    
    show carissa bingung
    c "A-aku cuma..."
    
    show aksara serius
    
    a "(mendekat) Carissa, kenapa tiba-tiba kamu nyari tau hal ini?"
    
    menu:
        "Jujur - 'Iya, aku butuh tau apa yang terjadi sama aku'":
            jump honest_aksara
        
        "Bohong - 'Enggak kok, cuma penasaran aja'":
            jump lie_aksara

label honest_aksara:
    $ aksara_points += 3
    
    show carissa sedih
    
    c "(menunduk) Iya... aku butuh tau apa yang sebenarnya terjadi sama aku, Aksara."
    c "Mimpi buruk terus, bayangan-bayangan yang ngikutin... aku takut."
    
    show aksara khawatir
    
    a "(menghela napas, duduk di sebelah Carissa) Makasih udah jujur."
    a "Aku paham perasaan kamu. Tapi... ini berbahaya, Carissa."
    
    show carissa normal
    
    c "Makanya aku harus tau! Aku ga bisa terus-terusan ketakutan kayak gini."
    
    show aksara normal
    
    a "(tersenyum tipis) Baiklahh..."
    a "(serius lagi) Tapi janji sama aku, kalau ada apa-apa langsung hubungi aku."
    
    show carissa senyum
    
    c "Janji."
    
    jump after_choice_scene5

label lie_aksara:
    $ aksara_points -= 1
    
    show carissa normal
    
    c "(tertawa gugup) Enggak kok! Aku cuma... penasaran aja."
    c "Kan lagi tugas sejarah, butuh referensi mitos lokal."
    
    show aksara serius
    
    n "Aksara menatapnya lama. Matanya tajam, seolah bisa melihat kebohongan Carissa."
    
    a "(pelan) Kamu bohong."
    
    show carissa kaget
    with hpunch
    
    c "A-aku nggak—"
    
    show aksara sedih
    
    a "(menghela napas) Kita udah kenal dari kecil, Carissa. Aku tau kapan kamu bohong..."
    a "Aku takut kamu kenapa-kenapa cuma karena hal-hal yang kamu cari tau sendirian."
    
    show carissa sedih
    
    c "(dalam hati) Maaf, Aksara..."
    
    jump after_choice_scene5

label after_choice_scene5:
    show aksara normal
    
    a "Yaudah, lagian dah sore nih. Ayo balik bareng..."
    
    show carissa senyum
    
    c "(senyum kecil) Oke!"
    
    hide carissa senyum
    hide aksara normal
    with dissolve
    
    n "Mereka berdua berjalan keluar dari perpustakaan."
    
    scene bg perpustakaan
    with dissolve
    
    play sound audio.wind
    
    n "Keheningan kembali menyelimuti ruangan."
    n "Di balik rak buku paling belakang, sebuah bayangan gelap mengintip."
    
    show bayangan at center
    with dissolve
    suara "(bergema pelan) Jadi, sudah dimulai..."
    
    show mata_biru at center behind bayangan
    with flash_blue
    
    suara "(tertawa pelan) Dia akan menjadi milikku..."
    
    hide bayangan
    hide mata_biru
    with flash_white
    
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
    
    play music audio.mystery_theme fadein 3.0
    
    n "Pagi yang tenang. Carissa terbangun dengan perasaan lega—hari ini libur."
    
    show carissa normal at center
    with dissolve
    
    c "(meregangkan badan) Akhirnya bisa istirahat..."
    
    n "Namun ketenangan itu hanya sesaat."
    n "Mimpi semalam masih membekas, wajah-wajah tanpa rupa serta bisikan-bisikan asing yang mengganggu."
    
    show carissa sedih
    
    c "(menyentuh kalung di lehernya) Kalung ini..."
    
    n "Sebuah kalung perak dengan liontin berbentuk bulan sabit."
    n "Pemberian ibunya saat Carissa masih kecil."
    
    show kalung_glow at center
    with dissolve
    
    c "(berbisik) Kenapa akhir-akhir ini sering hangat?"
    
    hide kalung_glow
    with dissolve
    
    play sound audio.door_open
    
    nenek "(dari luar) Carissa, sarapan!"
    
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek normal at left
    show carissa normal at right
    with dissolve
    
    n "Carissa duduk di meja makan bersama neneknya."
    n "Aroma nasi goreng dan teh hangat mengisi ruangan."
    
    show nenek senyum
    
    nenek "Kamu keliatan capek, Nduk. Sekolahmu berat ya?"
    
    show carissa sedih
    
    c "Nek... aku mau tanya sesuatu."
    
    show nenek khawatir
    
    nenek "(berhenti mengunyah) ada apa, Nduk?"
    
    show carissa normal
    
    c "Soal... Ibu."
    c "Nenek pernah cerita kalo Ibu sering ngalamin hal-hal aneh, kan?"
    
    show nenek normal
    
    n "Nenek terdiam. Tangannya yang memegang cangkir sedikit bergetar."
    
    nenek "(menghela napas) Iya..."
    
    show carissa sedih
    
    c "Aku... akhir-akhir ini sering liat sesuatu, Nek."
    c "Bayangan-bayangan sama suara-suara yang nggak ada orangnya."
    
    show nenek khawatir
    with vpunch
    
    nenek "(terkejut) Carissa..."
    
    menu:
        "Tanya tentang orang tua - 'Kenapa Ibu juga bisa liat, Nek?'":
            jump ask_parents
        
        "Tanya tentang kalung - 'Kalung ini... ada hubungannya?'":
            jump ask_necklace

label ask_parents:
    show carissa normal
    
    c "Kenapa Ibu juga bisa liat, Nek?"
    
    show nenek sedih
    
    nenek "Itu sudah menjadi warisan nenek moyang kita, Nduk."
    nenek "Tapi, kamu sama Ibumu itu berbeda dari yang lainnya."
    
    show carissa bingung
    
    c "Berbeda gimana?"
    
    show nenek normal
    
    nenek "(mengaduk tehnya pelan) Nenek, Ibu, sama kamu... kita semua itu bisa melihat 'mereka'."
    nenek "Hanya saja... Ibumu dulu cepat mempelajari apa yang dilatih."
    
    show carissa kaget
    
    c "Dilatih?"
    
    show nenek khawatir
    
    nenek "(mengangguk) Ibumu belajar cara melawan mereka, cara melindungi diri, cara bikin segel..."
    nenek "Dia kuat, Nduk. Sangat kuat."
    
    show carissa sedih
    
    c "(pelan) Terus kenapa... aku nggak diajarin juga?"
    
    show nenek sedih
    
    n "Nenek terdiam lama. Matanya berkaca-kaca."
    
    nenek "(suara bergetar) Karena Ibumu nggak mau kamu ngalamin hal yang sama."
    nenek "Dia bilang... 'Biar aku saja yang terakhir, Mbok. Carissa harus hidup normal.'"
    
    show carissa normal
    
    c "Tapi akhirnya... tetep aja aku ngalamin ini."
    
    show nenek khawatir
    
    nenek "(menggenggam tangan Carissa) Iya, Nduk... maafin Nenek."
    nenek "Yang penting sekarang... kamu harus hati-hati."
    
    show carissa sedih
    
    c "Tapi Nek—"
    
    show nenek normal
    
    nenek "(memotong) Carissa, dengerin Nenek."
    nenek "Kamu punya sesuatu yang istimewa. Lebih dari Nenek, bahkan lebih dari Ibumu."
    nenek "Makanya... 'mereka' tertarik sama kamu."
    
    show carissa bingung
    
    c "Istimewa apanya? Aku cuma bisa melihat doang, Nek. Aku nggak bisa apa-apa!"
    
    show nenek khawatir
    
    nenek "(mengusap pipi Carissa) Justru itu yang bikin kamu berbahaya, Nduk."
    
    show carissa takut
    
    c "(berbisik) Nek..."
    
    show nenek senyum
    
    nenek "(memeluk Carissa) Tenang aja, Nduk. Kan ada Nenek sama Aksara."
    nenek "Dan... kalung itu."

    hide nenek senyum
    hide carissa takut
    with dissolve 
    jump after_choice_scene6

label ask_necklace:
    show carissa normal
    
    c "(menyentuh kalung) Kalung ini... ada hubungannya sama yang aku alami?"
    
    show nenek khawatir
    
    nenek "(menatap kalung) Itu... kalung untuk melindungmu."
    nenek "Ibumu sendiri yang memberikan waktu kamu masih bayi."
    
    show carissa kaget
    
    c "Bayi? Jadi... aku udah punya ini dari dulu?"
    
    show nenek sedih
    
    nenek "(mengangguk) Itu pemberian terakhir Ibumu sebelum dia..."
    nenek "(terhenti) ...sebelum dia pergi."
    
    show carissa bingung
    
    c "Pelindung dari apa, Nek?"
    
    show nenek normal

    nenek "...yang penting kamu jangan lepas kalung itu ya."
    nenek "Apapun yang terjadi."
    
    show carissa normal
    
    c "Baik, Nek..."
    
    hide nenek normal
    hide carissa normal 
    with dissolve
    jump after_choice_scene6

label after_choice_scene6:
    n "Mereka melanjutkan sarapan dalam keadaan hening."
    n "Meski begitu, pikiran Carissa masih berkecamuk tentang informasi yang baru saja dia dapatkan."
    
    scene black
    with Dissolve(2.0)
    
    jump scene7_siang

label scene7_siang_sendirian:
    scene bg ruang_tamu_terang
    with dissolve
    
    stop music fadeout 2.0
    play music audio.mystery_theme fadein 2.0 volume 0.5
    
    n "Siang itu, matahari bersinar cerah."
    n "Carissa duduk santai di ruang tamu, scrolling ponselnya tanpa tujuan."
    
    show carissa normal at center
    with dissolve
    
    c "(menguap) Bingung mau ngapain..."
    
    play sound audio.door_open
    
    show nenek senyum at left
    with easeinleft
    
    nenek "Carissa, bantuin Nenek yuk!"
    
    show carissa senyum
    
    c "Oke! Bantuin apa emangnya, Nek?"
    
    show nenek normal
    
    nenek "Nenek mau bikin kue lapis sama gulai ayam."
    nenek "Carissa kan udah besar, harus bisa masak juga."
    
    show carissa normal
    
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
    
    n "Di dapur yang hangat, Carissa dan neneknya mulai memasak."
    
    nenek "Oke, sekarang kita bikin gulai ayam dulu."
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
    
    nenek "Sempurna! Carissa hebat!"
    
    show carissa senyum
    
    c "Yeay! Aku berhasil!"
    
    centered "{color=#0f0}★ GULAI AYAM BERHASIL DIBUAT! ★{/color}"
    pause 1.5
    
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek senyum at left
    show carissa senyum at right
    with dissolve
    
    n "Setelah gulai matang, mereka berdua duduk santai sambil menunggu nasi."
    
    nenek "Carissa makin pinter masak nih!"
    
    show carissa normal
    
    c "Hehe, makasih Nek. Aku belajar dari yang terbaik!"
    
    show nenek normal
    
    nenek "(tersenyum lembut) Ibumu juga dulu suka bantuin Nenek masak."
    nenek "Dia jago bikin rendang, loh."
    
    show carissa sedih
    
    c "(pelan) Aku... pengen bisa kayak Ibu."
    
    show nenek senyum
    
    nenek "(mengelus kepala Carissa) Kamu pasti bisa, sayang."
    nenek "Kamu keturunan ibumu. Pasti bisa dan lebih enak rasanya."
    
    show carissa senyum
    
    c "Heheheh, makasih ya Nek udah jagain aku selama ini."
    
    show nenek khawatir
    
    nenek "(memeluk Carissa) Nenek yang harusnya makasih sama kamu."
    nenek "Kamu sudah menjadi cucu yang baik buat Nenek."
    
    n "Mereka berdua memeluk dalam keheningan yang hangat."
    n "Moment sederhana yang terasa begitu berharga."
    
    hide carissa senyum
    hide nenek khawatir
    scene black
    with Dissolve(2.0)
    
    n "Siang itu berlalu dengan hangat."
    n "Namun di balik kehangatan itu, bayangan ancaman mulai mendekat."
    n "Carissa tidak tahu... Bahaya sedang menunggunya."
    n "Apakah besok akan jadi hari yang mengubah segalanya? atau hanya pikiranya saja?"
    pause 1.0

    centered "{color=#fff}Seminggu Kemudian...{/color}"
    pause 1.5
    
    scene bg halaman_sekolah
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Pagi yang cerah di sekolah."
    n "Siswa berlalu-lalang di koridor dengan riuh."
    
    show carissa normal at right
    with easeinright
    
    n "Carissa berjalan menuju kelasnya sambil bermain ponsel."
    
    play sound audio.footsteps
    
    show aksara normal at left
    with easeinleft
    
    n "Dari arah berlawanan, Aksara berjalan sambil membawa setumpuk buku tebal."
    
    show carissa senyum
    
    c "(berseru) Aksaraa!"
    
    show aksara senyum
    
    a "(menoleh) Hai, Carissa!"
    
    show carissa normal at center
    with move
    
    c "(melihat buku-buku) Wah, banyak banget. Kamu habis kemana?"
    
    show aksara normal
    
    a "(mengangkat buku) Ini habis ke perpus, buat ngembaliin buku."
    a "Udah telat seminggu, takut kena denda."
    
    show carissa senyum
    
    c "(tertawa) Hahaha, kamu tuh jarang banget telat. Pasti sibuk di kuil ya?"
    
    show aksara khawatir
    
    a "Iya... Kakek lagi butuh bantuan lebih banyak akhir-akhir ini."
    
    show aksara normal
    
    a "Oh iya, tadi aku denger dari Bu Retno kalau besok angkatan kita ada outing class."
    
    show carissa bingung
    
    c "Hah? Bukannya bulan depan ya?"
    
    show aksara bingung
    
    a "Loh, emang belum dikasih tau sama wali kelas kamu?"
    a "Aneh juga sih, kok kelasmu nggak dapet pemberitahuan."
    
    show carissa normal
    
    c "Hmm, mungkin Bu Sari lupa ngasih tau kali. Biasa deh, suka telat update."
    
    show aksara senyum
    
    a "(tertawa kecil) Hahaha, iya juga sih."
    
    c "Terus kemana emang outing class-nya?"

    show aksara normal
    
    a "Dari yang aku denger sih, kita bakal ke candi-candi gitu."
    a "Buat pelajaran sejarah."
    
    show carissa bingung
    
    c "(mengerutkan kening) Candi? Candi apa?"
    
    a "Kalau nggak salah... Candi Reksana Sewu."
    
    show carissa normal

    c "(pelan) Reksana Sewu..."
    
    show carissa bingung
    
    c "(menatap Aksara) Kamu kayaknya pernah ke sana kan?"
    
    show aksara serius
    
    a "(menghela napas) Iya... Cuma sekali aja sih."
    
    show aksara normal
    
    a "(menggeleng) Ah, sudahlah..."
    a "Yang penting kamu jangan lupa bawa jimat yang aku kasih ya."
    
    show carissa normal
    
    c "Iya iya, tenang aja. Aku selalu bawa kok."
    
    show aksara senyum
    
    a "Baguslah."
    
    play sound audio.school_bell
    
    n "Bel masuk berbunyi."
    
    show carissa senyum
    
    c "Keburu telat nih. Nanti kita ngobrol lagi ya!"
    
    show aksara normal
    
    a "Oke. Hati-hati di jalan."
    
    hide carissa senyum
    with easeoutright
    
    hide aksara normal
    with easeoutleft
    scene black
    with Dissolve(1.0)
    
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
    
    n "Pagi itu, bus sekolah melaju meninggalkan kota."
    n "Suara mesin dan obrolan siswa memenuhi perjalanan."
    
    show carissa normal at right
    with dissolve
    
    n "Carissa duduk di dekat jendela, menatap pemandangan yang berlalu."
    
    show dewa senyum at center
    with easeinright
    
    d "(muncul dari bangku belakang) Hei! Ngapain ngelamun?"
    
    c "Nggak lah, ini lagi nikmatin pemandangan aja kok."
    
    show dewa normal
    
    d "(duduk di sandaran kursi) Hmm, masa sih?"
    d "(menatap Carissa) Kamu excited nggak ke candinya?"
    
    show carissa senyum
    
    c "Lumayan sih, aku belum pernah ke sana soalnya."
    
    show dewa misterius
    
    d "(tersenyum aneh) Tempatnya keren loh!"
    d "Kamu bakal ngerasain sesuatu yang berbeda di sana."
    
    c "emang kamu udah pernah ke sana?"
    
    show dewa senyum
    
    d "Hmm... Yahh, bisa dibilang gitu."
    
    play sound audio.bus_stop
    
    guru "(dari depan bus) Anak-anak, kita sudah sampai!"
    
    scene bg candi_gerbang
    with slow_dissolve
    
    stop sound fadeout 2.0
    
    n "Bus berhenti di depan gerbang besar Candi Reksana Sewu."
    n "Bangunan kuno menjulang tinggi dengan ukiran-ukiran yang rumit."
    
    show carissa bingung at center
    with dissolve
    
    c "(menatap candi) Wow... besar banget."

    n "Setelah Aksara turun dari busnya, ia menghampiri Carissa yang sibuk berselfi-selfi di sekitar candi."
    
    show aksara normal at left
    with easeinleft
    
    a "Gimana perjalanannya tadi?"

    show carissa normal 
    c "Amann dongg."
    
    a "Lagi-lagi aku ngerasain energi gelap yang kuat..."

    n "Seperti hembusan angin, Dewa berjalan menghampiri Carissa dan Aksara. Mereka berdua terkejut dengan kehadiran Dewa yang tiba-tiba."

    show dewa misterius at right
    with easeinright
    
    d "(berbisik) Sebentar lagi kamu jadi milikku."
    
    show aksara serius
    with hpunch
    
    a "(menoleh tajam) Apa yang kamu bilang?"
    
    show dewa senyum
    
    d "(tertawa) Haha, cuma becanda kok!"
    
    hide dewa senyum
    with easeoutright
    
    c "(menatap Aksara) Dia... aneh nggak sih?" 
    a "(serius) Emang, kan aku dah bilang. Pokoknya jangan tinggalin aku ya. Apapun yang terjadi."
    
    show carissa takut
    
    c "(menelan ludah) K-kamu bikin aku takut..."

    hide aksara serius 
    with easeoutleft

    hide carissa takut
    with dissolve
    
    guru "Baiklah anak-anak! Kita akan dibagi menjadi beberapa kelompok."
    guru "Kelompok 1 akan explore bagian utara, kelompok 2 bagian selatan..."
    
    scene black
    with Dissolve(1.0)
    
    
    
    scene bg candi_gerbang
    with dissolve
    
    n "Setelah pembagian kelompok, Carissa dan Aksara berada di kelompok yang sama."
    n "Mereka bersama rombongan berjalan memasuki area dalam candi."
    n "Udara terasa lebih dingin saat mereka memasuki lorong batu."
    n "Cahaya matahari hampir tidak tembus masuk."
    
    show npc generic at center
    with dissolve    
    siswa2 "Kok gelap banget ya?"
    
    siswa3 "(menyalakan senter ponsel) Iya, bikin merinding deh!"

    siswa1 "Guys, kalian ngerasa dingin nggak sih?"
    
    play sound audio.wind
    
    n "Angin tiba-tiba berhembus kencang dari dalam candi."
    
    show npc generic
    with vpunch
    
    siswa1 "Wah! Dari mana anginnya tuh?!" 

    n "Para siswa mulai ketakutan dan bergaduh satu sama lain."
    
    show npc generic at left
    with dissolve

    show pemandu at right
    with dissolve
    
    p "Tenang semuanya!"
    p "Struktur candinya memang buat aliran udara jadi terasa kencang."

    hide npc generic
    hide pemandu
    with dissolve
    
    n "Di sisi lain, Carissa mendengar samar-samar bisikan dari pantulan dinding-dinding."
    n "Suara itu berbeda dari keributan siswa lainnya."

    suara "(bergema dari kedalaman candi) Carissaaaa..."
    suara "Akhirnya... kau datang..."
    
    show carissa takut
    
    c "(gemetar) S-suara itu lagi!"
    
    show aksara serius
    
    a "(menoleh cepat) Kamu dengar sesuatu?"
    
    show carissa sedih
    c "(berbisik) Ada... ada yang manggil namaku."

    n "Jimat di saku Carissa bergetar makin kencang."
    n "Kalung di lehernya mulai bersinar samar."

    show jimat_glow at center behind carissa
    with dissolve
    
    show kalung_glow at center
    with flash_blue
    
    show aksara serius
    with vpunch

    a "(menatap kalung) Carissa, kalungmu—!"
    
    n "Tiba-tiba lantai candi bergetar."
    with hpunch


    show npc generic at center behind aksara
    with dissolve
    
    siswa1 "(panik) GEMPA!"
    
    siswa2 "KELUAR! KITA HARUS KELUAR!"
    
    p "(berteriak) TENANG! JANGAN PANIK! IKUT AKU!"
    
    hide jimat_glow
    hide kalung_glow
    with dissolve
    
    n "Semua siswa berlarian menuju pintu keluar."
    n "Namun Carissa terpaku di tempat, menatap lorong dalam candi."
    
    show carissa takut at right
    
    c "(dalam hati) Kenapa... kenapa aku ngerasa harus ke sana?"
    
    show aksara khawatir at left
    
    a "(menarik tangan Carissa) Carissa! Kita harus keluar!"
    
    hide npc generic
    with dissolve
    
    n "Tapi Carissa tidak bergerak. Matanya seperti terhipnotis."
    
    suara "(lebih keras) DATANGLAH KE SINI!"
    
    show carissa bingung
    
    c "(pelan) Aku... harus ke sana..."
    
    show aksara serius
    with vpunch
    
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
    
    c "O-oke!"
    
    show aksara senyum
    
    a "Bagus! Ayo cepat!"
    
    hide carissa normal
    hide aksara senyum
    with dissolve
    
    n "Carissa dan Aksara berlari menuju pintu keluar."
    
    play sound audio.running
    
    n "Di belakang mereka, bayangan-bayangan mulai muncul dari kegelapan."
    
    show hantu weak at center
    with flash_red
    
    suara "(menjerit) JANGAN PERGI!"
    
    show carissa kaget at right
    show aksara serius at left
    with dissolve
    
    c "(menoleh) A-apa itu?!"
    
    show aksara serius
    
    a "(menarik Carissa lebih kencang) JANGAN LIHAT! TERUS LARI!"
    
    n "Aksara mengeluarkan jimat berbentuk permata biru dari sakunya."
    n "Jimat itu bersinar terang, membentuk perisai di belakang mereka."
    
    show aura_biru at left
    with flash_blue
    
    play sound audio.magic
    
    n "Bayangan-bayangan itu terpental dan tidak bisa mendekat."
    
    hide hantu weak
    with flash_white
    
    hide aura_biru
    with dissolve
    
    scene bg candi_gerbang
    with Dissolve(1.0)
    
    n "Mereka berhasil keluar tepat waktu."
    n "Pintu candi tertutup dengan sendirinya di belakang mereka."
    
    show carissa sedih at right
    show aksara khawatir at left
    with dissolve
    
    c "(terengah-engah) Hah... hah... Itu tadi... apa?"
    
    show aksara normal
    
    a "(tersenyum lega) Yang penting kita selamat."
    a "Kamu dengerin aku, dan itu yang paling penting."
    
    show carissa senyum
    
    c "Makasih, Aksara... Kalau nggak ada kamu..."
    
    a "Untuk itu aku ada, kan?"
    a "(serius lagi) Tapi kita harus hati-hati. "
    
    show carissa sedih
    
    c "Iya... Aku ngerti kok."
    
    n "Di kejauhan, Dewa berdiri sambil menatap mereka."
    n "Ekspresinya tidak terbaca."
    
    show dewa misterius at center behind aksara
    with dissolve
    
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
    
    c "(melepas tangan Aksara) A-aku... harus ke sana."
    
    show aksara kaget
    with vpunch
    
    a "CARISSA! JANGAN!"
    
    hide carissa bingung
    with easeoutright
    
    n "Carissa berlari ke dalam kegelapan candi."
    n "Mengikuti suara yang terus memanggilnya."
    
    play sound audio.running
    
    show aksara sedih at center
    with move
    
    a "(berteriak) CARISSA!"
    
    n "Aksara mencoba mengejar, tapi..."
    
    with hpunch
    
    n "Pintu batu besar jatuh, memblokir jalannya."
    
    a "(memukul pintu) CARISSA! JAWAB AKU!"
    
    scene black
    with Dissolve(1.0)
    
    n "Di dalam kegelapan, Carissa terus berjalan."
    n "Suara itu semakin jelas."
    
    show carissa takut at center
    with dissolve
    
    c "(ketakutan) H-halo? Siapa di sana?"
    
    show dewa wujud_asli at right
    with flash_red
    
    d "(suara berbeda, lebih dalam) Akhirnya... kau datang sendiri."
    
    show carissa kaget
    with vpunch
    
    c "D-Dewa?! Kenapa wujudmu—"
    
    show dewa wujud_asli
    
    d "Ini wujud asliku, Carissa."
    
    show aura_merah at right
    with dissolve
    
    n "Aura merah gelap menyelimuti Dewa."
    
    show carissa takut
    
    c "(mundur) A-aku... aku harus balik!"
    
    show dewa wujud_asli
    
    d "(mengangkat tangan) Sudah terlambat."
    
    n "Carissa merasakan tubuhnya tidak bisa bergerak."
    
    show carissa kaget
    
    c "A-apa yang kamu lakukan?!"
    
    show dewa wujud_asli
    
    d "Tenang... aku tidak akan sakiti kamu."
    d "Kamu terlalu berharga untuk dilukai."
    
    n "Di luar, Aksara masih berusaha membuka pintu."
    
    hide carissa kaget
    hide dewa wujud_asli
    hide aura_merah
    with dissolve
    
    show aksara sedih at center
    with dissolve
    
    a "(menangis) Carissa... Kenapa kamu nggak dengerin aku..."
    
    scene black
    with Dissolve(2.0)
    
    n "Ketika pintu akhirnya terbuka, Aksara menemukan Carissa terbaring tidak sadarkan diri."
    n "Sedangkan Dewa sudah menghilang dalam kegelapan."
    
    jump bad_ending_chapter2

# ===== NEUTRAL ENDING ROUTE =====
label stay_neutral_ending:
    $ aksara_points += 1
    $ dewa_points += 1
    
    show carissa sedih
    
    c "(bingung) A-aku... aku nggak tau harus gimana!"
    
    show aksara khawatir
    
    a "Carissa, fokus! Lihat aku!"
    
    n "Aksara memegang kedua bahu Carissa dengan erat."
    
    show aksara serius
    
    a "Tarik napas... dan ikuti aku perlahan."
    
    show carissa normal
    
    c "(menarik napas) H-huh... O-oke..."
    
    n "Perlahan, mereka berjalan mundur menuju pintu keluar."
    n "Suara itu masih terus memanggil, tapi Carissa berusaha mengabaikannya."
    
    suara "(semakin lemah) Carissa... jangan pergi..."
    
    show carissa takut
    
    c "(menutup telinga) Pergi... pergi dari kepalaku!"
    
    show aksara normal
    
    a "Hampir sampai... terus bergerak!"
    
    play sound audio.running
    
    n "Mereka berdua akhirnya sampai di pintu keluar."
    
    scene bg candi_gerbang
    with Dissolve(1.0)
    
    show carissa sedih at right
    show aksara khawatir at left
    with dissolve
    
    c "(terduduk) Huh... huh... kenapa... kenapa aku hampir ngikutin suara itu?"
    
    show aksara normal
    
    a "(mengelus punggung Carissa) Karena mereka punya pengaruh ke kamu."
    a "Tapi yang penting... kamu bertahan."
    
    show carissa normal
    
    c "Aku... masih bingung, Aksara."
    c "Apa sebenarnya yang terjadi sama aku?"
    
    show aksara khawatir
    
    a "(menghela napas) Aku juga belum yakin sepenuhnya."
    a "Tapi satu hal yang pasti... kamu istimewa, Carissa."
    a "Dan itu yang bikin kamu jadi target."
    
    show carissa sedih
    
    c "Istimewa... atau dikutuk?"
    
    show aksara normal
    
    a "Tergantung gimana kamu ngeliatnya."
    
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
    
    n "Kembali ke sekolah, suasana sudah lebih tenang."
    n "Rombongan kelompok Carissa serta Guru menganggap getaran tadi hanya gempa kecil biasa."
    
    show carissa normal at right
    show aksara normal at left
    with dissolve
    
    a "Kamu yakin gapapa?"
    
    show carissa senyum
    
    c "Iya, aku oke kok. Makasih ya, Aksara."
    c "Kalau nggak ada kamu... aku nggak tau bakal gimana."
    
    show aksara senyum
    
    a "Untuk itu aku ada."
    a "(serius) Tapi mulai sekarang, kamu harus lebih waspada."
    a "Mereka udah tau siapa kamu. Dan mereka nggak akan berhenti."
    
    show carissa bingung
    
    c "Mereka itu... siapa sebenernya?"
    
    show aksara khawatir
    
    a "Roh-roh yang terjebak di dunia ini."
    a "Mereka nyari jalan untuk bisa bebas..."
    
    show carissa takut
    
    c "Gitu ya..."
    
    show aksara normal
    
    a "Yang penting, kamu sekarang udah tau kamu nggak sendirian."
    
    show carissa senyum
    
    c "(mengangguk) Iya. Aku punya kamu."
    
    n "Mereka tersenyum satu sama lain."

    scene bg langit_jingga
    with slow_dissolve
    
    n "Matahari sore menyinari mereka dengan hangat."
    n "Meski bahaya telah berlalu, perjalanan baru saja dimulai."
    n "Namun kali ini, Carissa tahu ia memiliki seseorang yang bisa ia percaya."
    
    centered "{color=#0f0}★ GOOD ENDING - KEPERCAYAAN YANG KUAT ★{/color}"
    pause 2.0
    
    centered "{color=#fff}Chapter 2 - SELESAI{/color}"
    pause 2.0
    
    centered "{color=#888}Kepercayaanmu pada Aksara telah membuka jalan yang lebih aman...{/color}"
    pause 2.0
    

# ===== BAD ENDING CHAPTER 2 =====
label bad_ending_chapter2:
    scene bg ruang_tamu_temaram
    with slow_dissolve
    
    play music audio.tension fadein 2.0
    
    n "Carissa terbangun di kamarnya."
    n "Ia tidak ingat bagaimana ia bisa pulang."
    
    show carissa bingung at center
    with dissolve
    
    c "(memegang kepala) Kepalaku... sakit banget."
    
    show nenek khawatir at left
    with easeinleft
    
    nenek "Carissa! Syukurlah kamu udah bangun, Nduk."
    nenek "Kamu pingsan di candi tadi. Aksara yang bawa kamu pulang."
    
    show carissa kaget
    
    c "Aksara? Di mana dia?"
    
    show nenek sedih
    
    nenek "Dia langsung pergi setelah nganterin kamu."
    nenek "Mukanya sedih banget, Nduk."
    
    show carissa sedih
    
    c "(dalam hati) Aksara... maafin aku..."
    
    hide nenek sedih
    with dissolve
    
    n "Carissa mengambil ponselnya, mencoba menghubungi Aksara."
    n "Tapi tidak ada jawaban."
    
    show carissa takut
    
    c "Dia... marah sama aku."
    
    n "Di pojok kamar, bayangan Dewa muncul sekilas."
    
    show dewa misterius at right
    with dissolve
    
    d "(berbisik) Baru sekarang menyesal?"
    
    hide dewa misterius
    with dissolve
    
    show carissa kaget
    with vpunch
    
    c "Siapa?!"
    
    n "Tapi tidak ada siapa-siapa."
    n "Hanya keheningan yang mencekam."
    
    scene bg langit_jingga
    with slow_dissolve
    
    n "Senja tiba dengan cepat."
    n "Carissa menatap ponselnya, berharap Aksara akan membalas pesannya."
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
    
    play music audio.mystery_theme fadein 2.0
    
    n "Perjalanan pulang terasa sunyi."
    n "Carissa dan Aksara duduk berdampingan di bus, tapi tidak banyak bicara."
    
    show carissa sedih at right
    show aksara khawatir at left
    with dissolve
    
    a "Kamu... masih denger suara-suara aneh?"
    
    show carissa normal
    
    c "(menggeleng) Nggak. Udah berkurang kok."
    
    show aksara normal
    
    a "Syukurlah..."
    a "(menghela napas) Tapi aku khawatir ini cuma baru permulaannya aja."
    
    show carissa bingung
    
    c "Maksudnya?"
    
    show aksara serius
    
    a "Mereka udah tau siapa kamu. Dan mereka nggak akan berhenti sampai dapet apa yang mereka mau."
    
    show carissa takut
    
    c "Ohhh..."
    
    show aksara normal
    
    a "Kita harus lebih hati-hati."
    a "Dan... kamu harus mulai belajar melindungi diri."
    
    show carissa sedih
    
    c "Aku... nggak yakin bisa."
    
    show aksara khawatir
    
    a "Kamu bisa. Aku percaya."
    a "(tersenyum tipis) Lagipula, kamu nggak sendirian."
    
    show carissa senyum
    
    c "Makasih, Aksara."
    
    n "Namun di dalam hati Carissa, masih ada keraguan."
    n "Suara itu... terasa begitu meyakinkan."
    n "Bagian dirinya masih penasaran... apa yang sebenarnya ada di dalam candi?"
    
    scene bg langit_jingga
    with slow_dissolve
    
    n "Senja menyelimuti kota dengan warna oranye kemerahan."
    n "Carissa berdiri di antara dua pilihan."
    n "Percaya sepenuhnya pada Aksara... atau mencari tahu sendiri kebenarannya."
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
    
    play music audio.mystery_theme fadein 2.0
    
    n "Pagi itu, Carissa bangun dengan perasaan lebih tenang."
    n "Meski kejadian di candi masih membayangi, ia merasa lebih siap menghadapinya."
    
    show carissa normal at center
    with dissolve

    show kalung_glow at center
    with dissolve
    
    n "Kalung ibunya bergetar lembut. Lebih hangat dari biasanya."
    
    c "(bingung) Aneh..."
    
    hide kalung_glow
    with dissolve
    
    n "Matanya tertuju ke kotak kayu di atas lemari yang sedari dulu ia selalu penasaran akan isinya."
    n "Bentuk kotak tersebut terlihat berdebu."
    
    show carissa bingung
    
    c "(dalam hati) Hmmmm, aku kepo."
    
    jump chapter3_scene2

label chapter3_scene1_bad_start:
    scene bg kamar_carissa
    with dissolve
    
    play music audio.tension fadein 2.0
    
    n "Carissa terbangun dengan nafas tersengal."
    n "Mimpi buruk lagi. Kali ini lebih menyeramkan dari sebelumnya."
    
    show carissa sedih at center
    with dissolve
    
    c "(memegang kepala) Kenapa... kenapa aku nggak dengerin Aksara waktu itu?"
    
    n "Ia meraih ponselnya. 3 hari tanpa kontak dengan Aksara."
    n "Pesannya terlihat dibaca saja tapi tidak ada balasan."
    
    show carissa takut
    
    c "(gemetar) Jangan-jangan..."
    
    play sound audio.wind
    
    suara "(berbisik lembut) Carissa..."
    
    show carissa kaget
    with vpunch
    
    c "Suara itu lagi?!"
    
    show kalung_glow at center
    with dissolve
    
    n "Kalung di lehernya bersinar redup."
    
    suara "Jangan takut... Aku cuma mau bantu kamu..."
    
    show carissa bingung
    
    c "(ragu) Bantu... aku?"
    
    hide kalung_glow
    with flash_white
    
    n "Suara itu menghilang, meninggalkan Carissa dalam kebingungan."
    
    show carissa sedih
    
    c "(dalam hati) Apa... apa yang harus aku lakukan?"

    n "Dalam renungan penyesalan, Carissa tanpa sadar melihat seisi kamarnya secara seksama."
    n "Lalu, ia cukup terkejut dengan adanya kotak kayu berdebu di atas lemarinya karena ia tidak pernah menyadari benda tersebut selama bertahun-tahun."

    show carissa bingung
    with hpunch 
    
    c "Apa ya isi kotak itu?"
    
    jump chapter3_scene2

label chapter3_scene1_neutral_start:
    scene bg kamar_carissa
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Carissa duduk di tepi tempat tidur, menatap ponselnya."
    n "Ada pesan dari Aksara sejak semalam, tapi ia belum membalasnya."
    
    show carissa bingung at center
    with dissolve
    
    c "(membaca pesan) 'Carissa, kita perlu ngobrol. Ada yang harus aku jelasin.'"
    
    n "Jari-jarinya menggantung di atas keyboard."
    n "Ia ingin membalas, tapi tidak tahu harus bilang apa."
    
    c "(dalam hati) Aku... masih bingung sama yang terjadi."
    c "Tapi aku juga nggak bisa terus-terusan hindarin dia."
    

    show kalung_glow at center
    with dissolve
    
    n "Kalung ibunya bergetar pelan, seolah merespons kegelisahannya."
    
    hide kalung_glow
    with dissolve

    show carissa normal
    with dissolve
    
    c "(menghela napas) Mungkin... aku harus cari tau sendiri dulu."
    
    n "Ia melirik ke arah atas lemarinya, disana terdapat kotak kayu berdebu."
    n "Tiga hari yang lalu, Carissa sempat sadar ada kotak tersebut seusai pulang dari studi tour."
    n "Tapi, ia memilih abai saat itu karena mungkin isinya tidak terlalu penting."
    n "Namun, saat ini Carissa berpikir ulang..."

    c "Mungkin, ada petunjuk disitu...?"

    jump chapter3_scene2

label chapter3_scene2:
    scene bg kamar_carissa
    with dissolve
    
    n "Carissa memutuskan untuk membuka kotak kayu tersebut."
    n "Sudah bertahun-tahun kotak itu tersimpan, tidak tersentuh."
    
    show carissa normal at center
    with dissolve
    
    n "Carissa berjinjit saat hendak mengambil kotak. Ia pun akhirnya berhasil menurunkannya dari lemari."

    play sound audio.thing_open
    
    n "Kotak terbuka dengan bunyi derit pelan."
    n "Debu beterbangan di udara."

    n "Di dalamnya: sebuah buku catatan tua, beberapa foto, dan sepotong kain merah yang sudah pudar."
    
    show carissa kaget
    
    c "Ini... buku catatan Ibu?"
    

    n "Carissa mengambil foto-foto lama."
    n "Foto pertama: Ibunya masih muda, berdiri di depan kuil dengan beberapa orang berpakaian tradisional."
    
    c "(membaca tulisan di belakang foto) 'Pertemuan Nirantara, 2007...'"
    
    show carissa bingung
    
    c "Nirantara? Apa itu?"
    
    n "Foto kedua: Ibunya sedang hamil besar, berdiri di depan candi saat... gerhana bulan."
    
    show carissa kaget
    with vpunch
    
    c "Ini... waktu Ibu lagi hamil?!"
    
    n "Ada tulisan di belakang: 'Malam kelahiran yang ditakdirkan. Semoga dia tidak menanggung beban ini.'"
    
    show carissa sedih
    
    c "(air mata menetes) Ibu..."
    
    hide carissa sedih
    with dissolve

    play sound audio.book_flip
    
    n "Carissa membuka buku catatan dengan tangan gemetar."
    
    centered "{i}'16 Tahun yang lalu...'{/i}"
    pause 1.0
    centered "{i}'Hari ini aku melahirkan Carissa.'{/i}"
    pause 1.0
    centered "{i}'Tepat saat gerhana bulan.'{/i}"
    pause 1.0
    
    play sound audio.book_flip
    
    centered "{i}'Para tetua Nirantara bilang... Carissa adalah Pembawa Darah Rakta.'{/i}"
    pause 1.0
    centered "{i}'Aku takut. Sangat takut.'{/i}"
    pause 1.0
    centered "{i}'Tapi aku akan lindungi dia. Apapun yang terjadi.'{/i}"
    pause 1.5
    
    show carissa sedih
    with dissolve
    
    c "(menangis) Jadi... aku..."
    

    play sound audio.book_flip
    
    centered "{i}'2 tahun kemudian...'{/i}"
    pause 1.0
    centered "{i}'Dewa Abinaya mulai bergerak.'{/i}"
    pause 1.0
    centered "{i}'Dia tau tentang Carissa. Dia akan datang.'{/i}"
    pause 1.5
    
    show carissa kaget
    with dissolve
    
    c "Dewa... Abinaya?"
    c "(terkejut) Nama itu... sama kayak—"
    
    
    show kalung_glow at center
    with flash_red
    
    play sound audio.heartbeat
    
    n "Kalung di leher Carissa tiba-tiba menyala merah terang!"
    
    show carissa takut
    with vpunch
    
    c "A-apaan ini?!"
    
    
    n "Pandangan Carissa kabur. Ruangan berputar."
    
    scene black
    with flash_white
    

    play music audio.tension fadein 2.0
    
    centered "{color=#8b0000}Pecahan Memori{/color}"
    pause 1.0
    
    scene bg candi_gerbang
    with nightmare_transition
    
    n "Carissa menemukan dirinya berdiri di depan gerbang besar."
    n "Tapi ini bukan dirinya. Dia... melihat dari mata orang lain."
    
    show carissa bingung at center
    with dissolve
    
    c "(suara bergema) Di mana... ini?"

    n "Di depannya, gerbang batu besar bergetar hebat."
    n "Retakan mulai muncul di permukaannya."
    
    show dewa wujud_asli at right
    with dissolve
    
    show aura_merah at right
    with flash_red
    
    d "(suara bergema, marah) BUKA GERBANG INI!"
    d "BIARKAN AKU LEWAT!"
    
    n "Dari balik gerbang, sosok besar dengan aura merah menyeramkan mencoba menembus."
    

    n "Tangan di depan Carissa (tangan ibunya) terangkat."
    n "Energi biru bersinar, membentuk segel."
    
    show aura_biru at left
    with flash_blue
    
    n "Ibunya berbisik mantra yang Carissa tidak pahami."
    
    show dewa marah
    
    d "(menjerit) KAU PIKIR KAU BISA TAHAN AKU?!"
    d "ANAKMU! ANAKMU ADALAH DARAH RAKTA!"
    d "AKU AKAN KEMBALI UNTUKNYA!"
    
    show aura_biru at center
    with flash_blue
    
    play sound audio.magic
    
    n "Segel menguat. Gerbang mulai tertutup."
    
    show dewa serius
    
    d "(suara melemah) Tunggu saja..."
    d "Aku akan kembali untuk anak itu!"
    
    hide dewa wujud_asli
    hide aura_merah
    with flash_white
    
    n "Sosok itu tersedot kembali ke dalam gerbang."
    

    hide aura_biru
    with dissolve
    
    n "Tubuh ibunya perlahan melemah."
    n "Energi terkuras habis."
    
    n "Pandangan mengabur... lalu gelap."
    
    scene black
    with flash_white
    
    scene bg kamar_carissa
    with dissolve
    
    show carissa takut at center
    with vpunch
    
    c "(terbangun) HAH!"
    
    n "Carissa terengah-engah, keringat dingin membasahi dahinya."
    
    show carissa sedih
    
    c "(gemetar) Itu... itu memori Ibu?"
    c "(terkejut) Jadi murid baru... Dewa yang sama?!"
    

    show carissa takut
    with vpunch
    
    c "Dia bilang... akan kembali lagi..."
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
    play sound audio.phone_vibrate
    
    n "Carissa menghubungi Aksara dengan tangan gemetar."

    if aksara_points > dewa_points + 3:
        
        n "Telepon diangkat setelah nada pertama."
        
        a "Carissa? Ada apa?"
        
        c "(bergetar) Aksara... aku... aku nemuin sesuatu."
        c "Bisa kamu ke rumahku sekarang?"
        
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
        
        c "Aksara, aku nemu catatan Ibu."
        c "Dan... aku lihat sesuatu yang—"
        
        a "(memotong) Jangan kemana-mana. Aku datang sekarang."
    
    scene black
    with Dissolve(1.0)
    
    jump aksara_arrives


label investigate_more:
    show carissa bingung
    
    c "(membuka lagi buku catatan) Mungkin ada info lain..."
    
    play sound audio.book_flip
    
    n "Carissa membolak-balik halaman dengan cepat."
    n "Sampai ia menemukan halaman yang berbeda—ditulis dengan tinta merah."
    
    show carissa kaget
    
    centered "{color=#8b0000}{i}'KALAU KAMU MEMBACA INI, CARISSA...'{/i}{/color}"
    pause 1.5
    
    c "Ini... pesan untuk aku?"
    
    centered "{color=#8b0000}{i}'Maafkan Ibu. Ibu tidak bisa lindungi kamu selamanya.'{/i}{/color}"
    pause 1.0
    centered "{color=#8b0000}{i}'Tapi ingat ini...'{/i}{/color}"
    pause 1.0
    centered "{color=#8b0000}{i}'Kamu punya pilihan. Kamu yang tentukan jalanmu sendiri.'{/i}{/color}"
    pause 1.5
    
    show carissa sedih
    
    c "..."
    
    centered "{color=#8b0000}{i}'Percayalah pada seseorang yang kamu yakini saat ini.'{/i}{/color}"
    pause 1.0
    
    show carissa bingung
    with vpunch
    
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
    
    n "Carissa segera berkemas-kemas dan hendak keluar dari rumah."
    
    c "(dalam hati) Aku harus dapet jawaban sekarang!"
    
    play sound audio.door_open
    
    n "Namun, tepat Carissa melangkah keluar..."

    show nenek khawatir at left
    with dissolve
    
    nenek "Carissa?! Mau kemana jam segini?"
    
    show carissa kaget at right
    with move
    
    c "Nek, aku—"
    
    show nenek serius
    
    nenek "(melihat buku di tangan Carissa) Kamu... udah buka kotak itu?"
    
    show carissa sedih
    
    c "Iya, Nek. aku jadi tahu dan yakin sekarang."
    c "Kalo aku... Darah Rakta."
    
    show nenek sedih
    
    nenek "Carissa..."
    
    show nenek khawatir
    
    nenek "Duduk dulu, Nduk. Nenek mau cerita semuanya."
    
    jump nenek_explains

label call_nenek_path:
    $ talked_to_nenek = True
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek khawatir at left
    show carissa sedih at right
    with dissolve
    
    c "Nek... aku nemu catatan Ibu."
    
    show nenek sedih
    
    nenek "(menghela napas panjang) Akhirnya... hari ini juga tiba."
    
    show carissa bingung
    
    c "Nenek tahu soal ini?"
    
    show nenek normal
    
    nenek "(mengangguk) Nenek tau sejak kamu lahir, Nduk."
    
    jump nenek_explains

label nenek_explains:
    $ talked_to_nenek = True
    scene bg ruang_tamu_terang
    with dissolve
    
    show nenek normal at left
    show carissa normal at right
    with dissolve
    
    nenek "Carissa... kamu itu lahir pas gerhana bulan."
    nenek "Tepat 200 tahun setelah Darah Rakta terakhir."
    
    show carissa sedih
    
    c "Jadi... aku emang ditakdirkan buat ini?"
    
    show nenek khawatir
    
    nenek "Para tetua Nirantara bilang begitu."
    nenek "Tapi Ibumu... dia menolak takdir itu."
    
    show carissa kaget
    
    c "Nolak?"
    
    show nenek sedih
    
    nenek "Dia bilang: 'Carissa itu bukan alat, Mbok. Dia punya hak untuk hidup normal.'"
    nenek "Makanya dia rela berkorban."
    nenek "Dia menahan roh kuat namanya Dewa Abinaya."
    
    show carissa takut
    
    c "Tapi... sekarang Dewa itu kembali lagi, Nek."
    
    show nenek normal
    
    nenek "(mengangguk) Iya. Nenek juga sebenernya udah ngerasain kalo segel Gerbang Roh agak melemah."
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
    
    nenek "Hubungi Aksara, Nduk. Dia juga Nirantara sama kayak kita."
    nenek "Dia bisa bantu kamu."
    
    $ aksara_points += 1
    
    show carissa normal
    
    c "(mengangguk) Oke, Nek."
    
    jump call_aksara_path

label call_aksara_path:
    play sound audio.phone_vibrate
    
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
        
        a "(langsung menghampiri) Carissa, kamu gapapa?"
        
        show carissa sedih
        
        c "(memeluk Aksara) Aksara... aku takut."
        
        show aksara normal
        
        a "(mengelus punggung Carissa) Tenang, aku di sini."
        
    elif dewa_points > aksara_points + 3:
        # Bad relationship
        show carissa sedih at right
        with dissolve
        
        a "(berdiri agak jauh) ...Jadi, ada apa?"
        
        show carissa takut
        
        c "Aksara... aku tau sekarang. Tentang Darah Rakta."
        
        show aksara kaget
        with vpunch
        
        a "Kamu... gimana bisa—"
        
        show carissa serius
        
        c "Aku nemu catatan Ibu. Dan aku... lihat memori dia sekilas."
        
        show aksara sedih
        
        a "(menunduk) Maafin aku. Aku harusnya ngomong dari awal."
        
    else:
        # Neutral
        show carissa normal at left
        with dissolve
        
        a "Kamu bilang nemu sesuatu?"
        
        c "(menyerahkan buku) Ini. Catatan Ibu."
        
        show aksara kaget at right
        with vpunch
        
        a "(membaca cepat) ..."
        a "(menutup buku) Carissa... kita perlu ngobrol serius."
    
    jump chapter3_scene3  

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
        
        a "(duduk di sebelah Carissa) Kamu bilang nemu sesuatu?"
        
        show carissa sedih
        
        c "(menyerahkan buku catatan) Ini... catatan Ibu."
        
        show aksara khawatir
        
        a "(membuka buku, membaca)"
        n "Aksara membaca dalam diam. Ekspresinya berubah."
        
        show aksara sedih
        
        a "Carissa... kamu udah baca semuanya?"
        
        show carissa normal
        
        c "(mengangguk) Iya. Dan aku... lihat sesuatu."
        c "Kayak memori Ibu waktu dia lawan... Dewa."
        
        show aksara kaget
        with vpunch
        
        a "Kamu... masuk ke memori ibumu?"
        
        show carissa bingung
        
        c "Iya. Itu... gimana bisa?"
        
        show aksara serius
        
        a "(menunjuk kalung) Mungkin... dari kalung itu, Carissa."
        a "Aku bisa rasain ada sisa-sisa memori jiwa di dalamnya."
        
        
    elif dewa_points > aksara_points + 3:
        show aksara khawatir at left
        show carissa sedih at right
        with dissolve
        
        a "(berdiri agak jauh) Carissa..."
        
        show carissa takut
        
        c "Aku tau sekarang, Aksara."
        c "Tentang aku. Tentang... Darah Rakta."
        
        show aksara sedih
        
        a "(menunduk) ..."
        a "Aku harusnya ngomong dari awal."
        
        show carissa bingung
        
        c "Kenapa kamu nggak pernah bilang?"
        
        show aksara khawatir
        
        a "Karena... aku takut kamu kenapa-napa."

        show aksara sedih

        a "Aku udah kehilangan orang tuaku dulu."
        a "(suara bergetar) Mereka juga Nirantara. Mereka juga... melindungi orang-orang."
        a "Dan aku... aku nggak bisa ngelakuin apa-apa."

        show carissa normal

        c "(terharu) Aksara..."

        show aksara khawatir

        a "Jadi sekarang, aku ga mau kehilangan lagi."
        a "Orang yang penting bagiku."
        
    else:
        show aksara serius at left
        show carissa normal at right
        with dissolve
        
        a "Jadi... kamu tau sekarang?"
        
        show carissa bingung
        
        c "(mengangguk) Iya. Dari catatan Ibu."
        c "Tapi... aku masih bingung banyak hal."
        
        show aksara normal
        
        a "(duduk) Oke. Tanya aja. Aku jawab sejujurnya."
        
        show carissa sedih
        
        c "Aku... kenapa aku Darah Rakta?"
        c "Apa... apa itu kutukan?"
        
        show aksara khawatir
        
        a "(menggeleng) Bukan kutukan. Itu... takdir."
    
    show aksara normal
    
    a "Carissa, aku mau jelasin dari awal."
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
    
    a "Oke. Jadi... kamu tau tentang Gerbang Roh?"
    
    show carissa bingung
    
    c "Yang... di candi itu?"
    
    show aksara normal
    
    a "(mengangguk) Iya. Gerbang yang misahin dunia manusia sama dunia roh."
    a "Selama ini, gerbang itu... setengah terbuka."
    
    show carissa kaget
    
    c "Setengah terbuka?!"
    
    show aksara khawatir
    
    a "Iya. Makanya kamu bisa liat roh. Makanya mereka bisa ganggu kamu."
    a "Dan... makanya Dewa bisa 'menyusup' ke dunia manusia."
    
    show carissa takut
    
    c "Dewa... dia bukan manusia?"
    
    show aksara serius
    
    a "(menggeleng) Dia roh. Roh yang sangat kuat."
    a "Aku curiga, Dewa yang ada di sekolah kita beneran roh kuno itu."
    
    show carissa sedih
    
    c "Gimana bisa dia wujudnya manusia? Terus apa tujuan dia?"
    
    show aksara normal
    
    a "Roh itu bisa manipulasi wujud mereka, Carissa."
    a "Terus... Aku dengar dari cerita Kakek, tujuan dia itu mau buka gerbang sepenuhnya."
    
    show carissa bingung
    
    c "Buat apa?"
    
    show aksara khawatir
    
    a "Buat menyatukan dunia manusia sama dunia roh."
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
    
    a "Carissa, Darah Rakta itu... kemampuan langka."
    a "Muncul cuma sekali dalam 200 tahun."
    
    show carissa kaget
    
    c "200 tahun?!"
    
    show aksara serius
    
    a "Iya. Dan kamu... lahir tepat 200 tahun setelah Darah Rakta terakhir."
    a "Apalagi tepat gerhana bulan. Waktu yang... sempurna."
    
    show carissa takut
    
    c "Jadi... aku ditakdirkan buat ini?"
    
    show aksara khawatir
    
    a "Bukan takdir. Waktu."
    a "(menatap Carissa) Tapi... apa yang kamu lakukan dengan kekuatan itu?"
    a "Itu pilihan kamu."
    
    jump scene3_common_part

label scene3_with_nenek_knowledge:
    if aksara_points > dewa_points + 3:
        show aksara normal at left
        show carissa normal at right
        with dissolve
        
        a "(duduk) Jadi... Nenek udah cerita?"
        
        show carissa sedih
        
        c "(mengangguk) Iya. Tentang Darah Rakta, gerbang, Dewa..."
        
        show aksara khawatir
        
        a "Dan... gimana perasaan kamu?"
        
        show carissa bingung
        
        c "Aku... bener-bener kelebihan info. Tapi setidaknya aku paham kenapa."
        
        show aksara normal
        
        a "(tersenyum tipis) Aku tau ini berat."
        a "Tapi aku janji... aku bakal bantu kamu."
        
    elif dewa_points > aksara_points + 3:
        show aksara sedih at left
        show carissa sedih at right
        with dissolve
        
        a "(berdiri agak jauh) Kamu... udah tau semuanya dari Nenek?"
        
        show carissa normal
        
        c "(mengangguk) Iya."
        
        n "Hening canggung."
        
        show aksara khawatir
        
        a "Maafin aku. Aku harusnya yang ngomong duluan."
        
        show carissa bingung
        
        c "Kenapa kamu nggak pernah bilang?"
        
        show aksara sedih
        
        a "Karena... aku takut kamu benci aku."
        
        show carissa normal
        
        c "..."
        
    else:
        show aksara serius at left
        show carissa normal at right
        with dissolve
        
        a "Jadi Nenek udah jelasin?"
        
        show carissa bingung
        
        c "Iya. Tapi... aku masih bingung beberapa hal."
        
        show aksara normal
        
        a "Oke. Tanya aja."
    
    show aksara serius
    
    a "Carissa, pasti Nenek udah bilang tentang pilihan kamu kan?"
    
    show carissa sedih
    
    c "(mengangguk) Tutup gerbangnya... atau buka seluruhnya."
    
    show aksara normal
    
    a "Iya. Tapi ada yang Nenek mungkin belum tahu."
    
    show carissa bingung
    
    c "Apa?"
    
    show aksara khawatir
    
    a "Tentang Dewa Abinaya, teman sekelasmu."
    
    show carissa kaget
    
    c "Dewa... yang di sekolah?"
    
    show aksara serius
    
    a "(mengangguk) Dia... bukan manusia."
    
    show carissa normal
            
    c "Berarti, dia-"
            
    show aksara sedih
            
    a "Ya... roh kuno yang udah diceritain sama nenekmu."
    a "Dia nyoba nyamar jadi manusia biar ga dicurigain sama Nirantara yang lain."
            
    show carissa kaget
    with vpunch
            
    c "APA?!"
            
    show aksara sedih
    
    a "Aku juga baru tau abis kita selesai studi tournya."
    a "Soalnya aku bener-bener udah dilatih cara agar tau aura roh Dewa itu kayak gimana."
    
    show carissa takut
    
    c "Terus... kenapa dia ga langsung ambil diriku?"
    
    show aksara serius
    
    a "Karena, kuliat kamu ada semacam pelindung yang kuat."
    a "(menunjuk kalung) kayaknya dari itu deh."
    a "Yah, intinya Dewa ga bisa sembarangan sih..."
    a "jadi dia ngutus kroco-kroconya untuk nakutin kamu dulu untuk manfaatin ketakutanmu."
    
    show carissa takut
    with vpunch
    
    c "Jadi... kalo aku takut—"
    
    a "Pelindung itu bakal goyah dikit."
    a "(menggenggam tangan Carissa) Makanya aku nggak mau kamu ambil risiko itu dan kasih kamu jimat untuk lapisan."
    
    jump scene3_common_part

label scene3_common_part:
    show aksara normal at left
    show carissa normal at right
    with dissolve
    
    a "Carissa, yang penting sekarang..."
    a "Kamu harus belajar mengendalikan kekuatan kamu."
    
    show carissa bingung
    
    c "Mengendalikan? Caranya gimana?"
    
    show aksara serius
    
    a "Aku bisa latih kamu."
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
    
    a "Carissa, ada satu hal lagi."
    
    show carissa normal
    
    c "Apa?"
    
    show aksara khawatir
    
    a "Konfrontasi terakhir... bakal terjadi di candi Reksana Sewu."
    a "Tempat gerbang Roh berada."
    
    show carissa takut
    
    c "Kapan?"
    
    show aksara serius
    
    a "Aku nggak tau pasti. Tapi... segera terjadi."
    a "Aku takut Dewa makin agresif, makanya kita harus selangkah di depannya."
    
    if not talked_to_nenek:
        play sound audio.door_open
        
        show nenek khawatir at center behind aksara
        with dissolve
        
        nenek "Carissa, Aksara..."
        
        show carissa kaget at right
        show aksara normal at left
        
        c "Nek! Dari tadi dengerin?"
        
        show nenek sedih
        
        nenek "(mengangguk) Iya, Nduk."
        nenek "Nenek harus tambahin sesuatu."
        
    else:
        show nenek normal at center behind aksara
        with dissolve
        
        nenek "Aksara bener, Nduk."
        nenek "Kamu harus berlatih."
    
    show nenek serius
    
    nenek "Apapun yang terjadi..."
    nenek "Keputusan semua ada di tangan kamu."
    
    show carissa sedih
    
    c "(mengangguk pelan)"
    
    show aksara normal
    
    a "Carissa, aku mau kamu tau satu hal."
    
    show carissa bingung
    
    c "Apa?"
    
    show aksara senyum
    
    a "Apapun yang kamu pilih nanti..."
    a "Aku bakal selalu di sisi kamu."
    
    $ aksara_points += 1
    
    show carissa senyum
    
    c "(tersenyum kecil) Makasih, Aksara."
    
    show nenek senyum
    
    n "Mata Nenek terlihat berkaca-kaca."

    show carissa normal
    
    c "Nenek...?"
    
    show nenek sedih
    
    nenek "(menggeleng) Nggak apa-apa, Nduk."
    nenek "Nenek cuma... bangga sama kamu."

    hide nenek sedih
    hide carissa normal
    hide aksara senyum
    with dissolve

    scene black
    with Dissolve(1.0)

    jump label chapter3_scene4

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
    
    n "Carissa dan Aksara bertemu di kuil untuk berlatih."
    n "Pagi itu udara terasa sejuk dan menyegarkan."
    
    show carissa senyum at right
    show aksara senyum at left
    with dissolve
    
    a "Pagi, Carissa! Udah sarapan?"
    
    show carissa normal
    
    c "Udah dong. Nenek masak bubur kesukaan aku."
    
    show aksara normal
    
    a "(tersenyum) Bagus. Kamu perlu energi buat latihan hari ini."
    
    show carissa bingung
    
    c "Emang latihannya berat?"
    
    show aksara senyum
    
    a "Lumayan. Tapi aku yakin kamu bisa."
    a "(menepuk bahu Carissa) Lagipula, aku bakal bantu kamu kok."
    
    show carissa senyum
    
    c "Makasih, Aksara."
    
    jump scene4_training_part1

# ===== BAD RELATIONSHIP PATH =====
label scene4_bad_relationship:
    scene bg kuil
    with dissolve
    
    play music audio.tension fadein 2.0
    
    n "Carissa tiba di kuil lebih awal."
    n "Suasana terasa... canggung."
    
    show carissa sedih at center
    with dissolve
    
    c "(dalam hati) Apa Aksara masih marah ya?"
    
    show aksara khawatir at left
    with easeinleft
    
    n "Aksara datang, berdiri agak jauh."
    
    a "...Kamu udah datang."
    
    show carissa bingung at right
    with move
    
    c "Iya..."
    
    n "Keadaan hening di sekitar membuat keduanya tampak canggung."
    
    show aksara serius
    
    a "(menghela napas) Oke. Kita mulai aja."
    
    show carissa normal
    
    c "Aksara... aku—"
    
    show aksara normal
    
    a "(menggeleng) Nggak usah. Sekarang fokus ke latihan dulu."
    a "Urusan yang lain... nanti aja."
    
    show carissa sedih
    
    c "(menunduk) ...Oke."
    
    jump scene4_training_part1

# ===== NEUTRAL RELATIONSHIP PATH =====
label scene4_neutral_relationship:
    scene bg candi_gerbang
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Carissa dan Aksara bertemu di kuil seperti yang dijanjikan."
    n "Tidak terlalu jauh, tapi juga tidak terlalu dekat."
    
    show carissa normal at right
    show aksara normal at left
    with dissolve
    
    a "Siap?"
    
    show carissa bingung
    
    c "Sejujurnya... nggak tau harus siap atau nggak."
    
    show aksara senyum
    
    a "(tersenyum tipis) Tenang. Kita mulai dari dasarnya ya."
    
    show carissa normal
    
    c "(mengangguk) Oke."
    
    jump scene4_training_part1

# ===== TRAINING PART 1: Merasakan Energi =====
label scene4_training_part1:
    show kakek normal at center behind aksara
    with dissolve
    
    k "Ah, kalian sudah datang."
    
    show carissa kaget
    
    c "Kakek!"
    
    show kakek senyum
    
    k "Carissa, senang bertemu lagi."
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
    
    k "Baik, kita mulai."
    k "Langkah pertama: merasakan energi spiritual di sekitarmu."
    
    show carissa normal at right
    
    c "Caranya?"
    
    show kakek normal
    
    k "Tutup matamu. Tarik napas dalam-dalam."
    k "Rasakan... aliran energi di dalam tubuhmu."
    
    show carissa normal
    
    c "(menutup mata)"
    
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
    
    n "Detak jantung. Aliran darah. Dan... sesuatu yang lebih."
    
    show carissa kaget
    with vpunch
    
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
    
    k "Bagus! Itu energi spiritual kamu."
    k "Sekarang, coba fokuskan ke tanganmu."
    
    jump scene4_training_part2

# ===== TRAINING PART 2: Manifestasi Energi =====
label scene4_training_part2:
    show carissa normal
    
    c "(menutup mata lagi)"
    
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
    
    c "(membuka mata) Cahaya ini—!"
    
    show kakek normal
    
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
    
    k "Sekarang, latihan kedua: membuat pelindung."
    k "Ini penting buat melindungi diri dari serangan spiritual."
    
    show carissa normal
    
    c "Sepenting itu ya?"
    
    show aksara normal
    
    a "(mengeluarkan jimat) Iya, beneran penting."
    
    show aura_biru at left
    with flash_blue
    
    play sound audio.magic
    
    n "Aksara mengeluarkan energi dari jimatnya."
    n "Cahaya biru tua membentuk perisai di sekitarnya."
    
    show carissa kaget
    
    c "Wah..."
    
    show kakek normal
    
    k "Sekarang giliran kamu, Nduk."
    k "Fokuskan energi ke benda yang jadi pelindungmu."
    
    show carissa normal
    
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
    
    n "Carissa dan Aksara duduk berdampingan di bawah pohon."
    n "Suasana hangat dan nyaman."
    
    a "Kamu hebat tadi."
    
    show carissa normal
    
    c "(tertawa kecil) Ah, berlebihan deh."
    c "Aku masih banyak yang harus belajar."
    
    show aksara normal
    
    a "Tapi kamu udah jauh lebih baik dari aku dulu."
    a "(tersenyum) Aku bangga sama kamu."
    
    show carissa senyum
    
    c "(tersenyum) Makasih, Aksara."
    c "Makasih udah selalu... ada buat aku."
    
    show carissa normal
    
    c "(menggenggam tangan Aksara) Aku janji nggak sembarangan kemana-mana."
    
    show aksara senyum
    
    a "(tersenyum) Oke. Aku percaya sama kamu."
    
    jump scene4_shadow

label scene4_rest_bad:
    show carissa sedih at right
    show aksara khawatir at left
    with dissolve
    
    n "Carissa dan Aksara duduk dengan jarak yang cukup jauh."
    n "Hening canggung menyelimuti mereka."
    
    show carissa normal
    
    c "Aksara..."
    
    show aksara serius
    
    a "..."
    
    show carissa sedih
    
    c "(menunduk) Aku tau kamu masih... marah."
    
    show aksara sedih
    
    a "(menghela napas) Aku nggak marah."
    a "(menatap Carissa) Aku cuma... kecewa."
    
    show carissa takut
    
    c "Kecewa...?"
    
    show aksara khawatir
    
    a "Kecewa sama diriku sendiri."
    a "Karena nggak bisa lindungi kamu dengan lebih baik."
    
    show carissa kaget
    
    c "Aksara, itu bukan salah kamu!"
    c "Itu... itu salah aku yang nggak dengerin kamu waktu itu."
    
    show aksara normal
    
    a "..."
    a "(tersenyum sedih) Kita berdua sama-sama salah kayaknya."
    
    show carissa normal
    
    c "Jadi... kita bisa mulai lagi?"
    c "Awal yang baru?"
    
    show aksara senyum
    
    a "(mengulurkan tangan) Awal yang baru."
    
    show carissa senyum
    
    n "Carissa pun menjabat tangan Aksara."
    
    $ aksara_points += 2
    
    jump scene4_shadow

label scene4_rest_neutral:
    show carissa normal at right
    show aksara normal at left
    with dissolve
    
    n "Carissa dan Aksara duduk sambil minum air."
    n "Mereka hening dalam sunyinya kuil tua tersebut."
    
    a "Kamu... gimana perasaanmu?"
    
    show carissa bingung
    
    c "Maksudnya?"
    
    show aksara khawatir
    
    a "Tentang... ya semua ini."
    a "Apa kamu udah bisa nerima dikit-dikit?"
    
    show carissa sedih
    
    c "(menghela napas) Yah, gimanapun juga aku harus ngelakuin ini kan?"
    
    show aksara normal
    
    a "Tenang, kamu nggak sendirian."
    a "Aku bakal bantuin kamu sebisa aku, jadi semuanya jangan kamu bebankan ke diri sendiri ya?"
    
    show carissa senyum
    
    c "(tersenyum tipis) Makasih, Aksara." 
    
    jump scene4_shadow

label scene4_shadow:
scene black
    with Dissolve(1.0)
    
    centered "{color=#fff}Beberapa jam setelah berada di kuil, Carissa memutuskan pulang karena ia merasa lelah.{/color}"
    pause 1.0
    
    scene bg cafe
    with dissolve
    
    play music audio.tension fadein 2.0
    
    n "Dalam perjalanan pulang, Carissa mampir sebentar ke salah satu kafe yang ada di pinggir jalan."
    n "Ia ingin membeli Iced Coffee kesukaannya."
    
    show carissa normal at center
    with dissolve
    
    c "(melihat-lihat rak menu) Mmmm..."
    
    play sound audio.wind
    
    n "Setelah membeli minuman favoritnya, ia berjalan menuju pintu keluar toko."
    n "Tepat ia keluarm tiba-tiba udara di sekelilingnya perlahan dingin yang menusuk kulit."
    
    show carissa bingung
    with hpunch
    
    c "(merinding) Ada apa ini?"

    n "Carissa tanpa sadar melihat sekelilingnya untuk memastikan bahwa itu hanya perasaannya sendiri."
    
    play sound audio.heartbeat
    
    scene bg cafe
    with flash_red
    
    show bayangan at center
    with dissolve
    
    play music audio.heartbeat fadein 1.0
    
    n "Dari balik salah satu pohon, sosok bayangan hitam pekat muncul mengawasi Carissa."
    n "Tanpa wajah dan bentuk yang jelas."
    n "Ia perlahan mendekati Carissa yang tepat di depan pintu kafe."
    
    show carissa takut at right
    with move
    
    c "(mundur) S-siapa?!"
    
    suara "(bergema) Carissa..."
    
    show carissa kaget
    
    c "K-kenapa kamu tau namaku?!"
    
    show bayangan
    
    suara "Pesan... dari Tuan Dewa..."
    
    show carissa bingung
    
    c "Dewa...?"
    
    # PESAN ULTIMATUM
    suara "Waktu... hampir habis..."
    suara "Ia... menunggu keputusanmu..."
    suara "Tiga hari lagi... datanglah ke candi..."
    suara "Sendirian..."
    
    show carissa takut
    with vpunch
    
    c "Kalau aku nggak datang?!"
    
    show bayangan
    
    suara "(menyeringai) Maka... orang-orang terkasihmu..."
    suara "Akan menjadi... korban pertama..."
    
    show carissa marah
    with hpunch
    
    c "JANGAN!"
    hide bayangan
    with flash_white
    
    play sound audio.wind
    
    n "Bayangan itu menghilang seperti asap."
    n "Tak ada yang tersisa dari bayangan tersebut."
    n "Dalam diam, Carissa merasakan tubuhnya bergetar hingga ia sampai mengepalkan tangannya."
    
    show carissa takut at center
    with move
    
    c "(terengah-engah) Hah... hah..."
    c "(gemetar) Tiga hari... aku harus... gimana?"
    
    show carissa sedih
    
    c "(dalam hati) Kalau aku bilang ke Aksara... dia pasti ikut."
    c "Tapi kalau aku sendirian... apa aku bisa lindungi mereka?"
    c "Atau... aku cuma nyusahin aja?"
    
    n "Carissa menggenggam erat kalung peninggalan ibunya."
    n "Keputusan besar menunggunya."
    n "Tapi untuk saat ini... ia harus bersiap."

    show carissa normal

    c "Bu... tolong bantu aku ya."
    
    scene black
    with Dissolve(2.0)
    
    jump chapter3_scene5


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
    
    play music audio.mystery_theme fadein 2.0
    
    n "Carissa langsung menghubungi Aksara dan memintanya datang."
    
    show aksara khawatir at left
    show carissa sedih at right
    with dissolve
    
    a "Ada apa lagi? Suaramu kayak ketakutan gitu."
    
    show carissa takut
    
    n "Lalu, Carissa menyeritakan seluruh kejadian singkat tadi saat berada di kafe."
    
    show aksara serius
    with vpunch
    
    a "Bayangan itu..."
    a "(mengepalkan tangan) Dia ngancam kamu?!"
    
    show carissa sedih
    
    c "(mengangguk) Dia bilang... tiga hari lagi aku harus datang ke candi."
    c "Sendirian."
    
    show aksara serius
    
    a "Kamu nggak akan sendirian."
    a "Aku ikut."
    
    show carissa bingung
    
    c "Tapi kalau aku nggak sendirian—"
    
    show aksara normal
    
    a "Aku nggak peduli apa maunya Dewa."
    a "(menatap Carissa) Aku nggak akan biarkan kamu hadapi dia sendirian."
    
    $ aksara_points += 2
    
    show carissa senyum
    
    c "(tersenyum sedih) Oke, Aksara..."
    
    jump scene5_preparation

label scene5_keep_secret:
    scene bg kamar_carissa
    with dissolve
    
    play music audio.tension fadein 2.0
    
    n "Carissa memutuskan untuk tidak memberitahu siapa pun."
    n "Setidaknya... belum."
    
    show carissa sedih at center
    with dissolve
    
    c "(duduk di tepi tempat tidur) Kalau aku bilang ke Aksara..."
    c "Dia pasti ikut. Dan mungkin... dia yang kena bahaya."
    
    show carissa bingung
    
    c "(menatap kalung) Tapi... apa aku kuat sendirian?"
    
    play sound audio.wind
    
    suara "(berbisik lembut) Kamu... cukup kuat..."
    suara "Percaya... pada dirimu sendiri..."
    
    show carissa takut
    with hpunch
    
    c "(menoleh cepat) ?!"
    
    n "Tidak ada siapa-siapa di dalam kamarnya."
    n "Hanya angin malam yang berhembus pelan lewat jendelanya."
    
    show carissa sedih
    
    c "(menghela napas) Aku... harus mikir jernih."
    c "Tiga hari. Aku punya waktu tiga hari."
    
    jump scene5_preparation


label scene5_tell_nenek:
    scene bg ruang_tamu_terang
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Carissa memutuskan untuk bercerita pada Nenek terlebih dulu."
    
    show nenek khawatir at left
    show carissa sedih at right
    with dissolve
    
    c "Nek... tadi aku didatengin satu bayangan."
    c "(menceritakan kejadian)"
    
    show nenek sedih
    
    nenek "(menghela napas berat) Akhirnya... waktunya tiba."
    
    show carissa bingung
    
    c "Nenek... apa yang harus aku lakukan?"
    
    show nenek serius
    
    nenek "Kamu harus cerita ke Aksara, Nduk."
    nenek "Jangan hadapi ini sendirian."
    
    show carissa takut
    
    c "Tapi kalau Aksara ikut... dia yang bahaya—"
    
    show nenek normal
    
    nenek "(menggenggam tangan Carissa) Justru kalau kamu sendirian, itu lebih berbahaya dari apapun."
    nenek "Aksara itu juga Nirantara yang terlatih, setidaknya ada orang yang bisa jagain kamu."
    
    show carissa sedih
    
    c "..."
    
    show nenek senyum
    
    nenek "Percayalah sama orang-orang terdekatmu, Nduk."
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
            
            show nenek sedih
            
            nenek "(menggeleng sedih) Carissa..."
            
            jump scene5_preparation

label scene5_aksara_from_nenek:
    scene black
    with Dissolve(0.5)
    
    n "Carissa menghubungi Aksara dan menceritakan semuanya."
    
    scene bg ruang_tamu_terang
    with dissolve
    
    show aksara serius at left
    show carissa normal at right
    show nenek normal at center 
    with dissolve
    
    a "(datang dengan cepat) Carissa, kamu gapapa kan?"
    
    show carissa sedih
    
    c "Iya... Nenek yang nyaranin aku buat hubungi kamu."
    
    show aksara normal
    
    a "(menatap Nenek) Terima kasih, Nek."
    
    show nenek senyum
    
    nenek "Jaga dia baik-baik, Aksara."
    
    show aksara serius
    
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
    centered "{color=#888}Apakah mereka berdua akan selamat atau justru tidak...?{/color}"
    pause 2.0
    
    jump chapter3_scene6

label chapter3_scene6:
    scene black
    with Dissolve(2.0)
    
    play music audio.tension fadein 3.0
    
    centered "{color=#fff}Candi Reksana Sewu{/color}"
    pause 1.0
    centered "{color=#888}Matahari turun di ufuk barat...{/color}"
    pause 1.5
    
    scene bg candi_gerbang
    with dissolve
    
    play sound audio.wind
    
    n "Langit berwarna jingga kemerahan, pertanda matahari akan segera tenggelam."
    n "Carissa berdiri di depan gerbang candi yang megah."
    
    
    if aksara_points > dewa_points + 3:
        jump scene6_with_aksara
    else:
        jump scene6_alone


label scene6_with_aksara:
    show carissa normal at right
    show aksara serius at left
    with dissolve
    
    a "(mengamati sekeliling) Kamu ngerasa nggak?"
    
    show carissa bingung
    
    c "Ngerasa apa?"
    
    show aksara khawatir
    
    a "Energi di sini... nggak stabil."
    a "Aku ngerasa gerbangnya perlahan-lahan kebuka."
    
    show carissa takut
    
    c "(menggunakan mata batinnya) iya... Nggak beraturan sama sekali."
    
    show aksara normal
    
    a "(menggenggam tangan Carissa) Aku di sini."
    a "Apapun yang terjadi, kita hadapi bareng."
    
    $ aksara_points += 1
    
    show carissa senyum
    
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
        
        c "(menoleh cepat) Siapa?!"
        
        show aksara serius at left
        with easeinleft
        
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
    
    n "Angin tiba-tiba bertiup kencang."
    n "Debu dan dedaunan beterbangan."
    
    show carissa takut
    show aksara serius
    
    play music audio.heartbeat fadein 2.0
    
    n "Gerbang batu di depan mereka mulai bergetar hebat."
    n "Retakan-retakan bercahaya merah muncul di permukaannya."
    
    show carissa kaget
    with vpunch
    
    c "Gerbangnya—!"
    
    show dewa wujud_asli at center
    with flash_red
    
    show aura_merah at center
    with dissolve
    
    play sound audio.magic
    
    n "Sosok tinggi besar muncul dari balik gerbang."
    n "Aura merah gelap menyelimutinya."
    n "Ini bukan lagi Dewa yang ramah di sekolah."
    n "Ini... wujud aslinya."
    
    d "(suara bergema) Carissa... akhirnya kau datang."
    
    show aksara guardian at left
    with flash_blue
    
    n "Aksara langsung berubah wujud menjadi sosok pucat biru kehijauan, aura biru tua menyelimutinya."
    
    a "(berteriak) JANGAN DEKATI DIA!"
    
    d "(tertawa pelan) Penjaga Nirantara... tetap setia seperti biasa."
    d "(menatap Carissa) Tapi aku tidak datang untuk bertarung."
    d "Aku datang... untuk memberikan pilihan, yah anggap saja sebagai kompromi."
    
    show carissa bingung
    
    c "Pilihan...?"
    
    d "Pilihan yang akan menentukan nasib dua dunia."
    d "Kamu secara sukarela mau memberikannya atau tidak."
    d "Kalau tidak mau, maka aku terpaksa ."
    

    
    show dewa sedih
    
    d "Iya. Dan aku memilih... membuka gerbang."
    d "Karena aku percaya... dunia yang menyatu adalah dunia yang lebih baik."
    
    show aksara serius
    
    a "Tapi kamu jadi terjebak! Nggak hidup, nggak mati!"
    
    show dewa misterius
    
    d "Itu konsekuensi yang aku terima."
    d "(menatap Carissa) Tapi kamu... kamu bisa berbeda."
    
    show carissa bingung
    
    c "Berbeda gimana?"
    
    show dewa normal
    
    d "Karena kau lebih kuat dari aku dulu."
    d "Darah Raktamu... murni. Sempurna."
    d "Kau bisa membuka gerbang tanpa harus berkorban."
    
    show aksara kaget
    with vpunch
    
    a "Itu bohong!"
    
    show dewa serius
    
    d "(mengabaikan Aksara) Carissa, lihat di sekelilingmu."
    d "Manusia takut pada roh. Roh dendam pada manusia."
    d "Tapi bayangkan... dunia tanpa sekat."
    d "Dunia di mana kedua ras bisa saling memahami."
    d "Bukankah itu indah?"
    
    # PILIHAN MULAI MUNCUL - Dewa memanipulasi
    show carissa sedih
    
    c "(ragu) Tapi... kata Aksara dan Nenek—"
    
    show dewa misterius
    
    d "Mereka takut kehilangan kekuasaan."
    d "Nirantara selama ini jadi 'penjaga'. Mereka punya status karena itu."
    d "Kalau gerbang terbuka... mereka tidak relevan lagi."
    
    show aksara marah
    with vpunch
    
    a "ITU NGGAK BENAR!"
    a "(menatap Carissa) Carissa, jangan dengerin dia!"
    
    # CRITICAL CHOICE POINT - First indication
    menu:
        "Apa yang Carissa rasakan?"
        
        "Aku percaya Aksara":
            $ aksara_points += 3
            
            show carissa normal
            
            c "(menggeleng) Nggak. Aksara nggak kayak itu."
            c "Dia... tulus peduli sama aku."
            
            show dewa sedih
            
            d "Naif..."
            
        "Aku... bingung":
            show carissa bingung
            
            c "Aku... aku nggak tau harus percaya siapa."
            
            show dewa senyum
            
            d "Maka biarkan hatimu yang memilih."
            
        "Mungkin Dewa ada benarnya":
            $ dewa_points += 2
            
            show carissa sedih
            
            c "Mungkin... memang ada yang disembunyiin dari aku?"
            
            show aksara sedih
            
            a "(terluka) Carissa..."
            
            show dewa senyum
            
            d "(tersenyum) Lihat? Kau mulai paham."
    
    # GERBANG MULAI TERBUKA LEBIH LEBAR
    play sound audio.magic
    with hpunch
    
    n "Gerbang bergetar lebih hebat."
    n "Cahaya merah menyembur dari retakan."
    
    show dewa serius
    
    d "Waktunya hampir tiba, Carissa."
    d "Kau harus memilih SEKARANG."
    
    # PILIHAN TERAKHIR PREPARATION
    show carissa takut
    
    c "Aku harus... memilih?"
    
    show dewa normal
    
    d "Iya. Tiga pilihan."
    
    # DEWA MENJELASKAN 3 PILIHAN
    show dewa serius
    
    d "PERTAMA: Bantu aku buka gerbang sepenuhnya."
    d "Dunia baru akan tercipta. Manusia dan roh menyatu."
    
    show dewa normal
    
    d "KEDUA: Tutup gerbang dengan darahmu."
    d "Dunia kembali seperti dulu. Tapi kau kehilangan kekuatanmu."
    
    show dewa misterius
    
    d "KETIGA: Tidak pilih apapun."
    d "Biarkan gerbang tetap setengah terbuka seperti sekarang."
    d "Tapi itu artinya... aku dan roh lain akan terus mengganggumu selamanya."
    
    show aksara serius
    
    a "Carissa, dengerin aku—"
    
    show dewa marah
    with flash_red
    
    d "(mengangkat tangan) DIAM, PENJAGA!"
    
    play sound audio.magic
    
    # AKSARA TERDORONG
    show aksara khawatir at left
    with hpunch
    
    n "Aksara terdorong oleh kekuatan Dewa."
    
    show carissa kaget
    with vpunch
    
    c "AKSARA!"
    
    show dewa serius
    
    d "Ini keputusan CARISSA. Bukan kamu."
    d "(menatap Carissa) Jadi... apa pilihanmu?"
    
    jump scene6_final_choice

# ================================================
# FINAL CHOICE - Menentukan Ending
# ================================================

label scene6_final_choice:
    scene bg candi_gerbang
    with dissolve
    
    show carissa sedih at center
    with dissolve
    
    n "Carissa berdiri sendirian di tengah."
    n "Di sebelah kirinya, Aksara yang terluka."
    n "Di depannya, Dewa yang menunggu jawaban."
    n "Keputusan terberat dalam hidupnya."
    
    # SHOW CURRENT POINTS (optional, for debugging)
    # "Aksara points: [aksara_points], Dewa points: [dewa_points]"
    
    play music audio.heartbeat fadein 2.0
    
    centered "{color=#fff}PILIHAN TERAKHIR{/color}"
    pause 2.0
    
    menu:
        "Apa yang Carissa pilih?"
        
        "Percaya Aksara - Tutup gerbang":
            jump ending_good
        
        "Percaya Dewa - Buka gerbang":
            jump ending_bad
        
        "Tolak keduanya - Jalan sendiri":
            jump ending_neutral

# ================================================
# GOOD ENDING - Trust Aksara, Close Gate
# ================================================

label ending_good:
    $ aksara_points += 5
    
    scene bg candi_gerbang
    with dissolve
    
    show carissa serius at center
    with dissolve
    
    c "(berteriak) AKU PILIH TUTUP GERBANG!"
    
    show dewa marah at right
    with dissolve
    
    d "(marah) APA?!"
    
    show aksara senyum at left
    with dissolve
    
    a "(tersenyum lega) Carissa..."
    
    show carissa normal
    
    c "(menatap Dewa) Maaf, Dewa. Aku ngerti kamu pengen dunia yang lebih baik."
    c "Tapi... aku percaya sama Aksara."
    c "Percaya sama orang-orang yang udah jaga aku selama ini."
    
    show dewa sedih
    
    d "Kau... membuang kesempatan ini?"
    
    show carissa senyum
    
    c "Bukan membuang. Tapi memilih jalan yang lebih aman."
    c "Dunia emang nggak sempurna. Tapi itu bukan alasan buat maksa perubahan."
    
    show dewa serius
    
    d "(menghela napas) Baiklah..."
    d "Kalau itu pilihanmu."
    
    # RITUAL PENUTUPAN GERBANG
    show carissa normal
    
    c "(menatap Aksara) Aku... harus gimana?"
    
    show aksara normal
    
    a "(mendekat) Kamu perlu alirkan darahmu ke gerbang."
    a "(menggenggam tangan Carissa) Aku akan bantu stabilkan energimu."
    
    show carissa sedih
    
    c "Aku... bakal kehilangan kekuatanku kan?"
    
    show aksara khawatir
    
    a "(mengangguk) Iya. Kamu nggak bisa liat roh lagi."
    
    show carissa senyum
    
    c "(tersenyum) Gapapa. Aku udah cukup capek liat mereka."
    
    # PROSES RITUAL
    play sound audio.magic
    
    show kalung_glow at center
    with flash_blue
    
    n "Carissa menyentuh gerbang dengan tangan kanannya."
    n "Darah dari luka kecil di telapaknya mengalir."
    
    show aura_biru at center
    with flash_blue
    
    n "Aksara menyalurkan energinya, membantu Carissa."
    n "Cahaya biru dan merah bercampur, membentuk segel baru."
    
    show dewa wujud_asli at right
    
    d "(menatap dengan sedih) Sampai jumpa... Carissa."
    
    hide dewa wujud_asli
    with flash_white
    
    play sound audio.wind
    
    n "Dewa perlahan menghilang, tersedot kembali ke dalam gerbang."
    
    # GERBANG TERTUTUP
    play sound audio.magic
    with flash_white
    
    hide kalung_glow
    hide aura_biru
    with dissolve
    
    n "Gerbang tertutup rapat."
    n "Retakan-retakan hilang."
    n "Kegelapan lenyap."
    
    # CARISSA COLLAPSE
    show carissa sedih at center
    
    n "Carissa merasakan tubuhnya melemah."
    n "Kekuatannya... hilang."
    
    show aksara khawatir at left
    
    a "(menangkap Carissa) Carissa!"
    
    show carissa senyum
    
    c "(tersenyum lemah) Aku... gapapa."
    c "Aku cuma... lelah."
    
    show aksara senyum
    
    a "(memeluk Carissa) Kamu hebat. Kamu udah selamatin semua orang."
    
    # EPILOG - Good Ending
    scene black
    with Dissolve(2.0)
    
    centered "{color=#0f0}★ GOOD ENDING ★{/color}"
    pause 1.5
    centered "{color=#fff}KEPERCAYAAN YANG KUAT{/color}"
    pause 2.0
    
    scene bg halaman_sekolah
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Beberapa minggu kemudian..."
    n "Carissa kembali ke kehidupan normalnya."
    n "Ia tidak bisa melihat roh lagi."
    n "Tapi... ia bahagia."
    
    show carissa senyum at right
    show aksara senyum at left
    with dissolve
    
    a "Gimana rasanya jadi manusia normal?"
    
    show carissa normal
    
    c "(tertawa) Enak juga. Nggak ada yang nakutin lagi."
    
    show aksara normal
    
    a "Kamu nggak nyesel?"
    
    show carissa senyum
    
    c "(menggeleng) Nggak. Aku pilih kehidupan yang tenang."
    c "(menatap Aksara) Dan... punya teman yang selalu ada."
    
    show aksara senyum
    
    a "(tersenyum) Aku akan selalu ada buat kamu."
    
    show nenek senyum at center behind aksara
    with dissolve
    
    nenek "Carissa! Ayo pulang, Nenek masak rendang kesukaan kamu!"
    
    show carissa senyum
    
    c "(berlari) Aku datang, Nek!"
    
    n "Dunia kembali seimbang."
    n "Dan Carissa... akhirnya bisa hidup tanpa beban."
    
    scene black
    with Dissolve(2.0)
    
    centered "{color=#fff}TAMAT{/color}"
    pause 2.0
    centered "{color=#888}Terima kasih telah bermain{/color}"
    pause 2.0
    
    return

# ================================================
# BAD ENDING - Trust Dewa, Open Gate
# ================================================

label ending_bad:
    $ dewa_points += 5
    
    scene bg candi_gerbang
    with dissolve
    
    show carissa serius at center
    with dissolve
    
    c "(berteriak) AKU... AKU PILIH BUKA GERBANG!"
    
    show aksara kaget at left
    with vpunch
    
    a "CARISSA, JANGAN!"
    
    show dewa senyum at right
    with dissolve
    
    d "(tersenyum lebar) Pilihan yang bijak."
    
    show carissa sedih
    
    c "(menatap Aksara) Maafin aku, Aksara..."
    c "Tapi aku percaya... ini jalan yang lebih baik."
    
    show aksara sedih
    
    a "(menangis) Carissa... kamu nggak tau apa yang kamu lakukan!"
    
    show dewa normal
    
    d "Tenang, Penjaga. Dunia baru akan indah."
    d "(menatap Carissa) Sekarang... alirkan darahmu ke gerbang."
    
    # RITUAL PEMBUKAAN GERBANG
    play sound audio.magic
    
    show kalung_glow at center
    with flash_red
    
    n "Carissa menyentuh gerbang dengan tangannya."
    n "Darahnya mengalir... tapi bukan untuk menutup."
    n "Untuk MEMBUKA."
    
    show aura_merah at center
    with flash_red
    
    play sound audio.heartbeat
    
    n "Gerbang bergetar hebat."
    n "Retakan melebar."
    n "Cahaya merah menyilaukan."
    
    # GERBANG TERBUKA PENUH
    with flash_red
    with hpunch
    
    n "GERBANG TERBUKA SEPENUHNYA!"
    
    show dewa wujud_asli at right
    
    d "(tertawa) AKHIRNYA! SETELAH 200 TAHUN!"
    
    # ROH-ROH KELUAR
    show hantu strong at center
    show bayangan at left
    with dissolve
    
    play sound audio.wind
    
    n "Ribuan roh keluar dari gerbang."
    n "Memenuhi dunia manusia."
    
    show aksara guardian at left
    
    a "(berteriak) CARISSA! APA YANG KAMU LAKUKAN?!"
    
    # CARISSA MULAI BERUBAH
    show carissa takut at center
    
    c "(merasakan tubuhnya) A-apa ini?"
    c "Tubuhku... kenapa... terasa aneh?"
    
    show dewa serius
    
    d "Itu konsekuensinya, Carissa."
    d "Kau telah membuka gerbang."
    d "Sekarang... kau terikat dengannya."
    
    show carissa sedih
    
    c "M-maksudnya?"
    
    show dewa misterius
    
    d "Kau tidak bisa mati. Tapi juga tidak sepenuhnya hidup."
    d "Seperti aku. Terjebak di antara dua dunia."
    
    show carissa kaget
    with vpunch
    
    c "NGGAK! KAMU BILANG AKU NGGAK AKAN BERKORBAN!"
    
    show dewa sedih
    
    d "Aku bilang kau tidak akan mati. Dan itu benar."
    d "Tapi... ada harga untuk kekuatan ini."
    
    # AKSARA MENCOBA SELAMATKAN
    show aksara serius
    
    a "(berlari ke Carissa) CARISSA!"
    
    show aura_merah at right
    with flash_red
    
    d "(menghalangi) Sudah terlambat, Penjaga."
    
    show aksara marah
    
    a "AKU NGGAK PEDULI! AKU AKAN SELAMATKAN DIA!"
    
    # BATTLE (implied, tidak full battle scene)
    play sound audio.magic
    with flash_blue
    with flash_red
    
    n "Aksara mencoba melawan Dewa."
    n "Tapi kekuatan Dewa terlalu besar."
    
    show aksara khawatir
    with hpunch
    
    n "Aksara terpental."
    
    show carissa sedih
    
    c "(menangis) AKSARA!"
    
    # EPILOG - Bad Ending
    scene black
    with Dissolve(2.0)
    
    centered "{color=#f00}★ BAD ENDING ★{/color}"
    pause 1.5
    centered "{color=#fff}DUNIA YANG KACAU{/color}"
    pause 2.0
    
    scene bg jalan_kota
    with dissolve
    
    play music audio.tension fadein 2.0
    
    n "Dunia berubah selamanya."
    n "Manusia dan roh hidup berdampingan."
    n "Tapi bukan dalam harmoni."
    
    n "Yang takut menjadi paranoid."
    n "Yang dendam mencari pembalasan."
    n "Chaos di mana-mana."
    
    show carissa sedih at center
    with dissolve
    
    n "Carissa hidup sebagai Penjaga Gerbang."
    n "Terjebak. Tidak bisa mati. Tidak sepenuhnya hidup."
    n "Ia menyesal... tapi sudah terlambat."
    
    c "(berbisik) Maafin aku... Aksara... Nenek..."
    c "Aku... salah pilih."
    
    scene black
    with Dissolve(2.0)
    
    centered "{color=#fff}TAMAT{/color}"
    pause 2.0
    centered "{color=#888}Pilihan memiliki konsekuensi...{/color}"
    pause 2.0
    
    return

# ================================================
# NEUTRAL ENDING - Solo Path, Both Disappear
# ================================================

label ending_neutral:
    scene bg candi_gerbang
    with dissolve
    
    show carissa serius at center
    with dissolve
    
    c "(berteriak) AKU NGGAK MAU PILIH KALIAN BERDUA!"
    
    show aksara kaget at left
    show dewa kaget at right
    with dissolve
    
    a "Carissa?!"
    d "Apa maksudmu?!"
    
    show carissa normal
    
    c "Aku... aku akan cari jalan sendiri!"
    c "Jalan yang nggak harus ngorbanin siapapun!"
    
    show dewa serius
    
    d "Itu mustahil!"
    
    show aksara khawatir
    
    a "Carissa, itu berbahaya!"
    
    show carissa serius
    
    c "Aku nggak peduli!"
    c "Ini tubuhku! Ini darahku!"
    c "AKU YANG TENTUIN!"
    
    # CARISSA MENGAMBIL JALAN SENDIRI
    play sound audio.magic
    
    show kalung_glow at center
    with flash_blue
    
    n "Carissa menyentuh gerbang dengan kedua tangannya."
    n "Ia mencoba... menutup gerbang TANPA pengorbanan penuh."
    
    show aura_biru at center
    show aura_merah at center
    with dissolve
    
    n "Energi biru dan merah bercampur secara chaos."
    n "Tidak stabil. Berbahaya."
    
    show aksara serius
    
    a "CARISSA! ENERGINYA TERLALU KUAT!"
    
    show dewa marah
    
    d "DIA AKAN MELEDAK!"
    
    # KEDUANYA MENCOBA BANTU
    show aksara guardian at left
    with flash_blue
    
    a "(berlari) AKU AKAN BANTU STABILKAN!"
    
    show dewa wujud_asli at right
    with flash_red
    
    d "(terpaksa) ...Aku juga."
    
    # LEDAKAN ENERGI
    play sound audio.magic
    with flash_white
    with hpunch
    
    scene white
    
    n "Energi meledak!"
    n "Cahaya putih menyilaukan!"
    
    scene black
    with Dissolve(2.0)
    
    # AFTERMATH
    scene bg candi_gerbang
    with dissolve
    
    play music audio.mystery_theme fadein 2.0
    
    n "Ketika asap menghilang..."
    n "Gerbang tertutup."
    n "Tapi..."
    
    show nenek sedih at center
    with dissolve
    
    nenek "(melihat sekeliling) Carissa? CARISSA?!"
    
    n "Carissa menghilang."
    n "Aksara... juga menghilang."
    n "Bahkan Dewa... lenyap."
    
    show nenek khawatir
    
    nenek "(menangis) Carissa... kemana kamu, Nduk?"
    
    
    scene
return   