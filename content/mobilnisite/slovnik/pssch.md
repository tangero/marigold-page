---
slug: "pssch"
url: "/mobilnisite/slovnik/pssch/"
type: "slovnik"
title: "PSSCH – Physical Sidelink Shared Channel"
date: 2025-01-01
abbr: "PSSCH"
fullName: "Physical Sidelink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pssch/"
summary: "Fyzický kanál v LTE a 5G NR používaný pro přímou komunikaci mezi zařízeními (D2D) a komunikaci vozidlo-se-vším (V2X). Přenáší uživatelská data a řídicí informace mezi uživatelskými zařízeními (UE) bez"
---

PSSCH je fyzický sdílený postranní kanál (Physical Sidelink Shared Channel) používaný v LTE a 5G NR pro přímou komunikaci mezi zařízeními (device-to-device), který přenáší uživatelská data a řídicí informace mezi uživatelskými zařízeními (UE) bez použití síťové infrastruktury.

## Popis

Fyzický sdílený postranní kanál (Physical Sidelink Shared Channel, PSSCH) je klíčový kanál fyzické vrstvy definovaný ve specifikacích 3GPP pro komunikaci přes postranní spojení (sidelink, [SL](/mobilnisite/slovnik/sl/)), zavedený v LTE Release 12 a pokračující v 5G NR. Postranní spojení označuje přímou komunikaci mezi uživatelskými zařízeními (UE) bez toho, aby data procházela přes základnovou stanici (eNodeB/gNB) nebo páteřní síť. PSSCH je primární kanál používaný k přenosu uživatelských dat (transportních bloků) a souvisejících řídicích informací pro postranní spojení ([SCI](/mobilnisite/slovnik/sci/)) mezi blízkými uživatelskými zařízeními. V LTE funguje ve spektru pro uplink (pro postranní spojení Módu 3 a 4) a v NR ve vyhrazeném nebo sdíleném spektru.

Přenos na PSSCH zahrnuje několik procedur fyzické vrstvy. Vysílající uživatelské zařízení (UE) nejprve odešle řídicí informace pro postranní spojení (SCI) na fyzický řídicí postranní kanál ([PSCCH](/mobilnisite/slovnik/pscch/)), který je typicky mapován na zdroje sousedící nebo blízké zdrojům pro PSSCH. Tyto SCI obsahují klíčové informace pro přijímající UE k dekódování následného přenosu na PSSCH, včetně alokace zdrojů, schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), ID skupinového cíle a časových informací. Skutečná uživatelská data jsou poté přenášena na PSSCH za použití zdrojů a parametrů uvedených v SCI. Kanál využívá podobná schémata modulace ([QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM v NR) a kódování (Turbo kódy v LTE, [LDPC](/mobilnisite/slovnik/ldpc/) v NR) jako jiné sdílené kanály.

Z hlediska alokace zdrojů jsou pro LTE V2X definovány dva hlavní módy: Mód 3 (naplánovaný), kde eNodeB přiděluje zdroje pro postranní spojení, a Mód 4 (autonomní), kde si UE autonomně vybírá zdroje pomocí protokolu snímání a rezervace. NR postranní spojení zavádí pokročilejší módy s větší flexibilitou. PSSCH je zásadní pro aplikace vyžadující nízkou latenci a vysokou spolehlivost, jako je formování kolon vozidel, koordinace autonomního řízení a veřejná bezpečnostní D2D komunikace. Jeho návrh zahrnuje funkce pro zvládání vysoké mobility, omezení polovičního duplexu (UE nemůže současně vysílat a přijímat na stejné frekvenci) a řízení interference v distribuovaném prostředí.

## K čemu slouží

PSSCH byl vytvořen k podpoře přímé komunikace mezi zařízeními, což je schopnost nezbytná pro nové případy užití přesahující tradiční mobilní komunikaci. Původním impulzem v LTE Release 12 byly služby založené na blízkosti (ProSe) pro veřejnou bezpečnost, umožňující záchranným složkám komunikovat přímo, když je síťová infrastruktura poškozená nebo nedostupná. Tím byla řešena kritická omezení konvenčních mobilních sítí, které jsou zcela závislé na pokrytí základnovými stanicemi.

Motivace se významně rozšířila se zavedením komunikace vozidlo-se-vším (V2X) v LTE Release 14. Stávající standardy vozidlové komunikace, jako IEEE 802.11p (DSRC), měly omezení v škálovatelnosti, pokrytí a integraci s mobilními sítěmi. PSSCH jako součást standardu 3GPP V2X byl navržen tak, aby poskytoval robustnější, vysokokapacitní a sítí spravovanou alternativu pro přímou komunikaci vozidel. Řeší problémy spojené s vysokorychlostní mobilitou, hustými scénáři a kvalitou služeb využitím mobilního spektra a návrhu fyzické vrstvy. Vytvoření PSSCH umožnilo vysílání (broadcast), skupinové vysílání (groupcast) a jednosměrnou komunikaci (unicast) s nízkou latencí mezi vozidly, chodci a infrastrukturou, čímž položilo základy pokročilé bezpečnosti jízdy a koordinace autonomních vozidel.

## Klíčové vlastnosti

- Přenáší uživatelská data a transportní bloky pro přímou komunikaci mezi uživatelskými zařízeními (UE) přes postranní spojení (sidelink).
- Funguje ve spojení s PSCCH, který přenáší potřebné řídicí informace pro postranní spojení (SCI) pro dekódování.
- Podporuje více režimů alokace zdrojů: naplánované sítí (Mód 3) a autonomní výběr uživatelským zařízením (UE) (Mód 4) v LTE.
- Využívá pokročilou modulaci (až 256QAM v NR) a kanálové kódování (LDPC v NR) pro vysokou spektrální účinnost.
- Navržen pro scénáře s vysokou mobilitou s podporou frekvenční a časové synchronizace mezi uživatelskými zařízeními (UE).
- Umožňuje různé typy přenosu: vysílání (broadcast), skupinové vysílání (groupcast) a jednosměrnou komunikaci (unicast) pro flexibilní služby V2X a D2D.

## Související pojmy

- [PSCCH – Physical Sidelink Control Channel](/mobilnisite/slovnik/pscch/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [SCI – Subscriber Controlled Input / Send Charging Information](/mobilnisite/slovnik/sci/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.788** (Rel-15) — V2X Phase 2 Technical Report for LTE
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.201** (Rel-19) — NR Physical Layer General Description
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pssch/)
