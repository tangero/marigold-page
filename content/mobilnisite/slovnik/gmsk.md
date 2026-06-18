---
slug: "gmsk"
url: "/mobilnisite/slovnik/gmsk/"
type: "slovnik"
title: "GMSK – Gaussian Minimum Shift Keying"
date: 2025-01-01
abbr: "GMSK"
fullName: "Gaussian Minimum Shift Keying"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gmsk/"
summary: "Digitální modulační schéma s konstantní amplitudou (konstantním obálkou), používané primárně v GSM. Aplikuje Gaussův filtr na datové impulzy před modulací, což vede ke kompaktnímu spektru s nízkými em"
---

GMSK je digitální modulační schéma s konstantní amplitudou (konstantním obálkou), používané primárně v GSM, které aplikuje Gaussův filtr na datové impulzy za účelem získání kompaktního spektra s nízkými emisemi mimo přidělený pásmo.

## Popis

Gaussian Minimum Shift Keying (GMSK) je modulační schéma s kontinuální fází a frekvenčním klíčováním (CPFSK), které je specifickou implementací Minimum Shift Keying ([MSK](/mobilnisite/slovnik/msk/)). Její definující charakteristikou je použití Gaussova dolopropustného filtru jako premodulačního filtru. Tento filtr tvaruje původní obdélníkové datové impulzy, zmírňuje jejich přechody a významně redukuje spektrální šířku modulovaného signálu. V GMSK má modulovaný signál konstantní amplitudu (konstantní obálku), což znamená, že jeho amplituda se nemění. Tato vlastnost je klíčová pro mobilní komunikace, protože umožňuje použití ne-lineárních, velmi účinných výkonových zesilovačů (např. zesilovače třídy C) ve vysílači bez způsobení významného spektrálního regrowthu nebo distorze.

Technická operace začíná binárním datovým tokem. Tento tok je nejprve prohnán Gaussovým filtrem. Produkt šířky pásma a časového intervalu filtru ([BT](/mobilnisite/slovnik/bt/)) je klíčový parametr; v GSM je použit BT produkt 0.3, který reprezentuje kompromis mezi spektrální kompaktností a intersymbol interference ([ISI](/mobilnisite/slovnik/isi/)). Filtrovaný signál, který má nyní pozvolnější fázové přechody, je následně přiveden na napětím řízený oscilátor ([VCO](/mobilnisite/slovnik/vco/)) nebo kvadraturní modulátor k vytvoření MSK signálu. V MSK je frekvenční odchylka přesně nastavena na polovinu bitové rychlosti (Δf = 1/(4Tb)), což je minimální odchylka, která garantuje ortogonalitu mezi symboly. Gaussovské filtrování dat zajišťuje, že změna fáze během jedné symbolové periody není abruptní, ale sleduje pozvolnou trajektorii, což limituje šířku pásma signálu.

V systému GSM funguje GMSK modulace na symbolové rychlosti 270.833 ksymbolů/s, což odpovídá hrubé bitové rychlosti 270.833 kbit/s v rámci kanálového pásma 200 kHz. Konstantní amplituda (konstantní obálka) a úzké spektrální footprint GMSK byly klíčové pro [FDMA](/mobilnisite/slovnik/fdma/)/[TDMA](/mobilnisite/slovnik/tdma/) strukturu GSM, umožňující blízké rozestupy sousedních kanálů (200 kHz) bez nadměrné interference. Demodulace GMSK může být provedena pomocí koherentních nebo nekoherentních detektorů. GSM typicky používá nekoherentní přijímač s Viterbiho ekvalizátorem pro potlačení ISI zaváděné Gaussovským filtrováním a multipath rádiovým kanálem.

## K čemu slouží

GMSK byla vybrána jako modulační schéma pro GSM k řešení několika kritických problémů v návrhu raných digitálních celulárních systémů. Předchozí analogové systémy trpěly nízkou spektrální účinností a náchylností k rušení. Rané digitální kandidáty jako prosté [FSK](/mobilnisite/slovnik/fsk/) měly široké spektrální postranní lobe, vedoucí k interferenci mezi sousedními kanály. Primární motivací pro GMSK bylo dosažení vysoké spektrální účinnosti – umístění mnoha uživatelů do omezeného rádiového spektra – spolu s možností návrhu levných, energeticky účinných mobilních terminálů.

Vlastnost konstantní amplitudy (konstantní obálky) přímo řeší potřebu účinného výkonového zesilování. Lineární výkonové zesilovače, potřebné pro modulační schémata s amplitudovými změnami (např. [QPSK](/mobilnisite/slovnik/qpsk/)), jsou inherentně méně účinné a rychle vyčerpávají život baterie. Použitím GMSK mohli návrháři GSM terminálů použít saturované výkonové zesilovače s vysokou účinností, vedoucí k delší době hovoru. Gaussovské filtrování bylo specificky vybráno pro potlačení vysokofrekvenčních komponent MSK signálu, vytvoření velmi kompaktní hustoty výkonového spektra. Toto kompaktní spektrum minimalizovalo interferenci mezi sousedními rádiovými kanály, což bylo zásadní pro těsné 200 kHz kanálové rozestupy GSM. Tato kombinace spektrální účinnosti, účinnosti výkonového zesilovače a robustnosti vůči rušení učinila GMSK ideální volbou pro první masově rozšířený digitální celulární standard.

## Klíčové vlastnosti

- Modulace s konstantní amplitudou (konstantní obálkou), umožňující použití účinných ne-lineárních výkonových zesilovačů
- Používá Gaussovské premodulační filtrování pro spektrální omezení (BT=0.3 v GSM)
- Vychází z Minimum Shift Keying (MSK) s modulačním indexem 0.5
- Poskytuje vysokou spektrální účinnost, umožňující 200 kHz rozestupy kanálů v GSM
- Robustní výkon v přítomnosti rušení a interference
- Zjednodušuje návrh RF vysílače v mobilních terminálech díky konstantní amplitudě (konstantní obálce)

## Související pojmy

- [MSK – Minimum-shift keying](/mobilnisite/slovnik/msk/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [8-PSK – 8-state Phase Shift Keying](/mobilnisite/slovnik/8-psk/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [GMSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmsk/)
