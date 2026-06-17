---
slug: "bbiff"
url: "/mobilnisite/slovnik/bbiff/"
type: "slovnik"
title: "BBIFF – Bearer Binding Intercept and Forwarding Function"
date: 2025-01-01
abbr: "BBIFF"
fullName: "Bearer Binding Intercept and Forwarding Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bbiff/"
summary: "Funkce zákonného odposlechu (LI), která zachycuje a přeposílá provoz v uživatelské rovině spojený s konkrétním přenosovým kanálem (bearerem). Je to klíčová komponenta v sítích 3GPP pro umožnění autori"
---

BBIFF je funkce zákonného odposlechu, která zachycuje a přeposílá provoz v uživatelské rovině konkrétního přenosového kanálu (beareru) a váže jej k cílové identitě a relaci pro autorizovaný dohled v sítích 3GPP.

## Popis

Funkce BBIFF (Bearer Binding Intercept and Forwarding Function) je specializovaná síťová funkce v architektuře zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) podle 3GPP, která působí v doméně odposlechu uživatelské roviny. Jejím hlavním úkolem je zachytávat toky IP paketů na konkrétním přenosovém kanálu (beareru) (např. na vyhrazeném nebo výchozím beareru) spojeném s cílovým subjektem pod dohledem a přeposílat kopie tohoto provozu do monitorovacího zařízení orgánu činného v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)). BBIFF je typicky umístěna společně nebo integrována do síťového uzlu, který zpracovává provoz uživatelské roviny, jako je Packet Data Network Gateway (PGW) v 4G nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G. Funguje na základě aktivačních příkazů přijatých od administrační funkce ([ADMF](/mobilnisite/slovnik/admf/)), která odposlech autorizuje na základě zákonného příkazu.

Z architektonického hlediska BBIFF komunikuje s několika komponentami LI. Přijímá informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) a spouštěče obsahu komunikace ([CC](/mobilnisite/slovnik/cc/)) od ADMF přes rozhraní [HI](/mobilnisite/slovnik/hi/) (Handover Interface). IRI obsahuje identifikátory cíle a konkrétní přenosový kanál (bearer), který má být monitorován. Po aktivaci BBIFF identifikuje bearer cíle pomocí parametrů, jako je EPS Bearer ID, QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)) nebo IP 5-tice (zdrojová/cílová IP adresa, porty, protokol). Poté provede hlubokou kontrolu paketů nebo přiřazení toku, aby vybrala relevantní pakety uživatelské roviny. Klíčovým technickým aspektem je 'binding' (svázání) – zajištění, že zachycený provoz je přesně přiřazen ke správné cílové identitě a kontextu relace, a to i při pohybu uživatele nebo změnách charakteristik beareru.

Z provozního hlediska BBIFF duplikuje zachycené pakety, zapouzdří je s nezbytnými metadaty (jako jsou časová razítka, identifikátor bodu odposlechu a korelační číslo) a bezpečně je přeposílá mediační funkci (MF) přes rozhraní X2 nebo X3. MF následně doručí zachycený obsah do LEMF. BBIFF musí fungovat s vysokou spolehlivostí a s minimálním dopadem na běžnou službu uživatelské roviny; je navržena tak, aby byla pro koncového uživatele transparentní. Její implementace vyžaduje přísné dodržování bezpečnostních specifikací 3GPP, aby se zabránilo neoprávněnému přístupu a zajistila integrita dat během přenosu k orgánům činným v trestním řízení.

## K čemu slouží

BBIFF byla vytvořena, aby řešila technické výzvy zákonného odposlechu v paketově přepínaných mobilních sítích, kde je uživatelský provoz dynamický a relací založený. Před její standardizací byly mechanismy odposlechu často specifické pro dodavatele a potýkaly se s komplexitou IP služeb, více souběžnými bearery na uživatele a událostmi mobility. BBIFF poskytuje standardizovanou, škálovatelnou metodu pro zachycování obsahu uživatelské roviny v sítích 3GPP, což zajišťuje, že orgány činné v trestním řízení mohou efektivně monitorovat cílenou komunikaci podle zákonných mandátů.

Její vývoj byl motivován regulatorními požadavky po celém světě, které ukládají telekomunikačním operátorům povinnost pomáhat při zákonném dohledu z důvodů národní bezpečnosti a vyšetřování trestných činů. BBIFF řeší problém přesného svázání zachycených IP toků s kontextem beareru konkrétního cíle, což je zásadní v moderních sítích, kde jeden uživatel může mít více souběžných datových relací (např. VoLTE, streamované video a prohlížení webu), každou na různých bearerech s odlišnými profily QoS. Bez přesného svázání s bearerem by zachycená data mohla být neúplná nebo špatně přiřazená, což by ohrozilo integritu vyšetřování.

Standardizací BBIFF v 3GPP Release 14 a novějších specifikace zajišťuje interoperabilitu mezi různými dodavateli síťových zařízení a poskytuje perspektivní rámec, který se vyvíjí spolu se síťovými architekturami, od 4G EPC po 5G Core. Řeší omezení dřívějších přístupů k odposlechu, které nebyly navrženy pro granularitu QoS na úrovni bearerů a oddělení řídicí a uživatelské roviny v pokročilých mobilních sítích.

## Klíčové vlastnosti

- Zachycuje provoz IP v uživatelské rovině na určených EPS nebo 5G QoS bearech
- Svazuje zachycený obsah se správnou cílovou identitou a kontextem relace pomocí identifikátorů beareru
- Přeposílá duplikované pakety s metadaty k mediační funkci přes standardizovaná rozhraní X2/X3
- Funguje na základě aktivačních příkazů od administrační funkce (ADMF)
- Podporuje odposlech pro stacionární i mobilní cíle s kontinuitou relace
- Zajišťuje minimální dopad na výkon normální datové cesty uživatelské roviny

## Definující specifikace

- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.827** (Rel-14) — LI for S8 Home Routed VoLTE Roaming

---

📖 **Anglický originál a plná specifikace:** [BBIFF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bbiff/)
