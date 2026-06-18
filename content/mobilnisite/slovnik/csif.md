---
slug: "csif"
url: "/mobilnisite/slovnik/csif/"
type: "slovnik"
title: "CSIF – Communication Service Interface"
date: 2025-01-01
abbr: "CSIF"
fullName: "Communication Service Interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csif/"
summary: "CSIF je standardizované rozhraní typu northbound definované v 3GPP pro zpřístupnění síťových schopností poskytovatelům komunikačních služeb třetích stran. Umožňuje integraci sítí 3GPP s externími apli"
---

CSIF je standardizované rozhraní typu northbound definované v 3GPP pro zpřístupnění síťových schopností poskytovatelům komunikačních služeb třetích stran za účelem umožnění integrace s externími aplikacemi a službami.

## Popis

Rozhraní pro komunikační služby (CSIF) je standardizovaný aplikační programovací rozhraní ([API](/mobilnisite/slovnik/api/)), které poskytuje rozhraní typu northbound ze sítě 3GPP směrem k externím poskytovatelům komunikačních služeb a aplikacím. Definované ve verzi 3GPP Release 16 a vylepšené v následujících verzích umožňuje CSIF poskytovatelům služeb třetích stran přistupovat k síťovým schopnostem a využívat je řízeným, bezpečným a standardizovaným způsobem. Rozhraní abstrahuje složitost podkladové sítě a zpřístupňuje síťové funkce jako znovupoužitelné služby, což externím subjektům umožňuje integrovat schopnosti sítě 3GPP do svých aplikací bez nutnosti hluboké znalosti vnitřní architektury sítě.

Architektonicky CSIF funguje jako vrstva pro zpřístupnění API, která se nachází mezi síťovými funkcemi 3GPP a externími aplikacemi. Poskytuje sadu dobře definovaných RESTful API se standardizovanými datovými modely, autentizačními mechanismy a bezpečnostními protokoly. Rozhraní podporuje jak synchronní, tak asynchronní komunikační vzory, což aplikacím umožňuje vyžádat si síťové služby a přijímat oznámení o síťových událostech. CSIF implementuje komplexní mechanismy řízení politik, které určují, jaké síťové schopnosti jsou zpřístupněny kterým aplikacím, a zajišťují, že síťové prostředky jsou využívány odpovídajícím a bezpečným způsobem v souladu s politikami definovanými operátorem.

Klíčové komponenty architektury CSIF zahrnují API Gateway, který slouží jako vstupní bod pro externí aplikace a zajišťuje autentizaci, autorizaci a správu provozu. Komponenta Service Exposure Function ([SEF](/mobilnisite/slovnik/sef/)) spravuje mapování mezi požadavky externího API a interakcemi vnitřních síťových funkcí. Policy Enforcement Point ([PEP](/mobilnisite/slovnik/pep/)) zajišťuje, že všechny požadavky API jsou v souladu s politikami operátora, než jsou předány síťovým funkcím. CSIF dále zahrnuje monitorovací a analytické komponenty, které sledují využití API, výkonnostní metriky a bezpečnostní události, a poskytují tak operátorům přehled o tom, jak jsou jejich síťové schopnosti využívány.

CSIF podporuje více kategorií služeb, včetně správy konektivity, řízení kvality služeb (QoS), lokalizačních služeb, síťové analytiky a správy zařízení. Pro správu konektivity poskytuje CSIF API pro vytváření, modifikaci a ukončování síťových připojení se specifickými charakteristikami QoS. Pro řízení QoS umožňuje aplikacím vyžádat si garantované přenosové rychlosti, limity latence a úrovně spolehlivosti pro svůj provoz. API pro lokalizační služby umožňují autorizovaným aplikacím vyžádat si informace o poloze zařízení s odpovídajícími ochrannými mechanismy soukromí. Rozhraní také podporuje schopnosti síťového řezání (network slicing), což aplikacím umožňuje vyžádat si vyhrazené síťové řezy se specifickými výkonnostními charakteristikami šitými na míru jejich požadavkům.

Při provozu CSIF následuje model požadavek-odpověď, kde se externí aplikace autentizují pomocí OAuth 2.0 nebo podobných mechanismů a následně volají API pro vyžádání síťových služeb. API Gateway ověří požadavek vůči bezpečnostním politikám a smlouvám o úrovni služeb, než jej předá příslušným síťovým funkcím. Odpovědi jsou vraceny ve standardizovaných formátech [JSON](/mobilnisite/slovnik/json/) nebo [XML](/mobilnisite/slovnik/xml/) s odpovídajícím zpracováním chyb a stavovými kódy. CSIF také podporuje mechanismy webhooků pro push oznámení, což aplikacím umožňuje přijímat aktualizace v reálném čase o síťových událostech, jako jsou změny v připojení zařízení, aktualizace polohy nebo porušení QoS.

## K čemu slouží

CSIF byl vytvořen, aby řešil rostoucí potřebu standardizovaných rozhraní, která umožňují poskytovatelům služeb třetích stran využívat schopnosti sítí 3GPP ve svých aplikacích. Před zavedením CSIF byly síťové schopnosti pro externí subjekty z velké části nedostupné, nebo dostupné pouze prostřednictvím proprietárních rozhraní, která se lišila mezi operátory a vyžadovala značné integrační úsilí. Toto omezení bránilo inovacím a rozvoji nových obchodních modelů, které by mohly využívat síťovou inteligenci a schopnosti.

Primárním motivem pro vývoj CSIF bylo umožnit obchodní modely typu síť-jako-sluzba (NaaS), kde mohou operátoři monetizovat své síťové schopnosti jejich zpřístupněním externím zákazníkům. Tím se řeší výzva klesajících tradičních příjmových toků vytvářením nových příjmových příležitostí prostřednictvím nabídek služeb založených na [API](/mobilnisite/slovnik/api/). CSIF také podporuje potřeby vertikálních odvětví, jako je automobilový průmysl, výroba a zdravotnictví, která vyžadují specializované síťové služby, jež lze snadno integrovat do jejich operačních technologických systémů.

Dalším klíčovým účelem CSIF je poskytnout standardizovaný, bezpečný rámec pro zpřístupňování služeb, který řeší bezpečnostní a ochranářské obavy spojené s otevíráním síťových schopností externím subjektům. Rozhraní zahrnuje robustní mechanismy autentizace, autorizace a účtování, které zajišťují, že pouze autorizované aplikace mohou přistupovat k síťovým schopnostem, a to pouze v mezích definovaných politikami operátora. Tento bezpečnostní rámec byl nezbytný pro získání přijetí konceptu zpřístupňování služeb ze strany operátorů, neboť poskytuje potřebné kontroly k ochraně integrity sítě a soukromí účastníků při současném umožnění nových služeb.

## Klíčové vlastnosti

- Standardizovaná RESTful API s OpenAPI specifikacemi
- Komplexní autentizace a autorizace využívající OAuth 2.0
- Řízení přístupu a omezení přenosové rychlosti na základě politik
- Podpora synchronních i asynchronních komunikačních vzorů
- Oznámení v reálném čase prostřednictvím mechanismů webhooků
- Schopnosti správy síťového řezání (network slicing)

## Definující specifikace

- **TS 22.104** (Rel-19) — Service requirements for cyber-physical control apps
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G

---

📖 **Anglický originál a plná specifikace:** [CSIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/csif/)
