---
slug: "dca"
url: "/mobilnisite/slovnik/dca/"
type: "slovnik"
title: "DCA – Direct Communication Accept"
date: 2025-01-01
abbr: "DCA"
fullName: "Direct Communication Accept"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dca/"
summary: "DCA je signalizační procedura v sítích 3GPP, která umožňuje přímou komunikaci mezi zařízeními (D2D). Umožňuje přijímajícímu UE přijmout nebo odmítnout žádost o přímou komunikaci od jiného UE a navázat"
---

DCA je signalizační procedura 3GPP, ve které přijímající UE akceptuje žádost o přímou komunikaci mezi zařízeními (device-to-device) a naváže peer-to-peer spojení bez směrování přes síťové jádro.

## Popis

Direct Communication Accept (DCA) je kritická signalizační zpráva a procedura v rámci standardů 3GPP pro služby založené na blízkosti (ProSe). Funguje v rámci zásobníku protokolu ProSe, konkrétně jako součást procedur přímé komunikace definovaných ve specifikacích rozhraní PC5. Procedura je zahájena poté, co vysílající UE odešle cílovému UE žádost o přímou komunikaci (Direct Communication Request, [DCR](/mobilnisite/slovnik/dcr/)). Zpráva DCA je formální odpovědí přijímajícího UE, která signalizuje jeho ochotu a schopnost navázat přímý komunikační spoj. Tato výměna zpráv je předpokladem pro zřízení one-to-one přímého komunikačního beareru mezi dvěma UE v autorizované blízkosti.

Technická implementace DCA zahrnuje několik síťových vrstev a bezpečnostní aspekty. Na vrstvě protokolu ProSe obsahuje zpráva DCA klíčové parametry, jako je Layer-2 ID odpovídajícího UE, bezpečnostní materiál pro navázání spojení a informace týkající se QoS. Procedura je úzce integrována s funkcí ProSe v síti, která autorizuje relaci přímé komunikace. Před odesláním DCA musí přijímající UE ověřit žádost vůči svým politikám a údajům o předplatném, což často vyžaduje interakci s funkcí ProSe pro autorizaci a zjišťování. Bezpečnostní rámec, podrobně popsaný ve specifikacích jako 33.836, zajišťuje ochranu procedury DCA proti odposlechu a útokům vydávání se za jiného, typicky za použití klíčů odvozených od funkce ProSe.

Z architektonického hlediska DCA umožňuje zřízení přímé komunikační cesty na referenčním bodě PC5, což je sidelink rozhraní pro [D2D](/mobilnisite/slovnik/d2d/) komunikaci. To se liší od tradiční buněčné komunikace, která směruje všechna data přes eNodeB a síťové jádro. Procedura spravuje konfiguraci rádiových prostředků pro přímý spoj, včetně přidělení prostředků od eNodeB (v režimu řízeném sítí) nebo výběru prostředků z fondu (v autonomním režimu). Jakmile je DCA úspěšně vyměněna, mohou obě UE pokračovat ve zřízení zabezpečeného přímého komunikačního beareru, což umožňuje výměnu dat s nízkou latencí a vysokou účinností, klíčovou pro veřejnou bezpečnost, vozidlovou komunikaci (V2X) a komerční aplikace ProSe.

## K čemu slouží

DCA byla vytvořena pro podporu základního požadavku na komunikaci mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)) v rámci buněčných sítí, což je funkce standardizovaná jako služby založené na blízkosti (ProSe) počínaje 3GPP Release 12. Před zavedením ProSe musela veškerá komunikace mezi uživatelskými zařízeními (UE) procházet síťovou infrastrukturou (eNodeB a síťové jádro), i když byla zařízení v těsné fyzické blízkosti. Tato architektura zaváděla zbytečnou latenci, spotřebovávala rádiové prostředky pro uplink a downlink a byla závislá na síťovém pokrytí – což je významné omezení pro scénáře veřejné bezpečnosti, kde může být infrastruktura poškozena nebo nedostupná.

Primární problém, který DCA řeší, je umožnění efektivního, autorizovaného a bezpečného navázání přímé komunikace mezi blízkými UE. Při zásazích pro veřejnou bezpečnost a kritické komunikace potřebují záchranáři komunikovat přímo, když je síťové pokrytí narušeno. Komerční aplikace také těží z přímých spojů pro sdílení obsahu, hraní her nebo sociální sítě. Procedura DCA jako součást nastavení přímé komunikace poskytuje řízený handshake, který zajišťuje, že pouze autorizovaná UE mohou navázat přímá spojení, spravuje očekávání QoS a integruje se s bezpečnostním a politickým rámcem sítě. Řeší tak omezení ad-hoc sítí tím, že začleňuje D2D komunikaci pod zastřešení standardů 3GPP, což zajišťuje spolehlivost, bezpečnost a interoperabilitu.

## Klíčové vlastnosti

- Autorizuje zřízení one-to-one přímých komunikačních bearerů mezi UE
- Integruje se s funkcí ProSe pro síťovou autorizaci a správu bezpečnostních klíčů
- Funguje na sidelink rozhraní PC5 nezávisle na infrastruktuře sítě Uu
- Podporuje jak režim přidělování prostředků řízený sítí, tak autonomní režim řízený UE
- Obsahuje bezpečnostní parametry pro zřízení chráněného přímého komunikačního spojení
- Nese informace o QoS pro vyjednání požadavků na službu pro přímý spoj

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TR 33.740** (Rel-18) — Security and Privacy Aspects of Proximity Based Services in 5G System Phase 2
- **TS 33.836** (Rel-16) — Security Study for Advanced V2X Services

---

📖 **Anglický originál a plná specifikace:** [DCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dca/)
