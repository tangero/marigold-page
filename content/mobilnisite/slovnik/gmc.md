---
slug: "gmc"
url: "/mobilnisite/slovnik/gmc/"
type: "slovnik"
title: "GMC – Group Management Client"
date: 2025-01-01
abbr: "GMC"
fullName: "Group Management Client"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gmc/"
summary: "Funkční entita v rámci UE, která spravuje služby a konfigurace související se skupinami. Zajišťuje členství ve skupině, příjem politik a autorizaci služeb pro skupinovou komunikaci, čímž umožňuje efek"
---

GMC je funkční entita v uživatelském zařízení (UE), která spravuje skupinové služby, zajišťuje členství, příjem politik a autorizaci služeb pro efektivní skupinovou komunikaci v sítích 3GPP.

## Popis

Klient pro správu skupin (GMC) je funkční komponenta umístěná v uživatelském zařízení (UE), která je zodpovědná za správu účasti UE ve službách založených na skupinách. Působí jako koncový bod pro procedury správy skupin definované sítí, konkrétně komunikuje se serverem pro správu skupin ([GMS](/mobilnisite/slovnik/gms/)) nebo funkcí [ProSe](/mobilnisite/slovnik/prose/) pro služby založené na blízkosti. Primární role GMC spočívá v zajišťování událostí životního cyklu členství ve skupině, včetně registrace, zrušení registrace a aktualizací. Přijímá a zpracovává konfigurační data a politiky skupiny ze sítě, jako jsou identifikátory skupin, bezpečnostní klíče a parametry služeb, které jsou nezbytné pro účast UE ve skupinové komunikaci, jako je Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) nebo přímé zjišťování a komunikace ProSe.

Z architektonického hlediska je GMC logická entita často implementovaná jako součást aplikační nebo servisní vrstvy UE, zejména pro služby standardizované v 3GPP. Rozhraní s protokoly nižších vrstev a dalšími klientskými funkcemi v rámci UE pro uplatňování přijatých skupinových politik. Například po přijetí autorizace členství ve skupině může GMC nakonfigurovat rádiovou a správu relací v UE tak, aby upřednostňovala provoz pro danou skupinu nebo zřídila potřebné přenosové cesty. Také spravuje lokální úložiště dat souvisejících se skupinou, čímž zajišťuje správnou funkci UE i při dočasném nedostupnosti síťového pokrytí, a to využitím předkonfigurovaných politik a klíčů.

GMC spolupracuje s funkcemi jádra sítě, jako je GMS v [HSS](/mobilnisite/slovnik/hss/) nebo specializovaném aplikačním serveru. Proces typicky začíná tím, že GMC iniciuje žádost o registraci pro konkrétní skupinovou službu. Síť autentizuje UE a autorizuje členství ve skupině, načež GMC obdrží konfigurační balíček. Tento balíček obsahuje klíčové informace, jako je klíč pro správu skupiny ([GMK](/mobilnisite/slovnik/gmk/)) pro zabezpečení, identifikátory skupin a parametry specifické pro službu. GMC je pak zodpovědný za vynucování těchto parametrů, sledování aktualizací ze sítě a zpracování událostí, jako je odvolání členství ve skupině. Jeho činnost je klíčová pro škálovatelné skupinové služby, protože odlehčuje síti od průběžné správy tím, že umožňuje UE spravovat lokální stavy skupin na základě počátečních pokynů sítě.

## K čemu slouží

GMC byl zaveden pro řešení rostoucí potřeby efektivních a škálovatelných služeb skupinové komunikace v sítích 3GPP, zejména s nástupem služeb pro kritickou komunikaci ([MCS](/mobilnisite/slovnik/mcs/)) a služeb založených na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) ve vydání 13. Předchozí přístupy často spoléhaly na mechanismy typu bod-bod nebo vysílání, které byly pro dynamické skupiny neefektivní a postrádaly v UE vyhrazené správní entity pro zpracování politik a zabezpečení specifických pro skupiny. To ztěžovalo poskytování služeb a omezovalo škálovatelnost skupinových aplikací, jako je komunikace pro veřejnou bezpečnost nebo skupinové zasílání zpráv v IoT.

Zavedení GMC standardizuje chování na straně klienta pro správu skupin, čímž zajišťuje interoperabilitu mezi různými implementacemi UE a síťovými dodavateli. Řeší problém decentralizovaného a nekonzistentního vynucování skupinových politik tím, že poskytuje definovanou funkční entitu v rámci UE, která může spolehlivě přijímat, ukládat a uplatňovat skupinové konfigurace poskytnuté sítí. To je zvláště důležité pro služby vyžadující bezpečnou skupinovou interakci s nízkou latencí, kde se musí UE rychle přizpůsobovat změnám ve skupině bez neustálé signalizace se sítí.

Historicky byla správa skupin často řešena ad-hoc v rámci konkrétních aplikací, což vedlo k fragmentaci. GMC jako součást architektury 3GPP poskytuje jednotný rámec. Umožňuje síťovým operátorům efektivně spravovat velké skupiny (např. týmy první pomoci) delegováním úloh správy na klienta, čímž se snižuje signalizační zátěž jádra sítě. Tento přístup zaměřený na klienta podporuje pokročilé funkce, jako je provoz mimo síť v ProSe, kde mohou UE v blízkosti komunikovat přímo pomocí skupinových politik spravovaných GMC.

## Klíčové vlastnosti

- Spravuje životní cyklus členství UE ve skupině (registrace, aktualizace, zrušení registrace)
- Přijímá a zpracovává konfigurační politiky skupiny ze síťových serverů
- Ukládá a uplatňuje parametry specifické pro skupinu, jako jsou identifikátory a bezpečnostní klíče
- Spolupracuje s funkcí ProSe pro služby skupin založené na blízkosti
- Podporuje síťem iniciované aktualizace a odvolání skupinových politik
- Umožňuje lokální vynucování skupinových politik pro snížení síťové signalizace

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [GMK – Group Management Key](/mobilnisite/slovnik/gmk/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management

---

📖 **Anglický originál a plná specifikace:** [GMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmc/)
