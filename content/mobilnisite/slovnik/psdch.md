---
slug: "psdch"
url: "/mobilnisite/slovnik/psdch/"
type: "slovnik"
title: "PSDCH – Physical Sidelink Discovery Channel"
date: 2025-01-01
abbr: "PSDCH"
fullName: "Physical Sidelink Discovery Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/psdch/"
summary: "Fyzický kanál v LTE a NR pro komunikaci typu zařízení-zařízení (D2D), konkrétně pro služby založené na blízkosti (ProSe). Umožňuje uživatelským zařízením vysílat a přijímat zprávy pro objevování přímo"
---

PSDCH (Physical Sidelink Discovery Channel) je přímý kanál typu zařízení-zařízení v LTE a NR pro vysílání a příjem zpráv pro objevování služby ProSe vzdušným rozhraním za účelem umožnění objevení protějšků.

## Popis

Physical Sidelink Discovery Channel (PSDCH) je klíčovou součástí postranního rozhraní ([SL](/mobilnisite/slovnik/sl/)) v LTE, definovanou pro služby založené na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) počínaje 3GPP Release 12. Funguje na rozhraní PC5, což je přímý rádiový spoj mezi uživatelskými zařízeními (UE). Na rozdíl od buněčného provozu, který prochází přes eNodeB/gNB, PSDCH umožňuje přímou komunikaci UE-UE pro specifický účel objevování. Jeho primární funkcí je přenášet oznámení o objevení a monitorovací zprávy, což umožňuje UE detekovat a být detekována jinými blízkými UE.

Z architektonického hlediska je PSDCH mapován z transportního kanálu Sidelink Discovery Channel ([SL-DCH](/mobilnisite/slovnik/sl-dch/)). Zpracování na fyzické vrstvě zahrnuje kanálové kódování, scramblování, modulaci (pomocí [QPSK](/mobilnisite/slovnik/qpsk/)) a mapování zdrojů na konkrétní bloky fyzických zdrojů ([PRB](/mobilnisite/slovnik/prb/)) v rámci fondů zdrojů pro postranní řídicí a datové kanály. Tyto fondy jsou konfigurovány sítí nebo předkonfigurovány pro scénáře mimo pokrytí. Kanál funguje v režimu vysílání (broadcast), přičemž přenosy jsou strukturovány do period objevování, což zajišťuje efektivní využití rádiových zdrojů a životnosti baterie.

Klíčové součásti zahrnují samotnou zprávu pro objevování, která obsahuje ProSe Application Code nebo ProSe Restricted Code pro otevřené, respektive omezené objevování. Protokolový zásobník UE pro objevování zahrnuje ProSe Protocol, který tyto kódy generuje, a přístupovou vrstvu (Access Stratum), která zajišťuje vysílání a příjem prostřednictvím PSDCH. Kanál podporuje jak procedury objevování Modelu A („Jsem tady“), tak Modelu B („Kdo je tam?“). Jeho role je zásadní pro umožnění přímých služeb [D2D](/mobilnisite/slovnik/d2d/) a představuje počáteční krok před navázáním přímého komunikačního spoje (např. přes [PSSCH](/mobilnisite/slovnik/pssch/)/[PSBCH](/mobilnisite/slovnik/psbch/)) pro aplikace veřejné bezpečnosti, komunikaci vozidlo-se-vším (V2X) nebo komerční aplikace ProSe.

## K čemu slouží

PSDCH byl vytvořen, aby řešil potřebu přímého objevování zařízení ve službách založených na blízkosti, což je základním kamenem pro aplikace veřejné bezpečnosti a komerční D2D aplikace. Před jeho zavedením veškerá buněčná komunikace procházela sítí, a to i pro zařízení v bezprostřední fyzické blízkosti. To způsobovalo zbytečnou latenci, spotřebovávalo zdroje jádra sítě a bylo zcela závislé na síťovém pokrytí, což je nepřijatelné pro scénáře první pomoci (např. při poškození sítě).

Historický kontext představuje práce 3GPP na službách založených na blízkosti (ProSe) zahájená v Release 12, řízená požadavky organizací veřejné bezpečnosti a potenciálem pro nové komerční služby. PSDCH řeší základní problém: „Jak se zařízení mohou vzájemně najít přímo přes vzdušné rozhraní?“ Poskytuje standardizovanou, efektivní a bezpečnou metodu, kterou mohou UE oznamovat svou přítomnost nebo objevovat služby od blízkých protějšků, což umožňuje následnou přímou komunikaci (postranní komunikaci). Tato schopnost je klíčová pro komunikaci veřejné bezpečnosti mimo síť, aplikace sociálních sítí a později se vyvinula v základ pro postranní komunikaci V2X založenou na LTE.

## Klíčové vlastnosti

- Funguje na postranním rozhraní PC5 pro přímou komunikaci UE-UE
- Přenáší ProSe Application Codes a ProSe Restricted Codes pro objevování
- Podporuje dva modely objevování: na bázi oznámení (Model A) a na bázi vyžádání (Model B)
- Využívá vyhrazené fondy zdrojů pro postranní komunikaci konfigurované sítí nebo předkonfigurované
- Používá režim vysílání (broadcast) v rámci definovaných period objevování
- Zásadní pro umožnění scénářů ProSe jak v pokrytí, tak mimo pokrytí (částečné nebo úplné)

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [PSCCH – Physical Sidelink Control Channel](/mobilnisite/slovnik/pscch/)
- [PSSCH – Physical Sidelink Shared Channel](/mobilnisite/slovnik/pssch/)
- [SL-DCH – Sidelink Discovery Channel](/mobilnisite/slovnik/sl-dch/)

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
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PSDCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/psdch/)
