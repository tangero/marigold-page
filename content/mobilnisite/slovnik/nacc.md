---
slug: "nacc"
url: "/mobilnisite/slovnik/nacc/"
type: "slovnik"
title: "NACC – Network Assisted Cell Change"
date: 2025-01-01
abbr: "NACC"
fullName: "Network Assisted Cell Change"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nacc/"
summary: "Funkce v GERAN (GSM/EDGE Radio Access Network), která umožňuje síti asistovat mobilní stanici při převzetí buňky (reselection) nebo předání hovoru (handover) tím, že jí předem poskytne systémové infor"
---

NACC je funkce GERAN, při níž síť během změny buňky asistuje mobilní stanici tím, že jí předem poskytne systémové informace cílové buňky, a tím sníží přerušení služby.

## Popis

Network Assisted Cell Change (NACC) je vylepšení správy mobility definované pro [GERAN](/mobilnisite/slovnik/geran/) (GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network) ve standardu 3GPP. Jeho hlavní funkcí je snížit dobu přerušení, kterou zažívá mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) při změně buňky, zejména během přenosů paketových dat v sítích [GPRS](/mobilnisite/slovnik/gprs/) nebo EDGE. Při tradiční změně buňky musí MS nejprve přejít na novou buňku, poté naslouchat vysílacímu kanálu, aby získala nezbytné systémové informace (jako kód směrovací oblasti, volby buňky a přístupové parametry), než může obnovit komunikaci. Tento proces získávání může způsobit přerušení datového toku v řádu stovek milisekund.

NACC funguje tak, že obsluhující řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) preventivně poskytne MS kritické systémové informace sousední buňky (nebo buněk) ještě před provedením změny buňky. Proces je typicky spouštěn během režimu přenosu paketů. Síť na základě měřicích hlášení od MS rozhodne o cílové buňce pro změnu. Obsluhující BSC poté komunikuje s cílovým BSC (pokud je jiný) přes rozhraní Gb nebo Iu-g a žádá o příslušné systémové informace ([SI](/mobilnisite/slovnik/si/)) pro cílovou buňku. Tyto SI zahrnují data ze systémových informačních zpráv 13 (pro GPRS) a případně dalších, obsahujících parametry nezbytné pro okamžitý přístup.

Obsluhující BSC pak tuto informaci zašle MS v rámci zprávy Packet Cell Change Order nebo Packet Neighbor Cell Data na kanálu [PACCH](/mobilnisite/slovnik/pacch/) (Packet Associated Control Channel). S těmito informacemi se může MS synchronizovat s novou buňkou a okamžitě ji začít využívat pomocí správných parametrů, čímž se obejde potřeba čekat na pomalý vysílací kanál a dekódovat jej. To je zvláště důležité pro služby reálného času, jako je Voice over IP nebo streamování. NACC může asistovat jak při převzetí buňky (kde rozhoduje MS), tak při předání řízeném sítí. Funkce vyžaduje podporu jak v síti (BSC), tak v MS a je klíčovou součástí pro zlepšení uživatelského zážitku u aplikací citlivých na zpoždění v sítích 2.5G.

## K čemu slouží

NACC byl vyvinut, aby řešil významné omezení výkonu v sítích [GPRS](/mobilnisite/slovnik/gprs/) a EDGE: dlouhou dobu přerušení během změn buněk pro paketové datové relace. Toto přerušení bylo škodlivé pro kvalitu služeb aplikací reálného času, jako je push-to-talk over cellular (PoC), VoIP a interaktivní hry, které se stávaly častějšími. Standardní postup změny buňky, při kterém MS musela získat systémové informace z vysílacího kanálu až po přesunu, byl zastaralý návrh optimalizovaný pro přepojování okruhů hlasu, kde byly krátká přerušení méně patrná.

Vznik NACC byl motivován potřebou učinit GERAN konkurenceschopnější pro služby s přepojováním paketů a poskytnout plynulejší mobilní zážitek, podobný tomu, který byl možný v UMTS. Vyřešil problém přenesením břemena sběru informací z MS na síť, která využila svou znalost sousedních buněk. Tato proaktivní asistence výrazně snížila dobu přerušení při změně buňky – z potenciálně více než 600 ms na méně než 200 ms – a učinila GERAN vhodnějším pro služby vyžadující plynulou mobilitu. Byl to klíčový evoluční krok pro sítě 2G, aby lépe podporovaly služby založené na IP před masivním nasazením sítí 3G/4G.

## Klíčové vlastnosti

- Snižuje dobu přerušení služby během změn buněk v GERAN pro paketová data
- Síť předem poskytne mobilní stanici (MS) systémové informace (SI) cílové buňky
- Podporuje jak převzetí buňky (reselection), tak procedury předání řízené sítí
- Využívá zprávy Packet Cell Change Order a Packet Neighbor Cell Data
- Vyžaduje koordinaci mezi obsluhujícím a cílovým BSC přes rozhraní Gb/Iu-g
- Zlepšuje výkon pro aplikace citlivé na zpoždění v sítích GPRS/EDGE

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 43.130** (Rel-19) — Iur-g Interface Overview
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TR 44.901** (Rel-19) — Extended NACC for External Cell Change
- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [NACC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nacc/)
