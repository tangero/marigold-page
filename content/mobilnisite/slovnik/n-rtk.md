---
slug: "n-rtk"
url: "/mobilnisite/slovnik/n-rtk/"
type: "slovnik"
title: "N-RTK – Network – Real-Time Kinematic"
date: 2025-01-01
abbr: "N-RTK"
fullName: "Network – Real-Time Kinematic"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/n-rtk/"
summary: "Síťově asistovaná lokalizační služba poskytující vysoce přesná polohová data tím, že doručuje RTK korekční data uživatelskému zařízení (UE) přes mobilní síť. Umožňuje přesnost na úrovni centimetrů pro"
---

N-RTK je síťově asistovaná lokalizační služba, která zajišťuje přesnost na úrovni centimetrů tím, že poskytuje korekční data Real-Time Kinematic uživatelskému zařízení prostřednictvím mobilní sítě.

## Popis

Network – Real-Time Kinematic (N-RTK) je lokalizační služba standardizovaná organizací 3GPP, která doručuje korekční data Real-Time Kinematic ze síťového serveru k uživatelskému zařízení (UE) za účelem dosažení polohové přesnosti na úrovni centimetrů. Na rozdíl od samostatného [GNSS](/mobilnisite/slovnik/gnss/) (Global Navigation Satellite System), které poskytuje přesnost na úrovni metrů, RTK koriguje chyby jako nepřesnosti satelitní oběžné dráhy a hodin, ionosférická zpoždění a troposférická zpoždění pomocí referenční stanice na známé pozici. Služba N-RTK integruje toto doručování korekčních dat do architektury mobilní sítě, což umožňuje UE přijímat korekce prostřednictvím řídicích nebo uživatelských rovinových protokolů, typicky za použití protokolu [LPP](/mobilnisite/slovnik/lpp/) (LTE Positioning Protocol) nebo jeho protějšku v NG-RAN pro 5G. Služba zahrnuje Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) nebo ekvivalentní lokalizační server, který získává RTK korekční datové proudy z referenčních sítí nebo od poskytovatelů služeb a formátuje je pro přenos k UE.

Architektura N-RTK zahrnuje několik klíčových komponent: UE s GNSS a RTK schopným přijímačem, rádiovou přístupovou síť (RAN – LTE nebo 5G NR), prvky core sítě (jako Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G) a lokalizační server (např. LMF nebo [E-SMLC](/mobilnisite/slovnik/e-smlc/)). Lokalizační server funguje jako brána mezi infrastrukturou RTK korekcí (často externími sítěmi jako [CORS](/mobilnisite/slovnik/cors/) – Continuously Operating Reference Stations) a mobilní sítí. Autentizuje UE, určí její přibližnou polohu pro výběr odpovídajících korekčních dat (protože korekce jsou prostorově korelované) a efektivně doručuje korekce s ohledem na požadavky na šířku pásma a latenci. Korekce mohou být rozesílány broadcastem více UE v určité oblasti nebo doručovány prostřednictvím unicastových relací přizpůsobených individuálním požadavkům UE.

N-RTK funguje tak, že naváže lokalizační relaci iniciovanou UE nebo sítí. UE indikuje svou schopnost podporovat RTK v lokalizačních schopnostech vyměňovaných se sítí. Na žádost lokalizační server získá RTK korekční data relevantní k hrubé poloze UE (odvozené z cell-ID nebo jiných metod). Tyto korekce, které zahrnují měření jako korekce fáze nosné vlny a korekce kódové fáze, jsou přenášeny k UE přes mobilní spoj. UE následně použije tyto korekce na svá vlastní GNSS měření (např. z [GPS](/mobilnisite/slovnik/gps/), Galilea, BeiDou) v reálném čase, provede výpočty s dvojitými diferencemi, aby eliminovala společné chyby a vypočítala svou přesnou pozici. Služba podporuje různé RTK formáty a může přizpůsobit doručování korekcí na základě mobility UE a požadavků na přesnost.

V rámci sítě hraje N-RTK klíčovou roli při umožňování vysoce přesných lokalizačních služeb (LBS) pro 5G a další generace. Je součástí širšího lokalizačního rámce 3GPP, který zahrnuje jiné metody jako OTDOA, A-GNSS a senzorové určování polohy. Integrací RTK do sítě umožňuje 3GPP mobilním operátorům nabízet prémiové lokalizační služby bez nutnosti, aby UE měla přímé internetové připojení k externím RTK službám, což zajišťuje spolehlivost, zabezpečení a kvalitu služby. Služba je definována v kontextu LTE (E-UTRA) i NR, přičemž specifikace pokrývají procedury, signalizaci a datové formáty pro zajištění interoperability napříč generacemi.

## K čemu slouží

N-RTK bylo zavedeno, aby uspokojilo rostoucí poptávku po vysoce přesném určování polohy v komerčních a průmyslových aplikacích, kde metrová přesnost GNSS není dostatečná. Před jeho standardizací se vysoce přesné určování polohy spoléhalo na proprietární nebo odvětvově specifické RTK systémy, které vyžadovaly dedikované přijímače, přímá spojení s referenčními stanicemi přes rádiové linky (např. UHF) nebo internetové proudy NTRIP (Networked Transport of RTCM via Internet Protocol), které nebyly optimalizovány pro mobilní síťová prostředí. Tyto přístupy často trpěly omezeným pokrytím, vysokými náklady, složitým nastavením a nedostatečnou integrací s autentizačními a fakturačními systémy mobilních sítí.

Vznik N-RTK v rámci 3GPP byl motivován vznikem případů užití jako autonomní vozidla, navigace dronů, precizní zemědělství a rozšířená realita, které vyžadují kontinuální, spolehlivé a centimetrově přesné určování polohy. Využitím stávající mobilní infrastruktury poskytuje N-RTK všudypřítomné pokrytí, plynulou podporu mobility a inherentní zabezpečení prostřednictvím síťové autentizace. Řeší problém efektivního doručování RTK korekcí přes rozsáhlá území bez nutnosti dodatečného hardwaru na UE kromě schopného GNSS čipsetu, což umožňuje masové přijetí vysoce přesného určování polohy.

Historicky se RTK primárně používalo v geodézii, mapování a stavebnictví. Standardizace 3GPP ve verzi 15 ji integrovala do mobilního ekosystému jako součást vylepšení určování polohy pro 5G, s vědomím, že budoucí služby budou záviset na přesné poloze. N-RTK řeší omezení předchozího A-GNSS (Assisted GNSS), které pouze zlepšovalo čas do prvního fixu a citlivost, nikoli však absolutní přesnost. Také doplňuje další vysoce přesné metody 3GPP tím, že poskytuje standardizovaný síťový mechanismus pro doručování korekčních dat, čímž zajišťuje interoperabilitu mezi operátory a výrobci zařízení.

## Klíčové vlastnosti

- Doručuje korekční data GNSS v reálném čase (např. ve formátu RTCM) k UE prostřednictvím mobilní sítě.
- Umožňuje přesnost určování polohy na úrovni centimetrů za vhodných podmínek.
- Podporuje obě přístupové technologie LTE i 5G NR prostřednictvím jednotných lokalizačních protokolů.
- Integruje se s lokalizační architekturou 3GPP (LMF/E-SMLC) pro správu relací.
- Poskytuje režimy doručování korekčních dat unicast a potenciálně broadcast.
- Obsahuje podporu pro různé GNSS konstelace (GPS, GLONASS, Galileo, BeiDou).

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [N-RTK na 3GPP Explorer](https://3gpp-explorer.com/glossary/n-rtk/)
