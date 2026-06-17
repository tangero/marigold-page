---
slug: "ansi"
url: "/mobilnisite/slovnik/ansi/"
type: "slovnik"
title: "ANSI – American National Standards Institute"
date: 2025-01-01
abbr: "ANSI"
fullName: "American National Standards Institute"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ansi/"
summary: "ANSI je soukromá nezisková organizace, která dohlíží na vývoj dobrovolných konsensuálních standardů ve Spojených státech. V kontextu 3GPP se na ni odkazuje z důvodu historické kompatibility a určitých"
---

ANSI je Americký národní institut pro standardy (American National Standards Institute), soukromá nezisková organizace dohlížející na dobrovolné konsensuální standardy v USA, na které se v 3GPP odkazuje z důvodu historické kompatibility, určitých kodeků a nasazení sítí v Severní Americe.

## Popis

Americký národní institut pro standardy (ANSI) není technologie vytvořená 3GPP, ale standardizační orgán. Ve specifikacích 3GPP je ANSI odkazováno především ve dvou klíčových kontextech: dědičná kompatibilita a specifické standardizované komponenty. Za prvé, standardy ANSI, zejména ty z výboru T1 (nyní [ATIS](/mobilnisite/slovnik/atis/)), tvořily základ mnoha severoamerických telekomunikačních standardů před globální harmonizací 3GPP. Tento historický vliv znamená, že určité odkazování na protokoly, specifikace signalizačních systémů (jako SS7) a principy síťové architektury převzaté ze standardů akreditovaných ANSI jsou ve dokumentech 3GPP uznávány kvůli interoperabilitě, zvláště pro nasazení integrující se se staršími severoamerickými sítěmi nebo migrující z nich (např. sítě ANSI-41).

Za druhé, a více operativně, je ANSI výslovně citováno v technických specifikacích (TS) 3GPP pro definici specifických kodekových algoritmů a testovacích procedur. Například specifikace jako TS 26.073, TS 26.104 a TS 26.173 odkazují na standardizované hlasové kodeky ANSI, jako je Enhanced Variable Rate Codec (EVRC) a Selectable Mode Vocoder (SMV). Ty jsou nedílnou součástí rodin kodeků Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a [AMR-WB](/mobilnisite/slovnik/amr-wb/) definovaných 3GPP pro okruhově a paketově přepínané hlasové služby. Specifikace podrobně popisují, jak jsou tyto kodeky původem z ANSI zapouzdřeny a přenášeny přes rozhraní definovaná 3GPP (jako Iu a Nb), což zajišťuje, že terminály a síťové prvky mohou správně kódovat a dekódovat řečové rámce podle standardů 3GPP i odkazovaných standardů ANSI.

Role ANSI v architektuře 3GPP je tedy role začlenění odkazem. 3GPP nedefinuje základní algoritmy těchto kodeků, ale specifikuje, jak je používat v rámci své vlastní systémové architektury. To zahrnuje definici rámcových struktur, bitově přesného algoritmického chování podle standardu ANSI, testovacích vektorů pro shodu (podrobně popsaných ve specifikacích jako TS 26.094 a TS 26.194) a integraci do přenosových a signalizačních protokolů 3GPP. Pro správu sítě a účtování mohou specifikace jako TS 32.859 odkazovat na formáty ANSI pro výměnu dat v určitých kontextech. Tento přístup umožňuje systémům 3GPP podporovat širší škálu kodeků, usnadňuje globální roamování a zpětnou kompatibilitu, zejména pro uživatele a síťové operátory působící v regionech, kde jsou tyto kodeky založené na ANSI vyžadovány nebo široce nasazeny.

## K čemu slouží

Zařazení odkazů na ANSI do specifikací 3GPP slouží kritickému účelu zajištění globální interoperability a zpětné kompatibility. Posláním 3GPP je vytvářet globálně použitelné technické specifikace, ale realita je taková, že regionální starší sítě, zejména v Severní Americe, byly postaveny na jiné standardizační linii (ANSI/[ATIS](/mobilnisite/slovnik/atis/)). Aby bylo možné zajistit bezproblémové služby pro roamující účastníky a umožnit operátorům migrovat sítě bez zastarávání stávající infrastruktury a koncových zařízení, potřebovalo 3GPP začlenit podporu klíčových technologií z těchto ekosystémů. Odkazování na standardy ANSI pro specifické kodeky a procedury tento problém efektivně řeší.

