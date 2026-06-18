---
slug: "pdsch"
url: "/mobilnisite/slovnik/pdsch/"
type: "slovnik"
title: "PDSCH – Physical Downlink Shared Channel"
date: 2025-01-01
abbr: "PDSCH"
fullName: "Physical Downlink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pdsch/"
summary: "Physical Downlink Shared Channel (PDSCH) je hlavní fyzický kanál v LTE a NR pro přenos uživatelských dat a signalizace vyšších vrstev ze sítě do uživatelského zařízení. Jedná se o sdílený zdroj dynami"
---

PDSCH je hlavní fyzický kanál v LTE a NR pro přenos uživatelských dat a signalizace vyšších vrstev ze sítě do uživatelského zařízení.

## Popis

Physical Downlink Shared Channel (PDSCH) je základní transportní kanál pro směr downlink v technologiích radiového přístupu 3GPP, včetně UMTS, LTE a NR. Přenáší všechna uživatelská data (například internetové pakety) a většinu řídicích informací (jako jsou zprávy [RRC](/mobilnisite/slovnik/rrc/) a bloky systémových informací) z základnové stanice (eNodeB v LTE, gNB v NR) do uživatelského zařízení (UE). Kanál je 'sdílený', protože jeho časově-frekvenční zdroje jsou v každém přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)) dynamicky přidělovány mezi více uživatelských zařízení plánovačem základnové stanice na základě faktorů, jako je kvalita kanálu, požadavky QoS a spravedlivost.

Při provozu využívá PDSCH v LTE přístup Orthogonal Frequency Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([OFDMA](/mobilnisite/slovnik/ofdma/)) a v NR cyklickou předponu [OFDM](/mobilnisite/slovnik/ofdm/) ([CP-OFDM](/mobilnisite/slovnik/cp-ofdm/)). Plánovač rozhoduje, které bloky zdrojů ([RB](/mobilnisite/slovnik/rb/)) jsou přiděleny kterému uživatelskému zařízení pro každý podrámec (LTE) nebo slot (NR). Uživatelské zařízení musí nejprve dekódovat Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)), aby našlo svou Downlink Control Information (DCI), která obsahuje přidělení plánování specifikující RB, modulační a kódovací schéma (MCS) a další parametry pro příjem svého PDSCH. Data na PDSCH jsou následně demodulována a dekódována pomocí uvedených parametrů.

Výkon PDSCH je klíčový pro celkovou kapacitu systému a datové rychlosti. Podporuje pokročilé funkce, jako je přenos Multiple Input Multiple Output (MIMO) (např. prostorové multiplexování, beamforming), hybridní automatický požadavek na opakování (HARQ) pro opravu chyb a adaptivní modulaci a kódování (AMC) pro přizpůsobení přenosu podmínkám rádiového kanálu. V NR byl návrh PDSCH vylepšen flexibilnější číselnou soustavou (rozestup podnosných), plánováním mini-slotů pro nízkou latenci a podporou různých případů užití od rozšířeného mobilního širokopásmového přístupu (eMBB) až po ultra-spolehlivou komunikaci s nízkou latencí (URLLC).

## K čemu slouží

PDSCH byl vytvořen, aby poskytoval efektivní, flexibilní a vysokokapacitní mechanismus pro přenos dat ve směru downlink v paketově spínaných celulárních systémech. Starší systémy, jako GSM, používaly pro každého uživatele vyhrazené časové sloty, což bylo pro trhavý datový provoz neefektivní. Koncept sdíleného kanálu, zavedený s UMTS a zdokonalený v LTE a NR, umožňuje statistické multiplexování dat více uživatelů nad společnou sadou rádiových zdrojů, což dramaticky zlepšuje spektrální účinnost.

Řeší problém, jak dynamicky přidělovat omezenou rádiovou šířku pásma mnoha uživatelům s proměnlivými a nepředvídatelnými datovými nároky. Díky tomu, že je řízen plánovačem, umožňuje PDSCH síti upřednostňovat provoz, řídit interferenci a přizpůsobovat se rychle se měnícím rádiovým podmínkám. Vývoj od modelu vyhrazeného kanálu ke sdílenému kanálu byl motivován potřebou podporovat širokopásmový přístup k internetu a multimediální služby, které vyžadují mnohem vyšší datové rychlosti a efektivnější využití zdrojů, než mohly nabídnout okruhově spínané nebo rané paketově spínané návrhy.

## Klíčové vlastnosti

- Přenáší uživatelská data a signalizaci vyšších vrstev ve směru downlink
- Dynamicky sdílený zdroj přidělovaný plánovačem na každý TTI/slot
- Podporuje adaptivní modulaci a kódování (QPSK, 16QAM, 64QAM, 256QAM, 1024QAM v NR)
- Umožňuje přenosy MIMO (např. prostorové multiplexování, beamforming)
- Využívá hybridní ARQ (HARQ) pro robustní opravu chyb
- Flexibilní přidělování zdrojů v časové a frekvenční doméně

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- … a dalších 47 specifikací

---

📖 **Anglický originál a plná specifikace:** [PDSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdsch/)
