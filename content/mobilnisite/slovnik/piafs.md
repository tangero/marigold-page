---
slug: "piafs"
url: "/mobilnisite/slovnik/piafs/"
type: "slovnik"
title: "PIAFS – PHS Internet Access Forum Standard"
date: 2025-01-01
abbr: "PIAFS"
fullName: "PHS Internet Access Forum Standard"
category: "Protocol"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/piafs/"
summary: "Standard protokolu pro datovou komunikaci přes sítě PHS (Personal Handy-phone System), umožňující přístup k internetu a datové služby. Definuje modulaci, rámcování a řízení chyb pro spolehlivý přenos"
---

PIAFS je standard protokolu pro datovou komunikaci přes sítě PHS, který umožňuje přístup k internetu definováním modulace, rámcování a řízení chyb pro propojení PHS s IP sítěmi.

## Popis

[PHS](/mobilnisite/slovnik/phs/) Internet Access Forum Standard (PIAFS) je specifikace protokolu vyvinutá pro Personal Handy-phone System (PHS), bezdrátový komunikační systém populární v Japonsku a částech Asie. Standardizuje datovou komunikaci přes sítě PHS a poskytuje rámec pro přístup k internetu, přenos souborů a další datové služby. PIAFS definuje procedury fyzické vrstvy a vrstvy spojení, včetně modulačních schémat, formátů rámců, opravy chyb a řízení toku, aby zajistil efektivní a spolehlivý přenos dat mezi PHS terminály a síťovými přístupovými body. Protokol funguje tak, že naváže okruhově nebo paketově přepínané spojení přes PHS rádiová rozhraní a poté adaptuje datové pakety pro přenos, často spolupracuje s [PPP](/mobilnisite/slovnik/ppp/) (Point-to-Point Protocol) pro integraci s IP sítěmi.

Architektonicky zahrnuje PIAFS klíčové komponenty, jako je PHS terminál (např. datová karta nebo telefon), PHS základnová stanice a síťový adaptér nebo server kompatibilní s PIAFS. Specifikuje více verzí (např. PIAFS 1.0, 2.0) s rostoucí přenosovou rychlostí od 32 kbps do 64 kbps nebo vyšší, využívajících pokročilou modulaci jako π/4-shift [QPSK](/mobilnisite/slovnik/qpsk/). Zásobník protokolů zahrnuje fyzickou vrstvu pro rádiový přenos, spojovou vrstvu pro rámcování a detekci chyb pomocí [CRC](/mobilnisite/slovnik/crc/) a síťovou adaptační vrstvu pro kompatibilitu s [TCP/IP](/mobilnisite/slovnik/tcp-ip/). Při provozu PHS zařízení iniciuje datové volání pomocí signalizace PIAFS, vyjedná parametry jako rychlost a kompresi a poté přenáší data v rámcích s potvrzeními a opakovanými přenosy pro spolehlivost, podobně jako modemové protokoly, ale optimalizované pro charakteristiky PHS, jako je dynamická alokace kanálů.

Úloha PIAFS v síti spočívala v umožnění mobilních datových služeb před rozšířením 3G a LTE. Umožňoval operátorům PHS nabízet internetové připojení, e-mail a prohlížení, čímž konkuroval raným datovým technologiím buněčné sítě. PIAFS funguje tak, že využívá mikrobuněčnou architekturu PHS pro nízkopříkonové pokrytí s vysokou hustotou, poskytuje nákladově efektivní datové řešení v městských oblastech. Jeho specifikace v dokumentech 3GPP, jako jsou TS 27.001 a TS 29.007, zajišťují interoperabilitu s prvky jádra sítě, podporují funkce jako spolupráce s [PSTN](/mobilnisite/slovnik/pstn/)/[ISDN](/mobilnisite/slovnik/isdn/) pro vytáčený přístup nebo s paketovými datovými sítěmi pro přímou IP konektivitu. Ačkoli PHS s nástupem 3G upadl, PIAFS zůstává historickým příkladem návrhu bezdrátového datového protokolu, který ovlivnil pozdější standardy pro mobilní data.

## K čemu slouží

PIAFS byl vytvořen, aby řešil potřebu standardizované datové komunikace přes sítě [PHS](/mobilnisite/slovnik/phs/), které se původně zaměřovaly na hlasové služby. Koncem 90. let 20. století, s růstem využívání internetu, chtěli operátoři PHS v Japonsku nabízet datové možnosti, ale proprietární řešení vedla k fragmentaci a omezené interoperabilitě. PHS Internet Access Forum vyvinul PIAFS, aby definoval jednotný protokol, který vyřešil problém nekompatibilních datových implementací a umožnil rozšířený přístup k internetu na PHS zařízeních, podobně jako standardizace V.90 modemů pro vytáčený přístup přes PSTN.

Historicky si PHS získal popularitu díky nízkonákladovým mikrobuňkám s vysokou kapacitou, ale postrádal nativní podporu dat. PIAFS tuto mezeru zaplnil poskytnutím robustního protokolu pro přenos dat přes TDMA/TDD rádiové rozhraní PHS, řešíc omezení jako proměnná kvalita signálu a výzvy spojené s předáváním hovoru. Umožnil PHS konkurovat raným datovým službám 2G, jako je GPRS, a nabízet vyšší rychlosti v hustě obydlených oblastech. Motivace zahrnovala podporu vznikajících aplikací, jako je webové prohlížení a e-mail na mobilních zařízeních, čímž se prodloužila životnost a užitečnost PHS v době před širokopásmovým připojením.

V kontextech 3GPP byl PIAFS odkazován pro spolupráci a podporu starších technologií, zejména při vývoji sítí směrem k 3G a dále. Řešil problémy s integrací při migraci uživatelů PHS na UMTS nebo LTE a zajišťoval zpětnou kompatibilitu. Bez PIAFS by datové služby PHS zůstaly okrajové a specifické pro operátora, což by bránilo přijetí mobilního internetu v regionech, kde byl PHS rozšířen, a oddálilo by konvergenci k globálním datovým standardům.

## Klíčové vlastnosti

- Standardizovaný datový protokol pro sítě PHS s verzemi až do 64 kbps
- Definuje modulaci fyzické vrstvy (např. π/4-shift QPSK) a rámcování
- Zahrnuje mechanismy řízení chyb, jako je CRC a ARQ, pro spolehlivost
- Podporuje okruhově a paketově přepínaná datová spojení
- Spolupracuje s PPP pro přístup k IP sítím a aplikace TCP/IP
- Umožňuje mobilní internetové služby, jako je prohlížení a přenos souborů

## Související pojmy

- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)

## Definující specifikace

- **TS 27.001** (Rel-19) — Terminal Adaptation Functions for PLMN
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements

---

📖 **Anglický originál a plná specifikace:** [PIAFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/piafs/)
