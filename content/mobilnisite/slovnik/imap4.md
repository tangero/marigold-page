---
slug: "imap4"
url: "/mobilnisite/slovnik/imap4/"
type: "slovnik"
title: "IMAP4 – Internet Message Access Protocol, version 4"
date: 2005-01-01
abbr: "IMAP4"
fullName: "Internet Message Access Protocol, version 4"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imap4/"
summary: "IMAP4 je standardizovaný protokol pro přístup k e-mailovým zprávám a jejich správu na vzdáleném poštovním serveru. Umožňuje uživatelům prohlížet, organizovat a manipulovat se zprávami bez jejich staže"
---

IMAP4 je standardizovaný protokol pro přístup k e-mailům a správu e-mailů na vzdáleném serveru, který uživatelům umožňuje prohlížet a organizovat zprávy bez jejich stažení, což usnadnilo mobilní e-mailové služby ve standardech 3GPP.

## Popis

Internet Message Access Protocol verze 4 (IMAP4) je protokol aplikační vrstvy definovaný Internet Engineering Task Force ([IETF](/mobilnisite/slovnik/ietf/)) a začleněný do specifikací 3GPP pro umožnění e-mailových služeb v mobilních sítích. Na rozdíl od jednodušších protokolů, jako je [POP3](/mobilnisite/slovnik/pop3/), umožňuje IMAP4 klientovi přistupovat k e-mailovým zprávám uloženým na serveru a manipulovat s nimi, jako by byly lokální. Protokol funguje přes trvalé TCP spojení, kde klient odesílá příkazy a server odpovídá daty a stavovými informacemi. Toto spojení zůstává otevřeno po celou dobu relace, což umožňuje synchronizaci změn stavu poštovní schránky mezi klientem a serverem v reálném čase.

Architektura IMAP4 je založena na modelu klient-server, přičemž klient (typicky e-mailová aplikace mobilního zařízení) zahájí relaci autentizací u serveru. Server hostuje poštovní schránku uživatele, která obsahuje zprávy organizované do hierarchie složek. Mezi klíčové operace patří výpis složek, načítání hlaviček nebo těl zpráv, vyhledávání zpráv podle kritérií, označování zpráv (např. jako přečtené, označené nebo smazané) a přesun zpráv mezi složkami. Všechny tyto operace se provádějí na serveru a klient přijímá aktualizovaný pohled. Tento model je zvláště výhodný pro mobilní zařízení s omezenou kapacitou úložiště, protože umožňuje uživatelům procházet velké poštovní schránky bez stažení veškerého obsahu.

V kontextu 3GPP je IMAP4 uvedeno v servisních specifikacích (např. TS 22.945, TS 23.140) jako součást rámce pro internetové zasílání zpráv. Nejde o protokol vynalezený 3GPP, ale o přijatý standard IETF pro zajištění interoperability mezi platformami služeb mobilních sítí a e-mailovými servery. Protokol podporuje více souběžných připojení ke stejné poštovní schránce, což umožňuje různým klientům (např. telefonu a notebooku) přistupovat ke stejným zprávám. Používají se také bezpečnostní rozšíření, jako je IMAP přes [SSL](/mobilnisite/slovnik/ssl/)/[TLS](/mobilnisite/slovnik/tls/), pro ochranu autentizace a přenosu dat. Jeho úloha v 3GPP spočívá v poskytnutí standardizované metody pro interakci mobilních e-mailových klientů s firemními nebo internetovými e-mailovými službami, čímž tvoří součást širší nabídky služeb zasílání zpráv a dat.

## K čemu slouží

IMAP4 byl vytvořen, aby řešil omezení dřívějších protokolů pro přístup k e-mailům, především [POP3](/mobilnisite/slovnik/pop3/), který byl navržen pro stažení zpráv na lokálního klienta a jejich následné smazání ze serveru. POP3 nepodporoval správu složek na straně serveru, což vedlo k fragmentaci zpráv mezi klienty a ztěžovalo přístup ke stejné poštovní schránce z více zařízení. Potřeba protokolu, který by uživatelům umožňoval spravovat e-maily centrálně na serveru s konzistentním stavem napříč různými přístupovými body, vedla k vývoji IMAP. To bylo obzvláště důležité pro podnikové uživatele a uživatele s více počítači.

V mobilním kontextu začlenilo 3GPP IMAP4 do svých standardů od Release 99, aby poskytlo dobře definovaný protokol pro e-mailové služby jako součást nabídky paketově přepínaných dat. Mobilní zařízení mají často omezené úložiště a přerušované připojení. Schopnost IMAP4 umožnit uživatelům procházet hlavičky a selektivně stahovat zprávy šetří paměť zařízení a šířku pásma. Navíc jeho podpora offline provozu (kde se změny ukládají do mezipaměti a synchronizují po opětovném připojení) vyhovuje mobilním vzorcům použití s kolísáním sítě. Standardizací na IMAP4 zajistilo 3GPP, že operátoři mobilních sítí a výrobci zařízení mohou implementovat interoperabilní e-mailové klienty, které fungují s existující internetovou e-mailovou infrastrukturou, což usnadnilo přijetí mobilního e-mailu jako základní služby.

## Klíčové vlastnosti

- Ukládání a správa zpráv na straně serveru
- Podpora hierarchických složek na serveru
- Selektivní načítání zpráv (hlavičky, těla, přílohy)
- Příkazy pro vyhledávání a filtrování zpráv na serveru
- Podpora více souběžných připojení klientů ke stejné poštovní schránce
- Offline provoz se synchronizací po opětovném připojení

## Související pojmy

- [POP3 – Post Office Protocol, version 3](/mobilnisite/slovnik/pop3/)
- [SMTP – Simple Message Transfer Protocol](/mobilnisite/slovnik/smtp/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition

---

📖 **Anglický originál a plná specifikace:** [IMAP4 na 3GPP Explorer](https://3gpp-explorer.com/glossary/imap4/)
