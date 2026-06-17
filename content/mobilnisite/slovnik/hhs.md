---
slug: "hhs"
url: "/mobilnisite/slovnik/hhs/"
type: "slovnik"
title: "HHS – Hand-held Speakerphone"
date: 2025-01-01
abbr: "HHS"
fullName: "Hand-held Speakerphone"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hhs/"
summary: "Hand-held Speakerphone (HHS), známý také jako hand-held hands-free, je režim hlasové komunikace, při kterém uživatel drží zařízení v ruce, ale pro poslech a snímání hlasu využívá vestavěný hlasitý rep"
---

HHS je standardizovaný režim hlasové komunikace podle 3GPP, při kterém uživatel drží zařízení v ruce, ale pro plně duplexní konverzaci bez použití rukou využívá jeho vestavěný hlasitý reproduktor a mikrofon.

## Popis

Režim Hand-held Speakerphone (HHS) je definovaný provozní stav uživatelského zařízení (UE), standardizovaný organizací 3GPP za účelem zajištění konzistentního audio výkonu při použití zařízení jako hands-free. V tomto režimu je UE drženo v ruce uživatele (nenošeno na hlavě) a audio je přehráváno přes hlavní hlasitý reproduktor zařízení, zatímco primární mikrofon(y) snímají uživatelův hlas. To kontrastuje s tradičním režimem 'handset', kdy je akustický měnič přikládán k uchu, a s režimem 'hands-free', který typicky znamená použití externí příslušenství, jako je Bluetooth headset nebo hands-free sada v autě. Režim HHS je v podstatě akustické řešení hands-free integrované přímo v zařízení.

Technicky vzato aktivace režimu HHS spouští specifické algoritmy zpracování signálu v audio subsystému UE. Klíčovou výzvou je zvládnutí akustické ozvěny a zlepšení snímání hlasu v potenciálně hlučném prostředí. Protože hlasitý reproduktor a mikrofon jsou v těsné blízkosti na stejném zařízení, mikrofon snímá výstup z reproduktoru, což vytváří silnou akustickou ozvěnu pro účastníka na druhém konci hovoru. Z tohoto důvodu je robustní potlačení akustické ozvěny ([AEC](/mobilnisite/slovnik/aec/)) povinnou součástí. Dále, mikrofon není umístěn blízko úst, proto jsou využívány algoritmy pro formování svazku, potlačení šumu a řízení zesílení, aby byl vylepšen signál řeči z blízkého konce a potlačen šum v pozadí a vlastní výstup uživatele z reproduktoru.

Specifikace 3GPP, konkrétně TS 26.931, definují výkonnostní požadavky pro režim HHS. Ty zahrnují minimální požadavky na hlasitost reproduktoru, citlivost mikrofonu a účinnost potlačení ozvěny a šumu. Standard například definuje metriky jako Terminal Coupling Loss (TCL), která měří, jak moc je ozvěna potlačena ekokancelérem. Dále specifikuje testovací scénáře a podmínky šumu v pozadí, aby zajistil, že zařízení poskytují přijatelnou a interoperabilní kvalitu zvuku. Implementace zahrnuje úzkou koordinaci mezi hlasovým kodekem v modemu (např. [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/)) a řetězcem digitálního zpracování audio signálu ([DSP](/mobilnisite/slovnik/dsp/)) v aplikačním procesoru.

Z pohledu sítě signalizuje UE své schopnosti týkající se režimu HHS během sestavování hovoru nebo prostřednictvím jiných mechanismů výměny informací o schopnostech. Samotná síť je k tomuto režimu z velké části agnostická; hlasový proud je stále normálně kódován a paketizován. Použití režimu HHS však může ovlivnit uživatelský dojem z kvality hlasu, protože akustické prostředí hraje větší roli. Standardizace zajišťuje, že bez ohledu na výrobce zařízení, když uživatel aktivuje režim hands-free, je zachována základní úroveň srozumitelnosti zvuku a výkonu bez ozvěny, což je klíčové pro interoperabilitu služeb a spokojenost uživatelů.

## K čemu slouží

Funkce HHS byla standardizována, aby řešila rostoucí používání mobilních zařízení jako hands-free, což byl režim, který se stával stále běžnějším, ale byl dříve implementován ad-hoc, specifickým způsobem pro každého výrobce. Bez standardizace by se kvalita zvuku – zejména úroveň potlačení ozvěny a zpracování šumu v pozadí – mohla mezi zařízeními drasticky lišit, což by vedlo ke špatným uživatelským zkušenostem a stížnostem během hovorů. Účelem bylo definovat minimální laťku výkonu pro tento základní způsob použití.

Řeší několik praktických problémů. Za prvé zmírňuje silnou akustickou ozvěnu, která vzniká, když výstup z hlasitého reproduktoru zařízení snímá jeho vlastní mikrofon, což může hovor znemožnit. Povinným požadavkem na účinné [AEC](/mobilnisite/slovnik/aec/) zajišťuje srozumitelnost hovoru. Za druhé zlepšuje srozumitelnost řeči v typických případech použití hands-free (např. v místnosti nebo autě), kde je mikrofon daleko od úst a je přítomen okolní šum. Standardizované potlačení šumu tomu napomáhá. Nakonec umožňuje bezpečné používání při řízení, protože mnoho regionů povoluje používání zařízení v režimu hands-free a vestavěný hands-free režim je nejdostupnější formou takového provozu.

Jeho vytvoření bylo motivováno potřebou konzistence kvality služeb. Jak se mobilní telefony vyvinuly z čistě hlasových zařízení na multimediální nástroje, funkce hands-free se stala základní utilitou pro skupinové konverzace, multitasking a použití v vozidle. Standardizace 3GPP zajišťuje, že tato utility funguje spolehlivě napříč ekosystémem, podporujícím jak základní telefonii, tak bohatší komunikační služby jako Voice over LTE (VoLTE) a Voice over NR (VoNR), kde se používají vysokokvalitní hlasové kodeky, což činí dobý akustický výkon ještě kritičtějším.

## Klíčové vlastnosti

- Definuje akustické a audio požadavky na použití vestavěného hands-free režimu zařízení
- Ukládá povinnost robustního potlačení akustické ozvěny (AEC) pro prevenci ozvěny na vzdáleném konci
- Specifikuje potlačení šumu a řízení zesílení mikrofonu pro snímání řeči na dálku
- Zahrnuje výkonnostní metriky jako Terminal Coupling Loss (TCL) pro potlačení ozvěny
- Zajišťuje interoperabilitu a konzistentní uživatelský zážitek napříč různými modely UE
- Podporuje bezpečný provoz v režimu hands-free, zvláště relevantní pro případy použití v automobilu

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 26.931** (Rel-19) — Acoustic Requirements Study for Terminals

---

📖 **Anglický originál a plná specifikace:** [HHS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hhs/)