Historicky, před dominancí 3GPP, byl telekomunikační krajina fragmentovaná. Ve Spojených státech vyvinul výbor TIA akreditovaný ANSI standardy jako IS-95 (cdmaOne) a následnou rodinu CDMA2000, které používaly kodeky jako EVRC. Když 3GPP vyvíjelo UMTS a později LTE, která jsou založena na technologii GSM/WCDMA, existovala přímá nekompatibilita pro hlasové služby mezi těmito světy. Aby byl tento rozdíl překlenut, zejména když operátoři nasazovali více technologické sítě a usilovali o globální roamingové dohody, 3GPP formálně standardizovalo zařazení těchto kodeků ANSI. Tím byla odstraněna omezení čistě evropsky orientované sady kodeků a zajištěno, že terminály 3GPP mohou podporovat vysoce kvalitní hlasové hovory při připojení k sítím používajícím tyto starší standardy nebo z nich.

Tento přístup navíc respektuje duševní vlastnictví a náročnou standardizační práci již dokončenou orgány akreditovanými ANSI. Místo znovuvynalézání nebo nepatrné modifikace těchto kodeků, což by mohlo vést k problémům s interoperabilitou, 3GPP vyžaduje přísné dodržování odkazovaných dokumentů standardu ANSI. To poskytuje implementátorům právní a technickou jasnost, snižuje duplicitu vývoje a zaručuje, že 3GPP UE implementující například EVRC bude plně kompatibilní s CDMA2000 koncovým zařízením používajícím stejný standardizovaný algoritmus EVRC podle ANSI, což usnadňuje plynulejší období technologického přechodu.

## Klíčové vlastnosti

- Odkazování na standardizované hlasové kodeky (např. EVRC, SMV) pro systémy 3GPP
- Definice testovacích sekvencí pro shodu a bitově přesného algoritmického chování podle standardů ANSI
- Specifikace přenosu a rámcování přes rozhraní definovaná 3GPP (Iu, Nb)
- Podpora interoperability se staršími síťovými prvky ANSI-41 (CDMA)
- Zařazení do protokolů pro adaptaci a konfiguraci kodeků 3GPP
- Odkazování ve specifikacích formátů dat pro účtování a správu

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [ITU-T – International Telecommunication Union Telecommunication Standardization Sector](/mobilnisite/slovnik/itu-t/)
- [ATIS – Alliance for Telecommunications Industry Solutions](/mobilnisite/slovnik/atis/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 26.073** (Rel-19) — AMR Speech Codec ANSI-C Implementation
- **TS 26.094** (Rel-19) — AMR Voice Activity Detector (VAD) Specification
- **TS 26.104** (Rel-19) — AMR Floating-Point Codec Implementation
- **TS 26.173** (Rel-19) — AMR-WB Codec ANSI-C Implementation
- **TS 26.194** (Rel-19) — Voice Activity Detector for AMR-WB DTX
- **TS 26.204** (Rel-19) — AMR-WB Floating-Point Codec Specification
- **TS 26.243** (Rel-19) — DSR Extended Advanced Front-end C Code
- **TS 26.268** (Rel-19) — eCall In-band Modem ANSI-C Code
- **TS 26.273** (Rel-19) — Fixed-point AMR-WB+ codec ANSI-C code
- **TS 26.304** (Rel-19) — Floating-point Extended AMR-WB+ Codec ANSI-C Code
- **TS 26.410** (Rel-19) — Enhanced aacPlus Floating-Point ANSI-C Code
- **TS 26.411** (Rel-19) — Enhanced aacPlus Fixed-Point ANSI-C Code
- **TS 32.859** (Rel-12) — Alarm Management Quality Improvement Study
- **TS 46.006** (Rel-19) — GSM Half Rate Codec ANSI-C Code
- **TS 46.042** (Rel-19) — GSM Half-Rate Voice Activity Detector Specification
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [ANSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ansi/)
