---
slug: "cnap"
url: "/mobilnisite/slovnik/cnap/"
type: "slovnik"
title: "CNAP – Calling Name Presentation"
date: 2025-01-01
abbr: "CNAP"
fullName: "Calling Name Presentation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cnap/"
summary: "CNAP je doplňková služba, která zobrazuje jméno volajícího účastníka volanému účastníkovi před přijetím hovoru. Zlepšuje uživatelský zážitek tím, že poskytuje identifikaci volajícího nad rámec samotné"
---

CNAP je doplňková služba v architektuře Inteligentní sítě (IN) 3GPP, která zobrazuje jméno volajícího účastníka volanému účastníkovi před přijetím hovoru, čímž vylepšuje identifikaci volajícího.

## Popis

Calling Name Presentation (CNAP) je standardizovaná doplňková služba definovaná v rámci standardů 3GPP, která umožňuje zobrazení jména volajícího účastníka na terminálu volaného účastníka. Služba funguje tak, že při zahájení hovoru dotazuje databázi obsahující mapování jmen na telefonní čísla. Tento dotaz probíhá během procedur navázání hovoru, typicky zahrnujících signalizaci mezi síťovými elementy za účelem získání a předání informace o jméně před tím, než je hovor prezentován volanému účastníkovi.

Architektonicky CNAP využívá možnosti Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)), konkrétně využívá framework Customized Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)) v sítích GSM/UMTS a rozhraní založená na protokolu Diameter v pozdějších vydáních 3GPP. Mezi klíčové síťové elementy zapojené do služby patří Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data účastníka, Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Mobile Management Entity ([MME](/mobilnisite/slovnik/mme/)) pro řízení hovoru a specializované CNAP servery či databáze, které ukládají a poskytují informace o jménech. Když je uskutečněn hovor, obsluhující síť dotazuje příslušnou databázi pomocí čísla volajícího účastníka jako klíče, získá přidružené jméno a zahrne jej do signalizace navázání hovoru (například v [ISUP](/mobilnisite/slovnik/isup/) nebo [SIP](/mobilnisite/slovnik/sip/) zprávách) směrem k terminálu volaného účastníka.

Technická implementace zahrnuje několik protokolových vrstev a rozhraní. V okruhově přepínaných doménách jsou informace CNAP typicky přenášeny v parametru Calling Party Name v rámci signalizačních zpráv ISDN User Part (ISUP). V paketově přepínaných doménách a doménách IMS jsou přenášeny prostřednictvím hlaviček Session Initiation Protocol (SIP), konkrétně hlavičky P-Asserted-Identity s parametry pro zobrazení jména. Služba vyžaduje koordinaci mezi sítí původu a sítí určení, což může zahrnovat dotazy mezi operátory, když volající a volaný účastník patří k různým sítím. Ohledy na soukromí jsou nedílnou součástí návrhu, s mechanismy pro respektování preferencí volajícího účastníka ohledně zobrazení jména.

Role CNAP přesahuje základní identifikaci volajícího a podporuje různé telekomunikační služby. Umožňuje vylepšené třídění hovorů, integraci se seznamy kontaktů a podporu obchodních aplikací, kde je důležitá verifikace identity volajícího. Služba musí zvládat scénáře mezinárodního roamingu, případy přenosnosti čísel a různé formáty číslovacích plánů při zachování požadavků na výkonnost doby navázání hovoru. Mezi operátory existují variace v implementaci, ale standardizace 3GPP zajišťuje základní interoperabilitu a konzistentní uživatelský zážitek napříč různými sítěmi a typy zařízení.

## K čemu slouží

CNAP byl vytvořen, aby řešil omezení tradiční identifikace volajícího (CLIP), která zobrazovala pouze telefonní čísla. Před CNAP mohli účastníci vidět pouze číslo volajícího účastníka, což vyžadovalo mentální rozpoznání nebo porovnání se seznamy kontaktů pro identifikaci volajícího. To bylo obzvláště problematické pro firmy přijímající hovory z neznámých čísel nebo pro jednotlivce snažící se vyhnout nechtěným hovorům. Služba si kladla za cíl zvýšit uživatelský komfort a správu hovorů tím, že poskytovala okamžitou vizuální identifikaci volajících.

Historický kontext vývoje CNAP zahrnuje vývoj služeb Inteligentní sítě v 90. letech 20. století, kdy telekomunikační operátoři usilovali o vytvoření služeb s přidanou hodnotou nad rámec základních hlasových hovorů. S růstem adopce mobilních telefonů se stala zřejmou potřeba lepšího třídění hovorů, zejména s rostoucím množstvím nevyžádaných a marketingových hovorů. CNAP navázal na existující službu Calling Line Identification Presentation (CLIP) přidáním rozměru jména, čímž vytvořil uživatelsky přívětivější metodu identifikace, která nevyžadovala od účastníků memorování čísel nebo udržování rozsáhlých seznamů kontaktů.

CNAP řeší několik praktických problémů v telekomunikacích. Pomáhá uživatelům činit informovaná rozhodnutí o přijetí hovoru, čímž snižuje rušení od nechtěných volajících. Pro firmy umožňuje lepší zákaznický servis tím, že umožňuje operátorům vidět jména volajících před přijetím hovoru. Služba také podporuje regulatorní požadavky na identifikaci volajícího v některých jurisdikcích. Standardizací CNAP napříč sítěmi 3GPP je zajištěna konzistentní funkčnost pro účastníky roamující mezi sítěmi různých operátorů, což udržuje kontinuitu služby bez ohledu na lokalitu nebo síťovou technologii.

## Klíčové vlastnosti

- Zobrazuje jméno volajícího účastníka na zařízení volaného účastníka
- Integruje se s architekturou Inteligentní sítě (IN)
- Podporuje jak okruhově přepínané, tak paketově přepínané domény
- Obsahuje prvky ochrany soukromí pro volající účastníky
- Funguje napříč různými síťovými operátory
- Dodržuje požadavky na výkonnost při navazování hovoru

## Související pojmy

- [CLIP – Calling Line Identification Presentation](/mobilnisite/slovnik/clip/)
- [CLIR – Calling Line Identification Restriction](/mobilnisite/slovnik/clir/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.096** (Rel-19) — Calling Name Presentation (CNAP)
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [CNAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cnap/)
