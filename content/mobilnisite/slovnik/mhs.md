---
slug: "mhs"
url: "/mobilnisite/slovnik/mhs/"
type: "slovnik"
title: "MHS – Message Handling System"
date: 2025-01-01
abbr: "MHS"
fullName: "Message Handling System"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mhs/"
summary: "MHS je rámec služby zasílání zpráv typu store-and-forward definovaný v raných vydáních 3GPP, založený na standardech ITU-T X.400. Poskytuje standardizovanou architekturu pro elektronickou poštu a výmě"
---

MHS je rámec služby zasílání zpráv typu store-and-forward založený na standardech ITU-T X.400, který poskytuje standardizovanou architekturu pro elektronickou poštu a výměnu zpráv v raných vydáních 3GPP.

## Popis

Message Handling System (MHS) v 3GPP je adaptací doporučení řady [ITU-T](/mobilnisite/slovnik/itu-t/) X.400 pro systémy pro zpracování zpráv. Definuje komplexní architektonický rámec pro elektronické zasílání zpráv, který podporuje doručování zpráv typu store-and-forward mezi uživateli, známými jako Message Transfer Agents ([MTA](/mobilnisite/slovnik/mta/)). Systém se skládá z několika klíčových funkčních komponent. User Agent (UA) slouží jako rozhraní pro koncového uživatele nebo aplikaci k přípravě, odeslání a přijetí zpráv. Message Transfer Agent (MTA) je zodpovědný za směrování, přeposílání a doručování zpráv systémem a tvoří Message Transfer System ([MTS](/mobilnisite/slovnik/mts/)). Message Store ([MS](/mobilnisite/slovnik/ms/)) poskytuje volitelnou úschovu zpráv jménem UA.

Provoz v rámci MHS začíná, když odesílající UA předá zprávu svému lokálnímu MTA. Zpráva se skládá z obálky (obsahující směrovací informace, jako jsou adresy odesílatele a příjemce) a obsahu (samotná data zprávy). MTA analyzuje adresu příjemce, která odpovídá formátu adresy X.400 Originator/Recipient (O/R). Pomocí směrovacích tabulek a adresářových služeb MTA určí další směrovací krok – buď cílové MTA přímo obsluhující příjemce, nebo mezilehlé MTA. Zpráva je pak přenášena metodou store-and-forward sítí MTA, dokud nedosáhne cílového MTA.

Po příchodu k cílovému MTA je zpráva doručena příjemcově UA. Pokud UA není dostupné, může být zpráva umístěna do Message Store pro pozdější vyzvednutí nebo je s ní nakládáno podle pravidel doručování. MHS podporuje různé typy obsahu a služby interpersonálního zasílání zpráv, ale jeho hlavní předností je poskytování spolehlivého, standardizovaného transportního mechanismu pro asynchronní komunikaci. V kontextu 3GPP specifikace MHS (především 21.905, slovník) zajišťují společnou terminologii pro koncepty související se zasíláním zpráv napříč ostatními technickými specifikacemi, což usnadňuje interoperabilitu tam, kde jsou služby zasílání zpráv odkazovány nebo vyžadovány jako součást větších systémových architektur, například pro administrativní komunikaci nebo komunikaci správy služeb.

## K čemu slouží

MHS byl do 3GPP začleněn od jeho raných vydání, aby poskytl standardizovaný, robustní základ pro služby elektronického zasílání zpráv v rámci telekomunikačního ekosystému. Před všudypřítomným internetovým e-mailem (SMTP/POP3/IMAP) byl MHS založený na X.400 hlavním mezinárodním standardem pro podnikové a operátorské zasílání zpráv, který nabízel funkce jako garantované doručení, nepopiratelnost a bezpečnostní služby, jež byly komplexnější než u raného internetového mailu.

Jeho začlenění do 3GPP sloužilo několika účelům. Za prvé poskytoval dobře definovaný architektonický model a terminologii pro jakékoli funkce zasílání zpráv vyžadované v samotných systémech 3GPP, například pro výměnu administrativních zpráv mezi systémy správy sítě nebo pro některé přidané služby. Za druhé zajišťoval, že pokud se operátoři rozhodli implementovat služby zasílání zpráv, měli k dispozici standardizovanou, interoperabilní šablonu, která podporovala konzistenci napříč různými sítěmi a dodavateli.

Zatímco praktická implementace plnohodnotného X.400 MHS mobilními operátory pro spotřebitelský e-mail byla z velké části nahrazena internetovými e-mailovými protokoly, konceptuální model a slovník v normách přetrvaly. Představuje důležitý historický kontext pro telekomunikační zasílání zpráv, ilustrující přechod od tradičních telekomunikačních architektur služeb k službám založeným na IP. Jeho dlouhodobá přítomnost napříč četnými vydáními 3GPP zdůrazňuje jeho roli stabilního referenčního modelu v rámci standardizačního slovníku.

## Klíčové vlastnosti

- Založeno na architektuře zasílání zpráv typu store-and-forward dle ITU-T X.400
- Definuje funkční komponenty: User Agent (UA), Message Transfer Agent (MTA), Message Store (MS)
- Používá standardizované adresy X.400 O/R pro směrování
- Podporuje spolehlivé, asynchronní doručování zpráv
- Poskytuje společný slovník a referenční model pro zasílání zpráv v 3GPP
- Umožňuje propojení mezi různými administrativními doménami zasílání zpráv

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MHS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mhs/)
