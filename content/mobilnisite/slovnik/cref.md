---
slug: "cref"
url: "/mobilnisite/slovnik/cref/"
type: "slovnik"
title: "CREF – SCCP Connection Refused"
date: 2025-01-01
abbr: "CREF"
fullName: "SCCP Connection Refused"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cref/"
summary: "Zpráva Signalizačního spojového řídicího subsystému (SCCP) signalizující zamítnutí požadavku na navázání spojení. Jedná se o kritickou chybovou odpověď v signalizační síti SS7, používanou k řízení sig"
---

CREF je chybová zpráva protokolu SCCP, která signalizuje, že požadavek na navázání signalizačního spojení byl odmítnut, aby se předešlo plýtvání síťovými prostředky mezi uzly, jako jsou MSC a HLR.

## Popis

CREF je specifický typ zprávy v rámci protokolu Signalizačního spojového řídicího subsystému (SCCP), který funguje na 4. vrstvě signalizačního zásobníku SS7/C7. Je generována jako negativní odpověď na zprávu SCCP Connection Request ([CR](/mobilnisite/slovnik/cr/)). Když síťový uzel (např. mobilní ústředna - [MSC](/mobilnisite/slovnik/msc/)) odešle zprávu CR k navázání signalizačního spojení s jiným uzlem (např. domovským registrem polohy - [HLR](/mobilnisite/slovnik/hlr/)), přijímající uzel může požadavek z různých důvodů odmítnout. Po takovém rozhodnutí přijímající uzel vytvoří a odešle zpět iniciátorovi zprávu CREF. Tato zpráva obsahuje povinné parametry, nejdůležitější z nich je Destination Local Reference (DLR), který je zkopírován z parametru Source Local Reference (SLR) příchozí zprávy CR, aby byla odpověď spojena s konkrétním požadavkem. Obsahuje také povinný parametr 'Refusal Cause' (příčina zamítnutí), což je klíčová informace udávající přesný důvod zamítnutí spojení, jako je 'žádný překlad pro adresu tohoto typu', 'přetížení sítě', 'uživatel nedosažitelný' nebo 'neplatná zpráva'. Zpráva CREF okamžitě ukončí proceduru navazování spojení pro tento konkrétní pokus a iniciující uzel musí interpretovat kód příčiny, aby určil další postup, který může zahrnovat přeuspořádání signalizačního požadavku, aplikaci časovačů pro odklad opakování nebo upozornění aplikací vyšší vrstvy na selhání. Spolehlivé a standardizované doručení této příčiny zamítnutí je nezbytné pro síťovou diagnostiku, správu chyb a udržení celkové stability signalizační sítě tím, že brání opakovaným pokusům o spojení s nedosažitelnými nebo přetíženými cíli. Postupy protokolu zajišťují, že po odeslání nebo přijetí zprávy CREF oba uzly uvolní všechny dočasné prostředky přidělené pro tento pokus o spojení.

## K čemu slouží

Zpráva CREF existuje, aby poskytovala řízený a informativní mechanismus pro zamítání požadavků na navázání SCCP spojení v okruhově komutovaných telekomunikačních sítích. Před standardizovanými signalizačními protokoly, jako je SS7, byly síťová propojení a správa chyb často proprietární a méně efektivní. Protokol SCCP a následně i zpráva CREF byly vytvořeny, aby poskytly spojově orientovanou službu nad inherentně nespojovou přenosovou částí ([MTP](/mobilnisite/slovnik/mtp/)) SS7, což umožňuje spolehlivé transakční dialogy pro služby, jako je mobilní roamování nebo inteligentní síť. Zpráva CREF řeší problém tichých selhání nebo nejednoznačných zamítnutí. Bez ní by uzel odesílající [CR](/mobilnisite/slovnik/cr/) mohl pouze vypršet časový limit, takže by zůstalo nejisté, zda protistrana je nedostupná, přetížená, nebo zda byla zpráva neplatná. Povinným zasláním zamítnutí s konkrétní příčinou umožňuje CREF iniciujícímu uzlu programově porozumět důvodu selhání. To umožňuje inteligentní síťové chování, jako je výběr alternativního [HLR](/mobilnisite/slovnik/hlr/) v případě 'uživatel neznámý', aplikace řízení toku v případě 'přetížení sítě' nebo zaznamenávání poruch pro zásah operátora. Je základním prvkem robustní signalizace, který zajišťuje, že síťové prostředky nejsou blokovány čekáním na odpovědi od neúspěšných spojení a že servisní logika dokáže selhání elegantně zpracovat, což je zásadní pro spolehlivost telefonie a raných mobilních služeb.

## Klíčové vlastnosti

- Definovaná negativní odpověď na zprávu SCCP Connection Request (CR)
- Nese povinný parametr 'Refusal Cause' pro diagnostickou jasnost
- Používá Destination Local Reference (DLR) pro přesnou korelaci požadavek-odpověď
- Okamžitě ukončí proceduru navazování spojení
- Umožňuje síťovým uzlům implementovat inteligentní strategie obnovy po selhání
- Základní prvek mechanismů řízení chyb a přetížení signalizace SS7

## Související pojmy

- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)
- [BSSAP – Base Station Subsystem Application Part](/mobilnisite/slovnik/bssap/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN

---

📖 **Anglický originál a plná specifikace:** [CREF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cref/)
