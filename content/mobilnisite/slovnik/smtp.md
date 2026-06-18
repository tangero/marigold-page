---
slug: "smtp"
url: "/mobilnisite/slovnik/smtp/"
type: "slovnik"
title: "SMTP – Simple Message Transfer Protocol"
date: 2025-01-01
abbr: "SMTP"
fullName: "Simple Message Transfer Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/smtp/"
summary: "Adaptace protokolu Simple Mail Transfer Protocol od IETF definovaná organizací 3GPP, používaná pro přenos krátkých zpráv (SMS) přes IP sítě. Umožňuje propojení SMS mezi tradičními mobilními sítěmi s p"
---

SMTP je adaptace protokolu IETF definovaná organizací 3GPP, která slouží pro přenos SMS přes IP sítě za účelem umožnění propojení s elektronickou poštou a dalšími IP-based messaging systémy.

## Popis

Simple Message Transfer Protocol (SMTP) v kontextu 3GPP je specializovaný profil protokolu založený na standardu SMTP od Internet Engineering Task Force ([IETF](/mobilnisite/slovnik/ietf/)) ([RFC](/mobilnisite/slovnik/rfc/) 5321). Používá se jako transportní mechanismus pro zprávy služby Short Message Service ([SMS](/mobilnisite/slovnik/sms/)) v rámci architektur sítí založených na IP, jako jsou ty definované pro IP Multimedia Subsystem (IMS) nebo pro přímé propojení se službami internetové elektronické pošty. Protokol funguje mezi IP Short Message Gateway ([IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/)) nebo jiným SMS aplikačním serverem a externími entitami založenými na IP, jako jsou email servery. Když je třeba SMS zprávu doručit emailovému příjemci, entita sítě 3GPP (např. IP-SM-GW) zapouzdří SMS [TPDU](/mobilnisite/slovnik/tpdu/) (Transfer Protocol Data Unit, definované v TS 23.040) do zprávy SMTP. Obsah SMS je typicky umístěn do těla emailu, zatímco hlavičky SMTP a obálkové informace se používají pro směrování a označení zdroje/cíle. Specifikace 3GPP (např. TS 23.040 a TS 29.198) definují přesná mapovací pravidla, hlavičky content-type (často text/plain nebo application/vnd.3gpp.sms) a zpracování doručovacích hlášení. Pro zprávy pocházející z internetu (email) určené pro [MSISDN](/mobilnisite/slovnik/msisdn/) probíhá opačný proces: IP-SM-GW přijme SMTP email, extrahuje obsah, přeformátuje jej do standardního SMS TPDU a vloží jej do infrastruktury pro směrování SMS mobilní sítě (např. přes [MAP](/mobilnisite/slovnik/map/) do [SMSC](/mobilnisite/slovnik/smsc/)). Protokol podporuje klíčové funkce jako překlad adres odesílatele/příjemce (mezi MSISDN a emailovými adresami), specifikaci portu pro odesílání a základní mechanismy spolehlivosti vlastní protokolu SMTP.

## K čemu slouží

3GPP definovala svůj profil SMTP za účelem propojení světa mobilních SMS s všudypřítomným systémem internetové elektronické pošty, což byla potřeba, která vznikla s vývojem sítí směrem k all-IP architekturám. Původně byly SMS přenášeny přes signalizační kanály s přepojováním okruhů (jako SDCCH v GSM). Se zavedením jader s přepojováním paketů (GPRS, později EPS a IMS) byl zapotřebí způsob přenosu SMS přes IP pro zvýšení efektivity a umožnění nových služebních paradigmat. Přijetí SMTP vyřešilo problém propojení mezi doménou mobilního zasílání zpráv a doménou pevné internetové pošty. Umožnilo mobilním operátorům nabízet služby jako 'email to SMS' a 'SMS to email', čímž vytvořilo nové zdroje příjmů a zlepšilo dostupnost služeb. Jeho vznik byl motivován konvergencí komunikačních technologií na počátku roku 2000 (období Rel-4/5), kde se klíčovým konstrukčním principem stalo oddělení služební logiky od podkladového transportu. Použití dobře etablovaného a robustního protokolu jako SMTP poskytlo pro tuto bránovou funkci standardizovaný, spolehlivý a široce srozumitelný mechanismus, čímž se vyhnulo nutnosti vytvářet zcela nový IP messaging protokol a zajistila se interoperabilita s rozsáhlou stávající emailovou infrastrukturou.

## Klíčové vlastnosti

- Vychází z IETF SMTP (RFC 5321) pro spolehlivý přenos zpráv přes IP
- Definuje mapovací pravidla mezi formátem SMS TPDU a formátem SMTP emailu
- Používán síťovými elementy jako IP-SM-GW pro propojení SMS a emailu
- Podporuje scénáře SMS přes IP iniciované mobilním zařízením i jím přijímané
- Zpracovává překlad adres mezi MSISDN a emailovými adresami
- Specifikuje hlavičky content-type pro správnou identifikaci SMS obsahu v emailu

## Související pojmy

- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [SMTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/smtp/)
