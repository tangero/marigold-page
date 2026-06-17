---
slug: "ec"
url: "/mobilnisite/slovnik/ec/"
type: "slovnik"
title: "EC – Extended Coverage System Information"
date: 2026-01-01
abbr: "EC"
fullName: "Extended Coverage System Information"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ec/"
summary: "Extended Coverage System Information (EC SI) je funkce, která vylepšuje přenos základních bloků systémových informací (SIBs), aby podpořila zařízení v náročných rádiových podmínkách, jako jsou hluboko"
---

EC je funkce, která vylepšuje přenos základních systémových informací pomocí opakování a robustní modulace, aby podpořila zařízení v náročných rádiových podmínkách, například pro IoT a MTC zařízení.

## Popis

Extended Coverage System Information ([EC](/mobilnisite/slovnik/ece-c/) SI) označuje mechanismy definované v 3GPP pro zlepšení spolehlivosti získávání systémových informací (SI) uživatelským zařízením (UE), zejména těch, která pracují v podmínkách rozšířeného pokrytí, jak je vyžadováno pro komunikaci typu Machine-Type Communication ([MTC](/mobilnisite/slovnik/mtc/)) a Narrowband-IoT (NB-IoT). Systémové informace poskytují UE základní parametry potřebné pro přístup k buňce a provoz v ní, včetně parametrů přístupu k buňce, informací o sousedních buňkách a konfigurace společných kanálů. Za normálních podmínek jsou SIBs periodicky vysílány na Broadcast Channel ([BCH](/mobilnisite/slovnik/bch/)) a Downlink Shared Channel ([DL-SCH](/mobilnisite/slovnik/dl-sch/)). Pro UE ve velmi špatných signálových podmínkách (např. hluboko uvnitř budov, v suterénech nebo na okraji pokrytí) však mohou být tato standardní vysílání nerozluštitelná.

EC SI funguje tak, že na přenos konkrétních SIBs aplikuje techniky vylepšení pokrytí. Tyto techniky primárně zahrnují opakování v časové oblasti, kde je stejný SIB přenášen vícekrát v po sobě jdoucích podrámcích. UE pak může tato opakovaná vysílání kombinovat pomocí soft kombinování na fyzické vrstvě, čímž zlepší efektivní poměr signálu k šumu (SNR) a úspěšně dekóduje informace. Dále mohou být pro technologie jako NB-IoT použity pro tyto SIBs s rozšířeným pokrytím robustnější modulační a kódovací schémata (např. modulace nižšího řádu jako [BPSK](/mobilnisite/slovnik/bpsk/)). Síť použití EC SI indikuje prostřednictvím hlavních informačních bloků (MIBs) nebo plánovacích informací, čímž UE sděluje, které SIBs jsou vysílány s rozšířeným pokrytím a jaký je jejich vzorec opakování.

Architektura zahrnuje úpravy na straně eNodeB (pro LTE) nebo gNB (pro NR) pro plánování a vysílání těchto opakovaných SIB bloků. Na straně UE je vyžadována odpovídající schopnost tato opakování sledovat a provádět potřebné kombinování. Konkrétní SIBs, které mohou být vysílány s rozšířeným pokrytím, jsou definovány podle technologie; například v LTE-M podporují EC SIB1-BR (pro UE s redukovanou šířkou pásma) a další kritické SIBs. V NB-IoT jsou základní MIB-NB a SIB1-NB a využívají opakování. Role EC SI je klíčová pro umožnění spolehlivého výběru počáteční buňky, připojení k síti a jejího přepojování pro IoT zařízení, která musí pracovat roky na baterii a často na místech s velmi slabým signálem, aby si vždy mohla přečíst potřebné parametry pro připojení k síti.

## K čemu slouží

[EC](/mobilnisite/slovnik/ece-c/) SI bylo vytvořeno, aby řešilo zásadní výzvu při nasazování rozsáhlých IoT sítí: poskytování spolehlivé služby zařízením v extrémně špatných rádiových podmínkách. Tradiční vysílání systémových informací v buněčných sítích bylo navrženo pro ruční zařízení typicky používaná lidmi v relativně dobrých oblastech pokrytí. Pro IoT aplikace, jako jsou chytré měřiče (instalované v suterénech), zemědělské senzory (v odlehlých polích) nebo sledovací zařízení (uvnitř kontejnerů), může být útlum na trase o 20 dB nebo více horší než v typických případech. Bez vylepšení by tato zařízení nedokázala přečíst systémové informace, což by jim zabránilo se k síti vůbec připojit.

Motivace vycházela z práce 3GPP na Cellular IoT (CIoT) v Releasech 13 a novějších, které definovaly LTE-M a NB-IoT. Klíčovým požadavkem pro tyto technologie byla podpora vylepšení pokrytí až o 15-20 dB ve srovnání se staršími verzemi LTE. Zatímco byla definována vylepšení datových kanálů (jako opakování pro fyzické datové kanály), bylo stejně důležité vylepšit řídicí kanály a vysílání systémových informací. Bez vylepšených SI by zařízení mohlo teoreticky mít vylepšený datový kanál, ale nedokázalo by přečíst instrukce, jak jej použít. EC SI to řeší tím, že zajistí, aby i úplně první zprávy, které zařízení potřebuje přečíst – systémové informace – byly také robustně přenášeny.

To řeší problém asymetrických rozpočtů pro spojení, kdy downlink (ze sítě do zařízení) se stává limitujícím faktorem pokrytí. Zajišťuje, že dostupnost sítě není slabým článkem jinak robustního IoT spojení. Tím, že garantuje spolehlivé doručení SI, EC SI umožňuje předvídatelné chování zařízení, snižuje selhání spojení a podporuje principy ultra-spolehlivé komunikace s nízkou latencí (URLLC) pro kritické IoT, a to vše při zachování energetické účinnosti vyžadované pro masivní nasazení IoT.

## Klíčové vlastnosti

- Používá opakování přenosů SIB v časové oblasti pro zisk pokrytí
- Podporuje soft kombinování na přijímači UE pro zlepšení spolehlivosti dekódování
- Aplikovatelné na klíčové bloky systémových informací (např. SIB1, MIB) v LTE-M a NB-IoT
- Indikováno prostřednictvím plánovacích informací v MIB nebo jiných řídicích kanálech
- Umožňuje až 15-20 dB dodatečného pokrytí pro počáteční přístup
- Kritické pro podporu IoT zařízení hluboko uvnitř budov a na odlehlých místech

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TR 22.882** (Rel-19) — Study on Energy Efficiency as a Service Criteria
- **TS 22.883** (Rel-20) — Energy Efficiency as Service Criteria Phase 2
- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TR 26.967** (Rel-19) — eCall via CTM Suitability Analysis
- **TS 28.310** (Rel-19) — Energy Efficiency Management for 5G Networks
- **TS 32.303** (Rel-9) — Notification IRP CORBA Solution Set
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- **TS 32.856** (Rel-15) — Energy Efficiency Assessment for RAN OAM
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.852** (Rel-17) — 1900MHz NR band for European Rail Mobile Radio
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [EC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ec/)
