# Deklarasi gambar
image bg_school_gate = "images/School_gate.jpg"
image bg_corridor = "images/Corridor.jpg"
image bg_classroom = "images/Classroom.jpg"
image bg_courtyard = "images/Courtyard.jpg"
image bg_street_evening = "images/Street_evening.jpg"

# Karakter sprites
image anya normal = "images/anya_normal.png"
image anya shocked = "images/anya_shocked.png"
image anya scared = "images/anya_scared.png"
image anya shy = "images/anya_shy.png"
image anya confused = "images/anya_confused.png"
image anya relieved = "images/anya_relieved.png"

image ayamoto normal = "images/ayamoto_normal.png"
image ayamoto smile = "images/ayamoto_smile.png"
image ayamoto serious = "images/ayamoto_serious.png"
image ayamoto mysterious = "images/ayamoto_mysterious.png"

image shadow_figure = "images/shadow_figure.png"
image ghost = "images/Ghost.png"

# Definisi karakter
define a = Character("Anya", color="#FF69B4")
define ay = Character("Ayamoto", color="#4169E1")
define unknown = Character("???", color="#8B0000")
define n = Character("Narator", color="#FFFFFF")

# Variabel kedekatan
default ayamoto_points = 0
default trust_level = 0

# Chapter 1: Bayangan Pertama
label start:
    
    # Prolog - Suara Misterius
    scene black
    with fade
    
    play sound "audio/whisper_dark.mp3" fadein 2.0
    
    unknown "Dunia ini... berutang padaku."
    
    unknown "Mereka mencuri hidupku, mencuri masa depanku, dan meninggalkanku terkubur dalam dendam."
    
    unknown "Aku tidak akan pernah tenang... sampai kutagih balasan itu selamanya."
    
    scene black
    with fade
    
    # Scene 1: Gerbang Sekolah Pagi
    scene bg_school_gate
    with fade
    
    play music "audio/school_morning.mp3" fadein 2.0
    
    n "Pagi itu terasa biasa saja bagi siswa lain di Sekolah Nakama Semarang."
    
    n "Tapi tidak untuk Anya, siswi SMA yang polos dan sederhana."
    
    show anya normal at center
    with dissolve
    
    a "Hari ini juga harus berangkat sekolah... semoga hari ini tidak ada kejadian aneh lagi."
    
    # Munculnya bayangan
    play sound "audio/ghost_whisper.mp3"
    
    show ghost at right
    with vpunch
    
    show anya shocked at center
    with hpunch
    
    a "KYAAAA! Ada lagi!"

    hide ghost
    with dissolve
    
    # Monolog internal Anya
    a "{i}Kenapa sih aku harus bisa lihat beginian? Baru masuk gerbang aja udah ada makhluk pucat berdiri sambil melototin aku!{/i}"
    
    a "{i}Ya Tuhan, kenapa bukan cowok ganteng aja yang nongol?!{/i}"
    
    show anya scared at center
    with dissolve
    
    # Anya berlari ketakutan
    show anya scared at left
    with move
    
    a "Hhhh... huhhh... udah ga ada lagi kan? Serem banget!"
    
    # Hembusan angin misterius
    play sound "audio/wind_whisper.mp3"
    
    unknown "Huhhh..."
    
    show anya shocked at left
    with vpunch
    
    # Kemunculan Ayamoto
    show ayamoto smile at right
    with easeinright
    
    ay "Anya... kamu lagi ngapain?"
    
    show anya shocked at left
    with hpunch
    
    a "AKHHHH!!! Ayamoto! Kamu ngagetin, tau nggak jantungku hampir copot!"
    
    show ayamoto normal at right
    with dissolve
    
    ay "Lagian kenapa pagi-pagi udah ngos-ngosan? Kayak liat setan aja."
    
    show anya confused at left
    with dissolve
    
    a "Nggak! Sereman Ayamoto daripada setan. Tadi aku lagi olahraga aja."
    
    show ayamoto mysterious at right
    with dissolve
    
    ay "Yakin, cuma olahraga?"
    
    show anya nervous at left
    with dissolve
    
    a "Maksud Ayamoto apa?"
    
    show ayamoto normal at right
    with dissolve
    
    ay "Bel udah bunyi. Ayo ke kelas."
    
    # Scene 2: Koridor Sekolah
    scene bg_corridor
    with fade
    
    show anya normal at right
    show ayamoto serious at left
    with dissolve
    
    ay "Beberapa hari belakangan ini tingkahmu keliatan aneh."
    
    show anya confused at right
    with dissolve
    
    # Pilihan penting untuk kedekatan
    menu:
        "Apa yang akan Anya lakukan?"
        
        "Ceritakan semuanya tentang kemampuan melihat hantu":
            jump tell_truth
            
        "Tidak menjawab dan tetap menyembunyikan":
            jump stay_silent

