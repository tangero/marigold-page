---
slug: "cltd"
url: "/mobilnisite/slovnik/cltd/"
type: "slovnik"
title: "CLTD – Closed Loop Transmit Diversity"
date: 2025-01-01
abbr: "CLTD"
fullName: "Closed Loop Transmit Diversity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cltd/"
summary: "Technika přenosové diverzity v 3GPP WCDMA/UMTS, kde UE poskytuje Node B zpětnou vazbu pro optimalizaci fáze a/nebo amplitudy signálů vysílaných z více antén. Tím se zlepšuje kvalita downlinkového sign"
---

CLTD je technika přenosové diverzity 3GPP WCDMA/UMTS, kde zpětná vazba od UE umožňuje Node B optimalizovat přenosy z více antén, čímž zlepšuje kvalitu downlinku, datové rychlosti a pokrytí potlačováním útlumu.

## Popis

Closed Loop Transmit Diversity (CLTD) je pokročilý schéma downlinkové přenosové diverzity standardizované pro sítě 3GPP [WCDMA](/mobilnisite/slovnik/wcdma/)/UMTS. Funguje na fyzické vrstvě rozhraní rádiového přístupu a je určeno speciálně pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Základní princip spočívá v tom, že User Equipment (UE) průběžně měří podmínky downlinkového kanálu z více vysílacích antén Node B (základnové stanice). Na základě těchto měření UE vypočítá a signalizuje zpět informace – konkrétně váhové faktory – zpět do Node B přes uplinkový Dedicated Physical Control Channel ([DPCCH](/mobilnisite/slovnik/dpcch/)). Node B následně tyto váhové faktory aplikuje, aby upravil fázi a v pokročilejších módech i amplitudu signálů vysílaných ze svých antén. Tato uzavřená smyčka úprav v reálném čase předkompenzuje vlivy kanálu a zajišťuje, že se signály z různých antén na přijímači UE spojí konstruktivně, čímž se maximalizuje přijímaný výkon signálu a poměr signálu k interferenci ([SIR](/mobilnisite/slovnik/sir/)).

Architektura CLTD je integrována do specifikací fyzické vrstvy WCDMA a řídí strukturu downlinkových vyhrazených fyzických kanálů ([DPCH](/mobilnisite/slovnik/dpch/)). Byly definovány dva hlavní módy: Mód 1 a Mód 2. V CLTD Módu 1 zpětná vazba z UE instruuje Node B, aby upravil pouze fázi signálu sekundární antény vzhledem k primární anténě. Zpětná vazba se skládá z jednoho bitu (pole [FBI](/mobilnisite/slovnik/fbi/)) přenášeného v každém slotu, který příkazuje úpravu fáze o 0 nebo π radiánů. Tím vzniká forma fázové modulace pro diverzitní signál. CLTD Mód 2 je pokročilejší a umožňuje společnou úpravu fáze a amplitudy. Zde se zpětná vazba z UE skládá z více bitů na slot, což umožňuje výběr váhového vektoru z předdefinované sady komplexních vah (kodek). To umožňuje přesnější beamforming směrem k UE a nabízí vyšší potenciální zisk za cenu zvýšené režie uplinkové zpětné vazby.

Provoz je těsně synchronizovaný. UE odvozuje příkazy zpětné vazby z Common Pilot Channel ([CPICH](/mobilnisite/slovnik/cpich/)) vysílaného z každé antény. Node B musí přijaté váhové faktory aplikovat s přesným načasováním podle specifikací standardů, aby zajistil, že UE dokáže správně demodulovat složený signál. Výkon CLTD je řízen protokoly vyšší vrstvy Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), které konfigurují parametry a aktivují/deaktivují tuto funkci. Jeho úlohou v síti je zlepšit výkon downlinku, zejména pro uživatele na okraji buňky nebo v náročném rádiovém prostředí, zmírněním účinků vícecestného útlumu a zlepšením spolehlivosti spoje bez zvýšení vysílacího výkonu. To přímo vede k vyšší uživatelské datové propustnosti a lepší kvalitě služeb.

## K čemu slouží

CLTD bylo vytvořeno, aby řešilo základní problém degradace signálu v mobilních bezdrátových kanálech, konkrétně vícecestný útlum, který způsobuje rychlé kolísání síly přijímaného signálu. V raných nasazeních WCDMA mohl být výkon downlinku limitujícím faktorem, zejména pro služby s vysokou datovou rychlostí. Zatímco existovala schémata Open Loop Transmit Diversity (OLTD), nevyužívala informace o stavu kanálu od UE a byla méně účinná v rychle se měnících podmínkách kanálu. Hlavní motivací pro CLTD bylo využít znalost UE o okamžitém downlinkovém kanálu k instruování vysílače, což umožnilo inteligentnější kombinaci signálů, která se v reálném čase přizpůsobuje rádiovému prostředí.

Tento přístup s uzavřenou smyčkou řeší problém fázového nesouladu mezi signály z více vysílacích antén na přijímači. Bez korekce mohou tyto signály dorazit s fázovým posunem a interferovat destruktivně, čímž oslabují celkový přijímaný signál. Tím, že umožňuje UE řídit vysílací fázi Node B, CLTD zajišťuje konstruktivní interferenci a efektivně mění více vysílacích cest ve výhodu. Řeší omezení jednodušších diverzitních metod tím, že poskytuje rychlejší adaptaci a vyšší potenciální zisk, což je klíčové pro podporu vyvíjejících se požadavků na datové služby v sítích UMTS, jako je streamování videa a mobilní přístup k internetu.

Historicky bylo CLTD součástí neustálého úsilí 3GPP o zlepšení spektrální účinnosti a uživatelského zážitku v rámci UMTS. Představovalo krok k pokročilejším víceanténním technikám (MIMO), které se stanou ústředními pro 4G LTE a 5G. Tím, že zlepšilo odolnost downlinku a datové rychlosti bez nutnosti dalšího spektra nebo nadměrného vysílacího výkonu, pomohlo CLTD operátorům maximalizovat využitelnost jejich stávající infrastruktury WCDMA a poskytovat konzistentnější kvalitu služeb.

## Klíčové vlastnosti

- Zpětná vazba od UE v reálném čase přes uplinkové pole FBI (Feedback Information)
- Dva provozní módy: úprava pouze fáze (Mód 1) a společná úprava fáze/amplitudy (Mód 2)
- Využití měření downlinkového CPICH pro výpočet vah
- Synchronní aplikace vah v Node B pro přesné kombinování signálů
- Zlepšení downlinkového SIR a snížení potřebného vysílacího výkonu
- Řízení a konfigurace signalizací vrstvy RRC

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)

## Definující specifikace

- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study

---

📖 **Anglický originál a plná specifikace:** [CLTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/cltd/)
