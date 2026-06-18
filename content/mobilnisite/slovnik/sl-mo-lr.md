---
slug: "sl-mo-lr"
url: "/mobilnisite/slovnik/sl-mo-lr/"
type: "slovnik"
title: "SL-MO-LR – Sidelink Mobile Originating Location Request"
date: 2025-01-01
abbr: "SL-MO-LR"
fullName: "Sidelink Mobile Originating Location Request"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sl-mo-lr/"
summary: "Služba umožňující uživatelskému zařízení (UE) vyžádat si vlastní polohu prostřednictvím sidelink komunikace bez nutnosti spoléhání na síťovou infrastrukturu. Podporuje scénáře ProSe (Proximity Service"
---

SL-MO-LR je služba ProSe a V2X, při které mobilní zařízení vyžádá vlastní polohu prostřednictvím přímé sidelink komunikace, nezávisle na jádru sítě, pro bezpečnostní nebo autonomní operace.

## Popis

SL-MO-LR (Sidelink Mobile Originating Location Request) je služba určování polohy definovaná v rámci standardů 3GPP, která umožňuje uživatelskému zařízení (UE) iniciovat žádost o stanovení vlastní geografické polohy pomocí komunikačních kanálů sidelink. Sidelink označuje přímé rozhraní komunikace mezi zařízeními, standardizované primárně pro aplikace [ProSe](/mobilnisite/slovnik/prose/) a [V2X](/mobilnisite/slovnik/v2x/), které funguje nezávisle na uplink a downlink buněčné sítě. V tomto postupu vystupuje UE jako iniciátor, který spouští žádost o polohu. Žádost je přenášena přes rozhraní PC5, standardizované sidelink komunikační rozhraní, k přijímající entitě, kterou může být jiné UE nebo specializovaný polohový server schopný zpracovat sidelinkové určování polohy. Postup zahrnuje signalizační výměny definované v dokumentech jako 23.273 pro architekturu fáze 2, 24.514 pro protokolové detaily a 38.355 pro aspekty rádiového přístupového sítě, což zajišťuje interoperabilitu napříč různými implementacemi.

Architektura pro SL-MO-LR je integrována do existujících sidelink rámců LTE a NR. Mezi klíčové komponenty patří iniciující UE, které generuje zprávu žádosti o polohu; rozhraní PC5, které zprostředkovává přímou komunikaci; a přijímající entita, která žádost zpracovává. Přijímající entita může pro výpočet polohy využít různé metody určování polohy, jako je [OTDOA](/mobilnisite/slovnik/otdoa/) (observed time difference of arrival) nebo sidelink-specifická měření. Postup podporuje jak řídicí, tak uživatelskou rovinu polohových protokolů a přizpůsobuje se dostupným síťovým podmínkám. Ve scénářích s omezeným nebo žádným pokrytím sítě, jako jsou odlehlé oblasti nebo výpadky sítě, umožňuje SL-MO-LR kritické služby založené na poloze využitím přímých spojení mezi zařízeními, čímž zvyšuje spolehlivost a snižuje závislost na infrastruktuře.

SL-MO-LR funguje tak, že UE vytvoří zprávu žádosti o polohu obsahující nezbytné parametry, jako jsou požadavky na QoS, preference metody určování polohy a identifikační informace. Tato zpráva je odeslána přes rozhraní PC5 pomocí sidelink sdíleného kanálu ([SL-SCH](/mobilnisite/slovnik/sl-sch/)). Po přijetí přijímající entita, pokud je vybavena polohovými schopnostmi, zahájí měřicí procedury. Ty mohou zahrnovat výměnu referenčních signálů, jako jsou [SL-PRS](/mobilnisite/slovnik/sl-prs/) (Sidelink Positioning Reference Signals), a provádění časových nebo úhlových měření. Vypočtená poloha je poté vrácena iniciujícímu UE přes stejné rozhraní PC5. Služba je navržena pro nízkou latenci a vysokou efektivitu, aby vyhovovala aplikacím v reálném čase, jako jsou záchranné služby ve V2X nebo polohově citlivé aplikace ProSe. Její integrace do širšího ekosystému 3GPP zajišťuje kompatibilitu se síťovými polohovými službami a poskytuje hybridní přístup, kde se sidelinkové a síťové určování polohy mohou vzájemně doplňovat na základě dostupnosti a požadavků.

## K čemu slouží

SL-MO-LR byl zaveden, aby řešil rostoucí potřebu spolehlivých polohových služeb ve scénářích, kde je tradiční síťové určování polohy nepraktické nebo nedostupné. S rozšiřováním aplikací [V2X](/mobilnisite/slovnik/v2x/) a [ProSe](/mobilnisite/slovnik/prose/) existuje kritická potřeba, aby zařízení mohla určit svou polohu nezávisle, zejména v prostředích se špatným pokrytím buněčnou sítí, jako jsou venkovské silnice, tunely nebo oblasti postižené katastrofami. Předchozí přístupy se silně spoléhaly na síťovou infrastrukturu, jako jsou základnové stanice nebo [GPS](/mobilnisite/slovnik/gps/), které mohou být za těchto podmínek nespolehlivé. SL-MO-LR umožňuje přímé žádosti o polohu mezi zařízeními, čímž zvyšuje odolnost a zajišťuje nepřetržitý provoz pro bezpečnostně kritické aplikace, jako je autonomní řízení nebo reakce na mimořádné události.

Historicky byly polohové služby v sítích 3GPP primárně síťově orientované, s postupy jako MO-LR (Mobile Originating Location Request) závislými na prvcích jádra sítě. Vývoj směrem k sidelink komunikaci v releasích jako Rel-14 pro LTE a Rel-16 pro NR poukázal na omezení těchto metod ve scénářích přímé komunikace. SL-MO-LR tuto mezeru zaplňuje rozšířením polohových služeb do sidelink domény, což umožňuje UE využívat polohování založené na blízkosti bez zásahu sítě. To je motivováno zejména požadavky automobilového průmyslu na vysoce přesné polohování s nízkou latencí ve V2X systémech, kde vozidla potřebují sdílet polohová data pro předcházení kolizí a efektivitu provozu.

Vytvoření SL-MO-LR také podporuje regulatorní a komerční potřeby, jako jsou služby typu E911 v sidelink kontextech, kdy musí být uživatelé lokalizováni během mimořádných událostí i bez přístupu k síti. Integrací do standardů 3GPP zajišťuje standardizovaný přístup, snižuje fragmentaci a podporuje interoperabilitu napříč zařízeními a sítěmi. Tím se řeší omezení ad-hoc řešení a připravuje se půda pro pokročilé aplikace v IoT a veřejné bezpečnosti, kde je spolehlivé povědomí o poloze prvořadé.

## Klíčové vlastnosti

- Umožňuje žádosti o polohu iniciované UE přes sidelink rozhraní PC5
- Podporuje jak řídicí, tak uživatelskou rovinu polohových protokolů
- Integruje se s aplikacemi ProSe a V2X pro přímé určování polohy mezi zařízeními
- Poskytuje odolnost ve scénářích s výpadkem sítě nebo omezeným pokrytím
- Využívá sidelink-specifické metody určování polohy, jako jsou měření SL-PRS
- Zajišťuje provoz s nízkou latencí pro bezpečnostně kritické služby v reálném čase

## Související pojmy

- [SL-MT-LR – Sidelink Mobile Terminating Location Request](/mobilnisite/slovnik/sl-mt-lr/)
- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SL-MO-LR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-mo-lr/)
