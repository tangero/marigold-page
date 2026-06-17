---
slug: "ci"
url: "/mobilnisite/slovnik/ci/"
type: "slovnik"
title: "CI – Cancellation Indication"
date: 2025-01-01
abbr: "CI"
fullName: "Cancellation Indication"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ci/"
summary: "Cancellation Indication (CI) je signalizační mechanismus v sítích 3GPP, který umožňuje síti informovat uživatelské zařízení (UE) o zrušení dříve přidělených přenosových zdrojů pro uplink. Tento mechan"
---

CI je signalizační mechanismus v sítích 3GPP, který informuje uživatelské zařízení (UE) o zrušení jemu dříve přidělených přenosových zdrojů pro uplink.

## Popis

Cancellation Indication (CI) funguje jako signalizační mechanismus řídicího kanálu v downlinku v rámci specifikací 3GPP, konkrétně navržený pro správu rádiových zdrojů ve směru uplink. Když síťový prvek (typicky eNodeB v LTE nebo gNB v 5G NR) přidělí prostřednictvím uplink grantu zdroje pro uplink uživatelskému zařízení (UE), mohou nastat okolnosti, kdy je třeba tyto zdroje odvolat ještě předtím, než je UE využije. Mechanismus CI poskytuje standardizovaný způsob, jak síť tuto informaci o zrušení signalizuje dotčenému UE, čímž zabrání jeho přenosu na zdrojích, které již nejsou dostupné nebo vhodné.

Technická implementace CI zahrnuje specifické struktury řídicích kanálů a časové vztahy. V systémech LTE může být CI přenášeno prostřednictvím Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) nebo Enhanced PDCCH ([EPDCCH](/mobilnisite/slovnik/epdcch/)) za použití specifických formátů Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)). Indikace zrušení obsahuje informace identifikující, které dříve přidělené uplinkové zdroje jsou odvolávány, typicky s odkazem na konkrétní podrámce, bloky zdrojů nebo konfigurace grantů. UE monitoruje tyto indikace zrušení podle předdefinovaných časových pravidel, aby bylo schopno na ně vhodně reagovat před svým naplánovaným časem přenosu.

Z architektonického hlediska je funkce CI primárně umístěna ve vrstvě Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) na straně sítě i UE, ačkoliv pro přenos spoléhá na signalizaci fyzické vrstvy. Plánovač sítě má přehled o všech aktivních grantech a může spustit generování CI, když dojde ke konfliktu zdrojů, objeví se vyšší prioritní provoz nebo se změní podmínky interference. Na straně UE entita MAC zpracovává přijaté CI signály a odpovídajícím způsobem aktualizuje svůj přenosový buffer a plánování, případně přerušuje probíhající přípravu na zrušený přenos.

CI plní několik klíčových rolí v moderních mobilních sítích. Umožňuje agresivnější strategie plánování tím, že síti dovoluje podmínečně přidělovat zdroje při zachování možnosti je v případě potřeby zpětně získat. To je zvláště cenné v dynamickém prostředí s rychle se měnícími vzorci provozu nebo podmínkami interference. CI také podporuje pokročilé funkce, jako je uplinková agregace nosných, kde může koordinace zdrojů napříč více nosnými vyžadovat včasné úpravy. Dále v systémech s časovým duplexem (TDD) s flexibilní konfigurací uplink-downlink pomáhá CI řídit přechody mezi směry přenosu tím, že zajišťuje nevyužívání uplinkových zdrojů během přeconfigurovaných period pro downlink.

Návrh tohoto mechanismu zahrnuje aspekty spolehlivosti a zpracování chyb. Protože přehlédnutí indikace zrušení může vést ke kolizím přenosů nebo neefektivnímu využití zdrojů, specifikace obsahuje ustanovení pro robustní přenos CI signálů, často s konzervativnějšími kódovacími poměry než u běžných grantů. Navíc časový odstup mezi přenosem CI a dotčeným uplinkovým přenosem musí poskytovat dostatečnou rezervu pro zpracování v UE, aby bylo zajištěno, že UE může spolehlivě přerušit přípravu svého přenosu.

## K čemu slouží

Cancellation Indication byl zaveden k řešení základních výzev v dynamické správě rádiových zdrojů, které se objevily s paketově orientovanými mobilními sítěmi. Před existencí mechanismů CI měla síť jen omezenou možnost zpětně získat již přidělené uplinkové zdroje pro UE, pokud se podmínky změnily. Tato nepružnost vedla k několika neefektivnostem: přidělené, ale nevyužité zdroje plýtvaly kapacitou, naléhavý vysokoprioritní provoz čelil zpožděním při čekání na uvolnění naplánovaných zdrojů a koordinace interference mezi buňkami byla narušena neschopností rychle upravit uplinkové přenosy v sousedních buňkách.

Vznik CI byl motivován vývojem směrem k sofistikovanějším algoritmům plánování a řízení kvality služeb (QoS) v systémech 3GPP. Jak sítě přecházely od okruhově orientované hlasové služby k paketovým datovým službám s různými požadavky na latenci a propustnost, plánovače potřebovaly větší flexibilitu. CI umožňuje takzvané 'podmínečné plánování' – kdy síť může podmínečně přidělovat zdroje při zachování možnosti jejich zrušení. To je zvláště cenné pro služby jako Voice over LTE (VoLTE), kde náhlá hlasová aktivita vyžaduje okamžité zdroje, nebo pro nouzové služby, které musí přednostně přerušit běžný provoz.

Historicky se omezení řešená CI stala výraznějšími se zavedením LTE a jeho plně IP architektury. Zvýšená závislost na dynamickém plánování pro uplink i downlink, kombinovaná s funkcemi jako semi-persistentní plánování pro hlas, vytvořila scénáře, kde byly konflikty zdrojů nevyhnutelné. Bez CI by síť musela být buď příliš konzervativní v přidělování zdrojů (což snižuje účinnost), nebo tolerovat kolize a opakované přenosy (což zvyšuje latenci a snižuje spolehlivost). CI poskytlo elegantní řešení, které vyvážilo flexibilitu plánování s přenosovou spolehlivostí, a stalo se stále důležitějším v 5G systémech s jejich požadavky na ultra-spolehlivou komunikaci s nízkou latencí (URLLC), kde je přednostní přerušení provozu nezbytné.

## Klíčové vlastnosti

- Umožňuje dynamické odvolání dříve přidělených uplinkových zdrojů
- Podporuje koordinaci interference mezi buňkami tím, že umožňuje včasnou úpravu uplinkových přenosů
- Usnadňuje zpracování priorit a přednostní přerušení pro vysokoprioritní provoz
- Snižuje zbytečné přenosy UE, čímž šetří energii baterie
- Umožňuje agresivnější strategie plánování s podmínečným přidělováním zdrojů
- Poskytuje standardizovanou signalizaci prostřednictvím specifických formátů DCI na downlinkových řídicích kanálech

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TR 28.832** (Rel-18) — Technical Report on URLLC Management
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 36.896** (Rel-14) — Study on Flexible eNB-ID and Cell-ID in E-UTRAN
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [CI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ci/)
