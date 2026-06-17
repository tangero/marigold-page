---
slug: "fref"
url: "/mobilnisite/slovnik/fref/"
type: "slovnik"
title: "FREF – RF Reference Frequency"
date: 2025-01-01
abbr: "FREF"
fullName: "RF Reference Frequency"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fref/"
summary: "FREF je fundamentální, vysoce stabilní zdroj kmitočtu použitý k vygenerování všech ostatních rádiových kmitočtů v rámci uživatelského zařízení (UE) nebo základnové stanice. Jde o hlavní hodinový signá"
---

FREF je fundamentální, vysoce stabilní hlavní zdroj frekvence hodinového signálu, který slouží k generování všech ostatních rádiových kmitočtů v rámci uživatelského zařízení nebo základnové stanice.

## Popis

Referenční rádiový kmitočet (FREF) je klíčový prvek generování kmitočtu v jakémkoli 3GPP rádiovém zařízení, ať už jde o UE nebo gNB. Typicky je odvozen z teplotně kompenzovaného krystalového oscilátoru (TCXO) nebo, ve špičkovějším zařízení, z krystalového oscilátoru s termostatem (OCXO). FREF slouží jako primární reference pro kmitočtový syntetizér zařízení, který generuje signály místního oscilátoru ([LO](/mobilnisite/slovnik/lo/)) používané pro převod nahoru (vysílání) a převod dolů (příjem). Ve vysílacím řetězci je digitální základnový signál převeden na analogový a poté smíchán se signálem LO, což je násobek FREF, aby byl přeložen na požadovaný kmitočet RF nosné. Jakákoli chyba nebo drift FREF způsobí úměrnou chybu ve výsledném kmitočtu vysílané nosné, což vede k emisím mimo přidělený kanál a rušení sousedních buněk. V přijímači je příchozí RF signál převeden dolů do základního pásma pomocí LO, také odvozeného z FREF. Nepřesný FREF zde způsobí nesprávné naladění přijímače, což může umístit požadovaný signál mimo propustné pásmo kanálových filtrů a degradovat výkon demodulace. Specifikace 3GPP (např. TS 38.101, 38.104) definují přísné požadavky na přesnost FREF, často ve formě počtu dílů na milion (ppm), pro různé kategorie zařízení a provozní podmínky. Například typický požadavek pro UE může být ±0,1 ppm za normálních podmínek a ±0,25 ppm za extrémních teplot. Síť se spoléhá na agregovanou přesnost FREF všech zařízení, aby udržela ortogonalitu v [OFDM](/mobilnisite/slovnik/ofdm/) systémech a umožnila úspěšné předávání hovorů (handover).

## K čemu slouží

Účelem FREF je zajistit, aby všechny radiostanice v mobilní síti pracovaly na přesně definovaných kmitočtech. Bez stabilní a přesné společné frekvenční reference by koherentní komunikace byla nemožná. Řeší problémy s kmitočtovým driftem, který způsobuje rušení a přerušení hovorů, a neschopností přijímačů zachytit vysílané signály. Historicky, jak se zvětšovala šířka kanálu a modulační schémata se stávala složitějšími (např. [OFDM](/mobilnisite/slovnik/ofdm/) s těsně rozmístěnými subnosnými), tolerance k frekvenční chybě se stala mimořádně přísnou. Vytvoření standardizovaných požadavků na FREF v 3GPP bylo motivováno potřebou, aby hromadně vyráběná nízkonákladová zařízení udržovala síťovou kmitočtovou synchronizaci bez nutnosti neustálé korekce ze strany sítě. Řeší omezení levnějších, méně stabilních oscilátoru definováním minimálního potřebného výkonu pro spolehlivý provoz, což zajišťuje, že i nízkonákladové UE dokáže splnit požadavky systému na spektrální čistotu a citlivost přijímače.

## Klíčové vlastnosti

- Hlavní zdroj hodinového signálu pro veškeré RF a zpracování základního pásma
- Definován centrálním kmitočtem (např. 19,2 MHz, 26 MHz, 38,4 MHz) a jeho přesností
- Podléhá přísným požadavkům na kmitočtovou chybu specifikovaným v ppm
- Požadavky na stabilitu v závislosti na teplotě, napětí a čase
- Ovlivňuje jak chybu kmitočtu vysílací nosné, tak přesnost naladění přijímače
- Často je realizován komponentou TCXO nebo OCXO

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [FREF na 3GPP Explorer](https://3gpp-explorer.com/glossary/fref/)
