---
slug: "fdma"
url: "/mobilnisite/slovnik/fdma/"
type: "slovnik"
title: "FDMA – Frequency Division Multiple Access"
date: 2025-01-01
abbr: "FDMA"
fullName: "Frequency Division Multiple Access"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fdma/"
summary: "FDMA je metoda přístupu k rádiovému kanálu, při níž je celé dostupné rádiové spektrum rozděleno na více jednotlivých frekvenčních kanálů, z nichž je každý přiřazen jinému uživateli po dobu jeho hovoru"
---

FDMA je metoda přístupu k rádiovému kanálu, při níž je celé dostupné rádiové spektrum rozděleno na více jednotlivých frekvenčních kanálů, z nichž je každý přiřazen jinému uživateli pro jeho hovor nebo relaci.

## Popis

Frequency Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (FDMA) je jednou ze základních schémat vícenásobného přístupu používaných v bezdrátové komunikaci k umožnění sdílení společného rádiového frekvenčního pásma více uživateli. V čistém FDMA systému je celé přidělené systémové šířky pásma rozděleno na řadu užších, vyhrazených frekvenčních kanálů. Každému aktivnímu uživateli nebo komunikační relaci je na dobu jeho spojení přidělen výhradně jeden z těchto kanálů. Informační signál uživatele moduluje nosnou frekvenci odpovídající jeho přiřazenému kanálu. Všechny kanály jsou přenášeny současně, ale jsou odděleny ve frekvenční oblasti, což umožňuje více souběžných komunikací.

Z architektonického pohledu vyžaduje FDMA buňková síť, jako byla síť první generace (1G) AMPS nebo rádiové rozhraní satelitní komunikace, přesnou frekvenční syntézu a filtrování. Každá základnová stanice je vybavena transceivery naladěnými na specifické frekvence kanálů. Uživatelskému zařízení (UE) je přidělen uplink kanál (pro vysílání k základnové stanici) a spárovaný downlink kanál (pro příjem), což je v podstatě [FDD](/mobilnisite/slovnik/fdd/) aplikované na uživatele. Klíčovými síťovými komponentami jsou kanálové prvky v základnové stanici, z nichž každý obsluhuje specifickou frekvenci, a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), které spravuje přidělování a předávání těchto kanálů při pohybu uživatelů mezi buňkami.

FDMA funguje na principu udržování striktního oddělení mezi kanály pomocí ochranných pásem – malých nevyužitých frekvenčních intervalů mezi sousedními kanály. Tato ochranná pásma zabraňují mezikanálovému rušení ([ICI](/mobilnisite/slovnik/ici/)) způsobenému nedokonalými vysílacími filtry a Dopplerovými posuvy. Když uživatel zahájí hovor, řídicí systém sítě přiřadí dostupný frekvenční pár. UE a základnová stanice poté naladí své vysílače a přijímače na tyto frekvence. Komunikace je po dobu hovoru nepřetržitá, na rozdíl od systémů s časovým dělením. Tato jednoduchost je zároveň silnou i slabou stránkou; umožňuje přímočarou implementaci, ale postrádá flexibilitu pro trhaný datový provoz.

V systémech 3GPP se čisté FDMA nepoužívá jako primární přístupová metoda pro digitální buňkové standardy jako GSM, UMTS, LTE nebo NR. Jeho principy jsou však hluboce zakotveny. GSM například kombinuje FDMA (dělení 25 MHz na 124 nosných frekvencí po 200 kHz) s TDMA (dělení každé frekvence na 8 časových slotů). Co je důležitější, FDMA je koncepčním předchůdcem pokročilejších technik ve frekvenční oblasti. Moderní Orthogonal Frequency Division Multiple Access ([OFDMA](/mobilnisite/slovnik/ofdma/)), používaný v downlinku LTE a 5G NR, je digitální, efektivní formou FDMA, kde jsou subnosné ortogonální, což eliminuje potřebu ochranných pásem mezi nimi a umožňuje dynamické přidělování skupin subnosných (bloků zdrojů) různým uživatelům.

## K čemu slouží

FDMA bylo vyvinuto k řešení základního problému umožnění více uživatelům přístupu ke sdílenému, omezenému zdroji rádiového spektra pro mobilní komunikaci. Před buňkovými sítěmi byly mobilní rádiové systémy často jednokanálové nebo používaly neefektivní ruční výběr. FDMA poskytlo systematický, škálovatelný způsob rozdělení spektra na jednotlivé 'konverzační pruhy', což umožnilo současnou obsluhu mnoha uživatelů v geografické oblasti. Toto byl technologický základ prvních komerčních buňkových sítí (1G), díky čemuž se mobilní telefonie stala službou pro masový trh.

Primární problém, který řešilo, byla izolace uživatelů – zabránění interferenci signálu jednoho uživatele se signálem jiného. Přiřazením jedinečných frekvenčních kanálů FDMA poskytlo přirozenou, statickou izolaci. To bylo s analogovou technologií 70. a 80. let snazší implementovat ve srovnání se složitějšími časově synchronizovanými nebo kódovými systémy. Umožnilo nepřetržité vysílání, které bylo ideální pro analogový hlas, a poskytovalo konzistentní kvalitu bez přerušovanosti, která mohla vzniknout při časovém sdílení.

FDMA však mělo významná omezení, která motivovala vývoj hybridních a digitálních technik. Bylo neefektivní pro trhaný datový provoz, protože kanál zůstával přidělen i během období ticha. Potřeba ochranných pásem snižovala spektrální účinnost. Každý kanál navíc vyžadoval vyhrazenou transceiverovou jednotku v základnové stanici, což zvyšovalo náklady a složitost. Tyto nedostatky vedly k vývoji TDMA (jako ve 2G GSM) a [CDMA](/mobilnisite/slovnik/cdma/) (jako v 3G UMTS), které nabídly větší kapacitu a flexibilitu. Nicméně účel FDMA jako jasné, základní metody pro rozdělování zdrojů zůstává historicky klíčový. Jeho koncepty jsou zvěčněny ve strategiích přidělování zdrojů ve frekvenční oblasti všech následujících generací buňkových sítí, kde základní akt přiřazení konkrétního bloku spektra uživateli nebo buňce zůstává v jádru principem FDMA.

## Klíčové vlastnosti

- Dělí celkové spektrum na jednotlivé, vyhrazené frekvenční kanály pro každého uživatele
- Poskytuje nepřetržitý přenos po dobu trvání spojení
- Používá ochranná pásma mezi kanály k zabránění interferenci
- Umožňuje více uživatelům komunikovat současně prostřednictvím frekvenčního oddělení
- Tvoří základ pro hybridní přístupová schémata (např. FDMA/TDMA v GSM)
- Koncepční základ pro moderní přidělování zdrojů v OFDMA

## Související pojmy

- [CDMA – Code Division Multiple Access](/mobilnisite/slovnik/cdma/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [FDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/fdma/)
