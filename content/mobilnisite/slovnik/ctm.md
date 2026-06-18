---
slug: "ctm"
url: "/mobilnisite/slovnik/ctm/"
type: "slovnik"
title: "CTM – Cellular Text telephone Modem"
date: 2025-01-01
abbr: "CTM"
fullName: "Cellular Text telephone Modem"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ctm/"
summary: "CTM je služba 3GPP umožňující komunikaci pomocí textu v reálném čase pro uživatele se sluchovým nebo řečovým postižením přes mobilní sítě. Poskytuje alternativu k hlasovým hovorům přenosem textových z"
---

CTM je služba 3GPP umožňující komunikaci pomocí textu v reálném čase pro uživatele se sluchovým nebo řečovým postižením přes mobilní sítě jako alternativu k hlasovým hovorům.

## Popis

Cellular Text telephone Modem (CTM) je standardizovaná služba v rámci 3GPP, která umožňuje komunikaci pomocí textu v reálném čase ([RTT](/mobilnisite/slovnik/rtt/)). Funguje tak, že převádí psané textové znaky na modulovaný signál vhodný pro přenos přes hlasový kanál mobilní sítě nebo vyhrazené datové přenosové cesty, v závislosti na implementaci a vydání specifikace. Architektura zahrnuje koncové zařízení, jako je textový telefon nebo mobilní zařízení se softwarem CTM, které komunikuje s modemovou funkcionalitou sítě. Tento modem zajišťuje kódování, modulaci a synchronizaci textových dat, aby byl přenášen jako souvislý datový proud napodobující časování hlasové konverzace. Mezi klíčové síťové komponenty patří Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) pro implementace s přepojováním okruhů a IP Multimedia Subsystem (IMS) pro verze s přepojováním paketů zavedené v pozdějších vydáních, které spravují zřizování relací, směrování a propojení s dalšími službami textové telefonie.

CTM v principu funguje tak, že naváže komunikační relaci, ve které je každý napsaný znak odeslán okamžitě po jeho zadání, bez čekání na stisknutí tlačítka 'odeslat'. Tento přenos v reálném čase je realizován pomocí specifických protokolů definovaných ve specifikacích 3GPP, jako je TS 26.226, které detailně popisují modulační schémata, rámcování dat a mechanismy korekce chyb. Pro CTM s přepojováním okruhů jsou textová data typicky přenášena přes kanál hlasového kodeku s adaptivní vícerychlostní modulací ([AMR](/mobilnisite/slovnik/amr/)) nebo přes vyhrazený datový kanál, přičemž se používají modulační techniky jako frekvenční klíčování ([FSK](/mobilnisite/slovnik/fsk/)) pro vložení textu do audio signálu. V implementacích s přepojováním paketů CTM využívá protokol [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol) přes IP sítě, což umožňuje efektivnější využití šířky pásma a integraci se službami založenými na IMS, jako je Voice over LTE (VoLTE) a 5G Voice.

Úlohou CTM v síti je poskytovat přístupnou komunikační službu, která je interoperabilní se staršími systémy textové telefonie, jako jsou ty používané v pevných sítích (např. zařízení [TTY](/mobilnisite/slovnik/tty/)). Zajišťuje, že uživatelé s postižením mohou bezproblémově komunikovat napříč různými typy sítí. Relace CTM mohou být navázány mezi dvěma zařízeními podporujícími CTM, nebo mezi zařízením CTM a bránou, která převádí signál CTM do formátu kompatibilního s jinými službami textové telefonie. Služba zahrnuje funkce jako procedury navázání hovoru, přenos textu během hovoru a podporu více jazyků prostřednictvím standardů kódování znaků. Její integrace do sítí 3GPP podtrhuje důležitost inkluzivity v telekomunikacích a zpřístupňuje mobilní služby všem uživatelům bez ohledu na jejich fyzické schopnosti.

## K čemu slouží

CTM byl vytvořen, aby řešil komunikační potřeby osob se sluchovým nebo řečovým postižením v mobilních sítích. Před jeho zavedením ve vydání 3GPP Release 99 se mobilní telefonie primárně spoléhala na hlasové hovory, což vylučovalo uživatele, kteří nemohli efektivně slyšet nebo mluvit. Existující služby textové telefonie, jako je [TTY](/mobilnisite/slovnik/tty/) (Teletypewriter) na pevných linkách, nebyly v mobilním prostředí nativně podporovány, což vytvářelo významnou mezeru v přístupnosti. CTM měl tuto mezeru překlenout poskytnutím standardizované metody pro komunikaci textem v reálném čase přes sítě GSM a UMTS, a zajistit tak, aby mobilní technologie mohla sloužit širší populaci.

Motivace pro CTM pramenila z regulatorních a společenských tlaků na zvýšení přístupnosti v telekomunikacích, stejně jako z technické výzvy přizpůsobení textové telefonie omezením bezdrátových sítí. Tradiční zařízení TTY používala pro přenos textu analogové audio frekvence, které mohly být narušeny kompresí a zpracováním v digitálních mobilních kodecích. CTM tento problém vyřešil definicí specifických modulačních a kódovacích schémat, která jsou odolná vůči degradaci v síti, jak je popsáno např. v TS 26.226. Umožnil interoperabilitu se staršími systémy, což uživatelům dovolilo komunikovat mezi mobilními a pevnými textovými telefony, a podpořil tak inkluzivní komunikaci bez nutnosti zcela nové infrastruktury.

V průběhu času se CTM vyvíjel, aby řešil omezení raných implementací, jako byla neefektivita využití šířky pásma a nedostatečná integrace se službami založenými na IP. Původní CTM s přepojováním okruhů využíval prostředky hlasového kanálu, což mohlo být pro přenos dat suboptimální. Pozdější vydání zavedla CTM s přepojováním paketů přes IMS, které využívá IP sítě pro lepší výkon a škálovatelnost. Tento vývoj zajistil, že CTM zůstal relevantní při přechodu sítí na LTE a 5G, udržel přístupnost v službách mobilních sítí nové generace a zároveň zlepšil uživatelský zážitek prostřednictvím funkcí jako vyšší rychlost textu a podpora multimediálních kontextů.

## Klíčové vlastnosti

- Přenos textu v reálném čase s odesíláním znak po znaku
- Interoperabilita se staršími systémy textové telefonie jako je TTY
- Podpora implementací pro sítě s přepojováním okruhů i paketů
- Modulační schémata definovaná v TS 26.226 pro robustní přenos přes audio kanál
- Integrace s IMS pro služby VoLTE a 5G Voice
- Řízení hovoru a správa relací prostřednictvím signalizačních protokolů 3GPP

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TS 26.231** (Rel-19) — CTM Minimum Performance Requirements Testing
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 26.269** (Rel-19) — eCall In-band Modem Conformance Testing
- **TR 26.967** (Rel-19) — eCall via CTM Suitability Analysis
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [CTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctm/)
