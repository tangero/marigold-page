---
slug: "vplmna"
url: "/mobilnisite/slovnik/vplmna/"
type: "slovnik"
title: "VPLMNA – Visited Public Land Mobile Network of the A subscriber"
date: 2025-01-01
abbr: "VPLMNA"
fullName: "Visited Public Land Mobile Network of the A subscriber"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vplmna/"
summary: "VPLMNA identifikuje mobilní síť (PLMN), ve které se volající strana (A-účastník) aktuálně nachází v roamingu během sestavování hovoru. Jde o klíčový parametr pro směrování, účtování a aplikaci roaming"
---

VPLMNA je veřejná pozemní mobilní síť (PLMN), kterou volající účastník navštěvuje a používá při roamingu mimo svou domovskou síť během sestavování hovoru.

## Popis

VPLMNA je identifikátor sítě používaný v rámci procedur řízení hovorů a správy mobility 3GPP, konkrétně definovaný v technické specifikaci 23.018. Představuje navštívenou veřejnou pozemní mobilní síť ([VPLMN](/mobilnisite/slovnik/vplmn/)), ve které se A-účastník – strana iniciující hovor nebo relaci – fyzicky nachází a je v ní registrován v době sestavování hovoru. Tento parametr není statický identifikátor, ale dynamický, určený během signalizačního toku sestavování hovoru. Když mobilní účastník zahájí hovor, obsluhující [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) nebo příslušný uzel jádra sítě v navštívené síti zahrne VPLMNA do zprávy Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) nebo jiných relevantních signalizačních zpráv odesílaných směrem k síti volané strany (B-účastník). Hodnotou je typicky Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) operátora navštívené sítě.

Z architektonického hlediska je VPLMNA datový prvek přenášený v rámci signalizačních protokolů, jako je [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Bearer Independent Call Control (BICC), a v poslední době také v hlavičkách [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) v sítích IP Multimedia Subsystem (IMS). Jeho primární role je v mezisíťové signalizaci mezi navštíveným MSC (VMSC) A-účastníka a Gateway MSC (GMSC) nebo jinými přepínacími uzly v domovských nebo tranzitních sítích. Zařazení tohoto parametru umožňuje každé síti zapojené do cesty hovoru identifikovat roamingový kontext volající strany. To je nezbytné pro funkce jako směrování hovorů, zejména pro optimální směrování a procedury zpětného volání, a pro generování přesných záznamů o účtovaných datech (CDR), které odrážejí roamingový vztah.

Z pohledu provozu sítě VPLMNA umožňuje několik klíčových procesů. Pro účtování umožňuje operátorovi domovské sítě aplikovat specifické tarifní dohody pro hovory uskutečněné při roamingu v dané konkrétní navštívené síti. Pro regulatorní soulad pomáhá identifikovat jurisdikci a příslušné zákony pro původ hovoru. Z hlediska servisní logiky může ovlivnit, jak jsou služby (jako zákaz hovorů nebo prezentace čísla) aplikovány na základě polohy účastníka. Parametr funguje v součinnosti s dalšími identifikátory, jako je MSISDN (Mobile Subscriber ISDN Number) a IMSI (International Mobile Subscriber Identity), aby poskytl úplný kontext pro hovor. Jeho konzistentní definice od Release 4 výše zajišťuje zpětnou kompatibilitu a stabilní signalizaci mezi operátory, čímž tvoří základní prvek globálního roamingového ekosystému.

## K čemu slouží

Parametr VPLMNA byl zaveden, aby řešil složitosti obsluhy hovorů a účtování v prostředí víceoperátorového globálního roamingu. Před standardizovanou roamingovou signalizací bylo identifikování přesné sítě, ze které roamingový účastník hovor uskutečnil, obtížné, což vedlo k problémům s efektivitou směrování a přesným vyúčtováním mezi operátory. Vytvoření VPLMNA poskytlo jasný, strojově čitelný identifikátor, který putuje se signalizací sestavování hovoru, a tyto problémy řeší.

Jeho existence je motivována potřebou přesného směrování hovorů. Například umožňuje optimální směrování (také známé jako vyhýbání se 'trombónování'), kdy může být hovor od roamingového účastníka k účastníkovi v jeho domovské zemi směrován přímo z navštívené sítě k cíli, místo aby byl nejprve 'trombónován' zpět do domovské sítě. Tím se snižuje latence a využití síťových zdrojů. Dále je zásadní pro generování záznamů Transferred Account Procedures (TAP) používaných pro finanční vypořádání mezi operátory. Přesnou identifikací navštívené sítě může domovský operátor aplikovat správnou roamingovou cenovou dohodu a účastníka přesně účtovat.

Historicky, jak se GSM vyvíjelo v globální systém, vyžadovala signalizace mezi sítěmi různých operátorů společnou sadu parametrů pro zajištění interoperability. VPLMNA spolu se svým protějškem VPLMNB se staly standardizovanými prvky v záznamech Call Detail Records (CDR) a signalizačních zprávách, poskytující potřebný kontext pro každý mobilní hovor. Tím se vyřešilo omezení dřívějších systémů, kde byl původ roamingového hovoru nejednoznačný, což umožnilo automatizované, rozsáhlé komerční roamingové dohody, které jsou základem moderných mobilních telekomunikací.

## Klíčové vlastnosti

- Dynamická identifikace sítě pro volajícího (A) účastníka během roamingu
- Kódována jako PLMN ID (MCC+MNC) v rámci protokolů signalizace hovorů
- Nezbytná pro přesné účtování a vypořádání mezi operátory (záznamy TAP)
- Umožňuje optimální směrování hovorů, aby se zabránilo zbytečnému 'trombónování'
- Podporuje roamingově specifickou servisní logiku a vynucování politik
- Standardizovaný parametr zajišťující globální interoperabilitu mezi síťovými operátory

## Související pojmy

- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [TAP – Transferred Account Procedure](/mobilnisite/slovnik/tap/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain

---

📖 **Anglický originál a plná specifikace:** [VPLMNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/vplmna/)
