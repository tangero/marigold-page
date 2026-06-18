---
slug: "udt"
url: "/mobilnisite/slovnik/udt/"
type: "slovnik"
title: "UDT – SCCP Unitdata Message"
date: 2025-01-01
abbr: "UDT"
fullName: "SCCP Unitdata Message"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/udt/"
summary: "Spojení nevyžadující (connectionless) zpráva SCCP používaná k přenosu signalizačních dat bez navázání virtuálního okruhu. Poskytuje základní datagramovou službu pro signalizační síťové prvky, umožňují"
---

UDT je spojení nevyžadující (connectionless) zpráva SCCP používaná k přenosu signalizačních dat jako datagram bez nutnosti navázání virtuálního okruhu, což umožňuje efektivní přenos krátkých zpráv.

## Popis

Zpráva [SCCP](/mobilnisite/slovnik/sccp/) Unitdata (UDT) je základní součást protokolu Signalizační spojovací řídicí část (SCCP) v rámci signalizačního systému [SS7](/mobilnisite/slovnik/ss7/)/C7, který je nedílnou součástí tradičních okruhově přepínaných a raných paketově přepínaných jader sítí v architekturách 3GPP. SCCP pracuje na vrstvě 4 zásobníku protokolů SS7 a poskytuje rozšířené směrovací a řídicí schopnosti nad základní přenosovou částí zpráv ([MTP](/mobilnisite/slovnik/mtp/)). Zpráva UDT je spojení nevyžadující služba, což znamená, že před přenosem dat nevyžaduje navázání a udržování logického spojení neboli virtuálního okruhu mezi signalizačními body. Každá zpráva UDT je nezávislý datagram obsahující kompletní adresní informace – konkrétně adresu volaného účastníka (CdPA) a adresu volajícího účastníka (CgPA) – spolu s uživatelskými daty neboli signalizační informací, která má být doručena. Vrstva SCCP v uzlu původu směruje UDT na základě CdPA, přičemž využívá služby MTP pro skutečný přenos přes signalizační síť. Po přijetí vrstva SCCU v cílovém uzlu zprávu zpracuje a doručí uživatelská data příslušné aplikaci vyšší vrstvy, jako je [MAP](/mobilnisite/slovnik/map/) nebo [BSSAP](/mobilnisite/slovnik/bssap/).

Architektura podporující UDT zahrnuje entitu protokolu SCCP na každém signalizačním bodě, která rozhraní s MTP níže a s různými aplikačními částmi výše. Klíčové komponenty ve formátu zprávy UDT zahrnují diskriminátor protokolu pro identifikaci SCCP, kód typu zprávy pro UDT a parametry pro délku, povinné pevné části (jako CdPA a CgPA) a volitelné proměnné části obsahující vlastní uživatelská data a případné volitelné parametry, jako jsou indikátory segmentace nebo pořadí, ačkoli plná segmentace základní UDT nepodporuje. Směrovací schopnost SCCP, využívající překlad globálního názvu ([GT](/mobilnisite/slovnik/gt/)), umožňuje směrování zpráv UDT na základě volaných číslic nebo jiných identifikátorů, což poskytuje flexibilní a škálovatelnou signalizaci napříč mezinárodními a národními sítěmi bez nutnosti, aby každý uzel znal bodový kód všech ostatních uzlů.

V kontextu sítě 3GPP se zprávy UDT používají v mnoha procedurách, zejména v raných vydáních ([R99](/mobilnisite/slovnik/r99/) a Rel-4), pro signalizaci nesouvisející s okruhem, kde není odůvodněno trvalé spojení. Používají se například pro aktualizaci polohy, autentizaci účastníka a doručování služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)) mezi prvky jádra sítě, jako je HLR, VLR a MSC. Úlohou UDT je poskytnout odlehčený a efektivní mechanismus pro přenos samostatných jednotek signalizačních dat, minimalizující signalizační zátěž a zpoždění pro transakce, které jsou krátké a uzavřené. Zatímco pozdější architektury 3GPP se vyvíjely směrem k IP-based signalizačním protokolům, jako jsou SIGTRAN a Diameter, zpráva UDT a spojení nevyžadující služba SCCP zůstaly základním kamenem pro legacy propojení a určité administrativní funkce, zajišťující zpětnou kompatibilitu a spolehlivý signalizační přenos v hybridních síťových prostředích.

