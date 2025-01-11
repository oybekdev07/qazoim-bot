# main texts
faq_main_text = """
Namozni qazo qilib qo‘ysam, qanday qilishim kerak?
Namozni vaqtida o‘qishdan ko‘ra, qazo qilib o‘qishning hukmi qanday?
Qazo namozlari uchun tartib kerakmi?
Namozning qazo bo‘lishiga qanday sabablar bor?
Bir kunda bir necha qazo namozini o‘qisam bo‘ladimi?
Qazo namozini o‘qish uchun maxsus duolar bormi?
"""

forget_prayer_text = """
Qazo namozlari haqida ma'lumot:
Qazo namozlarini tartib bilan o‘qish tavsiya etiladi.
Har kuni ma'lum vaqt ajratib, qazo namozlarini to‘kib tashlash mumkin.
Agar qazo namozlarining aniq sanog‘i noma'lum bo‘lsa, taxminiy sanog‘ni aniqlab, shunga qarab davom eting.
"""

main_text = """
Assalomu alaykum! {name}
Bu bot sizning namoz qazolaringizni doimiy hisoblab borishda ko‘maklashadi.
Keling birinchi navbatda, qancha namozingiz qazo bo'lganini aniqlashga yordam beramiz.
Hisoblash uchun pastdagi Qazo hisoblash knopkasidan foydalaning.
"""

prayer_time_region_text = """
namoz vaqtlari
"""

prayer_time_districts_text = """
{region_name}ning qaysi shaxar (tuman) namoz vaqtini bilishni xoxlaysiz?
"""

prayer_time_text = """
🕌 Namoz Vaqtlari (Sana: {date})

Bomdod: {fajr}
Quyosh: {shuhr}
Peshin: {dhuhr}
Asr: {asr}
Shom: {maghrib}
Xufton: {isha}

Namozvaqti.uz sayt orqali ma'lumot olindi.
Bot: @Qazoimbot
"""

about_bot_text = """
bot haqida text
"""

something_went_wrong = "Kechirasiz nimadur xato ketdi (("
# keyboard button texts
forget_prayer_btn_text = "Qazolarim"

faq_btn_text="Ko'p berilgan savollar"
prayer_btn_text="Namoz vaqtlari"
about_bot_btn_text="Bot haqida"
go_back_btn_text="◀️ Orqaga"
how_to_use_bot = "Bot ishlatish bo'yicha video"


