---
slug: "rpe-ltp"
url: "/mobilnisite/slovnik/rpe-ltp/"
type: "slovnik"
title: "RPE-LTP – Regular Pulse Excited codec with Long Term Prediction"
date: 2025-01-01
abbr: "RPE-LTP"
fullName: "Regular Pulse Excited codec with Long Term Prediction"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rpe-ltp/"
summary: "Řečový kódovací algoritmus používaný v raných systémech GSM pro plnorychlostní řečové kanály. Převádí analogové hlasové signály na komprimovaný digitální bitový tok pro efektivní přenos přes rádiová r"
---

RPE-LTP je řečový kódovací algoritmus používaný v raných systémech GSM, který převádí analogový hlas na komprimovaný digitální bitový tok pro efektivní rádiový přenos.

## Popis

Regular Pulse Excited codec with Long Term Prediction (RPE-LTP) je specifický řečový kódovací algoritmus standardizovaný pro plnorychlostní provozní kanál GSM ([TCH/FS](/mobilnisite/slovnik/tch-fs-2/)). Pracuje s přenosovou rychlostí 13 kbit/s a vytváří komprimovanou digitální reprezentaci 20ms řečového rámce (260 bitů). Kodek je založen na hybridním kódovacím schématu kombinujícím lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/)) pro modelování hlasového traktu, dlouhodobou predikci ([LTP](/mobilnisite/slovnik/ltp/)) pro modelování základního tónu (znělé zvuky) a excitaci pravidelnými pulzy (RPE) pro modelování reziduálního signálu.

Z architektonického hlediska proces kódování probíhá v několika stupních. Nejprve je vstupní řečový signál (vzorkovaný na 8 kHz) rozdělen na rámce. Pro každý rámec krátkodobá LPC analýza vypočítá sadu reflexních koeficientů (převedených na logaritmické poměry ploch, LAR), které modelují spektrální obálku hlasového traktu. Tyto LAR jsou kvantovány a přenášeny. Následně LTP analýza odstraní dlouhodobou redundanci (periodicitu základního tónu) z LPC reziduálního signálu. To zahrnuje nalezení zpoždění (pitch lag) a faktoru zesílení, které nejlépe odpovídají aktuálnímu reziduu s minulým reziduem. LTP parametry (lag a gain) jsou také kvantovány a odeslány. Nakonec je zbývající signál, nazývaný LTP reziduum, zakódován pomocí techniky RPE. RPE vybere jednu ze čtyř prokládaných podposloupností pravidelně rozmístěných pulsů, která nejlépe aproximuje reziduum. Číslo vybrané podposloupnosti, pozice pulsů a amplitudy pulsů jsou kvantovány a přenášeny.

Dekodér provádí inverzní proces: rekonstruuje excitační signál z přijatých RPE parametrů, použije LTP parametry k přidání dlouhodobé periody a poté tento signál profiltruje přes LPC syntézní filtr (pomocí přijatých LAR) k reprodukci řečového signálu. Klíčové komponenty zahrnují LPC analýzní/syntézní filtr, adaptivní kódovou knihu LTP a logiku výběru a kvantizace RPE. Jeho role byla zásadní v rádiovém rozhraní GSM, definovala kvalitu hlasu a kapacitu původní plnorychlostní služby. Specifikace TS 46.008 podrobně popisuje bitově přesný algoritmický popis a mapování parametrů na 260bitový kanálový rámec.

## K čemu slouží

Kodek RPE-LTP byl vyvinut k řešení základní výzvy přenosu hlasu přijatelné kvality přes digitální rádiové kanály raných sítí GSM s výrazně omezenou šířkou pásma. Před GSM používaly analogové celulární systémy frekvenční modulaci, která byla neefektivní a měla nízkou kvalitu. Přechod na digitální přenos vyžadoval řečový kodek, který by dokázal komprimovat 64 kbit/s [PCM](/mobilnisite/slovnik/pcm/) telefonní signál na přibližně 13 kbit/s, aby se vešel do dostupné přenosové rychlosti kanálu, při zachování kvality hovoru na úrovni veřejné telefonní sítě a odolnosti vůči přenosovým chybám.

Vytvoření RPE-LTP bylo motivováno soutěžním výběrovým procesem. Byl vybrán před ostatními kandidáty (jako například Multi-Pulse Excited codec) pro svůj dobrý kompromis mezi kvalitou řeči, výpočetní složitostí (důležitou pro raný mobilní hardware) a robustností. Řešil omezení jednodušších vlnových kodeků (jako [ADPCM](/mobilnisite/slovnik/adpcm/)), které nedokázaly dosáhnout tak vysoké komprese, a komplexnějších vokodérů, které zněly nepřirozeně. Zařazení dlouhodobé predikce ([LTP](/mobilnisite/slovnik/ltp/)) bylo klíčovou inovací, která efektivně modelovala kvaziperiodickou povahu znělé řeči a výrazně zlepšila kvalitu při cílové přenosové rychlosti. Tento kodek byl klíčový pro komerční úspěch GSM, protože poskytoval čistý digitální hlas, umožňoval efektivní využití spektra a stanovil měřítko pro následný vývoj kodeků, jako jsou Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)) a Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)).

## Klíčové vlastnosti

- Pracuje s rychlostí 13 kbit/s pro plnorychlostní kanál GSM
- Používá hybridní kódování: LPC, LTP a RPE
- Zpracovává řeč v 20ms rámcích (260 bitů/rámec)
- Poskytuje dobrou kvalitu řeči při střední složitosti
- Obsahuje ochranu proti chybám prostřednictvím uspořádání parametrů podle důležitosti
- Bitově přesná specifikace pro interoperabilitu

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [LPC – Linear Predictive Coding](/mobilnisite/slovnik/lpc/)

## Definující specifikace

- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [RPE-LTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpe-ltp/)
