---
slug: "sees"
url: "/mobilnisite/slovnik/sees/"
type: "slovnik"
title: "SEES – Service Exposure and Enablement Support"
date: 2026-01-01
abbr: "SEES"
fullName: "Service Exposure and Enablement Support"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sees/"
summary: "Rámec pro bezpečné zpřístupnění síťových schopností a informací autorizovaným aplikacím a poskytovatelům služeb třetích stran. Umožňuje tvorbu nových služeb tím, že externím subjektům umožňuje kontrol"
---

SEES je architektonický rámec pro bezpečné zpřístupnění síťových schopností a informací autorizovaným aplikacím třetích stran za účelem umožnění nových služeb a obchodních modelů.

## Popis

Service Exposure and Enablement Support (SEES) je standardizovaný architektonický rámec v rámci 3GPP, který definuje mechanismy pro bezpečné a efektivní zpřístupňování síťových schopností a informací důvěryhodným poskytovatelům aplikací třetích stran. Funguje jako vrstva abstrakce mezi funkcemi jádra sítě a externími aplikacemi a poskytuje sadu aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)), která abstrahují složitost podkladové sítě. Tato API umožňují externím subjektům požadovat síťové služby, přistupovat k datům účastníků (s jejich souhlasem) a spouštět síťové události bez nutnosti hluboké znalosti proprietárních síťových protokolů. Tento rámec je klíčový pro umožnění nových vertikálních služeb a partnerství, například v oblasti IoT, podnikových komunikací a edge computingu.

Architektura SEES typicky zahrnuje klíčové funkční entity, jako je Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) v 5G Core, která slouží jako hlavní bod pro zpřístupnění API. SEES na tuto funkci navazuje tím, že poskytuje správu politik, zabezpečení a životního cyklu pro tato zpřístupnění. Definuje standardizovaná northbound API (např. založená na RESTful principech), která mohou využívat aplikační funkce ([AF](/mobilnisite/slovnik/af/)) třetích stran. Rámec zajišťuje, že veškeré zpřístupnění je řízeno politikami, které vynucují zabezpečení, ochranu soukromí a ochranu síťových zdrojů. Zpracovává autentizaci a autorizaci třetích stran, spravuje správu verzí API a jejich vyřazování a poskytuje rozhraní pro účtování a fakturaci za účelem monetizace zpřístupněných schopností.

SEES funguje tak, že překládá požadavky na služby vysoké úrovně od externích aplikací na konkrétní síťové příkazy nebo získávání informací z příslušných funkcí jádra sítě. Například aplikace může požadovat zvýšení kvality služeb (QoS) pro konkrétní uživatelskou relaci a SEES by tento požadavek přeložil do příslušných interakcí řízení politik s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). Také podporuje zpřístupňování událostí, kdy síť může informovat přihlášené aplikace o konkrétních výskytech, jako je změna polohy uživatele nebo aktualizace stavu připojení. Tento model řízený událostmi je nezbytný pro aplikace v reálném čase. Úlohou rámce je učinit síť programovatelnou a otevřenou, čímž se z uzavřené infrastruktury transformuje na platformu pro inovace služeb při zachování přísné provozní kontroly a zabezpečení.

## K čemu slouží

SEES byl vytvořen, aby reagoval na rostoucí poptávku podniků a vývojářů aplikací po přímém, programovatelném přístupu k schopnostem telekomunikačních sítí. Historicky byly síťové funkce izolované a přístupné pouze prostřednictvím proprietárních rozhraní, což pro třetí strany ztěžovalo a prodražovalo integraci a tvorbu nových služeb. Vzestup cloud-nativních aplikací a potřeba síťově-vědomých služeb (jako je rozšířená realita, připojená vozidla a chytré továrny) si vyžádaly standardizovanou, bezpečnou metodu pro zpřístupnění. SEES řeší problém síťových 'uzavřených zahrad' (walled gardens) tím, že poskytuje kontrolovanou bránu.

Primární motivací bylo odemknout nové zdroje příjmů pro mobilní operátory tím, že jim umožní monetizovat své síťové aktiva nad rámec základní konektivity. Zpřístupněním schopností, jako je řízení QoS, informace o poloze, stav sítě a spouštění zařízení, mohou operátoři nabízet služby s přidanou hodnotou vertikálním odvětvím. SEES také řeší technickou výzvu škálovatelného a bezpečného zpřístupnění; bez rámce jako je SEES by každé nové [API](/mobilnisite/slovnik/api/) nebo partner vyžadoval vlastní integraci, což by zvyšovalo složitost a bezpečnostní rizika. Standardizuje vrstvu pro zpřístupnění, čímž snižuje čas a náklady na integraci a zároveň zajišťuje konzistentní vynucování zabezpečení a politik napříč všemi interakcemi s třetími stranami.

## Klíčové vlastnosti

- Standardizovaná northbound RESTful API pro využití aplikacemi třetích stran
- Řízení založené na politikách, které určuje, jaké síťové schopnosti jsou komu zpřístupněny
- Bezpečná autentizace a autorizace externích aplikačních funkcí (AF)
- Podpora jak interakčních modelů typu request-response, tak modelů řízených událostmi (subscribe/notify)
- Integrace s účtovacími systémy pro monetizaci zpřístupněných služeb
- Abstrakce podkladové síťové složitosti a heterogenity

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)
- [SBA – Scene-Based Audio (Ambisonics)](/mobilnisite/slovnik/sba/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements

---

📖 **Anglický originál a plná specifikace:** [SEES na 3GPP Explorer](https://3gpp-explorer.com/glossary/sees/)