# regions | viloyatlar ro'yxati
regions = [
    {
        "name": "Andijon viloyati",
        "callback": "region_andijon",
        "districts": [
            {"name": "Andijon shahri", "callback": "city_andijon"},
            {"name": "Xo'jaobod", "callback": "city_xojaobod"},
            {"name": "Poytug'", "callback": "city_paytug"},
            {"name": "Xonobod", "callback": "city_xonobod"},
            {"name": "Asaka", "callback": "city_asaka"},
            {"name": "Bo'ston", "callback": "city_Boston"},
            {"name": "Shahrixon", "callback": "city_shahrixon"},
            {"name": "Marxamat", "callback": "city_marhamat"}
        ]
    },
    {
        "name": "Buxoro viloyati",
        "callback": "region_buxoro",
        "districts": [
            {"name": "Buxoro", "callback": "city_buxoro"},
            {"name": "Qorakol", "callback": "city_qorakol"},
            {"name": "Gazli", "callback": "city_gazli"},
            {"name": "Jondor", "callback": "city_jondor"},
            {"name": "G'ijduvon", "callback": "city_gijduvon"}
        ]
    },
    {
        "name": "Farg‘ona viloyati",
        "callback": "region_fargona",
        "districts": [
            {"name": "Farg‘ona", "callback": "fargona"},
            {"name": "Marg'ilon", "callback": "margilon"},
            {"name": "Qo'qon", "callback": "qoqon"},
            {"name": "Quva", "callback": "quva"},
            {"name": "Rishton", "callback": "rishton"},
            {"name": "Bog'dod", "callback": "rishton"},
            {"name": "Oltiariq", "callback": "oltiariq"},
        ]
    },
    {
        "name": "Jizzax viloyati",
        "callback": "region_jizzax",
        "districts": [
            {"name": "Jizzax shahri", "callback": "jizzax"},
            {"name": "Zomin", "callback": "zomin"},
            {"name": "Forish", "callback": "forish"},
            {"name": "G‘allaorol", "callback": "gallaorol"},
            {"name": "Do'stlik", "callback": "dostlik"}
        ]
    },
    {
        "name": "Xorazm viloyati",
        "callback": "region_xorazm",
        "districts": [
            {"name": "Urganch shahri", "callback": "urganch"},
            {"name": "Hazorasp", "callback": "hazorasp"},
            {"name": "Xiva", "callback": "district_xiva"},
            {"name": "Shovot", "callback": "district_shovot"},
            {"name": "Bog‘ot", "callback": "district_bogot"},
        ]
    },
    {
        "name": "Namangan viloyati",
        "callback": "region_namangan",
        "districts": [
            {"name": "Namangan shahri", "callback": "district_namangan_shahri"},
            {"name": "Chortoq", "callback": "district_chortoq"},
            {"name": "Chust", "callback": "district_chust"},
            {"name": "Pop", "callback": "district_pop"},
            {"name": "Kosonsoy", "callback": "district_kosonsoy"}
        ]
    },
    {
        "name": "Navoiy viloyati",
        "callback": "region_navoiy",
        "districts": [
            {"name": "Navoiy shahri", "callback": "district_navoiy_shahri"},
            {"name": "Zarafshon", "callback": "district_zarafshon"},
            {"name": "Uchquduq", "callback": "district_uchquduq"},
            {"name": "Qiziltepa", "callback": "district_qiziltepa"},
            {"name": "Karmana", "callback": "district_karmana"}
        ]
    },
    {
        "name": "Qashqadaryo viloyati",
        "callback": "region_qashqadaryo",
        "districts": [
            {"name": "Qarshi shahri", "callback": "district_qarshi_shahri"},
            {"name": "Shahrisabz", "callback": "district_shahrisabz"},
            {"name": "G‘uzor", "callback": "district_guzor"},
            {"name": "Kitob", "callback": "district_kitob"},
            {"name": "Koson", "callback": "district_koson"}
        ]
    },
    {
        "name": "Qoraqalpog‘iston Respublikasi",
        "callback": "region_qoraqalpogiston",
        "districts": [
            {"name": "Nukus shahri", "callback": "district_nukus_shahri"},
            {"name": "Xo‘jayli", "callback": "district_xojayli"},
            {"name": "Mo‘ynoq", "callback": "district_moynoq"},
            {"name": "To‘rtko‘l", "callback": "district_turtkol"},
            {"name": "Amudaryo", "callback": "district_amudaryo"}
        ]
    },
    {
        "name": "Samarqand viloyati",
        "callback": "region_samarqand",
        "districts": [
            {"name": "Samarqand shahri", "callback": "district_samarqand_shahri"},
            {"name": "Urgut", "callback": "district_urgut"},
            {"name": "Kattaqo‘rg‘on", "callback": "district_kattakorgon"},
            {"name": "Ishtixon", "callback": "district_ishtixon"},
            {"name": "Jomboy", "callback": "district_jomboy"}
        ]
    },
    {
        "name": "Sirdaryo viloyati",
        "callback": "region_sirdaryo",
        "districts": [
            {"name": "Guliston shahri", "callback": "district_guliston_shahri"},
            {"name": "Sirdaryo", "callback": "district_sirdaryo"},
            {"name": "Yangiyer", "callback": "district_yangiyer"},
            {"name": "Sayxunobod", "callback": "district_sayxunobod"},
            {"name": "Xovos", "callback": "district_xovos"}
        ]
    },
    {
        "name": "Surxondaryo viloyati",
        "callback": "region_surxondaryo",
        "districts": [
            {"name": "Termiz shahri", "callback": "district_termiz_shahri"},
            {"name": "Denov", "callback": "district_denov"},
            {"name": "Sherobod", "callback": "district_sherobod"},
            {"name": "Jarqo‘rg‘on", "callback": "district_jarqorgon"},
            {"name": "Qumqo‘rg‘on", "callback": "district_qumqorgon"}
        ]
    },
    {
        "name": "Toshkent viloyati",
        "callback": "region_toshkent",
        "districts": [
            {"name": "Nurafshon shahri", "callback": "district_nurafshon_shahri"},
            {"name": "Chirchiq", "callback": "district_chirchiq"},
            {"name": "Angren", "callback": "district_angren"},
            {"name": "Olmaliq", "callback": "district_olmaliq"},
            {"name": "Yangiyo‘l", "callback": "district_yangiyol"}
        ]
    },
    {
        "name": "Toshkent shahri",
        "callback": "region_toshkent_shahri",
        "districts": [
            {"name": "Toshkent shahri", "callback": "district_toshkent_shahri"}
        ]
    },
    {
        "name": "◀️ Orqaga",
        "callback": "main_menu",
        "districts": []
    }
]
