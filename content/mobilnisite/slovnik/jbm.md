---
slug: "jbm"
url: "/mobilnisite/slovnik/jbm/"
type: "slovnik"
title: "JBM – Jitter Buffer Management"
date: 2025-01-01
abbr: "JBM"
fullName: "Jitter Buffer Management"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jbm/"
summary: "Techniky a algoritmy pro správu jitterových bufferů v komunikačních službách v reálném čase, jako je Voice over IP (VoIP) a streamování videa. Zavedeno ve specifikaci 3GPP Release 8, řeší variaci zpož"
---

JBM (správa jitterového bufferu) je řízení jitterových bufferů pomocí technik pro zvládání variace zpoždění paketů, které zajišťuje plynulé přehrávání pro služby v reálném čase, jako je VoIP a streamování videa v mobilních sítích.

## Popis

Správa jitterového bufferu (JBM) označuje soubor mechanismů a politik používaných k řízení jitterového bufferu v paketových mediálních tocích v reálném čase. Jitterový buffer je fronta na přijímací straně, která krátce ukládá příchozí pakety, aby kompenzovala síťový jitter (variace v časech příchodu paketů). JBM zahrnuje dynamické přizpůsobování parametrů bufferu, jako je velikost, zpoždění přehrávání a strategie zpracování paketů, na základě pozorovaných síťových podmínek. Jejím cílem je minimalizovat jak latenci přehrávání, tak ztrátu paketů způsobenou pozdním příchodem, a tím optimalizovat kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)).

Z architektonického hlediska je JBM implementována v rámci komponent pro zpracování médií v UE nebo v mediální bráně, často jako součást zásobníku Real-Time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) nebo specializovaného mediálního procesoru. Funguje tak, že monitoruje časy mezi příchody paketů, odhaduje aktuální jitter a podle toho přizpůsobuje hloubku bufferu. Mezi klíčové algoritmy patří statické buffering, adaptivní buffering (kde se velikost bufferu dynamicky mění) a prediktivní algoritmy, které předvídají vzorce jitteru. Správa také zahrnuje rozhodování o zahazování paketů (u nadměrně opožděných paketů) a úpravy rychlosti přehrávání. Její role v síti je klíčová pro udržení přijatelné kvality zvuku/videa ve službách, jako je VoIP, videokonference a streamování přes IP sítě, které jsou nedílnou součástí IP Multimedia Subsystem (IMS) specifikace 3GPP a pozdějších hlasových/videokomunikačních služeb.

Specifikace pokrývá různé metody JBM, jejich výkon za různých síťových podmínek a jejich dopad na end-to-end zpoždění a ztrátu paketů. Podrobně popisuje, jak interagují úpravy bufferu s dalšími mechanismy QoS, jako je priorizace paketů a řízení zahlcení. JBM je klíčovou součástí zajištění toho, aby služby v reálném čase splňovaly očekávání uživatelů navzdory inherentní nepředvídatelnosti paketových sítí.

## K čemu slouží

JBM byla zavedena, aby řešila problém variace zpoždění paketů (jitteru) v IP komunikacích v reálném čase. Tradiční přepojování okruhů pro hlas mělo pevné zpoždění, ale paketové sítě zavádějí proměnlivé zpoždění v důsledku front, směrování a zahlcení. Tento jitter může, pokud není řízen, způsobovat mezery v audiu, trhané video a špatný uživatelský zážitek. Jednoduché pevné buffery buď zavádějí příliš velké zpoždění (pokud jsou velké), nebo nedokážou absorbovat jitter (pokud jsou malé).

Účelem JBM je dynamicky optimalizovat kompromis mezi zpožděním přehrávání a ztrátou paketů. Řeší problém přizpůsobení bufferingu na přijímači reálným síťovým podmínkám. Díky inteligentní správě bufferu umožňuje službám v reálném čase udržovat plynulé přehrávání médií i při kolísajícím výkonu sítě. Její vznik byl motivován migrací hlasových a videokomunikačních služeb na plně IP sítě v rámci 3GPP (např. IMS, VoLTE, ViLTE). Efektivní JBM je nezbytná pro dosažení kvality hovorů na úrovni veřejné telefonní sítě a vysoké kvality videa přes mobilní IP sítě, což z ní činí základní aspekt správy QoS pro média v reálném čase.

## Klíčové vlastnosti

- Dynamické přizpůsobování velikosti jitterového bufferu na základě síťových podmínek
- Minimalizuje latenci přehrávání při kompenzaci variace zpoždění paketů
- Snižuje ztrátu paketů způsobenou pozdním příchodem pomocí adaptivního bufferingu
- Podporuje různé algoritmy (statické, adaptivní, prediktivní) pro různé scénáře
- Integruje se s RTP/RTCP pro monitorování statistik příchodu paketů
- Klíčová pro kvalitu uživatelského zážitku (QoE) u VoIP, videohovorů a streamování

## Související pojmy

- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.250** (Rel-19) — IVAS Codec Introduction
- **TS 26.251** (Rel-19) — IVAS Codec Fixed-Point C Code Specification
- **TS 26.252** (Rel-19) — IVAS Codec Test Sequences Specification
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.256** (Rel-19) — Jitter Buffer Management for IVAS
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.446** (Rel-19) — EVS Codec AMR-WB Backward Compatibility Spec
- **TS 26.447** (Rel-19) — EVS Frame Loss Concealment Procedure
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [JBM na 3GPP Explorer](https://3gpp-explorer.com/glossary/jbm/)
