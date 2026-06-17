---
slug: "fs"
url: "/mobilnisite/slovnik/fs/"
type: "slovnik"
title: "FS – DMSU Free Space Data Mode Screen Up"
date: 2026-01-01
abbr: "FS"
fullName: "DMSU Free Space Data Mode Screen Up"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/fs/"
summary: "FS je mechanismus pro přepnutí do datového režimu pro DMSU (Data Mode Screen Up) v prostředí volného prostoru, zavedený ve specifikaci 3GPP Release 12. Jedná se o technickou funkci související s manip"
---

FS je mechanismus pro přepnutí do datového režimu pro DMSU (Data Mode Screen Up) v prostředí volného prostoru, zavedený ve specifikaci 3GPP Release 12 pro manipulaci s daty a správu zobrazení.

## Popis

FS ([DMSU](/mobilnisite/slovnik/dmsu/) Free Space Data Mode Screen Up) je specifický provozní mód a mechanismus pro manipulaci s daty definovaný v rámci standardů 3GPP, primárně referencovaný v technických specifikacích od Release 12 do Release 19. Týká se řízení a filtrování dat v kontextu „volného prostoru“, což je termín používaný pro popis konkrétních přenosových nebo provozních podmínek, které nejsou vázány tradičními omezeními fyzického kanálu. Tato funkce je integrována do širšího rámce DMSU (Data Mode Screen Up), který je zodpovědný za řízení způsobu prezentace, zpracování nebo filtrování dat na obrazovkách uživatelských zařízení (UE) či v datových cestách sítě v určitých módech.

Architektonicky FS funguje jako podfunkce v rámci datové managementové vrstvy zařízení nebo zpracovatelské logiky síťového uzlu. Zahrnuje parametry a procedury, které určují, jak jsou datové toky zpracovávány, když je zařízení nebo síť nakonfigurováno pro provoz v „volném prostoru“. To může souviset se scénáři zahrnujícími specifické konfigurace rádiových prostředků, stavy úspory energie nebo specializované módy poskytování služeb. Specifikace podrobně popisující FS, jako je TS 38.300 (NR and NG-RAN Overall Description) a TS 38.306 (User Equipment (UE) radio access capabilities), ukazují jeho význam pro schopnosti rádiového přístupového sítě (RAN) a chování UE.

Klíčové součásti mechanismu FS zahrnují konfigurační parametry pro datové módy přepnutí zobrazení, časovače pro přechody stavů a kritéria pro vstup do či výstup z datového režimu volného prostoru. Interaguje s protokoly nižších vrstev pro efektivní správu rádiových prostředků a s aplikacemi vyšších vrstev pro zajištění konzistentní prezentace dat. Úlohou FS v síti je optimalizace manipulace s daty a uživatelského zážitku během specifických provozních podmínek, což může přispívat k energetické účinnosti, řízení interference nebo kontinuitě služeb v dynamicky se měnících rádiových prostředích. Jeho časté zmínky napříč specifikacemi fyzické vrstvy, řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a schopností UE podtrhují jeho zásadní průřezový význam pro zajištění spolehlivých a efektivních datových služeb.

## K čemu slouží

Funkce FS byla zavedena k řešení specifických technických požadavků na správu datových módů v rozvíjejících se mobilních sítích, zejména když se standardy 3GPP rozšiřovaly s LTE-Advanced a směrem k 5G NR. Před Release 12 bylo zpracování datových módů a správa zobrazení více obecné a postrádaly optimalizované procedury pro specializované provozní scénáře „volného prostoru“, které se objevily s pokročilými rádiovými technikami a novými případy použití. Vytvoření FS bylo motivováno potřebou standardizovaných a efektivních mechanismů pro řízení prezentace a zpracování dat za těchto jedinečných podmínek, což mělo zajistit interoperabilitu a výkon napříč různými implementacemi UE a nasazeními sítí.

Historicky, jak sítě zaváděly složitější funkce jako agregace nosných ([CA](/mobilnisite/slovnik/ca/)), vylepšené duální spojení ([EN-DC](/mobilnisite/slovnik/en-dc/)) a později schopnosti NR, stalo se řízení datových módů kritičtějším. Koncept „volného prostoru“ pravděpodobně souvisí s provozními stavy, při kterých jsou tradiční předpoklady týkající se kanálu uvolněny, což vyžaduje konkrétní pravidla pro filtrování k zachování kvality služby a účinnosti zařízení. FS řeší problém nekonzistentního zpracování dat během těchto stavů tím, že poskytuje jednotný rámec, který zabraňuje degradaci služby, snižuje spotřebu energie UE a zajišťuje bezproblémový uživatelský zážitek. Odstraňuje tak omezení dřívějších, méně definovaných přístupů tím, že v rámci specifikací 3GPP poskytuje explicitní parametry a procedury, což umožňuje výrobcům a operátorům implementovat robustní a kompatibilní řešení.

## Klíčové vlastnosti

- Definuje standardizovanou proceduru přepnutí do datového režimu pro prostředí volného prostoru
- Integruje se s rámcem DMSU pro konzistentní manipulaci s daty
- Stanovuje konfigurační parametry a časovače pro přechody mezi módy
- Podporuje optimalizaci využití rádiových prostředků během specifických provozních stavů
- Zvyšuje energetickou účinnost UE prostřednictvím řízení zobrazení a zpracování dat
- Zajišťuje interoperabilitu mezi implementacemi UE a sítě prostřednictvím podrobných specifikací

## Související pojmy

- [DMSU – Data Mode Screen Up](/mobilnisite/slovnik/dmsu/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TR 26.999** (Rel-19) — VR Streaming Interoperability Test Material
- **TS 28.532** (Rel-20) — Management and orchestration specification
- **TS 28.545** (Rel-17) — Fault Supervision for 5G Networks
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 37.814** (Rel-12) — L-band Supplemental Downlink for UTRA/E-UTRA
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.561** (Rel-19) — UE Conformance for TRP/TRS FR1
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [FS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fs/)