## K čemu slouží

Zpráva SCCP Unitdata byla vytvořena, aby uspokojila potřebu jednoduchého, efektivního a spojení nevyžadujícího mechanismu pro přenos signalizace v telekomunikačních sítích založených na standardu SS7. Před vývojem SCCP byla signalizace primárně zajišťována přenosovou částí zpráv (MTP), která poskytovala základní směrování zpráv na bázi fyzických bodových kódů, ale postrádala flexibilitu pro pokročilé adresování na aplikační úrovni a globální směrování. Toto omezení se stalo palčivým s růstem mobilních sítí a služeb inteligentní sítě, které vyžadovaly signalizační transakce mezi uzly, které nemusely mít přímý vztah prostřednictvím bodových kódů, nebo které bylo potřeba identifikovat logickými adresami (jako čísla účastníků). Služba UDT to řeší tím, že umožňuje směrování signalizačních zpráv pomocí globálních názvů, což umožňuje dotazování databází, jako jsou HLR, z libovolného síťového uzlu bez předem nakonfigurovaných přímých signalizačních spojů.

Motivace pro spojení nevyžadující službu, na rozdíl od spojované, vychází z povahy mnoha signalizačních transakcí, které jsou krátké interakce typu požadavek-odpověď a neodůvodňují režii spojenou s navázáním a zrušením virtuálního okruhu. Příklady zahrnují dotazování databáze na data účastníka nebo doručení jedné SMS. Navázání spojení SCCP by vyžadovalo další zprávy (požadavek na spojení a potvrzení) a udržování stavu na obou koncích, což by spotřebovávalo síťové prostředky a zvyšovalo latenci u jednoduchých transakcí. UDT poskytuje službu podobnou datagramu, která tuto režii minimalizuje, a nabízí nižší latenci a sníženou signalizační zátěž pro takové aplikace. Řeší tak problém efektivní a škálovatelné signalizace pro funkce nesouvisející s okruhem, což bylo zásadní pro nasazení pokročilých mobilních služeb, jako je roaming a SMS v sítích GSM a UMTS.

Historicky byla UDT zavedena v 3GPP R99 jako součást zděděného signalizačního rámce jádra sítě GSM/SS7. Její vytvoření bylo motivováno potřebou podporovat narůstající signalizační provoz spojený se správou mobility, doplňkovými službami nezávislými na hovoru a SMS standardizovaným a interoperabilním způsobem. Zatímco pozdější vydání 3GPP zavedla IP-based alternativy, UDT zůstala relevantní pro propojení se legacy SS7 sítěmi a pro určité interní procedury jádra sítě, čímž zajišťovala kontinuitu a spolehlivost při vývoji sítí. Omezení, která řešila – konkrétně neefektivní okruhově orientovaná signalizace pro krátké transakce a nepružné směrování založené na MTP – byla kritickými úzkými místy v raných digitálních telekomunikačních sítích a spojení nevyžadující model UDT poskytl robustní řešení, které podpořilo desetiletí spolehlivé signalizace.

## Klíčové vlastnosti

- Spojení nevyžadující (connectionless) datagramová služba pro přenos signalizačních dat
- Používá směrování SCCP pomocí globálního názvu (Global Title) pro flexibilní, databázemi řízené adresování
- Nese v každé zprávě kompletní adresní informace (CdPA a CgPA)
- Podporuje přenos uživatelských dat pro aplikace vyšších vrstev, jako je MAP
- Minimální režie ve srovnání se spojovanými službami SCCP
- Umožňuje efektivní signalizaci založenou na transakcích pro procedury mobilních sítí

## Související pojmy

- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)
- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 24.007** (Rel-19) — GSM Um Interface Layer 3 Architecture
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [UDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/udt/)
