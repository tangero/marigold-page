---
slug: "lcf"
url: "/mobilnisite/slovnik/lcf/"
type: "slovnik"
title: "LCF – Location Client Function"
date: 2025-01-01
abbr: "LCF"
fullName: "Location Client Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcf/"
summary: "Funkční entita ve Vlastním Zařízení Uživatele (UE) nebo externím klientovi, která vyžaduje lokalizační služby od sítě. Iniciuje požadavky na určení polohy, přijímá odhady polohy a může interagovat s a"
---

LCF je funkční entita v UE nebo externím klientovi, která vyžaduje síťové lokalizační služby, iniciuje požadavky na určení polohy a přijímá odhady polohy pro aplikace.

## Popis

Location Client Function (LCF) je klíčovou součástí architektury lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) dle 3GPP, která vystupuje jako koncový bod žádající a spotřebovávající informace o poloze. Nachází se buď ve Vlastním Zařízení Uživatele (UE) jako klient vyžadující určení polohy iniciované mobilním zařízením ([MO-LR](/mobilnisite/slovnik/mo-lr/)), nebo v externí entitě, jako je server poskytovatele služeb (známý jako klient LCS s přidanou hodnotou). LCF formuluje žádost o určení polohy, specifikuje parametry jako cílová UE (nebo sama sebe, pokud je v UE), požadovanou kvalitu služby (QoS) jako přesnost a dobu odezvy a typ požadovaných lokalizačních informací (např. aktuální nebo periodická poloha). Tento požadavek je odeslán přes standardizovaná rozhraní na Location Server sítě, obvykle Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo Evolved Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)), v závislosti na generaci sítě.

Po přijetí žádosti lokalizační systém sítě (zahrnující Radio Access Network a uzly core networku) provede výpočet polohy pomocí metod jako Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)) nebo Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)). Výsledný odhad polohy je poté doručen zpět k LCF přes stejná rozhraní. Pokud je LCF externí, odpověď je směrována přes GMLC a případně Home Subscriber Server (HSS) pro autorizaci. Pokud je interní v UE, odpověď může přijít přímo od lokalizačního serveru obsluhující sítě. LCF může také podporovat odložené žádosti o polohu, kde je poloha nahlášena později nebo po spouštěcí události, což vyžaduje, aby LCF spravovala kontinuitu relace.

LCF hraje klíčovou roli při umožnění široké škály služeb založených na poloze (LBS), včetně služeb tísňového volání (např. E911), navigace, sledování vozového parku a marketing založený na blízkosti. Musí dodržovat předpisy na ochranu soukromí, často zahrnující mechanismy souhlasu uživatele podle specifikací 3GPP. Z architektonického hlediska LCF komunikuje s referenčním bodem Le (pro externí klienty) nebo s LTE positioning protocol (LPP) pro interakce založené na UE. Její implementace zajišťuje, že aplikace mohou získat lokalizační data bez nutnosti porozumět podkladové technologii rádiového přístupu, přičemž abstrahuje složitost metod určování polohy do standardizovaného modelu žádosti o službu.

## K čemu slouží

Location Client Function (LCF) byla vytvořena za účelem standardizace způsobu, jakým klienti vyžadují a přijímají informace o poloze ze sítí 3GPP, a to v reakci na rostoucí poptávku po službách založených na poloze (LBS). Před jejím formálním zavedením vedly proprietární řešení k fragmentaci, což ztěžovalo poskytovatelům služeb vývoj aplikací napříč různými sítěmi a zařízeními. LCF, představená v R99 jako součást funkce Location Services (LCS), poskytla sjednocené rozhraní pro žádosti o určení polohy, což umožnilo interoperabilitu a škálovatelnost.

Hlavním problémem, který LCF řeší, je oddělení spotřebitelů lokalizačních služeb od komplexních síťových lokalizačních mechanismů. Definováním jasné role klienta umožnila 3GPP různorodým entitám – od aplikací v UE po externí servery – bezproblémový přístup k lokalizačním datům. To bylo zvláště kritické pro regulované služby jako tísňové volání, kde je spolehlivé a rychlé získání polohy povinné. LCF se také zabývá otázkami soukromí a bezpečnosti začleněním postupů autentizace a autorizace, čímž zajišťuje, že k poloze uživatele mají přístup pouze povolení klienti, což buduje důvěru v přijetí LBS.

Historicky pramenila motivace z vývoje mobilních sítí za hranice hlasových služeb směrem ke službám s přidanou hodnotou. Jak GSM přecházelo na UMTS, stala se potřeba standardizovaného lokalizačního rámce zjevnou pro podporu vznikajících aplikací. LCF spolu s dalšími komponentami LCS poskytla základ pro komerční a bezpečnostní služby, podporujíc inovace v oblastech jako navigace a sledování majetku. Její pokračující vývoj napříč releasy odráží vylepšení přesnosti, snížení latence a podporu nových metod určování polohy, což zajišťuje, že splňuje požadavky moderních případů užití, jako je IoT a komunikace V2X.

## Klíčové vlastnosti

- Iniciuje žádosti o určení polohy pro sebe nebo jiná UE
- Podporuje scénáře s iniciací z mobilního zařízení a z externího klienta
- Specifikuje parametry QoS jako přesnost a dobu odezvy
- Komunikuje se síťovými lokalizačními servery přes standardizované protokoly
- Zpracovává odložené a periodické hlášení polohy
- Začleňuje mechanismy ochrany soukromí a autorizační kontroly

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcf/)
