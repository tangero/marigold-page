---
slug: "ssn"
url: "/mobilnisite/slovnik/ssn/"
type: "slovnik"
title: "SSN – Sub-System Number"
date: 2025-01-01
abbr: "SSN"
fullName: "Sub-System Number"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ssn/"
summary: "SSN je číselný identifikátor používaný v signalizaci SS7/SIGTRAN k jednoznačné identifikaci konkrétní aplikace nebo funkce v rámci síťového uzlu. Je klíčovým polem v Signal Connection Control Part (SC"
---

SSN je číselný identifikátor používaný v signalizaci SS7/SIGTRAN k jednoznačné identifikaci konkrétní aplikace nebo funkce (např. HLR nebo MSC) v rámci síťového uzlu pro směrování zpráv.

## Popis

Sub-System Number (SSN) je základní adresovací prvek v rámci [SS7](/mobilnisite/slovnik/ss7/) (Signaling System No. 7) a jeho IP-based evoluce, SIGTRAN. Funguje na vrstvě Signaling Connection Control Part ([SCCP](/mobilnisite/slovnik/sccp/)), která poskytuje rozšířené možnosti směrování a správy nad základní Message Transfer Part ([MTP](/mobilnisite/slovnik/mtp/)). Zatímco Point Code ([PC](/mobilnisite/slovnik/pc/)) identifikuje konkrétní signalizační uzel v síti, SSN identifikuje konkrétní aplikační podsystém *uvnitř* tohoto uzlu. Můžete si představit Point Code jako adresu budovy a SSN jako konkrétní číslo bytu nebo kanceláře uvnitř.

Technicky je SSN 8bitové pole (hodnoty 1-254, přičemž 0 a 255 jsou rezervovány) v parametrech SCCP Called Party Address a Calling Party Address. Když potřebuje být doručena signalizační zpráva – například [MAP](/mobilnisite/slovnik/map/) dotaz na Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) – zdrojová SCCP vrstva nastaví Destination Point Code na uzel HLR a Destination SSN na hodnotu přiřazenou aplikaci HLR (což je podle standardního přiřazení hodnota 6). MTP směruje zprávu ke správnému uzlu a po příchodu SCCP vrstva uzlu prozkoumá SSN, aby určila, který interní aplikační proces (podsystém) by měl zprávu přijmout. To umožňuje, aby jeden fyzický uzel s jedním Point Code hostil více logických funkcí, každou s vlastním SSN.

Standardní hodnoty SSN jsou definovány mezinárodními a 3GPP standardy pro zajištění globální interoperability. Klíčové příklady zahrnují SSN=5 pro Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), SSN=6 pro Home Location Register (HLR), SSN=8 pro Mobile Switching Center Visitor Location Register (MSC/[VLR](/mobilnisite/slovnik/vlr/)) a SSN=149 pro Gateway GPRS Support Node (GGSN). SSN je klíčový pro fungování veškeré signalizace MAP (Mobile Application Part), CAP (CAMEL Application Part) a INAP (Intelligent Network Application Part). V SIGTRAN (např. při použití M3UA) je SSN zachován a přenášen přes IP, což umožňuje bezproblémovou spolupráci mezi tradičními SS7 a IP-based core sítěmi.

## K čemu slouží

SSN byl vytvořen, aby vyřešil adresovací omezení základní MTP vrstvy v SS7, která mohla směrovat zprávy pouze k uzlu (pomocí jeho Point Code). Jak se telekomunikační sítě vyvíjely a uzly začaly hostit více různých aplikačních funkcí (jako MSC obsahující také VLR nebo kombinované MSC/HLR), byl potřebný mechanismus pro nasměrování zpráv ke správnému internímu softwarovému procesu. Bez SSN by každá aplikace vyžadovala vlastní vyhrazený fyzický uzel a Point Code, což by vedlo k obrovské neefektivitě a nákladům.

Jeho zavedení spolu se SCCP umožnilo efektivní konsolidaci síťových funkcí a vývoj složitých, vrstvených signalizačních architektur. Je to základní kámen, který umožňuje aplikačním protokolům, jako je MAP, fungovat nezávisle na podkladové fyzické topologii sítě. Pro 3GPP mobilní sítě jsou standardizované hodnoty SSN naprosto klíčové pro globální roaming; německé MSC musí vědět, že pro dotaz na data účastníka musí odeslat MAP zprávu na SSN pro HLR (hodnota 6) na Point Code domovské sítě. Tento jednoduchý číselný identifikátor je základem celé globální interoperability buněčné signalizace, od 2G GSM až po spolupráci 5G s legacy SS7 sítěmi.

## Klíčové vlastnosti

- 8bitový číselný identifikátor pro aplikační podsystémy v rámci signalizačního bodu
- Používá se v SCCP Called/Calling Party Address pro směrování na aplikační úrovni
- Globálně standardizované hodnoty pro klíčové síťové funkce (např. HLR=6, MSC=5)
- Umožňuje více logickým aplikacím sdílet jeden fyzický uzel a Point Code
- Nezbytný pro doručování zpráv protokolů MAP, CAP a INAP
- Zachován a používán jak v tradičních SS7, tak v IP-based SIGTRAN (M3UA) sítích

## Související pojmy

- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.040** (Rel-19) — SMS Technical Realization
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [SSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssn/)
