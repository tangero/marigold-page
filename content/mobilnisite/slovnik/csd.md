---
slug: "csd"
url: "/mobilnisite/slovnik/csd/"
type: "slovnik"
title: "CSD – Circuit Switched Data"
date: 2025-01-01
abbr: "CSD"
fullName: "Circuit Switched Data"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csd/"
summary: "Circuit Switched Data (CSD) je služba 2G/3G umožňující přenos dat přes vyhrazená spojově-komutovaná spojení, primárně pro nízkorychlostní aplikace jako fax a raný přístup k internetu. Položila základy"
---

CSD je služba 2G/3G umožňující přenos dat přes vyhrazená spojově-komutovaná spojení, primárně pro nízkorychlostní aplikace jako fax a raný přístup k internetu.

## Popis

Circuit Switched Data (CSD) je základní služba mobilního přenosu dat definovaná ve standardech GSM a UMTS (3G) organizací 3GPP. Funguje tak, že na dobu trvání datového hovoru vytvoří vyhrazené, koncové fyzické nebo logické okruhové spojení mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a sítí, což odpovídá tradičnímu spojově-komutovanému modelu používanému pro hlas. Toto spojení prochází rádiovou přístupovou sítí ([BSS](/mobilnisite/slovnik/bss/) v GSM, [UTRAN](/mobilnisite/slovnik/utran/) v UMTS) a je směrováno přes ústřednu mobilní komunikace ([MSC](/mobilnisite/slovnik/msc/)) buď k funkci pro propojení sítí ([IWF](/mobilnisite/slovnik/iwf/)), nebo přímo k dalšímu spojově-komutovanému koncovému bodu, jako je modem ve veřejné telefonní síti ([PSTN](/mobilnisite/slovnik/pstn/)) nebo v síti [ISDN](/mobilnisite/slovnik/isdn/). IWF je kritický síťový prvek, který provádí přizpůsobení přenosové rychlosti a konverzi protokolů, což umožňuje mobilnímu terminálu komunikovat s externími datovými sítěmi. CSD poskytuje transparentní datový kanál, což znamená, že síť neinterpretuje uživatelská datová přenášená data; pouze zajišťuje, že bity jsou doručeny v pořadí s minimálním zpožděním a kolísáním, což ji činí vhodnou pro časově citlivé aplikace s nízkou šířkou pásma.

Technická implementace CSD zahrnuje několik vrstev protokolů. Přes rádiové rozhraní jsou data přenášena na kanálu pro přenos uživatelských dat ([TCH](/mobilnisite/slovnik/tch/)), podobně jako hlasový hovor. Pro GSM je základní přenosová rychlost 9,6 kbit/s (nebo 14,4 kbit/s s vylepšeným kódováním) na časový slot, využívající stejné kanálové kódování a modulaci jako hlas, ale s odlišnými schématy kanálového kódování optimalizovanými pro data. V UMTS mohla být CSD přenášena přes vyhrazené kanály (DCH) ve spojově-komutované doméně, podporující rychlosti v souladu s definicemi přenosových služeb UMTS. Zpracování v jádrové síti provádí MSC, která s datovým hovorem zachází stejně jako s hlasovým pro účely komutace a správy mobility. Klíčovým rozlišovacím prvkem je zapojení IWF, které přizpůsobuje datový tok z protokolů optimalizovaných pro mobilní přenos (např. přizpůsobení rychlosti na rádiovém rozhraní) na standardní protokoly pevných modemů (jako V.110, V.120 nebo I.463) pro propojení s PSTN/ISDN nebo na IP přes modemový pool.

Z perspektivy síťové architektury představuje CSD počáteční integraci datových služeb do mobilního spojově-komutovaného jádra. Využívá stávající signalizační a řídicí mechanismy hovorů GSM/UMTS, konkrétně protokoly pro sestavení hovoru (pomocí DTAP a BSSAP), správu mobility (MM) a správu spojení (CM). Toto konstrukční rozhodnutí umožnilo rychlé nasazení využívající robustní, existující telefonní infrastrukturu, ale zároveň sdílelo její omezení: neefektivní využití rádiových a síťových zdrojů pro přerušovaný datový provoz, protože vyhrazený okruh zůstává obsazen a spotřebovává zdroje i během období nečinnosti. Služba je charakterizována svou spojení orientovanou povahou, poskytuje konstantní bitovou rychlost, nízkou latenci a vysokou spolehlivost v mezích rádiového kanálu, ale za cenu spektrální účinnosti a neschopnosti statisticky multiplexovat více uživatelů.

