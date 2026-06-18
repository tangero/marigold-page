---
slug: "nsa"
url: "/mobilnisite/slovnik/nsa/"
type: "slovnik"
title: "NSA – Non-Standalone"
date: 2025-01-01
abbr: "NSA"
fullName: "Non-Standalone"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nsa/"
summary: "Non-Standalone (NSA) je režim nasazení 5G, ve kterém přístupová síť 5G New Radio (NR) spoléhá na stávající 4G LTE páteřní síť (EPC) pro funkce řídicí roviny, zatímco 5G NR poskytuje zvýšenou datovou k"
---

NSA je režim nasazení 5G, ve kterém 5G rádiová síť využívá stávající 4G páteřní síť pro řídicí funkce, aby umožnil rychlejší zavedení služeb.

## Popis

Režim provozu Non-Standalone (NSA), formálně specifikovaný ve 3GPP Release 15, je síťová architektura, ve které je nové 5G rádiové rozhraní New Radio (NR) nasazeno souběžně a je úzce integrováno se stávající 4G LTE sítí. V NSA si zařízení (UE) udržuje duální spojení: je ukotveno k 4G LTE buňce (fungující jako hlavní uzel neboli MeNB) pro veškerou signalizaci řídicí roviny (jako je navázání spojení, správa mobility a paging), a současně se připojuje k 5G NR buňce (fungující jako sekundární uzel neboli SgNB), která poskytuje dodatečnou šířku pásma pro datovou rovinu. Tato architektura je nejčastěji spojována s variantou Option 3 (konkrétně variantami 3, 3a a 3x), kde je LTE [eNB](/mobilnisite/slovnik/enb/) připojen k 4G Evolved Packet Core (EPC) a 5G gNB poskytuje sekundární datovou cestu, která je také ukotvena v EPC.

Z technického pohledu je provoz NSA umožněn rámcem Dual Connectivity ([DC](/mobilnisite/slovnik/dc/)), původně vyvinutým pro LTE-Advanced. UE naváže primární spojení s LTE eNB přes rozhraní LTE-Uu. Když to podmínky dovolí a síť se rozhodne přidat 5G kapacitu, LTE eNB v roli hlavního uzlu koordinuje s 5G gNB vytvoření sekundární skupiny buněk pro UE. To zahrnuje signalizaci přes rozhraní [X2](/mobilnisite/slovnik/x2/) (konkrétně [X2-C](/mobilnisite/slovnik/x2-c/) pro řídicí rovinu a [X2-U](/mobilnisite/slovnik/x2-u/) pro datovou rovinu ve variantách Option 3). Tok dat uživatelské roviny může být rozdělen v různých bodech: ve variantě Option 3 prochází všechna data přes LTE eNB; ve variantě Option 3a jsou některé datové přenosy směrovány přímo z EPC na gNB; a ve variantě Option 3x LTE eNB zvládá signalizační ukotvení a část dat, zatímco gNB může zvládnout většinu provozu uživatelské roviny, přičemž dělení dat probíhá na eNB. Páteřní síť zůstává EPC, což znamená, že UE používá 4G [NAS](/mobilnisite/slovnik/nas/) protokoly pro komunikaci s [MME](/mobilnisite/slovnik/mme/) a služby jako IMS hlas nadále spoléhají na VoLTE.

Role NSA byla klíčová jako přechodová technologie. Umožnila mobilním síťovým operátorům ([MNO](/mobilnisite/slovnik/mno/)) zavést 5G NR rádiové stanice ve vybraných oblastech s vysokým provozem, aby zvýšili přenosové rychlosti a kapacitu, bez bezprostřední potřeby investovat a nasadit zcela novou páteřní síť 5G Core (5GC). To významně urychlilo uvedení 5G služeb na trh. Pro UE to zjednodušilo návrh raných 5G zařízení, protože nebylo vyžadováno komplexní signalizační rozhraní 5G páteřní sítě (5G NAS přes N1). NSA však neumožňuje plnou škálu 5G schopností, jako je síťové dělení (network slicing) založené na architektuře orientované na služby (SBA), ultra-spolehlivá komunikace s nízkou latencí (URLLC) s edge computingem nebo pokročilé funkce správy relací vlastní 5GC. Ty jsou umožněny režimem Standalone (SA), kde jsou nové jak rádiové rozhraní (NR), tak páteřní síť (5GC).

## K čemu slouží

Vytvoření režimu NSA bylo hnací silou jasného tržního a technického imperativu: umožnit rychlejší a nákladově efektivnější zavedení 5G služeb. Koncem roku 2010 měli operátoři masivně investováno do všudypřítomných a stabilních 4G LTE sítí. Nasazení zcela nového 5G systému s novým rádiovým rozhraním a novou páteřní sítí (SA) představovalo obrovskou současnou kapitálovou investici a provozní výzvu. NSA poskytla pragmatický přechodový krok. Vyřešila problém, jak dodat nejbezprostředněji prodejnou výhodu 5G – dramaticky vyšší datové rychlosti – pouhým přidáním 5G NR nosných do stávající síťové struktury.

Tento přístup řešil několik klíčových omezení. Za prvé využil zavedené pokrytí a spolehlivost LTE sítě pro řídicí funkce, což zajistilo kontinuitu služeb a podporu mobility od prvního dne. Za druhé umožnil fázované investice, kdy mohla být nákladná nová páteřní síť nasazena později, až budou její pokročilejší funkce potřeba a technologie bude zralejší. Za třetí vytvořil trh pro 5G zařízení a služby dříve, což podpořilo vývoj ekosystému. Bez NSA by bylo komerční spuštění 5G oddáleno o několik let. Účelem NSA tedy bylo v zásadě umožnit migraci a snížit riziko, poskytnout jasnou cestu od 4G k plné 5G vizi SA, a přitom v mezidobí přinést hmatatelné výhody pro uživatele.

## Klíčové vlastnosti

- 5G NR rádiový přístup je závislý na 4G LTE pro ukotvení řídicí roviny (prostřednictvím E-UTRA-NR Dual Connectivity - EN-DC).
- Využívá stávající 4G Evolved Packet Core (EPC) pro funkce páteřní sítě.
- Umožňuje vyšší špičkové přenosové rychlosti a kapacitu agregací spektra LTE a NR.
- Podporuje rychlejší nasazení 5G díky opětovnému využití zavedené LTE infrastruktury.
- Definován více variantami nasazení (např. Option 3, 3a, 3x) s různými body ukotvení uživatelské roviny.
- UE vyžaduje schopnost duální konektivity, ale nepotřebuje podporu protokolu 5G Core NAS.

## Definující specifikace

- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 29.153** (Rel-19) — Ns Reference Point Protocol between SCEF and RCAF
- **TS 32.423** (Rel-19) — Trace Data Definition and Management
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 37.718** — 3GPP TR 37.718
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.561** (Rel-19) — UE Conformance for TRP/TRS FR1
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [NSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsa/)
