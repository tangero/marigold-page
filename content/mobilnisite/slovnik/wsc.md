---
slug: "wsc"
url: "/mobilnisite/slovnik/wsc/"
type: "slovnik"
title: "WSC – Web Service Consumer"
date: 2025-01-01
abbr: "WSC"
fullName: "Web Service Consumer"
category: "Management"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/wsc/"
summary: "Web Service Consumer (WSC) je klientská entita, která vyvolává operace na webové službě, jak je definováno v rámci architektury platformy pro logování a auditování 3GPP (LAP). Hraje klíčovou roli v be"
---

WSC je klientská entita, která vyvolává operace na webové službě v rámci architektury platformy pro logování a auditování 3GPP za účelem generování standardizovaných auditních záznamů pro dodržování bezpečnostních předpisů.

## Popis

V rámci architektury 3GPP, konkrétně definované v kontextu platformy pro logování a auditování ([LAP](/mobilnisite/slovnik/lap/)) v TS 33.980, je Web Service Consumer (WSC) funkční role nebo entita, která iniciuje požadavky na Web Service Provider ([WSP](/mobilnisite/slovnik/wsp/)). Jedná se o aktivního klienta v transakci webové služby. Primární funkcí WSC podle LAP není pouze využívání služby, ale generování podrobných, standardizovaných záznamů auditní stopy pro bezpečnostní a compliance účely. Tyto záznamy evidují interakce mezi WSC a WSP a zachycují „kdo, co, kdy a kde“ každého vyvolání webové služby.

Jeho fungování je integrováno do komunikačního zásobníku webové služby. Když WSC (např. systém správy sítě, aplikační provizionování) zavolá WSP (např. Home Subscriber Server - [HSS](/mobilnisite/slovnik/hss/), Policy and Charging Rules Function - [PCRF](/mobilnisite/slovnik/pcrf/)), architektura LAP toto volání zachytí. WSC je odpovědné za vygenerování auditního záznamu, který zahrnuje kritické informace, jako je identita konzumenta (WSC-ID), identita poskytovatele (WSP-ID), jedinečný identifikátor relace, časové razítko, konkrétní vyvolaná operace a relevantní parametry či data. Tento auditní záznam je následně bezpečně přenesen na centralizovaný Audit Trail Server ([ATS](/mobilnisite/slovnik/ats/)) pro trvalé uložení a analýzu.

Klíčové komponenty role WSC zahrnují logiku generování auditů, která musí být integrována do jeho klientského zásobníku webové služby, a zabezpečený komunikační kanál k ATS. WSC funguje ve spolupráci s Web Service Provider (WSP) a Audit Trail Server (ATS) a tvoří tak kompletní auditní trojúhelník LAP. Jeho role v síti je klíčová pro zajištění bezpečnosti, dodržování regulatorních požadavků (např. pro zákonné odposlechy, předpisy na ochranu dat), diagnostiku chyb a nepopiratelnost (non-repudiation) řídicích a provizních akcí. Tím, že 3GPP vyžaduje, aby WSC generovala tyto záznamy, zajišťuje konzistentní a spolehlivou auditní stopu napříč všemi rozhraními založenými na webových službách v síti, což je zvláště důležité v prostředích s více dodavateli a virtualizovaných prostředích, kde se tradiční formáty logů mohou lišit.

## K čemu slouží

WSC jako definovaná entita v rámci architektury [LAP](/mobilnisite/slovnik/lap/) existuje k vyřešení problému nedostatečného a nestandardizovaného bezpečnostního auditu na rozhraních sítí 3GPP založených na webových službách. Jelikož síťové funkce jádra stále více zpřístupňovaly rozhraní pro správu a provizování jako webové služby (počínaje Release 8), tradiční mechanismy logování byly často ad-hoc, specifické pro dodavatele a zaměřené na systémové chyby spíše než na bezpečnostně relevantní auditní stopy. To ztěžovalo sledování akcí v síti, prokazování souladu s předpisy nebo efektivní vyšetřování bezpečnostních incidentů.

Historický kontext představuje vývoj směrem k principům servisně orientované architektury ([SOA](/mobilnisite/slovnik/soa/)) v telekomunikační správě sítí. Zatímco to zlepšilo flexibilitu a integraci, přineslo to nové bezpečnostní výzvy a výzvy v oblasti odpovědnosti. Předchozí přístupy postrádaly standardizovaný způsob, jak zaznamenat, která entita provedla jakou akci na kterém zdroji a v jaký čas. Architektura LAP a formální definice role WSC v ní byly motivovány potřebou jednotné, bezpečné a spolehlivé auditní schopnosti, která je vlastní samotnému modelu komunikace webové služby.

Řeší omezení tím, že přesouvá generování auditů z volitelné funkce dodatečně uvažované až po implementaci na povinnou součást funkcionality konzumenta webové služby. Tím je zajištěno, že každá interakce je zaznamenána u svého zdroje v konzistentním formátu. Účelem je umožnit nepopiratelnost (entita nemůže popřít provedení akce), podpořit forenzní analýzu po bezpečnostním incidentu, splnit regulatorní požadavky na auditní stopy v telekomunikacích a poskytnout operátorům přehledný pohled na všechny konfigurační a řídicí aktivity napříč jejich infrastrukturou sítě s více dodavateli.

## Klíčové vlastnosti

- Generuje standardizované záznamy auditní stopy pro každé vyvolání webové služby
- Zahrnuje povinná datová pole: WSC-ID, WSP-ID, ID relace, časové razítko, název operace
- Integruje generování auditů přímo do komunikačního zásobníku klienta webové služby
- Bezpečně přenáší auditní záznamy na určený Audit Trail Server (ATS)
- Podporuje nepopiratelnost (non-repudiation) řídicích a provizních akcí
- Funguje ve spolupráci s rolí Web Service Provider (WSP) definovanou v LAP

## Související pojmy

- [LAP – Liberty Alliance Project](/mobilnisite/slovnik/lap/)
- [SOAP – Simple Object Access Protocol](/mobilnisite/slovnik/soap/)

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [WSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/wsc/)
