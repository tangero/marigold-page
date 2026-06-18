---
slug: "lcn"
url: "/mobilnisite/slovnik/lcn/"
type: "slovnik"
title: "LCN – Local Communication Network"
date: 2025-01-01
abbr: "LCN"
fullName: "Local Communication Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcn/"
summary: "Obecný termín používaný v 3GPP pro komunikační síť s geograficky omezeným dosahem, jako je domácí síť, podniková síť nebo průmyslová kampusová síť. Představuje doménu, v níž jsou poskytovány lokální s"
---

LCN je obecný pojem pro geograficky omezenou komunikační síť, například domácí nebo podnikovou síť, která poskytuje lokální služby a rozhraní pro propojení se širší veřejnou mobilní sítí.

## Popis

V terminologii 3GPP je Lokální komunikační síť (LCN) široký koncept označující jakoukoli komunikační síť s omezeným geografickým pokrytím. Není to konkrétní technologie nebo protokol, ale kategorický termín používaný napříč různými specifikacemi k popisu síťových domén, jako jsou rezidenční domácí sítě, podnikové či univerzitní kampusové sítě, tovární sítě nebo izolované komunitní sítě. LCN typicky poskytuje konektivitu a služby definované, lokalizované skupině uživatelů nebo zařízení. Její architektura se může značně lišit; může být založena na drátových technologiích (např. Ethernet, [DSL](/mobilnisite/slovnik/dsl/)), bezdrátových lokálních sítích (např. Wi-Fi), nebo dokonce na lokalizované implementaci 3GPP radiové technologie, jako je femtobuňka, Home NodeB ([HNB](/mobilnisite/slovnik/hnb/)) nebo privátní 5G neveřejná síť ([NPN](/mobilnisite/slovnik/npn/)).

Provoz LCN zahrnuje poskytování lokálního přístupu, směrování a potenciálně i hostování lokálních služeb. Klíčovým aspektem v normách 3GPP je způsob, jakým LCN spolupracuje s veřejnou makro mobilní sítí, tj. s veřejnou pozemní mobilní sítí ([PLMN](/mobilnisite/slovnik/plmn/)). Například v kontextu femtobuněk a Home eNodeB (HeNB) se LCN (domácí síť) připojuje k jádrové síti operátora přes širokopásmové připojení v domácnosti, čímž vytváří zabezpečený tunel. Jádrová síť považuje HeNB za důvěryhodný přístupový bod, čímž rozšiřuje pokrytí mobilní sítě do lokální oblasti. U privátních NPN v 5G může být LCN plně samostatnou sítí s vlastními funkcemi jádra nebo síťovým segmentem (slice) virtuálně izolovaným v rámci veřejné PLMN. Zařízení uvnitř LCN mohou komunikovat mezi sebou lokálně a přistupovat k místním datovým serverům (např. k místnímu mediálnímu serveru v domácnosti nebo k výrobnímu prováděcímu systému v továrně), aniž by jejich provoz musel opustit lokální doménu.

Klíčové komponenty LCN, v závislosti na její konkrétní implementaci, zahrnují lokální přístupové body (Wi-Fi [AP](/mobilnisite/slovnik/ap/), femtobuňky), lokální směrovače a přepínače, místní bránu nebo firewall a případně lokální aplikační servery. V integrovaných scénářích 3GPP patří mezi kritické komponenty Lokální brána ([L-GW](/mobilnisite/slovnik/l-gw/)) pro odlehčení provozu, Bezpečnostní brána (SeGW) pro zabezpečení spojení s PLMN a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo ekvivalent pro správu místních účastníků v samostatných případech. Úlohou LCN v širším ekosystému je poskytovat přizpůsobené, výkonné a často zabezpečené komunikační služby pro konkrétní lokalitu nebo komunitu, které doplňují služby širokoplošné sítě PLMN.

## K čemu slouží

Koncept Lokální komunikační sítě existuje v 3GPP k formálnímu uznání a standardizaci integrace ne-širokoplošných sítí s ekosystémem mobilních sítí. Historicky byly mobilní sítě navrženy pro širokoplošné veřejné pokrytí. Významná část datového provozu je však generována a spotřebována uvnitř budov nebo v uzavřených kampusových areálech. Původní motivací bylo nákladově efektivní zlepšení pokrytí a kapacity uvnitř budov, což vedlo ke standardům pro femtobuňky (Home NodeB), které v podstatě vytvářejí zákaznickou LCN, která je součástí sítě operátora.

LCN řeší několik problémů: špatnou prostupnost signálu makrobuněk do budov, přetížení v oblastech s vysokou hustotou uživatelů, jako jsou kanceláře, a potřebu specializované, nízkolatenční komunikace v průmyslových prostředích. Poskytuje model pro odlehčení sítě, kde lze lokální provoz obsluhovat lokálně, čímž se snižuje zatížení makro sítě a zlepšuje se uživatelská zkušenost. Pro podniky a průmysl se koncept LCN vyvinul ve standardizovanou privátní síť ([NPN](/mobilnisite/slovnik/npn/)) v 5G, která řeší potřebu bezpečné, spolehlivé a přizpůsobitelné bezdrátové konektivity pro kritické operace bez závislosti na infrastruktuře veřejné sítě.

Dále LCN podporuje inovace služeb tím, že umožňuje hostování lokálních služeb. To umožňuje aplikace, jako je lokální ukládání obsahu do mezipaměti, edge computing a ultra-spolehlivá komunikace mezi stroji, které by byly nepraktické, pokud by veškerý provoz musel procházet veřejným internetem a jádrovou sítí. Představuje posun od čistě centralizovaného síťového modelu k více distribuovanému, s poznáním, že hodnota a funkčnost mohou sídlit na okraji sítě.

## Klíčové vlastnosti

- Geograficky omezené síťové pokrytí (např. budova, kampus)
- Může být implementována s různými přístupovými technologiemi (3GPP, Wi-Fi, drátové)
- Spolupracuje s veřejnou pozemní mobilní sítí (PLMN) pro rozšířené služby
- Podporuje lokální přepínání provozu a hostování služeb (místní breakout)
- Umožňuje přizpůsobené parametry výkonu (latence, spolehlivost) a bezpečnostní politiky
- Základ pro nasazení femtobuněk, podnikových sítí a privátních 5G sítí

## Související pojmy

- [NPN – Non-Public Network](/mobilnisite/slovnik/npn/)
- [HENB – Home Enhanced Node B](/mobilnisite/slovnik/henb/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [LCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcn/)