Role CSD se vyvíjela od primární mobilní datové služby v raných sítích GSM k doplňkové a zastaralé službě v éře 3G a později. Sloužila jako technologický základ pro pokročilejší spojově-komutované datové služby, jako je High-Speed Circuit-Switched Data (HSCSD), které agregovaly více časových slotů pro dosažení vyšších rychlostí. Přestože je CSD pro obecný spotřebitelský přístup k internetu z velké části zastaralá, její principy a podkladová spojově-komutovaná přenosová služba zůstávají definovány ve specifikacích 3GPP kvůli zpětné kompatibilitě, podpoře specializovaných aplikací komunikace mezi stroji (M2M) vyžadujících konstantní, předvídatelné spojení a jako záložní služba v oblastech bez pokrytí paketově-komutovanými sítěmi.

## K čemu slouží

CSD byla vytvořena, aby do rychle se rozšiřujících GSM mobilních sítí počátku 90. let 20. století zavedla základní možnosti datové komunikace. Před GSM nabízely analogové mobilní systémy velmi omezené a proprietární datové možnosti. Hlavní problém, který CSD řešila, bylo poskytnutí standardizované, spolehlivé metody pro mobilní zařízení k přenosu digitálních dat – jako faxových dokumentů, transakcí v místě prodeje nebo raného e-mailu – využívající stejnou síťovou infrastrukturu postavenou pro hlas. Motivací bylo rozšířit využitelnost mobilních telefonů mimo hlasové hovory, otevřít nové zdroje příjmů pro operátory a umožnit rané aplikace mobilních výpočtů a telemetrie. Řešila omezení neexistence integrované datové služby přizpůsobením osvědčené, spojení orientované spojově-komutované technologie.

Historický kontext je klíčový: v počátcích digitální mobilní komunikace byl internet v plenkách a datový provoz byl převážně modelován na paradigmatu spojově-komutované telefonie a pronajatých linek. Aplikace jako fax a vytáčené připojení modemem byly navrženy pro sítě s konstantní bitovou rychlostí a spojení orientované, jako je PSTN. Nejpraktičtějším technickým řešením tedy bylo, aby síť GSM pro koncovou aplikaci „vypadala“ jako připojení přes pevný modem. To vyžadovalo minimální změny v architektuře jádrové sítě (především přidání IWF) a umožnilo mobilním terminálům používat zavedené datové protokoly. CSD umožnila první vlnu mobilních datových služeb, prokázala poptávku na trhu a připravila cestu pro vývoj efektivnějších, paketově orientovaných technologií jako GPRS.

CSD také řešila problém interoperability a standardizace. Definováním jasné sady protokolů (např. pro přizpůsobení rychlosti) a síťových funkcí (IWF) zajistila, že mobilní zařízení od různých výrobců se mohou připojit k datovým službám napříč různými síťovými operátory po celém světě. To byl významný úspěch v éře proprietárních systémů. Zatímco její omezení v účinnosti se stala zřejmými s růstem prohlížení webu a dalších aplikací založených na IP, účelem CSD bylo poskytnout jednoduchou, spolehlivou a okamžitě nasaditelnou datovou službu využívající dostupnou technologii a architektonické myšlení své doby.

## Klíčové vlastnosti

- Vyhrazené koncové okruhové spojení na dobu trvání hovoru
- Dodávka s konstantní bitovou rychlostí (typicky 9,6 kbit/s nebo 14,4 kbit/s na časový slot v GSM)
- Transparentní přenos dat bez interpretace uživatelských dat síťovou vrstvou
- Využívá stávající spojově-komutované jádrové sítě (MSC) a signalizaci řízení hovoru
- Spoléhá na funkci pro propojení sítí (IWF) pro konverzi protokolů na PSTN/ISDN/IP
- Poskytuje předvídatelnou latenci a vysokou spolehlivost spojení

## Související pojmy

- [HSCSD – High Speed Circuit Switched Data](/mobilnisite/slovnik/hscsd/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [CSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/csd/)
