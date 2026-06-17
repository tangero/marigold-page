---
slug: "drns"
url: "/mobilnisite/slovnik/drns/"
type: "slovnik"
title: "DRNS – Drift Radio Network Subsystem"
date: 2025-01-01
abbr: "DRNS"
fullName: "Drift Radio Network Subsystem"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/drns/"
summary: "Souhrnný termín pro Drift Radio Network Controller (DRNC) a všechny jím řízené Node Bs. Představuje administrativní doménu rádiových prostředků, kterou UE používá, ale není na ni ukotvena během mezile"
---

DRNS je souhrnný termín pro Drift Radio Network Controller (DRNC) a jím řízené Node Bs. Představuje doménu rádiových prostředků, kterou UE používá, ale není na ni ukotvena během mezilehlého měkkého předávání (soft handover) mezi RNC v UMTS.

## Popis

Drift Radio Network Subsystem (DRNS) je logické seskupení v architektuře UMTS Terrestrial Radio Access Network (UTRAN). Zahrnuje jeden Drift Radio Network Controller ([DRNC](/mobilnisite/slovnik/drnc/)) a všechny základnové stanice (Node Bs), které jsou k tomuto DRNC připojeny a jím řízeny. Koncept DRNS je definován relativně vůči konkrétnímu uživatelskému zařízení (UE). Když je UE ve stavu mezilehlého měkkého předávání mezi RNC – tedy připojeno k buňkám patřícím různým RNC – je RNC, které není Serving RNC (SRNC), pro dané UE označeno jako DRNC a celá jeho řízená doména se stává DRNS pro spojení tohoto UE.

Architektonicky je DRNS podmnožinou UTRAN. Rozhraní k jádru sítě (core network) zprostředkovává přes rozhraní Iu (ačkoli typicky SRNC funguje jako jediný kontaktní bod s CN pro dané UE). Jeho nejkritičtějším externím rozhraním je rozhraní Iur, které jej spojuje se Serving RNS (SRNS) – doménou SRNC. Veškerá řídicí signalizace a uživatelská data týkající se UE, které procházejí mezi SRNC a Node Bs uvnitř DRNS, musí projít tímto spojením Iur. Interně DRNS používá rozhraní Iub pro připojení DRNC k jeho Node Bs.

DRNS funguje pod velením SRNC pro prostředky přidělené konkrétnímu UE. SRNC používá protokol Radio Network Subsystem Application Part (RNSAP) přes rozhraní Iur k vyžádání nastavení, změny nebo zrušení rádiového spoje uvnitř DRNS. DRNC jako správce DRNS je zodpovědný za převod těchto požadavků na akce na svých rozhraních Iub, přidělování lokálních prostředků (jako jsou kanalizační kódy a scrambling kódy) a správu fyzických rádiových spojů. V uživatelské rovině DRNS funguje jako přepínač: přijímá downlinkové rámce od SRNC, směruje je ke správným Node Bs a kombinuje uplinkové rámce ze svých Node Bs před předáním zkombinovaného rámce SRNC. To umožňuje SRNS udržovat jednotný a souvislý pohled na rádiové spojení při využívání rádiových prostředků z více domén RNS.

## K čemu slouží

Koncept DRNS byl vytvořen spolu s [DRNC](/mobilnisite/slovnik/drnc/) ve verzi Release 99, aby poskytl formální architektonický model pro správu rádiových prostředků mimo serving doménu během měkkého předávání. Řeší potřebu abstrahovat a spravovat sadu síťových prvků (RNC a jeho Node Bs) jako jedinou, řiditelnou entitu z pohledu serving řadiče. Před UMTS tvořily v GSM [BSC](/mobilnisite/slovnik/bsc/) a jeho BTSs podobný subsystém, ale předávání mezi BSC bylo tvrdé (hard) a nevyžadovalo trvalé, koordinované sdílení prostředků, které UMTS měkké předávání vyžaduje.

Definování DRNS umožňuje specifikacím 3GPP jasně vymezit odpovědnosti a rozhraní. Stanovuje, že SRNC má vztah peer-to-peer s jinou kompletní administrativní entitou (DRNS), nikoli pouze s jednotlivým RNC. Toto modelování je klíčové pro specifikaci procedur, jako je přidání rádiového spoje, kdy SRNC žádá o prostředek z jiného subsystému. Také zjednodušuje správu sítě a izolaci poruchových domén. Koncept DRNS zapouzdřuje všechny lokalizované funkce správy rádiových prostředků, což umožňuje SRNS se soustředit na správu end-to-end spojení pro UE. Toto oddělení odpovědností je klíčové pro dosažení škálovatelné a robustní mobility ve velké, více-výrobcové síti UMTS.

## Klíčové vlastnosti

- Představuje administrativní doménu Drift RNC a jím řízených Node Bs
- Slouží jako fond prostředků pro mezilehlé měkké předávání mezi RNC z pohledu Serving RNS
- Komunikuje se Serving RNS přes standardizované rozhraní Iur
- Spravuje interní rádiové prostředky (spojení Iub, kódy buněk) pro UE v režimu drift
- Provádí příkazy pro řízení rádiového spoje přijaté od SRNC přes RNSAP
- Poskytuje přenos uživatelské roviny a, pokud je aplikovatelné, makrodiverzitní kombinování uplinku pro své buňky

## Související pojmy

- [DRNC – Drift Radio Network Controller](/mobilnisite/slovnik/drnc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [DRNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/drns/)
