---
slug: "itcc"
url: "/mobilnisite/slovnik/itcc/"
type: "slovnik"
title: "ITCC – International Telecommunication Charge Card"
date: 2025-01-01
abbr: "ITCC"
fullName: "International Telecommunication Charge Card"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/itcc/"
summary: "International Telecommunication Charge Card (ITCC) je služba umožňující uživatelům účtovat komunikační služby na předplacený nebo postpaidový kartový účet, často pro mezinárodní roaming nebo prémiové"
---

ITCC je služba, která umožňuje uživatelům účtovat komunikační služby na předplacený nebo postpaidový kartový účet, typicky pro mezinárodní roaming nebo prémiové služby, prostřednictvím protokolů mezi sítí a vyhrazeným účtovacím serverem.

## Popis

International Telecommunication Charge Card (ITCC) je služba definovaná v 3GPP TS 29.163, která umožňuje účastníkovi účtovat telekomunikační služby (jako hlasové hovory, [SMS](/mobilnisite/slovnik/sms/) nebo datové relace) na specifický kartový účet, nikoli na jeho primární mobilní předplatné. To je zvláště užitečné ve scénářích, jako je mezinárodní roaming, kdy se uživatel může chtít vyhnout vysokým roamingovým poplatkům použitím samostatné předplacené mezinárodní telefonní karty. Služba ITCC zahrnuje interakce mezi navštívenou sítí (kde se uživatel nachází v roamingu), domovskou sítí a případně poskytovatelem služby kartového účtování (Charge Card Service Provider, CCSP).

Technicky je služba umožněna vylepšeními protokolu Camel Application Part ([CAP](/mobilnisite/slovnik/cap/)). Když uživatel zahájí hovor a indikuje použití ITCC (např. vytočením speciální předvolby nebo čísla), navštívená ústředna ([VMSC](/mobilnisite/slovnik/vmsc/)) nebo [SGSN](/mobilnisite/slovnik/sgsn/) spustí Camel dialog s vyhrazeným řídicím bodem služeb (Service Control Point, [SCP](/mobilnisite/slovnik/scp/)) známým jako Charge Card SCP. Tento SCP je zodpovědný za autentizaci kartového účtu (pomocí přihlašovacích údajů, jako je číslo karty a [PIN](/mobilnisite/slovnik/pin/)), kontrolu zůstatku účtu u předplacených karet a autorizaci služby. SCP následně instruuje přepínač navštívené sítě, aby spojení uskutečnil, často přes specifickou trasu, a spravuje události účtování v reálném čase.

Protokol definovaný v TS 29.163 specifikuje informační toky a CAP operace pro vyvolání služby ITCC, včetně triggerů počátečního detekčního bodu (Initial [DP](/mobilnisite/slovnik/dp/)), zpráv pro ověření karty a událostí účtování. Architektura odděluje funkci řízení hovoru v navštívené síti od servisní logiky a účtovací funkce v Charge Card SCP. To umožňuje centralizovanou správu kartových účtů a přenositelnost služby mezi různými navštívenými sítěmi. Služba může podporovat různé modely účtování, včetně odčítání z předplaceného zůstatku nebo kumulace na postpaidové faktuře.

## K čemu slouží

Služba International Telecommunication Charge Card byla vytvořena, aby řešila potřebu flexibilních alternativních platebních metod pro telekomunikace, zejména v přeshraničních scénářích. Před její standardizací existovala proprietární řešení telefonních karet, ale postrádala interoperabilitu mezi různými síťovými operátory a zeměmi. Cestující by potřeboval jinou kartu nebo mechanismus pro každou navštívenou zemi. Standard ITCC si kladl za cíl poskytnout jednotnou, na operátora nezávislou metodu pro používání kartových účtů, což zjednodušuje uživatelský zážitek a umožňuje globální nabídku služeb od poskytovatelů těchto karet.

Řeší problém vysokých a nepředvídatelných roamingových poplatků tím, že umožňuje uživatelům oddělit náklady. Uživatel může udržovat primární předplatné pro místní použití a samostatný, potenciálně předplacený, kartový účet pro mezinárodní hovory nebo data. To uživatelům dává větší kontrolu nad výdaji. Pro operátory a poskytovatele služeb třetích stran vytváří nový obchodní model a zdroj příjmů prostřednictvím poskytování služeb kartového účtování, včetně mezinárodních telefonních karet prodávaných v maloobchodě nebo online.

Motivace byla také technická: definovat čisté, standardizované rozhraní mezi sítí provádějící řízení hovoru a externí entitou spravující logiku kartového účtu a zůstatek. Použití stávající infrastruktury Camel pro služby inteligentní sítě poskytlo osvědčený, škálovatelný rámec. Tím se zabránilo nutnosti, aby operátoři vyvíjeli vlastní, neinteroperabilní řešení pro integraci systémů účtování třetích stran, čímž se snížily náklady a složitost a zároveň podpořil konkurenční trh s přidanými službami.

## Klíčové vlastnosti

- Umožňuje účtování služeb na samostatný kartový účet, odlišný od primárního předplatného
- Využívá protokoly Camel (CAP) pro řízení a spouštění služby
- Podporuje modely účtování předplacené i postpaidové
- Usnadňuje použití v scénářích mezinárodního roamingu
- Zahrnuje vyhrazený řídicí bod služeb pro kartové účtování (Charge Card SCP) pro autentizaci a autorizaci
- Definuje standardizované informační toky mezi navštívenou sítí a serverem kartového účtování (TS 29.163)

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [ITCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/itcc/)
