---
slug: "tup"
url: "/mobilnisite/slovnik/tup/"
type: "slovnik"
title: "TUP – Telephone User Part"
date: 2025-01-01
abbr: "TUP"
fullName: "Telephone User Part"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tup/"
summary: "TUP je součástí signalizačního protokolu SS7, používaná pro navazování a ukončování hovorů v tradičních okruhově přepínaných telefonních sítích. Zajišťuje základní funkce řízení hovoru, jako je signal"
---

TUP je Telephone User Part (uživatelská telefonní část) signalizačního protokolu SS7, který zajišťuje základní navázání, ukončení a dohled spojů pro okruhově přepínanou hlasovou komunikaci mezi ústřednami.

## Popis

Telephone User Part (TUP) je klíčový protokol v rámci sady Signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), speciálně navržený pro řízení hovorů v okruhově přepínaných telefonních sítích. Funguje na aplikační vrstvě SS7 protokolového zásobníku a spolupracuje s Message Transfer Part ([MTP](/mobilnisite/slovnik/mtp/)) pro spolehlivé doručování zpráv. Primární funkcí TUP je zřizování, udržování a uvolňování hlasových okruhů mezi telefonními ústřednami výměnou standardizovaných signalizačních zpráv. Tyto zprávy zahrnují Initial Address Messages ([IAM](/mobilnisite/slovnik/iam/)) pro zahájení hovoru, Address Complete Messages ([ACM](/mobilnisite/slovnik/acm/)) pro indikaci vyzvánění volaného účastníka a Answer Messages ([ANM](/mobilnisite/slovnik/anm/)) pro potvrzení spojení hovoru, spolu se zprávami Release (REL) a Release Complete ([RLC](/mobilnisite/slovnik/rlc/)) pro ukončení hovoru.

Z architektonického hlediska je TUP implementován v telefonních ústřednách nebo přepínačích, například v Public Switched Telephone Network ([PSTN](/mobilnisite/slovnik/pstn/)) nebo v raných mobilních ústřednách ([MSC](/mobilnisite/slovnik/msc/)) v sítích GSM. Zajišťuje nezbytné úkony související s hovorem, jako je přenos čísel (pomocí en-bloc nebo překrývající se signalizace), dohled nad hovorem pro sledování stavu spojení a základní indikace účtování. TUP nativně nepodporuje pokročilé služby, jako je zobrazení čísla volajícího nebo přesměrování hovorů; ty byly později zavedeny v ISDN User Part (ISUP). Protokol využívá pro adresování v síti SS7 point codes a používá circuit identification codes (CIC) k asociaci signalizačních zpráv s konkrétními fyzickými nebo logickými okruhy spojovacích linek.

Během provozu TUP umožňuje koncové řízení hovoru výměnou zpráv po vyhrazených signalizačních spojích, odděleně od hlasových přenosových kanálů. Při zahájení hovoru vysílá výchozí ústředna IAM obsahující volané číslice a informace o okruhu. Následné ústředny toto využívají ke směrování hovoru a rezervaci okruhu, přičemž zprávy ACM a ANM spojení dokončí. TUP také řídí chybové stavy, například odesíláním neúspěšných zpětných zpráv pro navázání při neúspěšných hovorech. Jeho role byla klíčová při automatizaci telefonie, nahrazení starších metod přímé signalizace v pásmu (jako je pulzní volání) a položení základů pro vývoj digitálních sítí. Přestože byl v moderních sítích z velké části nahrazen protokolem ISUP, TUP zůstává relevantní v legacy systémech a některých regionech.

## K čemu slouží

TUP byl vytvořen, aby poskytl standardizovaný, spolehlivý signalizační protokol pro řízení hovorů v digitálních telefonních sítích a řešil omezení starších analogových signalizačních metod. Před SS7 a TUP se telefonie spoléhala na přímou signalizaci v pásmu, kde se řídicí tóny a pulzy přenášely stejným kanálem jako hlas, což vedlo k neefektivitě, zranitelnosti vůči podvodům (např. phreaking) a omezené funkčnosti. Přechod na signalizaci mimo pásmo pomocí SS7 oddělil řídicí a přenosovou cestu, což zlepšilo bezpečnost, rychlost a kapacitu sítě. TUP konkrétně řešil problém automatizace navazování a ukončování hovorů mezi ústřednami v národních a mezinárodních PSTN sítích, což umožnilo funkce jako přímé volání a kratší dobu spojení.

Historický kontext sahá do 70. a 80. let 20. století, kdy telekomunikační operátoři přecházeli na digitální přepínání a potřebovali robustní signalizační systém pro podporu rostoucího provozu. TUP jako součást SS7 standardizovaného ITU-T poskytl globálně interoperabilní rámec pro základní telefonní služby. Řešil klíčové problémy, jako je efektivní využití spojovacích linek přes přesný dohled nad hovory, zkrácení prodlevy po vytočení urychlením signalizace a podpora postupných síťových upgradů. Omezení TUP v oblasti zpracování datových služeb nebo pokročilých funkcí hovorů však motivovalo vývoj ISUP, který integroval možnosti ISDN. V rámci 3GPP je TUP zmiňován pro legacy propojení, zejména v raných vydáních GSM, kde mobilní sítě rozhraní s infrastrukturou PSTN.

## Klíčové vlastnosti

- Základní navazování a ukončování hovorů pomocí zpráv IAM, ACM, ANM, REL a RLC
- Podpora metod en-bloc a překrývající se signalizace pro přenos čísel
- Dohled nad hovorem pro sledování stavů spojení a detekci událostí jako odpověď/rozpojení
- Identifikace okruhu pomocí CIC pro asociaci signalizace s prostředky spojovacích linek
- Zpětné zprávy pro navázání pro zpracování neúspěšných pokusů o hovor (např. při zahlcení)
- Kompatibilita s SS7 MTP pro spolehlivé, sekvenované doručování zpráv po signalizačních spojích

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network

---

📖 **Anglický originál a plná specifikace:** [TUP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tup/)
