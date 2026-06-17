---
slug: "ic"
url: "/mobilnisite/slovnik/ic/"
type: "slovnik"
title: "IC – Interference Cancellation"
date: 2025-01-01
abbr: "IC"
fullName: "Interference Cancellation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ic/"
summary: "Soubor technik zpracování signálu v přijímači pro odhad a odečtení rušivých signálů, čímž se zlepšuje kvalita požadovaného signálu a kapacita sítě. Je klíčový pro potlačení ko-kanálové a přilehlé kaná"
---

IC je soubor technik zpracování signálu v přijímači, které odhadují a odečítají rušivé signály za účelem zlepšení kvality požadovaného signálu a kapacity sítě. Je klíčový pro potlačení interference v hustých celulárních nasazeních.

## Popis

Interference Cancellation (IC, rušení) je základní technologie fyzické vrstvy ve standardech 3GPP navržená ke zlepšení výkonu přijímače v přítomnosti interference. Funguje tak, že využívá známou nebo odhadnutou strukturu rušivých signálů. Přijímač nejprve demoduluje a dekóduje nejsilnější signál, který je často dominantním rušičem. Poté rekonstruuje přesný odhad tohoto rušivého signálu, včetně jeho modulace, kódování a vlivů kanálu. Tato rekonstruovaná replika je následně odečtena od celkového přijatého signálu, čímž zůstane „čistší“ složený signál pro zpracování požadovaných uživatelských dat. Tento iterační proces lze aplikovat na více vrstev interference a postupně tak odstraňovat nežádoucí signály.

Architektura IC je typicky integrována do jednotky základního pásma (baseband processing unit) jak v uživatelském zařízení (UE), tak v základnových stanicích (např. gNB, [eNB](/mobilnisite/slovnik/enb/)). Mezi klíčové komponenty patří pokročilé odhadovače kanálu, detektory interference a sofistikované ekvalizéry. Algoritmy spoléhají na přesnou znalost referenčních signálů, pilotních sekvencí a potenciálně dekódovaných informací řídicího kanálu pro přesné modelování interference. Ve scénářích víceuživatelského [MIMO](/mobilnisite/slovnik/mimo/) ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)) jsou techniky IC nezbytné pro oddělení prostorově multiplexovaných datových proudů, kde signály určené pro jiné uživatele působí jako interference.

Role IC v síti je mnohostranná. Přímo zlepšuje poměr signálu k interferenci a šumu (SINR) na přijímači, což se převádí na vyšší dosažitelné datové rychlosti, zvýšenou spektrální účinnost a rozšířené pokrytí buňky, zejména na jejích okrajích, kde je interference nejzávažnější. Efektivní správou interference uvnitř buňky a mezi buňkami umožňuje IC agresivnější faktory opětovného využití frekvence a hustší nasazení sítě. Je klíčovým prvkem technologií, jako je Network-Assisted Interference Cancellation and Suppression ([NAICS](/mobilnisite/slovnik/naics/)) specifikovaná v 3GPP, kde síť může poskytnout UE pomocné informace o potenciálních rušičích pro zlepšení účinnosti potlačení.

## K čemu slouží

Interference Cancellation byl vytvořen, aby řešil základní kapacitní omezení celulárních sítí daná ko-kanálovou interferencí. Jak se sítě vyvíjely od 2G přes 3G až po 4G a používaly [CDMA](/mobilnisite/slovnik/cdma/) a [OFDMA](/mobilnisite/slovnik/ofdma/), stala se interference primárním omezením pro zvyšování spektrální účinnosti a uživatelských datových rychlostí. Tradiční metody, jako je řízení výkonu a frekvenční plánování, jsou nedostatečné v hustých, heterogenních sítích s nekoordinovanými malými buňkami.

Motivací pro standardizaci technik IC bylo přesunutí správy interference z problému síťového plánování na řešení v reálném čase založené na zpracování signálu v přijímači. Řeší problém degradované propustnosti a přerušení hovorů pro uživatele na hranicích buněk a ve scénářích s vysokou zátěží. Tím, že umožňuje přijímačům aktivně potlačovat známé rušiče, mohou sítě podporovat více současných uživatelů a modulační schémata vyššího řádu, která jsou jinak limitována interferencí. Jeho zavedení a průběžné vylepšování napříč releasy bylo hnací silou potřeby uspokojit neustále rostoucí poptávku po datech bez proporcionálního nárůstu licencovaného spektra.

## Klíčové vlastnosti

- Successive Interference Cancellation (SIC) pro sekvenční dekódování a odečítání nejsilnějších rušičů
- Využití známých referenčních signálů a informací řídicího kanálu pro přesnou rekonstrukci interference
- Podpora potlačení interference v uplinku i downlinku v základnových stanicích a UE
- Integrace s MIMO přijímači pro oddělení prostorově multiplexovaných proudů
- Možnosti síťové asistence (NAICS) pro informování UE o parametrech rušivého signálu
- Adaptivní algoritmy fungující napříč různými 3GPP technologiemi radiového přístupu (UTRAN, E-UTRAN, NG-RAN)

## Související pojmy

- [NAICS – Network-Assisted Interference Cancellation and Suppression](/mobilnisite/slovnik/naics/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TR 25.963** (Rel-19) — Feasibility Study on UMTS/HSDPA UE Interference Cancellation
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen
- **TS 36.859** (Rel-13) — Study on Downlink Multiuser Superposition Transmission
- **TS 36.866** (Rel-12) — Study on Network Assisted Interference Cancellation
- **TR 38.812** (Rel-16) — Study on NOMA for NR
- **TR 38.877** (Rel-18) — Technical Report
- **TS 45.820** (Rel-13) — CIoT for Internet of Things

---

📖 **Anglický originál a plná specifikace:** [IC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ic/)
