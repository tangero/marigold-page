---
slug: "pes"
url: "/mobilnisite/slovnik/pes/"
type: "slovnik"
title: "PES – IMS-based PSTN/ISDN Emulation Sub-system"
date: 2025-01-01
abbr: "PES"
fullName: "IMS-based PSTN/ISDN Emulation Sub-system"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pes/"
summary: "Subsystém umožňující provoz starších telefonních služeb PSTN/ISDN přes síť IP Multimedia Subsystem (IMS). Poskytuje operátorům migrační cestu pro přechod od sítí s přepojováním okruhů k plně IP sítím"
---

PES je subsystém založený na IMS, který emuluje služby starších telefonních sítí PSTN/ISDN, aby poskytl migrační cestu od přepojování okruhů k plně IP sítím při zachování kompatibility služeb.

## Popis

IMS-based [PSTN](/mobilnisite/slovnik/pstn/)/[ISDN](/mobilnisite/slovnik/isdn/) Emulation Sub-system (PES) je komplexní architektonický rámec definovaný 3GPP pro usnadnění migrace tradičních telefonních služeb na sítě nové generace založené na IP. Funguje jako funkční nadstavba uvnitř jádra IMS a umožňuje emulaci kompletní sady služeb veřejné telefonní sítě (PSTN) a sítě integrovaných digitálních služeb (ISDN). Tato emulace je pro koncového uživatele transparentní; uživatel nadále používá stávající koncová zařízení (jako tradiční telefony nebo ISDN terminály) a má k dispozici stejné služby, například základní hovorové služby, doplňkové služby (čekání hovoru, přesměrování hovoru atd.) a nouzové volání. Architektura PES je postavena na řídicí rovině IMS a využívá základní prvky IMS, jako je Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro řízení relací a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro uživatelská data, ale zavádí specifické funkce související s PES pro zpracování jedinečných požadavků signalizace a přenosu médií starších služeb.

Jádrem PES jsou klíčové funkční entity definované v dokumentech jako TS 23.517. Access Gateway Control Function ([AGCF](/mobilnisite/slovnik/agcf/)) je klíčovou komponentou, která funguje jako mezisíťový bod pro signalizaci. Ukončuje starší přístupové signalizační protokoly (jako ISDN PRI nebo signalizaci analogových linek) od zařízení na straně zákazníka nebo přístupových sítí a překládá je do signalizace [SIP](/mobilnisite/slovnik/sip/) kompatibilní s IMS pro komunikaci s jádrem IMS. AGCF také řídí přidružené Media Gateways ([MGW](/mobilnisite/slovnik/mgw/)) pro mezisíťové propojení přenosové cesty mezi okruhy s časovým dělením ([TDM](/mobilnisite/slovnik/tdm/)) a IP proudy založenými na protokolu RTP (Real-time Transport Protocol). Další klíčovou entitou je PSTN/ISDN Emulation Edge (PEE), která zajišťuje mezisíťové propojení s externími staršími sítěmi PSTN/ISDN a zaručuje bezproblémové směrování hovorů mezi emulovanou doménou a tradiční sítí.

Subsystém PES funguje na základě jasného oddělení mezi přístupovou/starší doménou a jádrovou doménou IMS. Když starší koncové zařízení zahájí hovor, jeho signalizaci zachytí AGCF. AGCF autentizuje uživatele (často s využitím dat z HSS), přeloží starou signalizaci na požadavek SIP INVITE a přepošle jej do jádra IMS. Jádro IMS následně zpracuje požadavek na relaci podle standardních procedur IMS, případně za účasti aplikačních serverů (AS) pro servisní logiku. Pro přenosovou cestu médií AGCF dá pokyn Media Gateway, aby převedl TDM přenos uživatele na IP/RTP proud. Tato architektura zajišťuje, že veškerá servisní logika a řízení relací zůstává v IP/IMS doméně, zatímco přístup uživatele zůstává nezměněn. PES je základním kamenem případu užití „migrace PSTN/ISDN“ definovaného 3GPP a poskytuje standardizovanou, mezi dodavateli interoperabilní cestu pro transformaci sítě.

## K čemu slouží

PES byl vytvořen, aby řešil zásadní výzvu migrace ze zastaralých, nákladných na údržbu telefonních sítí s přepojováním okruhů (PSTN/ISDN) na moderní, efektivní a na služby bohaté plně IP sítě založené na IMS. Tradiční PSTN, byť spolehlivá, je založena na vyhrazené TDM infrastruktuře, která je nákladná na provoz, špatně škáluje pro datové služby a omezuje zavádění nových multimediálních funkcí. Posun odvětví ke konvergentním pevným a mobilním sítím vyžadoval jednotnou řídicí rovinu založenou na IP, kterou poskytuje IMS. „Velký třesk“ – okamžitá výměna všech zařízení na straně zákazníka a přístupových linek – však byl pro operátory ekonomicky a prakticky nemožný.

PES tento problém řeší tím, že umožňuje postupnou, fázovanou migrační strategii. Umožňuje síťovým operátorům zavést jádro IMS a začít přechod služeb, aniž by byli nuceni okamžitě upgradovat každé koncové zařízení nebo přístupovou linku. Zákazníci mohou nadále používat své stávající telefony a služby, zatímco operátor těží z konsolidace síťových prvků do jedné IP infrastruktury, snížení provozních nákladů a uvolnění cenného prostoru a energie dříve spotřebovávaných staršími ústřednami. PES poskytuje jasnou hranici, kde může být starší přístupová síť postupně modernizována (např. nahrazena optickým nebo bezdrátovým přístupem), zatímco servisní vrstva v IMS zůstává konstantní.

Navíc PES tuto migrační cestu standardizuje, čímž předchází závislosti na jediném dodavateli a zajišťuje interoperabilitu mezi AGCF, Media Gateway a jádry IMS od různých výrobců. Před vznikem PES čelili operátory proprietární nebo nestandardní řešení pro VoIP brány, což komplikovalo rozsáhlá nasazení a integraci více dodavatelů. Definováním kompletního subsystému v rámci standardů 3GPP poskytl PES operátorům budoucí plán pro transformaci sítě, který zajišťuje kontinuitu služeb, soulad s regulacemi (zejména pro nouzové služby) a jasnou cestu vývoje směrem k plně nativním IMS službám (jako VoLTE a VoNR) v dlouhodobém horizontu.

## Klíčové vlastnosti

- Emulace kompletní sady služeb PSTN/ISDN přes IMS
- Mezisíťové propojení starší přístupové signalizace (např. ISDN, analogová) s IMS/SIP
- Řízení Media Gateway pro konverzi TDM přenosu na IP
- Bezproblémové propojení s externími staršími sítěmi PSTN/ISDN
- Opětovné využití základních funkcí IMS (CSCF, HSS) pro řízení a uživatelská data
- Podpora regulovaných služeb, jako je nouzové volání a zákonný odposlech

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [AGCF – Access Gateway Control Function](/mobilnisite/slovnik/agcf/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.412** (Rel-8) — Trunking Gateway Control Procedures
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework

---

📖 **Anglický originál a plná specifikace:** [PES na 3GPP Explorer](https://3gpp-explorer.com/glossary/pes/)