# Cabang: Menceritakan Kebenaran (+kedekatan)
label tell_truth:
    
    $ ayamoto_points += 2
    $ trust_level += 1
    
    show anya shy at right
    with dissolve
    
    a "Sebenernya... Aku nggak tahu harus cerita sama siapa."
    
    a "Tapi, kalau aku cerita ke kamu... Jangan anggap aku aneh ya."
    
    show ayamoto smile at left
    with dissolve
    
    ay "Aku janji. Aku nggak akan ngetawain, Anya. Kamu bisa percaya sama aku."
    
    show anya normal at right
    with dissolve
    
    a "Beberapa hari terakhir... Aku sering lihat hal-hal aneh."
    
    a "Kayak bayangan hitam yang tiba-tiba seliweran cepat, bisikan-bisikan minta tolong di telinga, sampe ada sosok pucat yang suka melototin aku dari jauh!"
    
    a "Awalnya kukira aku cuma halu aja, tapi... Makin lama makin nggak karuan."
    
    # Ayamoto menunjukkan reaksi misterius
    show ayamoto serious at left
    with dissolve
    
    ay "Jadi... Kamu bisa melihat mereka? Hantu atau apalah itu?"
    
    show anya shocked at right
    with vpunch
    
    a "Hah? I-iya. Kamu... Percaya sama ceritaku?"
    
    show ayamoto mysterious at left
    with dissolve
    
    ay "Jelas aku percaya. Dari awal aku ngerasa ada hal yang berbeda darimu."
    
    show anya relieved at right
    with dissolve
    
    a "{i}Dia... beneran percaya sama aku? Nggak kayak orang lain yang mungkin bakal mikir aku gendeng ya.{/i}"
    
    a "{i}Kenapa rasanya... aku malah kayak nyaman ya sama Ayamoto? Ah nggak mungkin ini!{/i}"
    
    show ayamoto smile at left
    with easeinleft
    
    ay "Dengerin aku, Anya. Kamu nggak sendirian."
    
    ay "Mulai sekarang, kalau kamu lihat atau denger sesuatu yang serem... Jangan dipendem sendiri."
    
    ay "Cari aku ya. Aku bakalan ada di sisimu."
    
    show anya shy at right
    with dissolve
    
    a "Ayamoto... kenapa kamu keliatan peduli banget sama aku?"
    
    show ayamoto mysterious at left
    with dissolve
    
    ay "Karena aku nggak mau kamu merasa sendirian, kayak aku yang dulu..."
    
    ay "Dunia ini terlalu kejam, Anya. Kamu butuh seseorang... Yang bisa melindungimu."
    
    jump after_choice

# Cabang: Tetap Diam (-kedekatan)
label stay_silent:
    
    $ ayamoto_points -= 1
    $ trust_level -= 1
    
    show anya normal at right
    with dissolve
    
    a "{i}Aku nggak bisa bilang ke dia... kalau aku cerita, bisa aja dia mikir aku gendeng.{/i}"
    
    a "{i}Aku harus diem aja.{/i}"
    
    a "Nggak gitu... Aku cuma... Nggak apa-apa kok intinya."
    
    show ayamoto serious at left
    with dissolve
    
    ay "Beneran? Atau cuma kamu yang nggak percaya sama aku?"
    
    show anya confused at right
    with dissolve
    
    a "Maksudku... Ya, akhir-akhir ini aku lagi kecapekan aja. Abis banyak tugas sih"

    a "Lagian peduli amat sih? Kan kita nggak deket-deket amat heheheh"
    
    show ayamoto mysterious at left
    with dissolve
    
    ay "Hmmm... Okelah, bener juga omonganmu."
    
    show anya scared at right
    with dissolve
    
    a "{i}Kenapa tatapannya kayak gitu? Rasanya kayak dia tahu kalau aku nyembunyiin sesuatu.{/i}"
    
    a "{i}Tapi aku nggak bisa cerita... aku takut.{/i}"
    
    jump after_choice

