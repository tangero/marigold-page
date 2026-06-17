---
slug: "lcs-ap"
url: "/mobilnisite/slovnik/lcs-ap/"
type: "slovnik"
title: "LCS-AP – LCS Application Protocol"
date: 2025-01-01
abbr: "LCS-AP"
fullName: "LCS Application Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lcs-ap/"
summary: "Protokol LCS-AP je řídicí protokol roviny definovaný 3GPP pro služby určování polohy. Umožňuje komunikaci mezi síťovými entitami, jako je Gateway Mobile Location Centre (GMLC) a Mobility Management En"
---

LCS-AP je řídicí protokol roviny 3GPP používaný pro komunikaci mezi síťovými entitami za účelem vyžádání a doručení polohových informací o cílovém UE.

## Popis

Protokol LCS-AP je klíčový řídicí protokol roviny v architektuře 3GPP, který je speciálně navržen pro podporu služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)). Funguje přes rozhraní SLg, spojuje Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) s entitami pro správu mobility v jádru sítě – konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) pro sítě LTE/EPC a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) pro sítě 2G/3G GPRS. Protokol definuje soubor procedur a zpráv, které umožňují GMLC, jež slouží jako externí rozhraní pro polohové požadavky, komunikovat se síťovými uzly, které mohou iniciovat a řídit proces určení polohy pro uživatelské zařízení (UE).

Z architektonického hlediska je LCS-AP aplikační protokol, který typicky využívá SCTP (Stream Control Transmission Protocol) jako transportní vrstvu pro spolehlivé doručování zpráv. Jeho hlavní funkcí je přenos požadavků na polohové služby z GMLC na MME/SGSN. Po přijetí požadavku MME/SGSN komunikuje s rádiovou přístupovou sítí (RAN) a případně i se samotným UE (např. u UE-bazovaných nebo UE-asistovaných metod určování polohy), aby získalo polohová měření nebo vypočítanou polohu. Protokol přenáší klíčové informace, jako je identifikátor cílového UE (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)), požadovaná kvalita služby (QoS) pro odhad polohy (jako přesnost a doba odezvy) a typ polohové události (např. okamžité určení polohy, odložené určení pro periodické hlášení).

Protokol podporuje různé metody určování polohy, včetně síťově-bazovaných (např. [OTDOA](/mobilnisite/slovnik/otdoa/) v LTE), UE-bazovaných (kde UE vypočítává svou vlastní polohu) a UE-asistovaných metod. Zprávy LCS-AP slouží k přenosu výsledného odhadu polohy (např. zeměpisných souřadnic) zpět do GMLC, který je následně doručí externímu LCS klientovi (např. centru tísňového volání nebo aplikačnímu serveru komerční služby). Protokol také řeší chybové stavy, ověření soukromí účastníka (kontrolu, zda je LCS klient oprávněn lokalizovat účastníka) a podporuje odložené hlášení polohy pro sledovací aplikace. Jeho role je striktně v rovině řízení, spravuje signalizaci potřebnou k navázání, provedení a ukončení polohové relace, nepřenáší však samotná data polohových měření, která jsou v novějších vydáních 3GPP řešena jinými protokoly v uživatelské rovině.

## K čemu slouží

LCS-AP byl zaveden za účelem standardizace řídicí signalizace pro služby určování polohy napříč sítěmi 3GPP, čímž reagoval na rostoucí potřebu spolehlivého a efektivního určování polohy mobilních zařízení. Před jeho standardizací byly tyto služby často implementovány pomocí proprietárních rozhraní, což bránilo interoperabilitě mezi síťovým vybavením různých výrobců a mezi různými operátory. Vytvoření LCS-AP jako součásti celkové architektury [LCS](/mobilnisite/slovnik/lcs/) ve 3GPP Release 9 poskytlo jednotný protokol pro komunikaci jádrových síťových entit ohledně polohových požadavků a odpovědí, což bylo zásadní pro komerční rozvoj služeb založených na poloze a pro splnění regulatorních požadavků, jako je Enhanced 911 (E911) v Severní Americe a její ekvivalenty po celém světě.

Protokol řeší problém, jak může externí entita (LCS klient) standardizovaným způsobem požádat síť o lokalizaci zařízení účastníka. Abstrahuje složitost podkladové rádiové přístupové technologie (např. UMTS, LTE) od servisní vrstvy. Definováním jasných primitiv pro vyvolání, zrušení a hlášení polohy umožňuje LCS-AP širokou škálu služeb včetně lokalizace tísňových volajících, sledování majetku, účtování na základě polohy a aplikací typu 'najdi přítele'. Jeho vývoj byl motivován posunem telekomunikačního průmyslu k architekturám orientovaným na služby a potřebou zpřístupnit síťové schopnosti, jako je určování polohy, prostřednictvím otevřených, standardizovaných rozhraní za účelem podpory inovací na aplikační vrstvě.

## Klíčové vlastnosti

- Standardizovaná řídicí signalizace roviny pro požadavky a doručení polohových služeb
- Funguje přes rozhraní SLg mezi GMLC a MME/SGSN
- Podporuje více typů polohových požadavků: okamžité, odložené a periodické
- Přenáší parametry QoS pro polohu, jako je přesnost, doba odezvy a vertikální přesnost
- Obsahuje procedury ověření soukromí pro autorizaci polohových požadavků
- Návrh nezávislý na transportu, typicky implementován přes SCTP pro spolehlivost

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [LCS-AP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcs-ap/)
