---
slug: "cdi"
url: "/mobilnisite/slovnik/cdi/"
type: "slovnik"
title: "CDI – Collision Detection Indicator"
date: 2025-01-01
abbr: "CDI"
fullName: "Collision Detection Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cdi/"
summary: "CDI je signál fyzické vrstvy používaný v uplinku 3GPP UTRA TDD (TD-CDMA) k indikaci detekce kolize na kanálu náhodného přístupu (RACH). Je vysílán Node B, aby informoval uživatelské zařízení (UE), že"
---

CDI je signál fyzické vrstvy v 3GPP UTRA TDD, který indikuje detekci kolize na kanálu náhodného přístupu (RACH), informuje UE, že jeho pokus o přístup selhal, a spouští retransmisi.

## Popis

Collision Detection Indicator (CDI) je specifický řídicí signál fyzické vrstvy definovaný v rámci 3GPP [UTRA](/mobilnisite/slovnik/utra/) [TDD](/mobilnisite/slovnik/tdd/) (Time Division Duplex) módu, známého také jako [TD-CDMA](/mobilnisite/slovnik/td-cdma/), dle specifikace TS 25.211. Funguje v rámci přenosového rámce uplinku. CDI není samostatný kanál, ale specifický indikační bit nebo vzor, který je vysílán Node B (základnovou stanicí) na downlinkovém fyzickém kanálu, typicky v reakci na signály přijaté na uplinkovém kanálu náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)). Jeho primární funkcí je poskytnout rychlou zpětnou vazbu na fyzické vrstvě uživatelskému zařízení (UE), které zahájilo pokus o náhodný přístup.

Když UE potřebuje navázat počáteční spojení nebo požádat o zdroje, vyšle preambuli na uplinkovém RACH. V TDD systémech může více UE zkusit přístup současně, což vede ke kolizím, pokud zvolí stejnou preambuli a přístupový časový slot. Přijímač Node B provádí korelační detekci na přijatých RACH preambulích. Pokud úspěšně detekuje a dekóduje preambuli bez interference, pokračuje standardní procedurou náhodného přístupu. Pokud však detekuje energii naznačující více překrývajících se preambulí (kolizi), ale nedokáže úspěšně dekódovat žádnou z nich, vygeneruje signál CDI.

CDI je vysílán Node B v předdefinovaném downlinkovém časovém slotu a struktuře fyzického kanálu, což zajišťuje, že jej UE může sledovat krátce po svém přenosovém pokusu. Po přijetí CDI jej UE interpretuje jako negativní potvrzení specificky pro kolizi, odlišné od pouhého selhání zachycení preambule. To spustí v Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) vrstvě UE algoritmus odložení. UE poté počká po náhodně vypočítaný časový interval před novým pokusem o proceduru náhodného přístupu s novou preambulí. Tato okamžitá zpětnovazební smyčka na fyzické vrstvě snižuje čas, který by UE ztratilo čekáním na timeout vyšší vrstvy, a pomáhá rychle řešit soutěžení, protože rozptyluje pokusy o opětovný přenos v čase, čímž snižuje pravděpodobnost opakovaných kolizí.

Architektura podporující CDI zahrnuje těsnou koordinaci mezi fyzickou vrstvou a MAC vrstvou jak v UE, tak v Node B. Klíčové komponenty zahrnují RACH vysílač v UE, RACH přijímač a obvody pro detekci kolizí v Node B a downlinkový vysílač fyzického kanálu pro CDI. Jeho role je zásadní pro efektivní řešení soutěžení v TDD-based buněčných sítích, přímo ovlivňuje latenci počátečního přístupu, kapacitu systému pro přístupové požadavky a celkové využití rádiových zdrojů během kritické fáze navazování spojení.

## K čemu slouží

CDI byl vytvořen k řešení specifické výzvy efektivního řešení kolizí na soutěživých kanálech náhodného přístupu v rámci 3GPP [UTRA](/mobilnisite/slovnik/utra/) [TDD](/mobilnisite/slovnik/tdd/) ([TD-CDMA](/mobilnisite/slovnik/td-cdma/)) systému. V raných 3G standardech byl kanál náhodného přístupu (RACH) základním mechanismem pro UE k navázání kontaktu se sítí, ale byl náchylný ke kolizím, když se více zařízení pokoušelo o přístup současně. Bez rychlé indikace kolize by se UE musela spoléhat na vypršení časovačů na vyšších vrstvách (jako je MAC vrstva), aby usoudila na selhání, což vedlo ke zvýšené latenci při navazování spojení a neefektivnímu využití rádiových zdrojů, protože kolidující UE by mohla retransmitovat ve stejný čas.

Motivace pro CDI vycházela z charakteristiky TDD provozu a snahy optimalizovat výkon systému. TDD systémy používají stejnou frekvenci pro uplink a downlink, oddělené v čase. To umožňuje rychlé obraty řídicích signálů. Konstruktéři toho využili k implementaci zpětnovazebního mechanismu na fyzické vrstvě, který je rychlejší než signalizace vyšších vrstev. CDI poskytuje okamžitou, explicitní zpětnou vazbu, informující UE o události kolize ve velmi krátkém čase po jejím přenosovém pokusu.

Tento přístup vyřešil omezení čistě časovačových nebo implicitních detekčních metod používaných v některých starších systémech nebo v FDD módu UTRA. Explicitní signalizací kolize může síť inteligentněji řídit chování UE při opakovaném vysílání a přimět je k odložení přenosu koordinovaným způsobem. To snižuje pravděpodobnost kolizí v následujících pokusech, snižuje zpoždění přístupu a zvyšuje celkovou kapacitu a spolehlivost procedury náhodného přístupu, což je klíčové pro podporu velkého počtu zařízení a služeb s nízkými požadavky na latenci.

## Klíčové vlastnosti

- Zpětnovazební signál fyzické vrstvy pro rychlé oznámení kolize
- Specificky navržen pro kanál náhodného přístupu (RACH) v UTRA TDD (TD-CDMA)
- Spouští okamžitou proceduru odložení na MAC vrstvě v UE
- Snižuje latenci náhodného přístupu tím, že se vyhne timeoutům vyšších vrstev
- Zlepšuje kapacitu systému rozptýlením pokusů o opětovný přenos
- Explicitně rozlišuje selhání kvůli kolizi od jiných druhů selhání příjmu

## Související pojmy

- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [TD-CDMA – Time Division - Code Division Multiple Access](/mobilnisite/slovnik/td-cdma/)

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels

---

📖 **Anglický originál a plná specifikace:** [CDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdi/)
