---
slug: "g-cs-rnti"
url: "/mobilnisite/slovnik/g-cs-rnti/"
type: "slovnik"
title: "G-CS-RNTI – Group Configured Scheduling Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "G-CS-RNTI"
fullName: "Group Configured Scheduling Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/g-cs-rnti/"
summary: "Identifikátor v rádiové síti používaný v 5G NR pro skupinové plánování s konfigurovaným přístupem, primárně pro IoT a MTC. Umožňuje efektivní přidělování zdrojů pro více UE sdílejících stejnou konfigu"
---

G-CS-RNTI je identifikátor v rádiové síti používaný v 5G NR pro skupinové plánování s konfigurovaným přístupem (configured scheduling), který umožňuje efektivní přidělování zdrojů pro více UE sdílejících stejnou polo-perzistentní konfiguraci za účelem snížení signalizační režie.

## Popis

G-CS-RNTI (Group Configured Scheduling Radio Network Temporary Identifier) je specializovaný RNTI zavedený ve specifikaci 3GPP Release 17 pro 5G New Radio (NR) na podporu skupinového plánování s konfigurovaným přístupem, což je funkce klíčová pro hromadnou komunikaci mezi stroji (mMTC) a scénáře Internetu věcí (IoT). Funguje v rámci vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a vrstvy řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)), jak je podrobně popsáno ve specifikacích 38.321 a 38.331. Na rozdíl od RNTI specifických pro UE, jako je [C-RNTI](/mobilnisite/slovnik/c-rnti/), je G-CS-RNTI sdílen skupinou UE, které byly nakonfigurovány s identickými parametry polo-perzistentního plánování (SPS) pro uplink. Tato skupinová konfigurace je stanovena prostřednictvím RRC signalizace, kdy síť přiřadí hodnotu G-CS-RNTI a přidružené SPS zdroje, jako je periodicita, časové/frekvenční alokace a schémata modulace a kódování, více zařízením současně.

Když je UE nakonfigurováno s G-CS-RNTI, monitoruje fyzický kanál řídicího signálu na downlinku ([PDCCH](/mobilnisite/slovnik/pdcch/)) pro řídicí informace na downlinku ([DCI](/mobilnisite/slovnik/dci/)) zašifrované tímto identifikátorem. Při detekci takové DCI ji všechna UE ve skupině interpretují jako příkaz pro aktivaci, deaktivaci nebo opakovaný přenos jejich předkonfigurovaných SPS zdrojů, dle specifikace 38.213. Tento mechanismus umožňuje síti spravovat zdroje pro četná UE pomocí jediné řídicí zprávy, což drasticky snižuje režii řídicí signalizace, která by jinak byla nutná, pokud by bylo každé UE adresováno individuálně. G-CS-RNTI je obzvláště účinný pro aplikace s periodickými, předvídatelnými vzorci provozu, jako je například hlášení dat ze senzorů nebo odečty chytrých měřičů, kde zařízení přenášejí malé pakety v pravidelných intervalech.

Z architektonického hlediska se G-CS-RNTI integruje s plánovačem MAC v NR v gNB, který zajišťuje přidělování zdrojů a rozhodování o plánování. Klíčové komponenty zahrnují protokol RRC pro správu konfigurace, vrstvu MAC pro aktivaci plánování a fyzickou vrstvu pro zpracování PDCCH. Jeho úlohou je zvýšit spektrální účinnost a životnost baterie zařízení minimalizací potřeby častých žádostí o plánování a přidělení zdrojů, čímž podporuje škálovatelná nasazení IoT. G-CS-RNTI také doplňuje další funkce NR, jako jsou režimy úspory energie a techniky vylepšení pokrytí, a zajišťuje tak spolehlivý a efektivní provoz v různých prostředích mMTC.

## K čemu slouží

G-CS-RNTI byl vytvořen, aby řešil rostoucí nároky hromadných nasazení IoT v 5G sítích, kde se tradiční mechanismy plánování pro jednotlivá UE stávají neefektivními a náročnými na zdroje. Před Release 17 se konfigurované plánování v NR opíralo o SPS specifické pro UE, což vyžadovalo individuální [RRC](/mobilnisite/slovnik/rrc/) konfigurace a [DCI](/mobilnisite/slovnik/dci/) aktivace pro každé zařízení, což vedlo k nadměrnému zahlcení řídicího kanálu a signalizační režii. Tento přístup byl neudržitelný pro scénáře zahrnující tisíce zařízení s nízkou spotřebou a periodickým přenosem, jako jsou chytrá města nebo průmyslový IoT, protože vyčerpával kapacitu sítě a zvyšoval spotřebu energie UE kvůli častému monitorování a signalizační interakci.

Motivován potřebou škálovatelnosti a energetické účinnosti v mMTC, zavedl 3GPP ve Release 17 skupinové plánování s konfigurovaným přístupem spolu s G-CS-RNTI. Tato inovace řeší problém neefektivního řízení zdrojů pro periodický provoz tím, že umožňuje jedinou řídicí zprávu plánovat více UE současně. Historický kontext zahrnuje dřívější vylepšení LTE, jako eMTC a NB-IoT, která nabízela skupinové plánování, ale byla omezena na užší šířky pásma a jednodušší případy užití; G-CS-RNTI rozšiřuje tyto koncepty na flexibilnější a vysokokapacitní rámec 5G NR. Přímo řeší omezení předchozích přístupů snížením pokusů o slepé dekódování [PDCCH](/mobilnisite/slovnik/pdcch/), snížením latence pro skupinové aktivace a úsporou životnosti baterie UE minimalizací signalizace, čímž podporuje vizi 5G o propojení obrovského počtu zařízení bezproblémově.

G-CS-RNTI dále usnadňuje síťové segmentování (network slicing) pro služby IoT tím, že umožňuje efektivní rozdělení zdrojů pro různé skupiny zařízení. Souladí s probíhajícími snahami 3GPP optimalizovat NR pro různé vertikály a zajistit, aby 5G mohlo splnit přísné požadavky na ultra-spolehlivou komunikaci s nízkou latencí (URLLC) a vylepšené mobilní širokopásmové připojení (eMBB) vedle mMTC. Řešením těchto klíčových výzev hraje G-CS-RNTI klíčovou roli při umožnění nákladově efektivních a škálovatelných řešení IoT v rámci ekosystému 5G.

## Klíčové vlastnosti

- Umožňuje skupinové polo-perzistentní plánování pro více UE se sdíleným RNTI
- Snižuje režii řídicí signalizace použitím jediné DCI pro skupinovou aktivaci/deaktivaci
- Podporuje periodické uplink přenosy ideální pro aplikace IoT a MTC
- Integruje se s vrstvami MAC a RNR v NR pro efektivní konfiguraci zdrojů
- Zlepšuje úsporu energie UE minimalizací frekvence žádostí o plánování
- Usnadňuje škálovatelné síťové řízení pro hromadná nasazení zařízení

## Související pojmy

- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [G-CS-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/g-cs-rnti/)
