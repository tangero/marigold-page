---
slug: "imrn"
url: "/mobilnisite/slovnik/imrn/"
type: "slovnik"
title: "IMRN – IP Multimedia Routeing Number"
date: 2025-01-01
abbr: "IMRN"
fullName: "IP Multimedia Routeing Number"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imrn/"
summary: "Dočasné číslo ve formátu E.164 přidělené za účelem umožnění směrování relací IP Multimedia Subsystem (IMS) k roamujícímu uživateli, když navštívená síť nemá roamingová rozhraní na úrovni IMS. Slouží j"
---

IMRN je dočasné číslo ve formátu E.164 přidělené pro směrování IMS relací k roamujícímu uživateli, když navštívená síť postrádá rozhraní pro IMS roaming, a slouží jako spojovací identifikátor pro kontinuitu relace.

## Popis

IP Multimedia Routeing Number (IMRN) je klíčový identifikátor v architektuře IMS dle 3GPP, specificky definovaný pro scénáře zahrnující IMS roaming. Jedná se o dočasné, globálně jednoznačné číslo ve formátu E.164, které přiděluje IMS entita navštívené sítě, typicky Visited Application Server (V-AS) nebo vyhrazená funkce pro přidělování IMRN. Jeho primární funkcí je sloužit jako směrovatelný kontaktní bod pro příchozí SIP relace (jako hlasové nebo videohovory) určené roamujícímu účastníkovi, když domácí a navštívená síť nemají přímou roamingovou dohodu na úrovni IMS nebo není k dispozici potřebné rozhraní Gm/SIP mezi User Equipment (UE) a [P-CSCF](/mobilnisite/slovnik/p-cscf/) domácí sítě.

Když uživatel přejde do roamingu v síti bez IMS roamingu, domácí síť nemůže směrovat SIP signalizaci přímo na IP adresu UE v navštívené síti. Pro vyřešení tohoto problému navštívená síť přidělí IMRN a asociuje jej s dočasnou registrací roamujícího uživatele. Toto IMRN je následně komunikováno zpět do domácí sítě uživatele, často prostřednictvím registrační procedury uživatele. Následně, když je uskutečněn hovor na trvalou Public User Identity uživatele (např. jeho SIP URI), IMS entity domácí sítě (jako S-CSCF) provedou překlad pomocí [ENUM](/mobilnisite/slovnik/enum/)/[DNS](/mobilnisite/slovnik/dns/) dotazu. Po zjištění, že je pro směrování asociováno IMRN, je žádost o relaci přesměrována na toto IMRN.

IMRN směruje hovor do okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) domény navštívené sítě nebo k funkci řízení mediální brány. Navštívená síť, která IMRN rozpozná, jej namapuje zpět na asociovanou IP konektivitu uživatele a doručí SIP relaci k UE přes paketově spínanou (PS) doménu. Tento mechanismus efektivně vytváří tzv. tromboning nebo kotvící bod, umožňující, aby řízení relace bylo zpracováno domácí sítí, zatímco média jsou doručována roamujícímu uživateli. Odděluje směrovací identifikátor od trvalé identity uživatele po dobu roamingu, čímž zajišťuje kontinuitu služby. IMRN je uvolněno po odregistrování uživatele nebo po vypršení jeho platnosti a vrací se do fondu pro opětovné použití.

## K čemu slouží

IMRN bylo zavedeno, aby vyřešilo zásadní problém v raných nasazeních IMS a roamingových scénářích: jak doručovat pokročilé multimediální služby založené na IP (VoIP, video, zasílání zpráv) uživatelům roamujícím v sítích, kterým chybělo přímé propojení na úrovni IMS. Počáteční verze 3GPP se zaměřovaly na poskytování služeb domácí sítí. Pro roaming výchozí model spoléhal na to, že navštívená síť poskytne IP konektivitu (PS doména), ale předpokládal, že signalizační cesta SIP (referenční bod Gm) bude vždy zavedena zpět k Proxy-CSCF domácí sítě. To vyžadovalo složité bezpečnostní a politické dohody mezi operátory.

V praxi mnoho operátorů, zejména v raných nasazeních, neimplementovalo roamingová rozhraní IMS kvůli nákladům, bezpečnostním obavám nebo postupným strategiím zavádění. Bez IMRN by byl roamující uživatel nedosažitelný pro příchozí IMS relace, což by vážně omezilo využitelnost IMS služeb. Mechanismus IMRN poskytl provizorní, pragmatické řešení. Využil existující, široce nasazenou infrastrukturu [CS](/mobilnisite/slovnik/cs/) roamingu (která pro směrování používá čísla E.164) jako 'přenašeče' pro signalizaci IMS relací. To umožnilo operátorům nabízet služby IMS roamingu bez nutnosti okamžitého, plnohodnotného vzájemného propojení IMS, čímž urychlilo dostupnost služeb a jejich přijetí.

Řešilo technické omezení směrování SIP požadavku na dynamicky přidělenou IP adresu v cizí síti, na kterou nemohla IMS jádrová síť domácí sítě přímo směrovat. Převodem problému na dobře známý problém telefonního směrování (směrování přes dočasné číslo E.164) překlenulo mezeru mezi legacy okruhově spínaným roamingem a službami IP multimédií nové generace, čímž zajistilo zpětnou kompatibilitu a usnadnilo plynulejší přechod na plně IP sítě.

## Klíčové vlastnosti

- Formát dočasného čísla E.164 pro kompatibilitu s globálním telefonním směrováním
- Dynamicky přidělováno a vázáno na kontext registrace roamujícího uživatele
- Umožňuje směrování SIP relací přes CS doménu nebo mediální brány, když chybí přímý IMS roaming
- Podporuje kontinuitu relace pro roamující uživatele bez přímého IMS propojení mezi domácí a navštívenou sítí
- Uvolněno po odregistrování uživatele pro správu fondu a šetření číselnými zdroji
- Umožňuje směrovací překlad založený na ENUM/DNS v domácí IMS síti

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [ENUM – E.164 telephone NUmber Mapping](/mobilnisite/slovnik/enum/)

## Definující specifikace

- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol

---

📖 **Anglický originál a plná specifikace:** [IMRN na 3GPP Explorer](https://3gpp-explorer.com/glossary/imrn/)
