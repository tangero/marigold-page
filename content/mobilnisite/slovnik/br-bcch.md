---
slug: "br-bcch"
url: "/mobilnisite/slovnik/br-bcch/"
type: "slovnik"
title: "BR-BCCH – Bandwidth Reduced Broadcast Control Channel"
date: 2025-01-01
abbr: "BR-BCCH"
fullName: "Bandwidth Reduced Broadcast Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/br-bcch/"
summary: "Vysílací kanál navržený pro zařízení LTE-M (LTE pro komunikaci typu Machine-Type Communications) a NB-IoT, pracující se sníženou šířkou pásma (1,08 MHz nebo 180 kHz), aby umožnil efektivní příjem zaří"
---

BR-BCCH je vysílací kanál pro zařízení LTE-M a NB-IoT, který pracuje se sníženou šířkou pásma, aby efektivně přenášel základní systémové informace pro zařízení s nízkou složitostí a omezeným napájením.

## Popis

Bandwidth Reduced Broadcast Control Channel (BR-BCCH) je klíčový kanál fyzické vrstvy zavedený ve specifikaci 3GPP Release 13 jako součást vylepšení LTE-M (eMTC) a NB-IoT pro Cellular IoT. Je primárním vysílacím mechanismem pro doručování základních systémových informací zařízením se sníženou šířkou pásma. Na rozdíl od konvenčního LTE Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)), který pracuje v plné systémové šířce pásma (např. až 20 MHz), je BR-BCCH omezen na provoz v mnohem užším pásmu: 1,08 MHz (šest zdrojových bloků) pro LTE-M a 180 kHz (jeden zdrojový blok) pro NB-IoT. Tento návrh je zásadní pro podporu nízkonákladových, nízkopříkonových IoT zařízení s omezenými [RF](/mobilnisite/slovnik/rf/) schopnostmi.

Z architektonického hlediska je BR-BCCH mapován na Bandwidth Reduced Physical Broadcast Channel (BR-PBCH) a Bandwidth Reduced Physical Downlink Shared Channel (BR-PDSCH) pro přenos Master Information Block ([MIB](/mobilnisite/slovnik/mib/)) a System Information Blocks (SIBs). Struktura kanálu je zjednodušená a opakující se, aby usnadnila energeticky efektivní příjem. Zařízení mohou využívat rozšířený nespojitý příjem (eDRX) a režim úspory energie ([PSM](/mobilnisite/slovnik/psm/)), periodicky se probouzet ke čtení BR-BCCH s minimální aktivní dobou. Přenášené informace zahrnují parametry přístupu k buňce, plánovací informace pro další kanály a konfigurační podrobnosti pro provoz se sníženou šířkou pásma.

Jeho provoz zahrnuje specifická časová a frekvenční přidělení uvnitř nosiče LTE. Při provozu in-band zabírá BR-BCCH úzkou část spektra hostitelského nosiče LTE. Kanál využívá robustní modulaci ([QPSK](/mobilnisite/slovnik/qpsk/)) a kódovací schémata, aby zajistil spolehlivý příjem i v náročných rádiových podmínkách. Klíčové komponenty zahrnují BR-MIB, který poskytuje základní časové a plánovací informace potřebné k dekódování BR-SIBs. BR-SIBs přenášejí detailní přístupové parametry, informace o převýběru buňky a konfigurace pro náhodný přístup a datové kanály jako BR-PDSCH a BR-PUSCH.

Role BR-BCCH v síti je základní pro připojení a mobilitu IoT zařízení. Umožňuje milionům zařízení s nízkou složitostí efektivně objevit síť, synchronizovat se a získat potřebné parametry pro procedury počátečního přístupu a režimu nečinnosti bez nutnosti zpracovávat širokopásmové signály. Tento kanál je úhelným kamenem rádiových přístupových sítí LTE-M a NB-IoT a zajišťuje, že doručování systémových informací je optimalizováno pro omezení nasazení masivní komunikace typu Machine-Type Communications (mMTC).

## K čemu slouží

BR-BCCH byl vytvořen, aby řešil specifické požadavky Cellular IoT (CIoT) zavedené ve specifikaci 3GPP Release 13, konkrétně pro LTE-M a NB-IoT. Před Release 13 bylo LTE navrženo primárně pro vysokorychlostní mobilní širokopásmový přístup, přičemž systémové informace byly vysílány přes celou šířku pásma nosiče. To bylo nevhodné pro nízkonákladová, nízkopříkonová IoT zařízení, která potřebovala zjednodušené [RF](/mobilnisite/slovnik/rf/) přední části (podporující pouze šířku pásma 1,08 MHz nebo 180 kHz), aby se snížily náklady a spotřeba energie. Příjem širokopásmového [BCCH](/mobilnisite/slovnik/bcch/) by vyžadoval nadměrnou energii a složité obvody, což by negovalo výhody optimalizovaných IoT zařízení.

Primární problém, který BR-BCCH řeší, je umožnění efektivního síťového přístupu pro tato zařízení se sníženou šířkou pásma. Umožňuje jim získat kritické systémové informace – jako je identita buňky, stav blokování přístupu a plánovací informace pro další kanály – při provozu v jejich úzkém přijímacím pásmu. To přímo podporuje klíčové cíle IoT: prodlouženou životnost baterie (přes 10 let pro některé aplikace), sníženou složitost a náklady zařízení a vylepšené pokrytí (až 20 dB vylepšení oproti staršímu LTE).

Historicky vycházela motivace z potřeby standardizované, na buňkové síti založené LPWAN (Low-Power Wide-Area Network) technologie, která by konkurovala ne-3GPP technologiím jako LoRa a Sigfox. BR-BCCH jako součást sady LTE-M/NB-IoT umožnil operátorům 3GPP znovu využít jejich stávající spektrum LTE a infrastrukturu pro masivní nasazení IoT. Řešil omezení předchozích vysílacích kanálů LTE zavedením varianty se sníženou šířkou pásma a optimalizovanou pro nízký příkon, která je v souladu s omezeními fyzické vrstvy zařízení CIoT, a umožňuje tak škálovatelnou konektivitu pro chytré měřiče, senzory, nositelnou elektroniku a další aplikace mMTC.

## Klíčové vlastnosti

- Pracuje v rámci snížené šířky pásma (1,08 MHz pro LTE-M, 180 kHz pro NB-IoT)
- Přenáší základní systémové informace (MIB a SIBs) pro zařízení se sníženou šířkou pásma
- Umožňuje rozšířený nespojitý příjem (eDRX) a režim úspory energie (PSM) pro extrémně nízkou spotřebu energie
- Používá robustní modulaci a kódování (QPSK) pro vylepšené pokrytí v náročných podmínkách
- Podporuje režimy nasazení in-band, guard-band a standalone v rámci spektra LTE
- Poskytuje plánovací informace pro další kanály se sníženou šířkou pásma, jako je BR-PDSCH

## Související pojmy

- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [SIB – System Information Block](/mobilnisite/slovnik/sib/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [BR-BCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/br-bcch/)
