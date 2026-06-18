---
slug: "tpkt"
url: "/mobilnisite/slovnik/tpkt/"
type: "slovnik"
title: "TPKT – Transport Packet"
date: 2025-01-01
abbr: "TPKT"
fullName: "Transport Packet"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tpkt/"
summary: "Standardizovaný formát paketu definovaný v 3GPP pro zabezpečený přenos informací souvisejících se zákonným odposlechem (LI), jako je odposlechnutý obsah nebo informace související s odposlechem, z fun"
---

TPKT je standardizovaný 3GPP formát paketu pro zabezpečený přenos dat zákonného odposlechu z odposlechové funkce k orgánu činnému v trestním řízení.

## Popis

Transportní paket (TPKT) je klíčová protokolová datová jednotka v architektuře zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) podle 3GPP, specifikovaná především v TS 33.108. Definuje standardizovaný kontejnerový formát pro zapouzdření a přenos odposlechnutého komunikačního obsahu ([CC](/mobilnisite/slovnik/cc/)) a informací souvisejících s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) přes rozhraní předání ([HI](/mobilnisite/slovnik/hi/)). Struktura TPKT je navržena tak, aby byla nezávislá na podkladovém síťovém transportním protokolu (např. [TCP/IP](/mobilnisite/slovnik/tcp-ip/), [UDP](/mobilnisite/slovnik/udp/) nebo jiném, jak se dohodnou operátoři a orgány činné v trestním řízení), a poskytuje konzistentní mechanismus rámcování na aplikační vrstvě. TPKT se skládá z přesně definované hlavičky a sekce s datovou částí. Hlavička obsahuje pole jako délka paketu, verze a pořadová čísla, která usnadňují vymezení hranic paketů, jejich opětovné složení a kontrolu integrity na přijímací straně.

Provozně TPKT generuje zprostředkovací funkce ([MF](/mobilnisite/slovnik/mf/)) nebo administrační funkce ([ADMF](/mobilnisite/slovnik/admf/)) v doméně síťového operátora. Když mají být odposlouchávány komunikace cílového účastníka, síťové elementy (jako GMLC, MSC nebo PGW) doručí surová odposlechová data do MF. MF poté tato data – která mohou být hlasové pakety, SMS, paketová data nebo přidružená metadata, jako jsou podrobnosti o volání – naformátuje do struktur TPKT. Datová část každého TPKT obsahuje konkrétní typ odposlechnuté informace a pro streamování průběžné odposlechové relace může být použito více TPKT. Pakety jsou poté zabezpečeně přenášeny přes HI k monitorovacímu zařízení orgánu činného v trestním řízení (LEMF). V LEMF jsou TPKT dekapulovány a jejich datová část je zpracována a předložena oprávněnému personálu.

Architektura TPKT zajišťuje několik klíčových požadavků pro zákonný odposlech: spolehlivost, zachování pořadí a podporu multiplexování různých odposlechových úloh. Pole délky paketu umožňuje přijímačům správně identifikovat hranice paketů i při použití proudově orientovaného transportu, jako je TCP. Pořadová čísla pomáhají detekovat ztrátu nebo přehození paketů, což je klíčové pro zachování chronologické věrnosti odposlechnutých komunikací. Dále může formát TPKT pojmout různá kódovací schémata pro datovou část (např. ASN.1 kódování pro IRI), jak je definováno ve standardech 3GPP. Jeho úlohou je sloužit jako společný lingua franca pro výměnu odposlechových dat, která abstrahuje složitosti různých síťových technologií (2G, 3G, 4G, 5G) a typů služeb do jednotného transportního mechanismu splňujícího regulatorní povinnosti.

## K čemu slouží

TPKT byl vytvořen, aby vyřešil problém heterogenních a nestandardizovaných formátů pro doručování dat v raných implementacích zákonného odposlechu. Před jeho standardizací používali různí výrobci síťových zařízení a operátoři proprietární formáty pro doručování odposlechnutých informací orgánům činným v trestním řízení (LEA). Tento nedostatek interoperability vytvářel pro LEA významné výzvy, protože musely spravovat více nekompatibilních přijímacích systémů, což zvyšovalo náklady a složitost. Hlavní motivací pro definici TPKT v 3GPP bylo vytvoření jediného, standardizovaného formátu paketu, který by mohl být používán globálně, a zajištění, aby odposlechová data z jakékoli kompatibilní sítě mohla být přijata a zpracována jakýmkoli standardizovaným LEMF.

Jeho zavedení v Release 15 bylo součástí širšího úsilí o zdokonalení a přípravu architektury LI na budoucí vývoj pro vyvíjející se síťové technologie, včetně 5G. TPKT řeší potřebu zabezpečeného, spolehlivého a efektivního transportního mechanismu, který garantuje integritu a důvěrnost citlivých odposlechnutých dat při jejich přenosu z domény operátora k zákonné autoritě. Poskytuje také rámec pro zpracování vysokokapacitních, reálných toků odposlechových dat spojených s moderními vysokorychlostními službami. Definováním jasné struktury paketu zjednodušuje vývoj zprostředkovacích a monitorovacích systémů, snižuje chyby v interpretaci dat a zajišťuje, že procesy zákonného odposlechu dodržují právní požadavky na autenticitu dat a možnost auditu.

## Klíčové vlastnosti

- Standardizovaný formát paketu pro přenos dat zákonného odposlechu
- Obsahuje hlavičku s poli délky, verze a pořadového čísla
- Zapouzdřuje jak informace související s odposlechem (IRI), tak komunikační obsah (CC)
- Nezávislý design na transportu, použitelný přes TCP, UDP nebo jiné protokoly
- Podporuje multiplexování více odposlechových relací
- Zajišťuje integritu dat a zachování pořadí pro účely auditní stopy

## Související pojmy

- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)
- [LEMF – Law Enforcement Monitoring Facility](/mobilnisite/slovnik/lemf/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [TPKT na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpkt/)
