---
slug: "ipeg"
url: "/mobilnisite/slovnik/ipeg/"
type: "slovnik"
title: "IPEG – In-Progress Emergency Group"
date: 2025-01-01
abbr: "IPEG"
fullName: "In-Progress Emergency Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ipeg/"
summary: "In-Progress Emergency Group (IPEG, Skupina pro probíhající mimořádnou událost) je služební funkce 3GPP, která umožňuje zřízení dočasné komunikační skupiny během mimořádné události, například pro missi"
---

IPEG je služební funkce 3GPP, která autorizovanému uživateli umožňuje dynamicky přidávat nebo odebírat účastníky z dočasného skupinového hovoru, který již probíhá během mimořádné události.

## Popis

In-Progress Emergency Group (IPEG, Skupina pro probíhající mimořádnou událost) je služební schopnost definovaná v rámci standardů 3GPP pro služby Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně Mission Critical Push To Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Jedná se o specializovanou funkci, která spravuje dynamické členství v probíhající komunikační relaci skupiny pro mimořádné události. Na rozdíl od předdefinovaných statických skupin je IPEG charakteristická svou proměnlivou skladbou, kterou může autorizovaný uživatel měnit v reálném čase, zatímco skupinový hovor aktivně probíhá.

Z architektonického hlediska je funkčnost IPEG implementována v rámci aplikačního serveru a klienta MCPTT. Když je zahájen skupinový hovor pro mimořádnou událost, může začít s určitou sadou počátečních členů (např. předkonfigurovaný tým pro zásah). Uživateli s autoritou "Floor Control", kterým je často velitel zásahu, jsou udělena zvláštní oprávnění pro správu IPEG. Prostřednictvím svého rozhraní klienta MCPTT může odesílat požadavky na server MCPTT, aby přidal nové účastníky (např. další zasahující jednotky dorazivší na místo) nebo odebral stávající. Server následně signalizuje zúčastněným stranám a aktualizuje jejich stav členství ve skupině a cesty pro distribuci médií.

Protokolové mechanismy jsou podrobně popsány v technických specifikacích, jako je 24.379 (protokol MCPTT). Proces zahrnuje specifické řídicí zprávy pro "In-Progress Emergency Group Add Request" a "In-Progress Emergency Group Remove Request". Zabezpečení je prvořadé; tyto příkazy mohou provádět pouze autorizovaní uživatelé se správnými přihlašovacími údaji, kteří aktuálně drží "slovo" (floor) v hovoru pro mimořádnou událost. Server MCPTT každý požadavek ověří, zkontroluje autorizační politiky a následně aktualizuje stav aktivní relace, čímž zajistí, že všichni účastníci obdrží aktualizovaný seznam členů a mediální streamy.

IPEG funguje v rámci širšího ekosystému služeb Mission Critical Services přes LTE/5G ([MCX](/mobilnisite/slovnik/mcx/)). Spoléhá se na základní jádro IMS pro registraci, autentizaci a řízení relací a využívá pokročilé podpůrné systémy skupinové komunikace. Tato funkce je klíčová pro přizpůsobení se nepředvídatelné povaze scénářů mimořádných událostí, kde se sada potřebných komunikujících stran rychle vyvíjí. Zajišťuje, že komunikační skupina zůstává relevantní a efektivní po celou dobu životního cyklu události, a přímo tak podporuje koordinované zásahové úsilí.

## K čemu slouží

IPEG byl vyvinut, aby řešil kritický nedostatek tradičních systémů skupinové komunikace používaných složkami integrovaného záchranného systému a prvními respondenty. V situacích mimořádných událostí se složení zapojeného personálu dynamicky mění – dorazí nové jednotky, jiné jsou převeleny nebo některé mohou být vyřazeny. Statické, předdefinované mluvící skupiny tuto proměnlivost nemohou akomodovat, což nutí zasahující přepínat mezi více skupinami nebo používat neefektivní metody vysílání, což plýtvá drahocenným časem a zvyšuje zmatek.

Vytvoření IPEG v rámci standardů služeb Mission Critical Services 3GPP bylo motivováno potřebou agilní, velitelem řízené komunikace. Dává veliteli zásahu možnost udržovat jediný, autoritativní komunikační kanál, který lze okamžitě přizpůsobit vyvíjející se taktické situaci. Tím se řeší problém informačních sil a zajišťuje, že všechny relevantní strany jsou zahrnuty do kritických pokynů a situačních aktualizací.

Před standardizovanými funkcemi [MCPTT](/mobilnisite/slovnik/mcptt/), jako je IPEG, byly podobné schopnosti proprietární konkrétních výrobců systémů pozemní mobilní radiokomunikace ([LMR](/mobilnisite/slovnik/lmr/)), což bránilo interoperabilitě mezi různými složkami. Standardizací IPEG ve vydání 3GPP 13 a novějších se zajišťuje, že nástroje pro kritickou komunikaci mohou bezproblémově fungovat přes komerční sítě LTE/5G, což usnadňuje společné operace policie, hasičů, zdravotníků a dalších služeb bez ohledu na jejich zařízení nebo poskytovatele sítě. Představuje posun od technologicky omezených rádiových kanálů k flexibilní, službami bohaté digitální skupinové komunikaci.

## Klíčové vlastnosti

- Dynamická úprava členství ve skupině během aktivního skupinového hovoru pro mimořádnou událost
- Řízena autorizovaným uživatelem (např. velitelem zásahu) s oprávněním pro floor control
- Podporuje jak přidávání, tak odebírání účastníků z probíhající relace
- Integrováno s procedurami a zabezpečením hovorů Mission Critical Push To Talk (MCPTT)
- Pro změny členství využívá specifické řídicí zprávy protokolu MCPTT (definováno v 24.379)
- Zvyšuje koordinaci situačního povědomí tím, že udržuje komunikační skupinu v souladu s potřebami v reálném čase

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [IPEG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipeg/)
