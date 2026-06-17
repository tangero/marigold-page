---
slug: "em"
url: "/mobilnisite/slovnik/em/"
type: "slovnik"
title: "EM – Electromagnetic Emanations"
date: 2026-01-01
abbr: "EM"
fullName: "Electromagnetic Emanations"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/em/"
summary: "EM označuje nezáměrné elektromagnetické záření vysílané telekomunikačními zařízeními. Jeho regulace je klíčová pro soulad s předpisy, bezpečnost a správu rušení. Normy definují metody měření a limity,"
---

EM (Electromagnetic Emanations) označuje nezáměrné elektromagnetické záření vysílané telekomunikačními zařízeními, které je regulováno za účelem zajištění shody, bezpečnosti a prevence škodlivého rušení nebo úniku informací.

## Popis

Elektromagnetické emise (EM) zahrnují nezáměrné elektromagnetické záření, které je za normálního provozu vysíláno z elektronických a telekomunikačních zařízení. Toto záření může pocházet z různých zdrojů uvnitř zařízení, jako jsou oscilátory, digitální obvody, napájecí zdroje a propojovací kabely. V kontextu norem 3GPP se EM řeší primárně ze dvou perspektiv: elektromagnetické kompatibility ([EMC](/mobilnisite/slovnik/emc/)) pro zajištění vzájemného nerušení zařízení a bezpečnosti pro prevenci úniku informací prostřednictvím kompromitujících emisí (často označovaných jako TEMPEST problematika). Technické specifikace definují přísné postupy měření, testovací prostředí (např. bezodrazové komory, otevřená testovací místa) a limity pro vyzařované a vedené emise v širokém frekvenčním spektru, typicky od několika kHz až po několik GHz, v závislosti na typu zařízení a jeho provozních pásmech.

Architektura pro správu EM zahrnuje úvahy jak ve fázi návrhu, tak testování po výrobě. Ve fázi návrhu inženýři používají techniky jako stínění, filtrování, uzemnění a pečlivé rozmístění desek plošných spojů, aby emise minimalizovali. Specifikace 3GPP, zejména v řadě 32 (Management) a 38 (NG-RAN), odkazují na harmonizované normy (např. od [ETSI](/mobilnisite/slovnik/etsi/) a CISPR), které definují přesné testovací sestavy včetně typů antén, měřicích vzdáleností a detekčních funkcí (např. špičková, kvazišpičková, průměrná). U síťových zařízení, jako jsou základnové stanice (NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB), testy hodnotí emise z krytu a přidruženého kabelového vedení. U uživatelských zařízení (UE) se testy provádějí v konkrétních provozních režimech (např. vysílání s maximálním výkonem), aby simulovaly nejhorší reálné scénáře.

Jejich role v síti je zásadní pro regulatorní shodu a koexistenci. Každá země má regulační orgány (např. [FCC](/mobilnisite/slovnik/fcc/) v USA, [CE](/mobilnisite/slovnik/ce/) značení v Evropě), které ukládají limity EM, aby zabránily zařízením v působení škodlivého rušení jiným radiovým službám, jako je letectví, vysílání nebo nouzová komunikace. Dále, z bezpečnostního hlediska, by nekontrolované EM emise mohly umožnit odposlech zpracovávaných dat, což z kontroly EM činí součást širšího zajištění bezpečnosti zařízení. Specifikace 3GPP zajišťují, že síťová infrastruktura a uživatelská zařízení jsou navržena jako dobré elektromagnetické subjekty, což umožňuje hustá, heterogenní nasazení charakteristická pro moderní mobilní sítě bez degradace celkové kvality rádiového prostředí.

## K čemu slouží

Účelem standardizace požadavků na elektromagnetické emise (EM) je zajistit spolehlivý a bezpečný provoz mobilních sítí ve sdíleném elektromagnetickém prostředí. Bez takových kontrol by rychlá proliferace bezdrátových zařízení a infrastruktury mohla vést k rozsáhlému rušení, které by degradovalo výkon nejen mobilních služeb, ale i dalších kritických rádiových systémů. Historicky, jak se telekomunikační zařízení stávala složitějšími a hustěji nasazovanými, významně rostlo riziko vzájemného rušení zařízení, což si vyžádalo mezinárodně harmonizované technické normy nahrazující nesourodou mozaiku národních předpisů.

Normy EM řeší problém nepředvídatelného elektromagnetického znečištění. Poskytují společný rámec pro výrobce, aby navrhovali zařízení, která inherentně minimalizují nežádoucí emise, čímž se snižuje potřeba nákladných dodatečných úprav nebo specifických opatření po nasazení. To je obzvláště klíčové pro síťové operátory, kteří nasazují zařízení od více dodavatelů; konzistentní EM výkon je nezbytný pro předvídatelné chování sítě. Dále řešení EM z bezpečnostní perspektivy zmírňuje riziko útoků vedlejším kanálem, kdy by citlivé informace (např. šifrovací klíče) mohly být extrahovány z nezáměrného záření zařízení, což je obava pro vládní, vojenská a podniková nasazení s vysokými bezpečnostními nároky.

Motivace pro jeho zavedení v rámci 3GPP vychází z potřeby odkazovat na komplexní, průmyslem přijímané normy [EMC](/mobilnisite/slovnik/emc/). Zatímco 3GPP se zaměřuje na rádiové a síťové protokolové aspekty, provozní realita vyžaduje, aby toto zařízení fungovalo v reálném světě. Proto specifikace 3GPP odkazováním začleňují podrobné testovací normy z organizací jako [ETSI](/mobilnisite/slovnik/etsi/) a CISPR, čímž zajišťují, že zařízení vyhovující 3GPP jsou také navržena tak, aby splňovala globální předpisy pro elektromagnetickou kompatibilitu a emise, což usnadňuje mezinárodní obchod a nasazení.

## Klíčové vlastnosti

- Definuje limity pro nezáměrné vyzařované elektromagnetické emise
- Specifikuje metodiky měření a testovací sestavy pro různé typy zařízení
- Pokrývá široký frekvenční rozsah relevantní pro mobilní a přilehlé služby
- Řeší emise jak z krytu zařízení, tak z přidružených kabelů
- Zahrnuje bezpečnostní hlediska pro prevenci kompromitujících emisí
- Odkazuje na harmonizované mezinárodní normy (např. ETSI EN, CISPR) pro globální shodu

## Související pojmy

- [EMC – Electromagnetic Compatibility](/mobilnisite/slovnik/emc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.625** (Rel-19) — State Management Data Definition IRP Information Service
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 28.655** (Rel-19) — GERAN NRM IRP Information Service
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 28.752** (Rel-19) — SuM NRM IRP Information Service
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- … a dalších 97 specifikací

---

📖 **Anglický originál a plná specifikace:** [EM na 3GPP Explorer](https://3gpp-explorer.com/glossary/em/)
