---
slug: "asc"
url: "/mobilnisite/slovnik/asc/"
type: "slovnik"
title: "ASC – Access Service Class"
date: 2025-01-01
abbr: "ASC"
fullName: "Access Service Class"
category: "QoS"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/asc/"
summary: "Access Service Class (ASC) je parametr QoS v UMTS, který stanovuje prioritu pokusů o náhodný přístup z UE k NodeB. Mapuje logické kanály na konkrétní třídy přístupové služby, spravuje kolize a zajišťu"
---

ASC je parametr QoS v UMTS, který stanovuje prioritu pokusů o náhodný přístup ze strany UE tím, že mapuje logické kanály na konkrétní třídy a spravuje kolize, aby zajistil, že kritické služby získají přístup k síti s vyšší prioritou.

## Popis

Access Service Class (ASC) je základní mechanismus kvality služeb (QoS) v rádiové přístupové síti UMTS (UTRAN), který konkrétně řídí počáteční přístupový postup uživatelského zařízení (UE) na náhodném přístupovém kanálu (RACH). Funguje tak, že klasifikuje různé typy provozu z logických kanálů (např. z [CCCH](/mobilnisite/slovnik/ccch/), [DCCH](/mobilnisite/slovnik/dcch/) nebo [DTCH](/mobilnisite/slovnik/dtch/)) do odlišných úrovní priority. Každému ASC je přiřazena sada parametrů pro přenos na RACH, včetně podmnožiny dostupných předpovědních signatur a hodnoty persistence (Pi). Hodnota persistence určuje pravděpodobnost, s jakou smí UE odeslat přístupový předpověd v daném přístupovém slotu, čímž implementuje řízený pravděpodobnostní mechanismus backoff pro správu zatížení a kolizí na RACH.

Z architektonického hlediska je konfigurace ASC stanovena vrstvou řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) v řadiči rádiové sítě (RNC) a je komunikována k UE prostřednictvím systémových informačních bloků (SIB) vysílaných na [BCCH](/mobilnisite/slovnik/bcch/) nebo pomocí vyhrazené signalizace RRC. Vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) v UE je zodpovědná za provedení postupu založeného na ASC. Když má MAC data k odeslání a potřebuje navázat spojení, vybere příslušný ASC na základě priority logického kanálu čekajících dat. Poté použije přidruženou podmnožinu předpovědních signatur a aplikuje test persistence – vygeneruje náhodné číslo a porovná jej s hodnotou persistence – aby určil, zda je pokus o přenos v aktuálním přístupovém slotu povolen.

Tento mechanismus je klíčový pro diferencovanou QoS na společném uplink kanálu. Služby s vysokou prioritou, jako jsou tísňová volání nebo signalizace pro předání spojení, jsou mapovány na ASC s vysokou hodnotou persistence (např. Pi=1), což jim poskytuje okamžité nebo téměř okamžité povolení k pokusu o přístup. Provoz s nižší prioritou (např. na pozadí) je mapován na ASC s nižší hodnotou persistence, což nutí UE v průměru čekat přes více přístupových slotů, a tím snižuje kolize a chrání latenci a úspěšnost přístupu kritických služeb. Rámec ASC tedy poskytuje základní řízení přetížení pro počáteční uplink přístup v UMTS, které zohledňuje třídy provozu.

## K čemu slouží

ASC byl zaveden ve 3GPP Release 99, aby řešil zásadní výzvu spojenou se správou kolizí a poskytováním diferenciace služeb na sdíleném, kolizním náhodném přístupovém kanálu v sítích WCDMA/UMTS. Předchozí systémy postrádaly standardizovaný, podrobný mechanismus pro stanovení priority počátečních přístupových pokusů. Bez ASC by všechna UE soutěžila o RACH se stejnou prioritou, což by vedlo k situacím, kdy nárůst provozu na pozadí (např. registrace zařízení, data s nízkou prioritou) mohl způsobit nadměrné kolize a zpoždění, a tím zablokovat časově kritické přístupové pokusy pro tísňové služby nebo signalizaci s vysokou prioritou. To bylo pro systém navržený pro přenos mixu hlasových, datových a služeb v reálném čase nepřijatelné.

Vytvoření ASC bylo motivováno potřebou implementovat klíčový aspekt architektury QoS v UMTS – diferenciaci tříd provozu – přímo v místě vstupu do sítě. Řeší problém nekontrolovaných kolizí tím, že poskytuje síťově řízené parametry, které statisticky stanovují prioritu přístupu. RNC může konfigurovat hodnoty persistence a sady signatur pro každý ASC na základě zatížení sítě a provozních politik, což operátorům umožňuje zajistit, aby rádiová přístupová síť respektovala požadavky na QoS od konce ke konci definované pro různé aplikace, a to již od úplně prvního přenosového pokusu ze strany UE.

## Klíčové vlastnosti

- Mapuje priority logických kanálů na specifické parametry přístupu k RACH
- Využívá pravděpodobnost persistence (Pi) pro řízený backoff a správu zatížení
- Přiřazuje vyhrazené podmnožiny předpovědních signatur různým třídám služeb
- Konfigurován dynamicky RNC prostřednictvím vysílání nebo vyhrazené signalizace
- Umožňuje stanovení priority kritického přístupu (např. tísňová volání, signalizace pro předání spojení)
- Poskytuje základní diferenciaci QoS pro kolizní uplink přístup

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.303** (Rel-19) — Radio Resource Control Procedures
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [ASC na 3GPP Explorer](https://3gpp-explorer.com/glossary/asc/)