# Scene 3: Setelah Pilihan - Menuju Kelas
label after_choice:
    
    hide anya
    hide ayamoto
    with dissolve
    

    if ayamoto_points >= 2:
        n "Setelah percakapan tadi, Anya merasa sedikit lebih lega."
        n "Akhirnya ada seseorang yang mengerti apa yang dialaminya."
    else:
        n "Meskipun masih menyimpan rahasianya, Anya tidak bisa mengabaikan tatapan tajam Ayamoto."
        n "Sepertinya Ayamoto tahu ada sesuatu yang disembunyikan walau Anya tak tahu alasannya."
    
    n "Mereka berdua berjalan menuju kelas dalam keheningan."
    
    scene bg_classroom
    with fade
    
    play music "audio/classroom_ambient.mp3" fadein 2.0
    
    show anya normal at right
    show ayamoto normal at left
    with dissolve
    

    if ayamoto_points >= 2:
        ay "Anya, duduk sebelahku aja ya? Tuh ada di belakang sana."
        
        show anya shy at right
        with dissolve
        
        a "I-iya."
    else:
        ay "Kita duduk di mana hari ini?"
        
        show anya normal at right
        with dissolve
        
        a "Te-terserah aja... Yang penting nggak terlalu depan."
        
        ay "Hmm, oke."
    
    hide ayamoto
    with dissolve

    hide anya
    with dissolve
    
    n "Pelajaran pun dimulai, tapi pikiran Anya sulit fokus."
    
    show anya confused at center
    with move
    
    if ayamoto_points >= 2:
        a "{i}Rasanya lega bisa cerita sama Ayamoto... Tapi kok dia bisa tahu duluan ya?{/i}"
        a "{i}Dan kenapa dia bilang 'mereka'? Emangnya Ayamoto bisa liat juga kayak aku?{/i}"
    else:
        a "{i}Kenapa tadi Ayamoto natapnya kayak gitu? Iiihh, serem banget...{/i}"
       
    # Munculnya bayangan di kelas - dengan timing yang lebih natural
    n "Tiba-tiba, ruangan terasa dingin."
    
    show shadow_figure at right
    with fade
    
    show anya scared at center
    with dissolve
    
    a "{i}Ih... Dingin banget. Kenapa AC-nya kenceng banget sih?{/i}"
    
    # Bayangan berbisik - lebih subtle
    play sound "audio/whisper_soft.mp3" volume 0.3
    
    unknown "Anya..."
    
    show anya shocked at center
    with vpunch
    
    a "{i}Hah? Ada yang manggil nama aku?{/i}"
    
    # Anya menoleh ke sekitar
    show anya confused at center
    with dissolve
    
    a "{i}Yang lain pada fokus sama pelajaran... Berarti cuma aku yang denger?{/i}"
    
    unknown "Kamu tidak bisa mengabaikan kami selamanya..."
    
    show anya normal at center
    with hpunch
    
    a "{i}Suara itu lagi! Lebih jelas dari sebelumnya...{/i}"
    

    show ayamoto mysterious at left
    with easeinleft
    
    if ayamoto_points >= 2:
        ay "{i}Dia ketakutan lagi... Pasti 'mereka' mulai mendekatinya.{/i}"
    else:
        ay "{i}Ekspresi wajahnya... Kayak liat sesuatu yang nggak normal.{/i}"
        ay "{i}Menarik...{/i}"
    
    hide shadow_figure
    with dissolve
    
    # Scene 4: Istirahat di Halaman Sekolah
    scene bg_courtyard
    with fade
    
    n "Bel istirahat berbunyi. Anya memutuskan untuk keluar kelas yang butuh udara segar."
    
    show anya normal at center
    with dissolve
    
    if ayamoto_points >= 2:
        a "{i}Setelah kejadian di kelas tadi... Mungkin aku butuh ngobrol sama Ayamoto.{/i}"
        a "{i}Dia bilang aku bisa cerita kalau ada apa-apa.{/i}"
    else:
        a "{i}Mudah-mudahan di halaman ini aku bisa tenang bentar...{/i}"
    
    
    if ayamoto_points >= 2:
        show ayamoto normal at right
        with easeinright
        
        ay "Anya! Aku cari kamu ke mana-mana."
        
        show anya surprised at center
        with dissolve
        
        a "Ayamoto? Kenapa nyari aku?"
        
        show ayamoto serious at right
        with dissolve
        
        ay "Tadi di kelas aku lihat mukamu pucat banget. Ada apa lagi?"
        
        show anya shy at center
        with dissolve
        
        a "Kamu... Merhatiin aku terus ya?"
        
        ay "Y-ya sih. Kan udah janji mau jaga kamu."
        
        show anya relieved at center
        with dissolve
        
        a "Tadi... Di kelas ada suara yang manggil nama aku lagi."
        a "Bahkan bilang aku nggak bisa mengabaikan mereka selamanya."
        
        show ayamoto mysterious at right
        with dissolve
        
        ay "Kayaknya mereka mulai serius ya..."
        
        show anya scared at center
        with vpunch
        
        a "Serius gimana? Kamu tahu sesuatu?"
        
        ay "Aku... Pernah denger cerita tentang orang-orang kayak kamu."
        ay "Yang bisa lihat 'mereka' biasanya punya hubungan khusus dengan dunia lain."
        
        show anya confused at center
        with dissolve
        
        a "Hubungan khusus? Aku nggak pernah ngapa-ngapain ke makhluk halus!"
        
        ay "Belum tentu kamu yang ngapa-ngapain. Bisa jadi... Mereka yang butuh sesuatu dari kamu."
        
    else:
        n "Anya baru duduk di bangku taman ketika..."
        
        show ayamoto normal at right
        with easeinright
        
        ay "Wah, ternyata di sini. Sendirian lagi?"
        
        show anya normal at center
        with dissolve
        
        a "Ayamoto... kamu nggak jajan di kantin?"
        
        ay "Kantin lagi rame. Aku sih lebih suka tempat sepi."
        
        show ayamoto mysterious at right
        with dissolve
        
        ay "Lagian... Kamu keliatan butuh teman ngobrol. Betul ga nih?"
        
        show anya confused at center
        with dissolve
        
        a "Maksud kamu?"
        
        ay "Tadi di kelas mukamu aneh. Kayak gitu lah, ga kayak orang normal."
        
        show anya scared at center
        with dissolve
        
        a "{i}Dia... ngeh juga ternyata. Gimana nih?{/i}"
        
        a "A-aneh gimana? Aku biasa aja kok."
        
        show ayamoto smile at right
        with dissolve
        
        ay "Hmm... Ya udah kalau kamu nggak mau cerita."
        ay "Tapi inget, kadang nyimpen rahasia sendirian itu lebih susah loh."
        
        show anya confused at center
        with dissolve
        
        a "Kamu... Kenapa kayak sok tahu ada sesuatu sih?"
        
        ay "Entah, feeling aja. Aku orangnya paham sama hal-hal begituan."
    
    # Scene 5: Pulang Sekolah 
    scene bg_street_evening
    with fade
    
    play music "audio/evening_ambient.mp3" fadein 2.0
    
    n "Sore hari, bel pulang sekolah berbunyi."
    
    # Situasi berbeda berdasarkan trust level
    if ayamoto_points >= 2:
        n "Setelah percakapan di halaman tadi, Anya merasa lebih dekat dengan Ayamoto."
        n "Meski masih bingung dengan beberapa hal yang dia katakan."
        
        show anya normal at left
        show ayamoto normal at right
        with dissolve
        
        ay "Anya, mau pulang bareng? Kebetulan searah."
        
        show anya shy at left
        with dissolve
        
        a "Ehhh... Iya boleh, makasih ya."
        

        n "Mereka berdua menaiki motor Ayamoto menyusuri jalan-jalan menuju rumah."
        
        ay "Ngomong-ngomong, dari kapan sih kamu mulai bisa lihat 'mereka'?"
        
        show anya confused at left
        with dissolve
        
        a "Baru beberapa hari ini... Sekitar seminggu yang lalu kali ya?"
        a "Tiba-tiba aja gitu. Awalnya cuma bayangan samar, tapi makin hari makin jelas."
        
        show ayamoto mysterious at right
        with dissolve
        
        ay "Hmm... Ada kejadian khusus nggak sekitar waktu itu?"
        
        show anya normal at left
        with dissolve
        
        a "Kejadian khusus? Nggak ada sih... Kayak hari-hari biasa aja kok."
        
        ay "Aneh juga ya... Biasanya kemampuan kayak gini muncul karena ada trigger sih."
        
        show anya surprised at left
        with vpunch
        
        a "Trigger? Kamu kok lagi-lai ngerti banget sih tentang hal beginian?"
        
        show ayamoto smile at right
        with dissolve
        
        ay "Aku suka baca-baca tentang hal mistis gitu. Ini mah hobi aja."
        ay "Makanya pas kamu cerita, aku langsung percaya."
        
        show anya relieved at left
        with dissolve
        
        a "Syukur deh... Aku takut kamu bakal anggap aku aneh."
        
        ay "Justru aku kagum. Nggak semua orang punya kemampuan kayak gitu."
        
        show anya confused at left
        with dissolve
        
        a "Kemampuan? Ini mah lebih kayak kutukan..."
        
        show ayamoto serious at right
        with dissolve
        
        ay "Belum tentu. Mungkin ini berkah yang belum kamu sadari."
        
        n "Ucapan Ayamoto membuat Anya berpikir."
        n "Ada sesuatu dalam cara dia bicara yang membuat hatinya tenang..."
        n "Sekaligus gelisah."
        
    else:
        n "Meskipun masih menyimpan rahasianya, Anya tidak bisa menghilangkan perasaan bahwa Ayamoto tahu lebih dari yang dia tunjukkan."
        
        show anya normal at center
        with dissolve
        
        n "Anya berjalan keluar gerbang sekolah sendirian."
        n "Dia sengaja menghindari Ayamoto yang sepertinya ingin mengajaknya pulang bersama."
        
        a "{i}Aku harus hati-hati... dia terlalu banyak tanya tentang hal-hal aneh.{/i}"
        
        
        show ayamoto mysterious at right
        with easeinright
        
        ay "{i}Masih nggak mau terbuka ya...{/i}"
        ay "{i}Tapi nggak apa-apa. Aku masih ada banyak waktu.{/i}"
        
        n "Ayamoto tersenyum tipis sambil memperhatikan Anya yang semakin menjauh."
        
        ay "{i}Cepat atau lambat, kamu akan butuh aku, Anya.{/i}"
        ay "{i}Dan saat itu tiba... Aku yakin kamu nggak bakalan kabur lagi.{/i}"
    

    scene black
    with fade
    
    if ayamoto_points >= 2:
        n "Anya merasa beruntung menemukan seseorang yang mengerti kondisinya."
        n "Tapi di balik rasa syukur itu, ada pertanyaan yang terus mengganggu pikirannya..."
        n "Kenapa Ayamoto begitu tahu banyak tentang hal-hal supernatural?"
        n "Dan apa maksudnya dengan 'berkah yang belum disadari'?"
    else:
        n "Meski memilih untuk berjaga-jaga, Anya tidak bisa mengabaikan fakta bahwa Ayamoto sepertinya tahu sesuatu tentang kondisinya."
        n "Pertanyaannya adalah... Apakah dia bisa dipercaya?"
        n "Atau justru harus diberi jarak?"
    
    centered "{color=#FF0000}Apapun pilihannya...{/color}"
    centered "{color=#FF0000}Takdir Anya sudah mulai berputar.{/color}"
    centered "{color=#FF0000}Bersambung ke Chapter 2...{/color}"
    
    return

# Label chapter 2
label chapter2:
    pass