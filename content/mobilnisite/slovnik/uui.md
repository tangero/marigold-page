---
slug: "uui"
url: "/mobilnisite/slovnik/uui/"
type: "slovnik"
title: "UUI – User-to-User Information"
date: 2026-01-01
abbr: "UUI"
fullName: "User-to-User Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uui/"
summary: "UUI je doplňková služba v sítích s přepojováním okruhů (CS), která umožňuje transparentní přenos omezeného množství uživatelem definovaných dat uvnitř signalizace řízení hovoru, typicky během sestavov"
---

UUI je doplňková služba v sítích s přepojováním okruhů, která umožňuje transparentní přenos omezeného množství uživatelem definovaných dat uvnitř signalizace řízení hovoru.

## Popis

User-to-User Information (UUI) je doplňková služba telefonie s přepojováním okruhů standardizovaná 3GPP, která usnadňuje výměnu malého, uživatelem generovaného datového užitečného zatížení mezi dvěma koncovými body jako součást procesu sestavení nebo ukončení hovoru. Na rozdíl od hlasové přenosové cesty je UUI přenášeno transparentně uvnitř signalizačních zpráv řízení hovoru, konkrétně v [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo v protokolech Q.931/Q.932 používaných v jádru sítě. Služba definuje prvek UUI, což je sekvence oktetů (bajtů) se stanovenou maximální délkou, který může vložit volající strana a který je doručen volané straně. Úlohou sítě je především tento informační prvek přenést bez interpretace nebo úpravy, ačkoli síťové uzly mohou potřebovat kontrolovat omezení délky a profily předplatného služby.

Z architektonického hlediska UUI funguje uvnitř signalizačních vrstev domény s přepojováním okruhů. Když uživatel zahájí hovor a zahrne UUI, uživatelské zařízení (UE) nebo terminál umístí data do příslušné zprávy SETUP nebo FACILITY. Tato zpráva prochází signalizační sítí (např. přes [MSC](/mobilnisite/slovnik/msc/)). Obsluhující MSC ověří, že odchozí účastník je autorizován pro službu UUI a že délka informace odpovídá síťovým limitům. Poté zkopíruje prvek UUI do odchozí ISUP Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)). Přijímající MSC provede podobné kontroly pro ukončujícího účastníka předtím, než zahrne UUI do zprávy SETUP odeslané do terminálu volané strany. Služba může být nakonfigurována pro jednosměrný přenos (od volajícího k volanému) nebo obousměrnou výměnu a může být odeslána při sestavení hovoru (UUI Setup), během aktivního hovoru (UUI Mid-Call) nebo při ukončení hovoru (UUI Release).

Mezi klíčové komponenty patří UE, které musí podporovat generování a příjem UUI; Mobile Switching Center (MSC), které funguje jako přepínací bod služby a vynucuje předplatné a síťové politiky; a samotné signalizační protokoly (např. [DSS1](/mobilnisite/slovnik/dss1/), ISUP). Úloha UUI v síti spočívá v umožnění rozšířených služeb bez nutnosti samostatného datového spojení. Poskytuje jednoduchý signalizační mechanismus v pásmu pro přenos kontextu, což je klíčové pro integraci telefonie se službami inteligentní sítě, funkcemi podnikových ústředen [PBX](/mobilnisite/slovnik/pbx/) nebo tísňovými službami (např. předání polohy nebo lékařských dat). Její fungování je definováno v řadě specifikací 3GPP pokrývajících popis služby (22.087, 23.087), podrobnosti protokolu (24.087, 25.415) a terminologii (21.905).

## K čemu slouží

UUI bylo vytvořeno za účelem rozšíření funkcionality základních hlasových hovorů s přepojováním okruhů tím, že umožňuje výměnu dat aplikační vrstvy spolu se signalizací hovoru. Před jeho zavedením vyžadovalo vytváření služeb, které potřebovaly sdílení kontextu mezi volajícími (jako například vyskakovací okna v call centrech, bezpečné tokeny pro zpětné volání nebo předání identifikátoru zákazníka), složité datové systémy mimo pásmo nebo proprietární implementace. UUI tento problém řeší tím, že poskytuje standardizovaný, síťově transparentní kanál uvnitř všudypřítomného procesu sestavení hovoru, což umožňuje interoperabilitu mezi zařízeními od různých výrobců a přes síťové hranice.

Historický kontext spočívá ve vývoji služeb [ISDN](/mobilnisite/slovnik/isdn/) a inteligentní sítě v 80. a 90. letech 20. století. Jak se obchodní a nadstavbové služby stávaly sofistikovanějšími, vznikla jasná potřeba předávat informace o účelu hovoru nebo identitě volajícího. UUI, standardizované od 3GPP Release 4 dále, tuto potřebu pro [CS](/mobilnisite/slovnik/cs/) sítě GSM a UMTS naplnilo. Překonalo omezení, kdy byl signalizační systém čistě 'hloupou trubkou' pro směrování hovorů, a proměnilo ho v nástroj umožňující inovace služeb. Ačkoli bylo UUI z velké části nahrazeno IP mechanismy v IMS, zůstává relevantní pro starší CS služby a specifické regulatorní aplikace.

## Klíčové vlastnosti

- Transparentní přenos uživatelem definovaných dat uvnitř signalizace řízení hovoru (ISUP/Q.931)
- Podpora přenosu při sestavení hovoru (UUI Setup), během hovoru (UUI Mid-Call) a při ukončení hovoru (UUI Release)
- Možnost konfigurace pro jednosměrnou (od volajícího k volanému) nebo obousměrnou výměnu informací
- Vynucování maximální délky informace a autorizace služby účastníka ze strany sítě
- Umožňuje rozšířené služby, jako je doručování jména volajícího, předání kontextu aplikace a bezpečná autentizace
- Definovaná interoperabilita napříč více releasy a specifikacemi 3GPP pro konzistentní implementaci

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.087** (Rel-19) — User-to-User Signalling (UUS) Supplementary Service
- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 24.087** (Rel-19) — User-to-User Signalling (UUS) Stage 3
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol

---

📖 **Anglický originál a plná specifikace:** [UUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/uui/)
