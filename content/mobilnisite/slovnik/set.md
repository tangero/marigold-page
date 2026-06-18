---
slug: "set"
url: "/mobilnisite/slovnik/set/"
type: "slovnik"
title: "SET – SUPL Enabled Terminal"
date: 2025-01-01
abbr: "SET"
fullName: "SUPL Enabled Terminal"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/set/"
summary: "SUPL Enabled Terminal (SET) je mobilní zařízení (UE), které podporuje protokol Secure User Plane Location (SUPL) pro určení své geografické polohy. Komunikuje přes uživatelskou rovinu (IP spojení) s p"
---

SET je mobilní zařízení podporující protokol Secure User Plane Location (SUPL) pro určení své geografické polohy komunikací s lokalizační platformou přes IP spojení.

## Popis

[SUPL](/mobilnisite/slovnik/supl/) Enabled Terminal (SET) je klientské zařízení v architektuře [OMA](/mobilnisite/slovnik/oma/) Secure User Plane Location (SUPL), kterou převzal a specifikoval 3GPP pro polohové služby. SET je typicky uživatelské zařízení (UE), jako je smartphone nebo IoT zařízení, které obsahuje klientský softwarový stack SUPL. Tento klient komunikuje se síťovým serverem zvaným SUPL Location Platform ([SLP](/mobilnisite/slovnik/slp/)) za účelem výpočtu polohy zařízení. Na rozdíl od metod lokalizace v řídicí rovině, které používají signalizační kanály, SUPL přenáší všechny zprávy polohového protokolu (např. z LTE Positioning Protocol, [LPP](/mobilnisite/slovnik/lpp/)) zabudované v zabezpečeném IP datovém spojení (uživatelská rovina), jako je běžná mobilní datová relace.

Operace začíná, když je spuštěn požadavek na polohu, a to buď samotným SET (mobilně iniciováno), nebo sítí (mobilně ukončeno, např. pro nouzové volání). SET naváže zabezpečené [TLS](/mobilnisite/slovnik/tls/)/[SSL](/mobilnisite/slovnik/ssl/) spojení se SLP. Následně si vymění informace o podporovaných možnostech, aby se dohodly na podporovaných metodách určování polohy, které mohou zahrnovat satelitní metody jako [GPS](/mobilnisite/slovnik/gps/), [A-GPS](/mobilnisite/slovnik/a-gps/), GLONASS, Galileo a terestrické metody jako Observed Time Difference of Arrival (OTDOA) v LTE nebo Downlink Time Difference of Arrival (DL-TDoA) v 5G. SLP může poskytnout SET asistenční data, jako jsou efemeridy satelitů nebo polohy buněčných věží, aby výrazně urychlila určení a zlepšila přesnost (jedná se o Assisted-GNSS).

SET využívá svůj interní GNSS přijímač a/nebo měří signály z okolních buněčných základnových stanic. Skutečný výpočet polohy může proběhnout v SET (režim založený na SET), kde si zařízení vypočte svou vlastní polohu a odešle ji SLP, nebo v SLP (asistovaný režim SET), kde SET odešle surová měřicí data (např. pseudovzdálenosti) do SLP k výpočtu. Protokol SUPL (konkrétně verze jako 1.0, 2.0, 3.0) definuje toky zpráv pro zahájení relace, vyjednávání možností, doručování asistenčních dat a hlášení polohy. Role SET je klíčová pro umožnění efektivních, škálovatelných a přesných polohových služeb pro spotřebitelské aplikace (mapy), podnikové sledování a regulatorní služby jako E911/E112 bez přetížení signalizační sítě řídicí roviny.

## K čemu slouží

SET a rámec SUPL byly vytvořeny, aby poskytly standardizovanou, efektivní a škálovatelnou metodu pro poskytování polohových služeb přes buněčné sítě. Před SUPL většina síťových polohových služeb využívala řídicí rovinu, kde byla lokalizační signalizace přenášena přes SS7 nebo jiné kanály s přepojováním okruhů. Tento přístup byl neefektivní pro velký objem polohových požadavků (např. z nesčetných aplikací ve smartphonech), mohl zpomalit signalizaci jádra sítě a nebyl vhodný pro stále připojená IP zařízení.

Přístup SUPL v uživatelské rovině tyto problémy řeší využitím existujícího datového spojení. To činí polohové služby snadněji nasaditelné (protože využívají IP infrastrukturu), škálovatelnější a dostupnější širšímu okruhu vývojářů aplikací. Účelem definice SET bylo zajistit interoperabilitu mezi zařízeními od různých výrobců a síťovými servery (SLP) od různých dodavatelů. Umožňuje zařízením získávat od sítě asistenční data pro dosažení rychlejšího času do prvního určení (TTFF) a lepšího výkonu GNSS v interiérech, což je klíčová funkce známá jako Assisted-GPS (A-GPS).

SUPL a SET jsou navíc nezbytné pro splnění regulatorních požadavků na lokalizaci při nouzových voláních (např. FCC E911) v sítích s přepojováním paketů. Jak se sítě vyvíjely směrem k LTE a 5G, které jsou plně IP, řídicí rovina pro starší lokalizaci zastarala. SUPL poskytl cestu vpřed. Vývoj SET prostřednictvím vydání 3GPP integroval podporu nových polohových technologií, jako je OTDOA pro LTE a NR positioning, což zajišťuje neustálé zlepšování přesnosti a spolehlivosti služeb od navigace po jednotlivých krocích až po lokalizační reklamu a sledování IoT aktiv.

## Klíčové vlastnosti

- Klient pro uživatelskou rovinu polohového protokolu OMA SUPL
- Podporuje více metod určování polohy: A-GNSS (GPS, Galileo), OTDOA, WLAN positioning
- Funguje v režimech založených na SET (terminál počítá) a asistovaných SET (síť počítá)
- Používá zabezpečené TLS/SSL spojení s platformou SUPL Location Platform (SLP)
- Přijímá síťově poskytovaná asistenční data pro rychlejší a přesnější určování polohy
- Umožňuje jak mobilně iniciované (MO), tak mobilně ukončené (MT) požadavky na polohu

## Související pojmy

- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [SLP – Service Location Protocol](/mobilnisite/slovnik/slp/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [SET na 3GPP Explorer](https://3gpp-explorer.com/glossary/set/)
