---
slug: "cot"
url: "/mobilnisite/slovnik/cot/"
type: "slovnik"
title: "COT – Channel Occupancy Time"
date: 2025-01-01
abbr: "COT"
fullName: "Channel Occupancy Time"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cot/"
summary: "Channel Occupancy Time (COT, doba obsazení kanálu) je regulatorní a technický koncept definující maximální nepřerušovanou dobu, po kterou může zařízení vysílat na sdíleném nebo nelicencovaném rádiovém"
---

COT je maximální nepřerušovaná doba, po kterou může zařízení vysílat na sdíleném nebo nelicencovaném rádiovém kanálu, čímž zajišťuje spravedlivé sdílení spektra a dodržování regulatorních požadavků.

## Popis

Channel Occupancy Time (COT, doba obsazení kanálu) je základní parametr pro provoz ve sdíleném a nelicencovaném spektru, definovaný ve specifikacích 3GPP pro technologie jako Licensed-Assisted Access ([LAA](/mobilnisite/slovnik/laa/)), MulteFire a New Radio in Unlicensed spectrum ([NR-U](/mobilnisite/slovnik/nr-u/)). Určuje maximální dobu, po kterou může gNB (základnová stanice) nebo UE (uživatelské zařízení) nepřetržitě obsadit kanál po úspěšném získání přístupu prostřednictvím procedury Listen-Before-Talk ([LBT](/mobilnisite/slovnik/lbt/)). Délka COT není 3GPP pevně stanovena, ale je omezena regionálními regulatorními požadavky, které určují maximální hodnoty (např. 4 ms, 6 ms, 10 ms) a související pravidla, jako je povinná klidová perioda (neboli doba uvolnění kanálu), která musí následovat po vysílacím bloku.

Z architektonického hlediska je správa COT integrována do vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a fyzické vrstvy ([PHY](/mobilnisite/slovnik/phy/)) rádiového protokolového stacku. Proces začíná procedurou LBT kategorie 4, což je mechanismus snímání nosné s náhodným odstupem, podobný Wi-Fi [CSMA/CA](/mobilnisite/slovnik/csma-ca/). Po zisku kanálu iniciující uzel (kterým může být gNB nebo UE v uplinku) spustí časovač odpovídající povolenému maximu COT. Během této COT může uzel vysílat downlink data, uplink přístupová práva a přidružené řídicí informace. Klíčovou vlastností je sdílení COT, kdy iniciující uzel může přidělit části své zbývající COT jiným zařízením (např. gNB sdílí s naplánovanými UE pro uplink přenos) bez nutnosti, aby tato zařízení prováděla plné LBT, čímž se zvyšuje efektivita a snižuje latence.

Struktura COT je rozdělena na vysílací bloky a klidové mezery. V rámci jedné COT mohou být přenosy nespojité, přičemž krátké mezery (např. do 16 μs) se nezapočítávají do doby obsazení, což umožňuje flexibilitu v plánování. Po vypršení COT musí uzel kanál uvolnit na minimální klidovou periodu, což umožňuje jiným systémům soutěžit o přístup. Tento cyklický proces LBT, COT a klidové periody tvoří základ spravedlivé koexistence. V 5G NR-U se správa COT stala dynamičtější, podporuje flexibilní numerologii a adaptivní délky COT na základě priority provozu a stavu kanálu, což je klíčové pro splnění přísných požadavků na QoS pro ultra-spolehlivé nízkolatenční komunikace ([URLLC](/mobilnisite/slovnik/urllc/)) a rozšířené mobilní širokopásmové služby (eMBB) v nelicencovaných pásmech.

## K čemu slouží

COT byl zaveden, aby umožnil buněčným systémům fungovat spravedlivě a legálně v nelicencovaných pásmech spektra, jako jsou pásma 5 GHz U-NII a pásmo 6 GHz, která jsou globálně dostupná, ale podléhají přísným regulatorním požadavkům zajišťujícím koexistenci se zavedenými technologiemi, jako je Wi-Fi a radarové systémy. Před [LAA](/mobilnisite/slovnik/laa/) a NR-U fungovaly buněčné sítě výhradně v licencovaném spektru, což zaručovalo provoz bez rušení, ale s omezenou dostupnou šířkou pásma. Exploze mobilního datového provozu vyvolala potřebu dodatečné kapacity, což vedlo 3GPP ke standardizaci přístupu k nelicencovanému spektru. Bez mechanismu jako je COT by však buněčné základnové stanice mohly vysílat nepřetržitě, což by způsobovalo škodlivé rušení a monopolizaci sdílených kanálů, což by porušovalo regulace a zhoršovalo výkon pro všechny uživatele.

Hlavním problémem, který COT řeší, je regulatorní soulad pro spravedlivé sdílení spektra. Předpisy v regionech jako Evropa (ETSI EN 301 893) a Spojené státy (FCC Part 15) nařizují LBT a ukládají maximální doby vysílání, aby se zabránilo zabírání kanálu. COT poskytuje technický rámec pro systémy 3GPP, aby tato pravidla dodržovaly. Dále COT řeší technickou výzvu koexistence s ne-3GPP systémy, především s Wi-Fi. Omezením nepřetržité doby vysílání a vynucením klidových period COT zajišťuje, že zařízení Wi-Fi mají pravidelné příležitosti pro přístup ke kanálu, čímž vytváří rovné podmínky. To byl klíčový designový cíl pro získání regulatorního schválení a přijetí v odvětví pro buněčné technologie v nelicencovaných pásmech.

Historicky byl koncept poprvé podrobně popsán v 3GPP Release 13 pro LTE-LAA, čerpající z existujících regulací pro Wi-Fi a radarové systémy. Jeho vytvoření bylo motivováno potřebou zvýšit kapacitu LTE prostřednictvím agregace nosných s nelicencovanými nosnými, a zároveň být 'dobrým sousedem' pro jiné technologie. Vývoj přes Release 14, 15 a dále pro NR-U rozšířil roli COT, aby podporoval složitější případy užití 5G, což vyžaduje sofistikovanější mechanismy sdílení a adaptivní načasování pro splnění různých servisních požadavků, a to vše při zachování základního principu vynucených limitů vysílání, aby sdílené spektrum zůstalo životaschopným zdrojem pro více přístupových technologií.

## Klíčové vlastnosti

- Definuje maximální nepřerušovanou dobu vysílání po úspěšném LBT
- Umožňuje dodržování regulatorních požadavků pro provoz v nelicencovaných pásmech spektra
- Podporuje sdílení COT, což iniciujícímu uzlu umožňuje přidělit části své COT jiným zařízením bez nutnosti, aby tato zařízení prováděla plné LBT
- Usnadňuje spravedlivou koexistenci s jinými systémy, jako je Wi-Fi, vynucováním povinných klidových period po obsazení
- Je integrován s procedurami LBT (např. LBT kat. 4) jako součást mechanismu přístupu ke kanálu
- Má přizpůsobitelnou délku na základě regionálních regulací a stavu kanálu, zejména v NR-U pro 5G

## Definující specifikace

- **TS 23.284** (Rel-19) — Local Call Local Switch Stage 2
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.789** (Rel-13) — LAA Multi-Node Coexistence Test Methodology
- **TS 37.213** (Rel-19) — Shared Spectrum Physical Layer Procedures
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding

---

📖 **Anglický originál a plná specifikace:** [COT na 3GPP Explorer](https://3gpp-explorer.com/glossary/cot/)
