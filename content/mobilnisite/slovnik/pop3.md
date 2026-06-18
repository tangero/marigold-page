---
slug: "pop3"
url: "/mobilnisite/slovnik/pop3/"
type: "slovnik"
title: "POP3 – Post Office Protocol, version 3"
date: 2005-01-01
abbr: "POP3"
fullName: "Post Office Protocol, version 3"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pop3/"
summary: "POP3 je internetový standardní protokol používaný e-mailovými klienty pro stahování zpráv z poštovního serveru. V 3GPP je odkazován pro podporu e-mailových služeb v raných mobilních datových službách,"
---

POP3 je internetový standardní protokol používaný e-mailovými klienty pro stahování zpráv z poštovního serveru, který umožňuje základní přístup k e-mailům přes mobilní sítě, jak je uvedeno v 3GPP pro rané mobilní datové služby.

## Popis

Post Office Protocol verze 3 (POP3) je aplikační internetový protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 1939) a odkazovaný ve specifikacích 3GPP pro podporu e-mailových služeb v mobilních sítích. Funguje na TCP portu 110 a používá jednoduchý model klient-server, kde se e-mailový klient (uživatelský agent na mobilním zařízení) připojuje k poštovnímu serveru za účelem stažení zpráv. Protokol pracuje prostřednictvím série textových příkazů a odpovědí; po autentizaci (obvykle pomocí příkazů USER a PASS) může klient vypisovat, stahovat a mazat zprávy ze serverové schránky. POP3 je primárně protokol typu „stáhnout a smazat“ nebo „stáhnout a ponechat“, což znamená, že zprávy jsou po stažení typicky odstraněny ze serveru, i když lze konfigurovat ponechání kopií. To je v kontrastu s pokročilejšími protokoly jako IMAP, které podporují správu schránky na straně serveru.

V rámci architektury 3GPP, zejména v raných vydáních jako [R99](/mobilnisite/slovnik/r99/), byl POP3 integrován jako součást přenosových služeb a teleslužeb pro zasílání zpráv. Síť poskytuje IP konektivitu (prostřednictvím [GPRS](/mobilnisite/slovnik/gprs/) nebo pozdějších paketově orientovaných jader), která umožňuje mobilní stanici navázat TCP spojení s externím poštovním serverem. Specifikace 3GPP, jako TS 22.945 a TS 23.140, definují požadavky a aspekty služeb pro zasílání zpráv, včetně podpory e-mailů prostřednictvím standardních internetových protokolů jako POP3. Samotný protokol není 3GPP modifikován, ale je využíván jako existující standard pro zajištění e-mailové funkčnosti, což zaručuje interoperabilitu se širší internetovou e-mailovou infrastrukturou.

Role POP3 v sítích 3GPP spočívá v usnadnění základního stahování e-mailů jako přidružené služby přes mobilní datová spojení. Funguje ve spojení s dalšími protokoly, jako je [SMTP](/mobilnisite/slovnik/smtp/) pro odesílání e-mailů, a poskytuje tak kompletní e-mailové řešení. Přestože je jednoduchý a široce podporovaný, jeho omezení – jako nedostatek synchronizace složek na straně serveru a omezená správa v offline režimu – vedla k adopci protokolu IMAP v pozdějších mobilních e-mailových řešeních. V kontextu 3GPP pomohlo odkazování na POP3 standardizovat způsob nabízení e-mailových služeb a zajistit, aby operátoři a výrobci zařízení mohli implementovat konzistentní schopnosti e-mailových klientů pro rané uživatele mobilního internetu.

## K čemu slouží

POP3 byl zahrnut do standardů 3GPP za účelem umožnění standardizovaného přístupu k e-mailům přes mobilní sítě, což reagovalo na rostoucí poptávku po datových službách nad rámec hlasu. Koncem 90. let a počátkem 21. století, kdy se mobilní sítě vyvíjely pro podporu paketově orientovaných dat (např. [GPRS](/mobilnisite/slovnik/gprs/) v 2.5G), vznikla potřeba definovat, jak mohou tradiční internetové aplikace jako e-mail fungovat na mobilních zařízeních. 3GPP odkazovalo na existující [IETF](/mobilnisite/slovnik/ietf/) protokoly, aby se předešlo zbytečnému vynalézání a zajistila kompatibilita s globálním internetovým e-mailovým systémem.

Protokol řešil problém stahování e-mailů ze vzdáleného serveru na mobilního klienta s omezeným úložištěm a přerušovanou konektivitou. Před rozšířením mobilních dat byl přístup k e-mailům z velké části omezen na stolní počítače s trvalým připojením. Jednoduchý, bezestavový design POP3 jej činil vhodným pro rané mobilní implementace, kde byla omezena šířka pásma a výpočetní výkon. Umožnil uživatelům stahovat zprávy do svého zařízení pro offline čtení, což bylo klíčové vzhledem k nespolehlivým a drahým mobilním připojením té doby.

Nicméně omezení POP3, jako neschopnost synchronizovat složky nebo spravovat zprávy na serveru, nakonec vedla k adopci pokročilejších protokolů jako IMAP v pozdějších mobilních e-mailových řešeních. Zařazení POP3 do specifikací 3GPP, jako [R99](/mobilnisite/slovnik/r99/), poskytlo základní standard pro mobilní e-mail, umožnilo interoperabilitu a vedlo vývoj raných mobilních e-mailových klientů a služeb.

## Klíčové vlastnosti

- Jednoduchý protokol klient-server pro stahování e-mailů
- Používá TCP port 110 pro spolehlivou komunikaci
- Podporuje autentizaci pomocí příkazů USER/PASS v čistém textu
- Umožňuje stahování a mazání zpráv ze serveru
- Lze nakonfigurovat pro ponechání kopií na serveru
- Funguje dle standardu IETF RFC 1939, což zajišťuje internetovou interoperabilitu

## Související pojmy

- [SMTP – Simple Message Transfer Protocol](/mobilnisite/slovnik/smtp/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [TCP/IP – Transmission Control Protocol / Internet Protocol](/mobilnisite/slovnik/tcp-ip/)

## Definující specifikace

- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition

---

📖 **Anglický originál a plná specifikace:** [POP3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/pop3/)
