---
slug: "r-fax"
url: "/mobilnisite/slovnik/r-fax/"
type: "slovnik"
title: "R-FAX – Reception Side Facsimile"
date: 2025-01-01
abbr: "R-FAX"
fullName: "Reception Side Facsimile"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/r-fax/"
summary: "Přijímací koncový bod ve službě faxu s přepojováním okruhů podle 3GPP v mobilních sítích. Představuje terminálové nebo bránové zařízení, které přijímá a dekóduje faxový přenos odeslaný z T-FAX (vysíla"
---

R-FAX je přijímací koncový bod ve službě faxu s přepojováním okruhů podle 3GPP, který přijímá a dekóduje faxové přenosy odeslané z T-FAX přes hlasové kanály GSM nebo UMTS.

## Popis

R-FAX neboli Reception Side Facsimile je funkční role definovaná v architektuře služby faxu s přepojováním okruhů podle 3GPP. Není to samostatné zařízení, ale logická funkce vykonávaná mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) nebo síťovou mezisystémovou jednotkou ([IWF](/mobilnisite/slovnik/iwf/)), která ukončuje faxové volání ze strany mobilní sítě. Hlavní odpovědností R-FAX je přijmout modulovaný audio signál nesoucí faxová data, demodulovat jej, dekódovat zprávy faxového protokolu (založené na [ITU-T](/mobilnisite/slovnik/itu-t/) T.30) a nakonec zobrazit přijatý faxový obraz. Při typickém faxovém volání iniciovaném z mobilní sítě od [T-FAX](/mobilnisite/slovnik/t-fax/) (vysílací strana) by R-FAX byl pevný faxový přístroj nebo faxový server v síti [PSTN](/mobilnisite/slovnik/pstn/)/[ISDN](/mobilnisite/slovnik/isdn/), k němuž se přistupuje přes [PLMN](/mobilnisite/slovnik/plmn/). Při volání přijímaném mobilní sítí je funkce R-FAX umístěna v mobilním terminálu nebo datovém adaptéru k němu připojeném.

Služba funguje v doméně s přepojováním okruhů, konkrétně využívá transparentní nebo netransparentní datovou přenosovou službu. Síť pro volání zřídí přenosový kanál ([TCH](/mobilnisite/slovnik/tch/)) a faxové modemy v entitách T-FAX a R-FAX provedou standardní T.30 handshake. Pro mobilní stanice fungující jako R-FAX to vyžaduje integrovaný faxový software a modemové schopnosti pro interpretaci signalizace V.21 HDLC pro řízení volání a modulace V.27ter/V.29 pro data stránky. Specifikace 3GPP definují potřebné adaptace a scénáře mezisystémového provozu, zejména když volání prochází různými typy sítí (např. z PLMN do PSTN). Mezisystémová funkce (IWF) v síti může také převzít roli R-FAX za jednoduchou MS, provádějící modemovou konverzi a adaptaci protokolu.

Její role v síti spočívala v rozšížení všudypřítomné faxové služby na mobilní uživatele, což byl v před-broadbandové éře klíčový nástroj obchodní komunikace. Architektura zajišťovala zpětnou kompatibilitu s globálním faxovým systémem PSTN. Funkce R-FAX spolu s T-FAX tvořila kompletní koncově-koncovou službu, umožňující uživatelům odesílat a přijímat faxové dokumenty přímo z notebooků nebo specializovaných mobilních zařízení. Ačkoli je dnes již z velké části zastaralá, představovala významnou přidanou službu pro sítě GSM a rané 3G, podporující kontinuitu podnikání a funkce mobilní kanceláře před rozšířeným přijetím e-mailu a mobilních dat.

## K čemu slouží

R-FAX byl vytvořen pro podporu mobilních faxových služeb jako součást sady přenosových služeb GSM a UMTS. V 90. letech a na počátku 21. století byl fax dominantní formou přenosu dokumentů pro obchodní a právní účely. Omezení raných mobilních sítí spočívalo v tom, že byly primárně navrženy pro hlas. Účelem definice R-FAX (a T-FAX) bylo specifikovat, jak lze standardní analogové faxové protokoly adaptovat pro práci přes digitální a někdy náchylný k chybám rádiový spoj buňkové sítě.

Toto řešilo problém mobilních profesionálů, kteří potřebovali přístup k faxovým přístrojům mimo kancelář. Bez této služby by uživatelé museli hledat fyzický faxový přístroj na pevné lince. Specifikace 3GPP poskytly standardizovaný způsob, jak mohou mobilní terminály a síťová zařízení emulovat faxový přijímač, a zajistit tak interoperabilitu mezi terminály různých výrobců a globální faxovou sítí PSTN. Řešila technickou výzvu převodu mezi analogovými modemovými signály faxu a digitálním datovým proudem mobilního přenosového kanálu, řízení časování, opravy chyb a adaptace přenosové rychlosti pro zachování integrity faxové relace.

## Klíčové vlastnosti

- Definuje funkčnost přijímacího koncového bodu pro fax s přepojováním okruhů podle 3GPP
- Podporuje standardní faxový protokol ITU-T T.30 přes mobilní přenosové cesty
- Může být implementována v mobilní stanici (MS), terminálovém adaptéru nebo síťové mezisystémové funkci (IWF)
- Funguje s transparentními i netransparentními datovými přenosovými službami
- Umožňuje příjem faxů přijímaných mobilní sítí do ručních zařízení
- Poskytuje specifikace pro mezisystémový provoz pro připojení k faxovým přístrojům PSTN/ISDN

## Související pojmy

- [T-FAX – Transmission side facsimile](/mobilnisite/slovnik/t-fax/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization

---

📖 **Anglický originál a plná specifikace:** [R-FAX na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-fax/)
