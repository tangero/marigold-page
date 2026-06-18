---
slug: "pgw-cdr"
url: "/mobilnisite/slovnik/pgw-cdr/"
type: "slovnik"
title: "PGW-CDR – P-GW (enhanced by FBC) generated – Charging Data Record"
date: 2025-01-01
abbr: "PGW-CDR"
fullName: "P-GW (enhanced by FBC) generated – Charging Data Record"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pgw-cdr/"
summary: "Záznam o účtování dat (Charging Data Record) generovaný bránou P-GW (Packet Data Network Gateway) rozšířenou o funkce účtování na základě toku (Flow-Based Charging, FBC). Obsahuje podrobné informace o"
---

PGW-CDR je záznam o účtování dat (Charging Data Record) generovaný bránou paketové datové sítě (Packet Data Network Gateway) s podporou účtování na základě toku (Flow-Based Charging), který obsahuje podrobné informace o datové relaci uživatele pro účely offline účtování a účetnictví.

## Popis

PGW-CDR ([P-GW](/mobilnisite/slovnik/p-gw/) generated Charging Data Record) je standardizovaná datová struktura definovaná organizací 3GPP, která obsahuje podrobné účetní informace o relaci připojení uživatele k paketové datové síti (Packet Data Network, [PDN](/mobilnisite/slovnik/pdn/)). Generuje ji brána P-GW (Packet Data Network Gateway) v architektuře Evolved Packet Core (EPC) a je specificky spojena s funkcí této brány pro účtování na základě toku (Flow-Based Charging, [FBC](/mobilnisite/slovnik/fbc/)). Tento [CDR](/mobilnisite/slovnik/cdr/) je primárním výstupem pro systémy offline účtování a poskytuje surová data, která doména fakturace operátora využívá pro výpočet poplatků za využití služeb účastníkem.

Architektura generování CDR zahrnuje několik síťových funkcí. P-GW, která vystupuje jako funkce spouštění účtování (Charging Trigger Function, [CTF](/mobilnisite/slovnik/ctf/)), monitoruje datové relace uživatele na základě předdefinovaných datových toků služeb (service data flows) a účtovacích pravidel poskytnutých funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)). Když nastanou specifické účtovací události (např. začátek relace, konec relace, dosažení limitu objemu dat, dosažení časového limitu), P-GW shromáždí relevantní informace a sestaví je do PGW-CDR. Tento záznam je následně přenesen přes rozhraní Gz k funkci Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)), která je součástí Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)). CDF může pro jednu relaci shromáždit více dílčích CDR, než předá konsolidovaný Charging Data Record (CDR) funkci Charging Gateway Function (CGF) a nakonec doméně fakturace (Billing Domain).

PGW-CDR obsahuje komplexní sadu polí specifikovanou v dokumentu 3GPP TS 32.251. Mezi klíčové informace patří IMSI (International Mobile Subscriber Identity) a MSISDN (Mobile Subscriber ISDN Number) uživatele, identifikátor PDN připojení, použitý Access Point Name (APN), přidělená IP adresa(ady), časy začátku a konce relace a příčina ukončení. Zásadní pro účtování na základě toku je, že záznam obsahuje počty objemu dat (vzestupný a sestupný směr) pro každý datový tok služby (service data flow) nebo ratingovou skupinu. Dále zaznamenává parametry QoS spojené s relací, jako je QoS Class Identifier (QCI) a Allocation/Retention Priority (ARP), stejně jako lokalizační informace, například identitu Serving Network a User Location Info.

Proces generování CDR je úzce integrován se zpracováním provozu v P-GW. Když pakety patřící k datovému toku služby procházejí bránou, jsou započítávány vůči příslušným prahovým hodnotám objemu. P-GW aplikuje účtovací pravidla, která určují, kdy generovat průběžný nebo konečný CDR. Například pravidlo může spustit generování průběžného CDR po každé spotřebované 1 GB dat nebo každou hodinu. Toto podrobné, na toku založené účtování umožňuje sofistikované fakturační modely přesahující jednoduché ceny za megabajt, jako je nulové účtování (zero-rating) pro konkrétní aplikace, datové tarify s různými úrovněmi nebo sponzorované datové služby. PGW-CDR poskytuje ověřitelnou stopu o využití, která je nezbytná pro implementaci těchto komerčních politik.

## K čemu slouží

PGW-CDR existuje za účelem poskytnutí standardizovaného, podrobného a spolehlivého mechanismu pro účtování využití služeb účastníky v mobilních paketových sítích. Před formalizací účtování na základě toku (Flow-Based Charging, FBC) ve verzi 3GPP Release 7 bylo účtování často založeno na jednodušších, méně podrobných metodách, které neumožňovaly podporu komplexních služeb. Exploze mobilních datových služeb a potřeba diferencovaných cenových modelů (např. různé účtování za sociální sítě, streamování videa a cloudové úložiště) vytvořila poptávku po sofistikovanějším účtování.

Zavedení architektury Policy and Charging Control (PCC), která zahrnuje FBC, bylo řešením. Umožnilo operátorům definovat účtovací pravidla na základě konkrétního datového toku služby (např. veškerý provoz na video server) namísto pouhého celkového PDN připojení. PGW-CDR je výstupem tohoto systému. Řeší problém, jak přesně zaznamenat a nahlásit tyto podrobné informace o využití fakturačnímu systému. Bez takto detailního CDR by operátoři nemohli účtovat za rozmanité "na službu citlivé" tarify, které jsou dnes běžné.

Historicky byl jeho vznik motivován potřebou překročit časové nebo paušální datové účtování. Umožnil monetizaci mobilního internetu tím, že operátorům dovolil vytvářet atraktivní, na službu specifické datové balíčky a partnerství s poskytovateli obsahu (např. "datový objem při streamování videa se nepočítá do vašeho limitu"). PGW-CDR poskytuje technický základ pro tyto obchodní modely tím, že zachycuje přesně to, jaká služba byla použita, kolik dat bylo přeneseno a s jakou kvalitou služby (QoS), čímž řeší omezení předchozích záznamů o účtování dat nezávislých na toku, kterým chyběly podrobnosti potřebné pro moderní diferenciaci služeb.

## Klíčové vlastnosti

- Účtování na základě toku: Zaznamenává objem dat (vzestupný/sestupný směr) pro každý datový tok služby (service data flow) nebo ratingovou skupinu, což umožňuje účtování specifické pro danou službu.
- Komplexní data o relaci: Zahrnuje identifikátory účastníka (IMSI, MSISDN), časová razítka relace, APN, IP adresu a příčinu ukončení.
- Zachycení informací o QoS: Eviduje QoS Class Identifier (QCI) a Allocation/Retention Priority (ARP) aplikované během relace.
- Hlášení polohy: Může obsahovat User Location Information a identitu Serving Network pro účtování založené na poloze.
- Generování spouštěné událostmi: CDR jsou generovány na základě spouštěčů, jako je začátek/konec relace, dosažení objemových limitů, časových limitů a změna QoS.
- Standardizovaný formát: Definován v dokumentu 3GPP TS 32.251, což zajišťuje interoperabilitu mezi síťovými prvky a fakturačními systémy od různých dodavatelů.

## Související pojmy

- [P-GW – Packet Data Network Gateway](/mobilnisite/slovnik/p-gw/)

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management

---

📖 **Anglický originál a plná specifikace:** [PGW-CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pgw-cdr/)
