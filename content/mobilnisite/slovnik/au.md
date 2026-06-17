---
slug: "au"
url: "/mobilnisite/slovnik/au/"
type: "slovnik"
title: "AU – Access Unit"
date: 2025-01-01
abbr: "AU"
fullName: "Access Unit"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/au/"
summary: "Access Unit (AU) je funkční entita definovaná v raných releasích 3GPP, založená na standardu CCITT X.31. Umožňuje připojení ne-ISDN koncového zařízení (TE) k ISDN síti a tím přístup k paketově přepína"
---

AU (Access Unit) je funkční entita z raných releasí 3GPP, která připojuje ne-ISDN koncové zařízení k ISDN síti a funguje jako adaptační vrstva pro zajištění přístupu k paketově přepínaným službám.

## Popis

Access Unit (AU) je funkční entita v síti specifikovaná v kontextu raných prací 3GPP na propojování s pevnými sítěmi a službami. Její definice vychází z doporučení [CCITT](/mobilnisite/slovnik/ccitt/) (nyní [ITU-T](/mobilnisite/slovnik/itu-t/)) X.31, které detailně popisuje procedury pro podporu terminálového zařízení v paketovém režimu prostřednictvím [ISDN](/mobilnisite/slovnik/isdn/). Architektonicky je AU umístěna mezi ne-ISDN koncové zařízení (TE) a ISDN síť. Jejím hlavním úkolem je poskytnout potřebné adaptační funkce, které umožní TE používajícímu protokoly jako X.25 přistupovat k paketově přepínaným službám přes digitální kanály ISDN pro přenos uživatelských dat (B-kanály) nebo signalizační kanály (D-kanály).

Provozně AU funguje implementací převodu a mapování protokolů. Ukončuje protokolový zásobník používaný terminálem (např. protokol X.25 přes fyzické rozhraní jako X.21 nebo V-série) a mapuje uživatelská data a řídicí signalizaci na příslušné vrstvy ISDN. To zahrnuje adaptaci procedur linkové vrstvy ([LAPB](/mobilnisite/slovnik/lapb/) pro X.25) na protokol [LAPD](/mobilnisite/slovnik/lapd/) používaný v ISDN na D-kanálu pro signalizaci a případně pro paketová data. Pro vlastní přenos dat AU spravuje zřizování a uvolňování spojení na B-kanálech podle požadavků paketů pro sestavení spojení X.25 z terminálu, čímž v podstatě funguje jako brána mezi doménami X.25 a ISDN.

Klíčové součásti funkčnosti AU zahrnují adaptaci fyzického rozhraní pro TE, bod ukončení protokolu X.25, zásobník protokolů ISDN (Q.931 pro řízení hovorů, Q.921/LAPD pro spojovou vrstvu) a logiku pro vzájemné propojení, která mapuje mezi těmito dvěma servisními doménami. V kontextu sítě 3GPP byla její role primárně definována pro scénáře, kdy služby mobilní sítě potřebovaly spolupracovat s nebo poskytovat přístup k tehdy převládajícím veřejným paketově přepínaným datovým sítím (PSPDN). Tvořila součást širší funkce pro vzájemné propojení ([IWF](/mobilnisite/slovnik/iwf/)) mezi PLMN a externími sítěmi.

Význam AU v raných specifikacích 3GPP spočívá v její roli mostu mezi vyvíjejícími se standardy mobilní digitální komunikace a existujícím, široce rozšířeným světem datových komunikací založených na X.25. Zajišťovala zpětnou kompatibilitu a kontinuitu služeb, což umožňovalo mobilním uživatelům a službám připojovat se k podnikovým sítím, online databázím a dalším službám s přidanou hodnotou, které fungovaly přes veřejné paketové sítě. Její specifikace v dokumentech jako 23.043 a 23.044 detailně popisují scénáře a procedury pro toto vzájemné propojení.

## K čemu slouží

Access Unit byl vytvořen, aby vyřešil základní problém vzájemného propojení sítí mezi novými digitálními sítěmi založenými na [ISDN](/mobilnisite/slovnik/isdn/) (včetně raných digitálních celulárních sítí jako GSM) a rozsáhlou instalovanou základnou ne-ISDN datových koncových zařízení, zejména těch používajících sadu protokolů X.25. Před nástupem ISDN a mobilních digitálních sítí datová komunikace terminálů často závisela na vyhrazených pronajatých linkách nebo vytáčených modemech používajících analogové telefonní sítě (PSTN) s protokolem X.25. Omezení těchto přístupů zahrnovala nízké rychlosti, šum na analogových linkách a neefektivní využití infrastruktury.

Nástup ISDN nabídl digitální koncové spojení s vyšší spolehlivostí a rychlostí prostřednictvím přenosových (B) kanálů. Stávající terminály X.25 však nemohly nativně používat protokoly ISDN. AU byla technologickým řešením této nekompatibility, motivovaným potřebou chránit investice do stávajících koncových zařízení a síťových služeb při migraci na moderní digitální sítě. Umožnila síťovým operátorům nabízet paketové datové služby svým účastníkům, aniž by nutila k plošné výměně zařízení na straně zákazníka.

V historickém kontextu 3GPP (počínaje Release 4) zahrnutí konceptu AU odráží snahu normalizačního orgánu definovat komplexní schopnosti vzájemného propojení pro jádrové sítě GSM/[GPRS](/mobilnisite/slovnik/gprs/) a UMTS. Řešilo požadavek, aby se mobilní stanice nebo funkce pro vzájemné propojení sítí mohly připojovat k externím PSPDN, a zajišťovalo, že mobilní datové služby mohou být bezproblémově integrovány s globální datovou komunikační infrastrukturou konce 20. století, která byla silně závislá na X.25 pro aplikace jako ověřování kreditních karet, rezervace letenek a přístup k podnikovým sítím.

## Klíčové vlastnosti

- Převod protokolů mezi X.25 a ISDN Q.931/Q.921
- Podpora provozních režimů X.31 Case A a Case B
- Ukončení linkové vrstvy LAPB z terminálu
- Mapování virtuálních volání X.25 na okruhově přepínané B-kanály ISDN nebo paketové D-kanály
- Adaptace fyzického rozhraní pro ne-ISDN terminály (např. X.21, V.24/V.28)
- Součást funkce pro vzájemné propojení (IWF) mezi PLMN a PSPDN

## Související pojmy

- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.043** (Rel-4) — GSM Videotex Service Support
- **TS 23.044** (Rel-4) — GSM Teletex Service Support
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [AU na 3GPP Explorer](https://3gpp-explorer.com/glossary/au/)
