---
slug: "cts-fpe"
url: "/mobilnisite/slovnik/cts-fpe/"
type: "slovnik"
title: "CTS-FPE – CTS-Fixed Part Equipment"
date: 2025-01-01
abbr: "CTS-FPE"
fullName: "CTS-Fixed Part Equipment"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cts-fpe/"
summary: "CTS-FPE je pevná infrastrukturní část systému bezšňůrové telefonie (Cordless Telephony System, CTS), jak je definováno v 3GPP TS 43.020. Zajišťuje rádiové rozhraní a síťovou konektivitu pro bezšňůrové"
---

CTS-FPE je pevná infrastrukturní část systému bezšňůrové telefonie (Cordless Telephony System), která zajišťuje rádiové rozhraní a síťovou konektivitu pro bezšňůrové telefonní přístroje v omezené lokální oblasti.

## Popis

CTS-Fixed Part Equipment (CTS-FPE) je základní síťový prvek specifikovaný 3GPP pro systémy bezšňůrové telefonie (Cordless Telephony Systems, [CTS](/mobilnisite/slovnik/cts/)). Funguje jako základnová stanice nebo přístupový bod v CTS nasazení a tvoří pevnou část systémové architektury. FPE navazuje a udržuje rádiové spojení s přenosnými částmi systému bezšňůrové telefonie (CTS-PPs), což jsou uživatelské bezšňůrové přístroje. Operuje ve vyhrazených kmitočtových pásmech a používá definované rádiové protokoly pro správu hovorů, zvládání mobility ve své pokryté oblasti (typicky jedné budově) a připojení k širší veřejné telefonní síti ([PSTN](/mobilnisite/slovnik/pstn/)) nebo privátní ústředně ([PBX](/mobilnisite/slovnik/pbx/)).

Architektura CTS je relativně jednoduchá a je soustředěna kolem FPE. FPE obsahuje rádiový transceiver, řídicí logiku pro sestavování a ukončování hovorů a rozhraní k pevné síti (např. analogová telefonní linka nebo digitální linka [ISDN](/mobilnisite/slovnik/isdn/)/PBX). Spravuje malou skupinu přenosných částí (Portable Parts), provádí jejich autentizaci a poskytuje základní funkce mobility, jako je registrace a předávání spojení (handover) v rámci vlastní buňky. FPE implementuje specifikované protokoly rozhraní pro CTS, které zahrnují modulaci fyzické vrstvy, rámování s časovým duplexem ([TDD](/mobilnisite/slovnik/tdd/)) a procedury linkové vrstvy pro spolehlivý přenos.

Klíčové vnitřní komponenty CTS-FPE zahrnují rádiovou frekvenční ([RF](/mobilnisite/slovnik/rf/)) jednotku, jednotku základního pásma (baseband), řídicí procesor a síťovou rozhranovou jednotku. RF jednotka zajišťuje vysílání a příjem v kmitočtových pásmech CTS. Jednotka základního pásma provádí modulaci/demodulaci, kanálové kódování a sestavuje/rozebírá TDD rámce. Řídicí procesor provádí CTS protokolový zásobník, spravuje řízení hovorů, správu mobility a rozhraní s přenosnou částí (Portable Part). Síťová rozhranová jednotka převádí interní signalizaci hovorů a hlasová data do formátu vyžadovaného externí pevnou linkou (např. analogová signalizace loop start nebo digitální [PCM](/mobilnisite/slovnik/pcm/)).

V celkovém síťovém ekosystému měla CTS-FPE roli mostu mezi bezdrátovými bezšňůrovými přístroji a tradiční telefonní sítí. Umožňovala uživatelům uskutečňovat a přijímat PSTN hovory bez nutnosti být připojen k zásuvce, což poskytovalo pohodlí v definovaném domácím nebo firemním prostředí. FPE byla zodpovědná za správu všech rádiových prostředků pro připojené přístroje, včetně přidělování kanálů, řízení výkonu a udržování kvality aktivních hlasových spojení.

## K čemu slouží

CTS-FPE bylo vytvořeno za účelem standardizace pevné infrastruktury pro systémy digitální bezšňůrové telefonie, což mělo umožnit interoperabilitu mezi zařízeními od různých výrobců. Před standardizací 3GPP dominovaly na trhu proprietární systémy bezšňůrových telefonů, které uzamykaly zákazníky do ekosystému jediného dodavatele pro přístroje i základnové stanice. Specifikace [CTS](/mobilnisite/slovnik/cts/), včetně FPE, si kladly za cíl tento problém vyřešit definováním společného rádiového rozhraní a síťové architektury, což mělo podpořit konkurenci a možnost volby pro zákazníky.

Technologie reagovala na rostoucí poptávku po pohodlné bezdrátové telefonii v budovách na konci 90. let a počátku 21. století. Poskytovala digitální náhradu za starší analogové bezšňůrové telefony s lepší kvalitou hlasu, vyšší bezpečností díky šifrování a zvýšenou spektrální účinností. FPE bylo kotvou, která toto umožňovala, poskytujíc standardizovanou bránu mezi novými digitálními bezšňůrovými přístroji a všudypřítomnou analogovou telefonní linkou.

Vytvoření CTS-FPE bylo motivováno úspěchem dřívějších standardů digitální bezšňůrové telefonie, jako byl DECT (Digital Enhanced Cordless Telecommunications) v Evropě. Práce 3GPP v TS 43.020 měla za cíl poskytnout globálně použitelný rámec, který často vycházel z principů DECT nebo je přizpůsoboval pro širší použití. Vyřešila omezení proprietárních systémů tím, že zajistila, aby CTS-PP od jednoho výrobce mohlo bezproblémově fungovat s CTS-FPE od jiného, což byl významný krok vpřed pro spotřebitelský trh i pro firemní nasazení vyžadující řešení od více dodavatelů.

## Klíčové vlastnosti

- Poskytuje rádiový přístupový bod pro přenosné části systému bezšňůrové telefonie (CTS-PP)
- Implementuje standardizované CTS rádiové rozhraní pro sestavení hovoru a přenos hlasu
- Propojuje bezšňůrové přístroje s veřejnou telefonní sítí (PSTN) nebo s PBX
- Spravuje základní funkce mobility, jako je registrace přístroje a předání spojení uvnitř buňky
- Provádí autentizaci a šifrování pro zabezpečení hlasové komunikace
- Operuje ve vyhrazených kmitočtových pásmech s využitím technologie časového duplexu (TDD)

## Související pojmy

- [DECT – Digital Enhanced Cordless Telecommunications](/mobilnisite/slovnik/dect/)

## Definující specifikace

- **TS 43.020** (Rel-19) — Security Procedures for GSM

---

📖 **Anglický originál a plná specifikace:** [CTS-FPE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cts-fpe/)
