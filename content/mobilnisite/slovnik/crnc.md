---
slug: "crnc"
url: "/mobilnisite/slovnik/crnc/"
type: "slovnik"
title: "CRNC – Controlling Radio Network Controller"
date: 2025-01-01
abbr: "CRNC"
fullName: "Controlling Radio Network Controller"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/crnc/"
summary: "CRNC je logická role v rámci řadiče rádiové sítě UMTS (RNC), která řídí sadu Node B a spravuje jejich rádiové prostředky. Je zodpovědná za správu rádiových prostředků, řízení přístupu a funkce mobilit"
---

CRNC je logická role v rámci řadiče rádiové sítě UMTS, která řídí sadu Node B a spravuje jejich rádiové prostředky pro efektivní provoz sítě.

## Popis

Controlling Radio Network Controller (CRNC) je základní logická entita v architektuře [UTRAN](/mobilnisite/slovnik/utran/), konkrétně definovaná jako funkční role řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). Z fyzického pohledu je RNC síťový prvek, ale logicky může fungovat v různých rolích vzhledem k připojení uživatelského zařízení (UE): Controlling RNC (CRNC), Serving RNC ([SRNC](/mobilnisite/slovnik/srnc/)) a Drift RNC ([DRNC](/mobilnisite/slovnik/drnc/)). Role CRNC je definována pro konkrétní sadu Node B (základnových stanic) a buněk, které provozují. Pro každou buňku v UTRAN existuje právě jeden RNC, který funguje jako její CRNC. CRNC je zodpovědná za celkové řízení logických prostředků (jako jsou kanalizační kódy a scrambling kódy), které patří jejím Node B. Provádí kritické funkce vrstvy 2 a vrstvy 3 pro společné řídicí kanály ([CCCH](/mobilnisite/slovnik/ccch/)) v těchto buňkách.

Architektonicky se CRNC připojuje ke svým řízeným Node B přes rozhraní Iub. Prostřednictvím tohoto rozhraní řídí provoz Node B, včetně konfigurace buněk, přidělování rádiových prostředků a reportování měření. CRNC je jediným bodem pro interakci správy a údržby (O&M) pro své Node B. Zpracovává navázání spojení [RRC](/mobilnisite/slovnik/rrc/) pro UE přistupující do sítě přes své buňky. Když UE poprvé naváže spojení, RNC řídící buňku, na které je přijímán náhodný přístupový kanál ([RACH](/mobilnisite/slovnik/rach/)), se stává CRNC pro tento počáteční přístup a následně Serving RNC (SRNC) pro spojení tohoto UE.

Hlavní provozní zodpovědnost CRNC zahrnuje správu rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) pro své buňky. To zahrnuje řízení přístupu, při kterém CRNC vyhodnocuje, zda jsou dostupné dostatečné rádiové a přenosové síťové prostředky pro přijetí nové žádosti o rádiový přístupový bearer bez degradace stávajících spojení. Také provádí řízení zahlcení a spravuje přidělování rádiových prostředků, jako je výkon a kanalizační kódy. Pro mobilitu CRNC zajišťuje přechody uvnitř Node B a mezi Node B (ale v rámci stejného CRNC), kde se UE pohybuje mezi buňkami, které jsou všechny řízeny stejným CRNC. Tyto přechody provádí koordinací nastavení a uvolňování rádiových spojení na zapojených Node B.

Klíčový rozdíl je mezi CRNC a SRNC. Zatímco CRNC je vázána na řízení fyzických Node B a buněk, SRNC je role vázaná na konkrétní spojení UE. SRNC je zodpovědná za kompletní spojení RRC s UE, včetně šifrování, ochrany integrity a ukončení rozhraní Iu směrem k jádru sítě. V mnoha případech, zejména když UE není v měkkém přechodu s buňkami od jiného RNC, jsou SRNC a CRNC pro aktivní buňku stejný fyzický RNC. Nicméně, když je UE v měkkém přechodu s buňkou řízenou jiným RNC (Drift RNC nebo DRNC), role SRNC a CRNC jsou oddělené. CRNC driftové buňky (DRNC) spravuje rádiové prostředky své buňky pro toto spojení UE, ale přeposílá data k/od SRNC přes rozhraní Iur.

## K čemu slouží

Koncept CRNC byl zaveden ve specifikaci 3GPP Release 99, aby řešil potřebu centralizované, inteligentní kontroly rádiových prostředků v nové síti UMTS založené na WCDMA. Na rozdíl od 2G GSM, kde řadič základnových stanic (BSC) měl relativně jednodušší správu založenou na časových slotech, rozhraní WCDMA založené na kódech a omezené interferencí vyžadovalo sofistikovanější a dynamičtější správu prostředků. Role CRNC byla navržena tak, aby poskytla tento centralizovaný řídicí bod pro skupinu Node B, což umožnilo efektivní využití vzácných rádiových prostředků, jako jsou ortogonální kódy s proměnným rozprostřením (OVSF), a správu vysílacího výkonu buňky pro kontrolu interference.

Tento centralizovaný řídicí model vyřešil několik problémů vlastních distribuované rádiové síti. Umožnil koordinovanou správu rádiových prostředků napříč více buňkami, což umožnilo funkce jako měkký přechod, kde je UE současně připojeno k více buňkám. CRNC jako jediný řadič pro sadu buněk mohla činit optimální rozhodnutí o přechodech a vyvažování zátěže. Také poskytla jediný bod pro správu a konfiguraci sítě, což zjednodušilo provoz rádiové přístupové sítě. Oddělením logických rolí (CRNC, SRNC, DRNC) dosáhla architektura UTRAN flexibility, což umožnilo ukotvit spojení UE u jednoho RNC (SRNC) a zároveň využívat rádiové prostředky z buněk řízených jinými RNC, což bylo zásadní pro plynulou mobilitu napříč rozsáhlými sítěmi spravovanými více RNC.

## Klíčové vlastnosti

- Řídí logické rádiové prostředky (kódy, výkon) pro definovanou sadu Node B a buněk
- Provádí řízení přístupu a řízení zahlcení pro své řízené buňky
- Spravuje rozhraní Iub směrem ke svým podřízeným Node B pro provoz a údržbu
- Zajišťuje funkce vrstvy 2/vrstvy 3 pro společné řídicí kanály (CCCH) ve svých buňkách
- Provádí přechody uvnitř CRNC (mobilita mezi buňkami pod její kontrolou)
- Slouží jako koncový bod pro protokol NBAP (Node B Application Part) od svých Node B

## Související pojmy

- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [SRNC – Serving Radio Network Controller](/mobilnisite/slovnik/srnc/)
- [DRNC – Drift Radio Network Controller](/mobilnisite/slovnik/drnc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 43.130** (Rel-19) — Iur-g Interface Overview

---

📖 **Anglický originál a plná specifikace:** [CRNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/crnc/)
