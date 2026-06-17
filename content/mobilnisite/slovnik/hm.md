---
slug: "hm"
url: "/mobilnisite/slovnik/hm/"
type: "slovnik"
title: "HM – High Mobility"
date: 2025-01-01
abbr: "HM"
fullName: "High Mobility"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hm/"
summary: "High Mobility (HM) je soubor funkcí 3GPP umožňující spolehlivou komunikaci pro uživatele pohybující se velmi vysokou rychlostí, například ve vysokorychlostních vlacích. Řeší výzvy jako výrazný Doppler"
---

HM je soubor funkcí 3GPP, který umožňuje spolehlivou komunikaci pro uživatele pohybující se velmi vysokou rychlostí tím, že řeší výzvy jako výrazný Dopplerův jev a rychlé změny buněk.

## Popis

High Mobility (HM) je komplexní soubor technických vylepšení definovaných ve specifikacích 3GPP, primárně v TS 26.935, pro podporu uživatelského zařízení (UE) pracujícího při velmi vysokých rychlostech, typicky až 350 km/h nebo více, jak je tomu u vysokorychlostní železniční dopravy. Hlavní výzvou v takovém prostředí je extrémní Dopplerův jev, který způsobuje výrazný posun frekvence přijímaného signálu, což může vést k selhání demodulace a degradaci výkonu spojení. HM zahrnuje pokročilé algoritmy jak v UE, tak v síti pro odhad a kompenzaci tohoto Dopplerova posunu v reálném čase, což zajišťuje přesné dekódování přijímaného signálu.

Z architektonického hlediska je podpora HM integrována napříč rádiovým protokolovým stackem a zahrnuje vylepšení fyzické vrstvy, řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) a správy mobility. Mezi klíčové komponenty patří pokročilé techniky odhadu kanálu, robustnější návrh referenčních signálů a optimalizované procedury předávání spojení. Fyzická vrstva využívá častější a přesnější sledování informací o stavu kanálu pro přizpůsobení rychlým změnám kanálu. RRC vrstva je rozšířena o parametry a signalizaci pro podporu rychlejšího a spolehlivějšího předávání spojení mezi buňkami, což minimalizuje přerušení služeb při vysokorychlostním pohybu.

Její úlohou v síti je garantovat kvalitu služeb (QoS) a kontinuitu služeb pro kritickou třídu mobilních uživatelů. Síťoví operátoři nasazují funkce HM v buňkách podél vysokorychlostních železničních koridorů nebo dálnic. Síť musí být schopna detekovat UE s vysokou mobilitou, často prostřednictvím měřicích hlášení indikujících vysoký Dopplerův jev nebo rychlost, a následně aplikovat příslušné konfigurace HM. Toto zajišťuje, že základní služby jako hlasové hovory, videostreaming a komunikace pro kritické mise zůstávají stabilní a splňují přísné požadavky na spolehlivost pro veřejnou dopravu a konektivitu vozidel.

## K čemu slouží

Účelem technologie High Mobility (HM) je řešit základní výzvy rádiové komunikace způsobené uživateli pohybujícími se velmi vysokou rychlostí, což je scénář, který se rozšířil s globální expanzí vysokorychlostních železničních sítí. Před zavedením specializovaných funkcí HM byly standardní mobilní sítě optimalizovány pro pěší a běžnou vozidlovou rychlost, kde byl Dopplerův jev a koherenční čas kanálu méně výrazné. Při rychlostech přesahujících 250 km/h tyto jevy způsobují vážnou degradaci signálu, častá selhání předání spojení a přerušené hovory, což činí základní služby nespolehlivými.

Historicky omezení sítí před 4G ve vysokorychlostních scénářích motivovalo její vytvoření v 3GPP Release 8, souběžně s vývojem LTE. Původní specifikace LTE si kladly za cíl podporu rychlostí až 350 km/h, což vyžadovalo speciální mechanismy. HM řeší tato omezení zavedením standardizovaných metod pro kompenzaci Dopplerova jevu a rychlé předávání spojení, které byly dříve řešeny proprietárními implementacemi výrobců nebo nebyly podporovány vůbec. Zajišťuje interoperabilitu a konzistentní uživatelský zážitek napříč různým síťovým vybavením a zařízeními od různých výrobců.

Vytvoření HM bylo hnací silou komerčního a bezpečnostního imperativu poskytovat bezproblémové připojení cestujícím ve veřejné dopravě, což umožňuje produktivitu a zábavu, stejně jako podporu provozních a nouzových komunikací. Představuje klíčový prvek pro 'propojený vlak' a budoucí služby mobility, a zajišťuje tak, že mobilní technologie drží krok s pokrokem v dopravě.

## Klíčové vlastnosti

- Algoritmy pro odhad a kompenzaci Dopplerova posunu
- Vylepšené referenční signály fyzické vrstvy pro sledování kanálu při vysoké rychlosti
- Optimalizované parametry a procedury předání spojení pro snížení latence
- Podpora rychlostí UE až 350 km/h (a vyšších v pozdějších release)
- Detekce a konfigurace UE s vysokou mobilitou na straně sítě
- Udržení QoS pro služby v reálném čase během vysokorychlostního pohybu

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [HM na 3GPP Explorer](https://3gpp-explorer.com/glossary/hm/)
