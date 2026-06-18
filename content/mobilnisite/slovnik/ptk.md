---
slug: "ptk"
url: "/mobilnisite/slovnik/ptk/"
type: "slovnik"
title: "PTK – ProSe Traffic Key"
date: 2025-01-01
abbr: "PTK"
fullName: "ProSe Traffic Key"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ptk/"
summary: "Kryptografický klíč používaný k zabezpečení přímé komunikace mezi zařízeními (D2D) ve službách Proximity Services (ProSe). Poskytuje důvěrnost a ochranu integrity uživatelských dat přenášených přímo m"
---

PTK je ProSe Traffic Key, kryptografický klíč používaný k zabezpečení přímé komunikace mezi zařízeními (device-to-device) tím, že poskytuje důvěrnost (confidentiality) a ochranu integrity uživatelských dat.

## Popis

[ProSe](/mobilnisite/slovnik/prose/) Traffic Key (PTK) je bezpečnostní klíč definovaný v architektuře 3GPP pro služby Proximity Services (ProSe), které umožňují přímou komunikaci mezi zařízeními (Device-to-Device, [D2D](/mobilnisite/slovnik/d2d/)), známou také jako sidelink komunikace. Jedná se o symetrický klíč odvozený jako součást hierarchie klíčů speciálně pro ochranu uživatelských dat (user plane traffic) vyměňovaných přímo mezi dvěma nebo více UEs s podporou ProSe. PTK je generován a spravován ProSe Function v síti, ale je bezpečně doručen zapojeným UEs, aby jim umožnil šifrovat a chránit integritu jejich dat přímé komunikace. Toto zajišťuje, že i když datová cesta neprochází síťovými uzly, komunikace zůstává bezpečná a soukromá.

Architektonicky PTK zapadá do bezpečnostního rámce ProSe definovaného v technických specifikacích, jako je 33.303. Hierarchie klíčů typicky začíná dlouhodobými přihlašovacími údaji a zahrnuje klíče jako ProSe Key (PK) a ProSe K_{[eNB](/mobilnisite/slovnik/enb/)} (pokud je asistováno eNB). PTK je odvozen z těchto nadřazených klíčů pomocí funkcí pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)), které zahrnují parametry jako čítače čerstvosti (freshness counters) nebo nonces, aby zajistily oddělení klíčů. Po odvození je PTK používán s definovanými kryptografickými algoritmy (např. [AES](/mobilnisite/slovnik/aes/) nebo SNOW 3G) v konkrétních režimech šifrování a ochrany integrity pro rozhraní PC5, což je přímé rádiové spojení mezi UEs pro komunikaci ProSe. Klíč se uplatňuje na každou komunikační relaci nebo skupinu ProSe.

Jak to funguje, zahrnuje koordinaci mezi UE, ProSe Function a někdy eNodeB. Pro přímou komunikaci ProSe typu one-to-one je navázán zabezpečený kanál, často zahrnující procedury autentizace a dohody o klíči zprostředkované sítí. ProSe Function vygeneruje nebo autorizuje PTK a poskytne jej UEs přes zabezpečené buněčné spoje (např. přes rozhraní Uu). UEs pak tento PTK používají k zabezpečení svého přímého spoje PC5. Pro skupinovou komunikaci může být skupinový PTK distribuován všem členům skupiny. Životní cyklus PTK zahrnuje generování, aktivaci, používání a případné smazání po ukončení relace. Jeho role je klíčová pro to, aby se ProSe stalo životaschopnou službou pro veřejnou bezpečnost, komerční D2D aplikace a [V2X](/mobilnisite/slovnik/v2x/) (Vehicle-to-Everything), protože poskytuje standardizovaný, robustní bezpečnostní mechanismus, který zabraňuje odposlechu a manipulaci na přímém spoji.

## K čemu slouží

PTK byl vytvořen, aby řešil bezpečnostní výzvy vlastní přímé komunikaci mezi zařízeními zavedené se službami Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) ve 3GPP Release 12. Tradiční bezpečnost v buňkových sítích spoléhá na síťovou kontrolu, kde se klíče používají k ochraně spoje mezi UE a základnovou stanicí. ProSe však umožňuje UEs komunikovat přímo přes rozhraní PC5, čímž pro datovou cestu obchází síťovou infrastrukturu. To vytvořilo novou útočnou plochu: přímý rádiový spoj mezi UEs byl zranitelný vůči odposlechu a manipulaci, pokud by zůstal nechráněn. PTK poskytuje potřebnou kryptografickou ochranu pro tento přímý spoj.

Jeho vývoj byl motivován silnými požadavky z případů užití veřejné bezpečnosti a kritické komunikace, kde je bezpečný přímý režim provozu nezbytný, zejména když síťové pokrytí chybí nebo je narušeno. Před ProSe přímé komunikační technologie, jako jsou vysílačky nebo ad-hoc Wi-Fi, postrádaly integrovanou, standardizovanou bezpečnost na úrovni buněčných sítí. PTK jako součást bezpečnostní architektury 3GPP ProSe přináší důvěru a správu klíčů z buněčné sítě do domény [D2D](/mobilnisite/slovnik/d2d/). Řeší problém, jak inicializovat bezpečné symetrické klíče mezi zařízeními, která spolu nemusí mít předchozí vztah důvěry, a využívá přitom existující infrastrukturu autentizace a klíčů buněčné sítě.

Historicky Release 12 znamenal začátek standardizovaného D2D v buněčných sítích. PTK řešil omezení spočívající v absenci definované bezpečnosti pro uživatelskou rovinu (user plane) PC5. Umožňuje důvěrnou a integritu chráněnou přímou komunikaci, která je zásadní pro aplikace jako mission-critical push-to-talk, bezpečnostní zprávy V2X a komerční D2D služby. Tím, že poskytuje bezpečný klíč pro provozní data (traffic key), zajišťuje, že komunikace ProSe splňuje přísná očekávání v oblasti bezpečnosti a soukromí síťových operátorů a uživatelů, a usnadňuje tak přijetí D2D technologie v rámci důvěryhodného ekosystému sítí 3GPP.

## Klíčové vlastnosti

- Symetrický kryptografický klíč pro zabezpečení dat uživatelské roviny (user plane) na přímém rozhraní PC5
- Odvozen z hierarchie klíčů ProSe spravované síťovou ProSe Function
- Poskytuje jak důvěrnost (šifrování), tak ochranu integrity pro přímou komunikaci ProSe
- Podporuje scénáře komunikace ProSe typu one-to-one i one-to-many (skupinové)
- Bezpečně poskytován UEs přes buněčný spoj (rozhraní Uu) před zahájením přímé komunikace
- Nezbytný pro aplikace veřejné bezpečnosti, V2X a komerční aplikace ProSe vyžadující zabezpečené D2D spoje

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 36.323** (Rel-19) — PDCP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PTK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptk/)
