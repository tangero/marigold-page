---
slug: "gktp"
url: "/mobilnisite/slovnik/gktp/"
type: "slovnik"
title: "GKTP – Group Key Transport Payload"
date: 2025-01-01
abbr: "GKTP"
fullName: "Group Key Transport Payload"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gktp/"
summary: "Zabezpečovací datová jednotka definovaná v 3GPP pro zabezpečený přenos skupinových klíčů, jako jsou MBMS Service Keys nebo klíče Group Communication System Enablers, po síti. Zajišťuje, že klíče jsou"
---

GKTP je zabezpečovací datová jednotka (payload) definovaná 3GPP pro důvěrný a integritu chráněný přenos skupinových klíčů, například MBMS Service Keys, k autorizovaným entitám za účelem zabezpečené skupinové komunikace a vysílacích služeb.

## Popis

Group Key Transport Payload (GKTP) je strukturovaný formát dat specifikovaný v 3GPP TS 24.481. Jeho primární funkcí je zapouzdřit a bezpečně přenášet kryptografické klíče určené pro skupinové použití, například klíče pro Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) nebo Group Communication System Enablers ([GCSE](/mobilnisite/slovnik/gcse/)). Datová jednotka je navržena k přenosu v rámci existujících signalizačních protokolů, což zajišťuje doručení klíčů z key management serverů, jako je Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)) nebo Key Management Function (KMF), k cílovým síťovým funkcím nebo uživatelskému zařízení.

Z architektonického hlediska GKTP funguje v rámci 3GPP Generic Authentication Architecture ([GAA](/mobilnisite/slovnik/gaa/)). Využívá existující infrastrukturu GAA, kde BSF funguje jako centrální bod pro distribuci klíčů. Když síťová funkce nebo aplikační server potřebuje skupinový klíč, vyžádá si jej od BSF. BSF poté klíč vygeneruje nebo získá, zabalí jej do struktury GKTP a odešle žadateli. Samotná datová jednotka obsahuje klíčový materiál spolu s nezbytnými metadaty, jako jsou identifikátory klíčů, období platnosti a přidružené skupinové identifikátory.

Zabezpečení přenosu klíče je prvořadé. GKTP je typicky chráněn pomocí zabezpečovacích asociací navázaných během procedury GAA bootstrappingu. To často zahrnuje použití sdíleného tajemství navázaného mezi uživatelským zařízením a sítí (např. pomocí klíče Ks_[NAF](/mobilnisite/slovnik/naf/)) k odvození šifrovacích a integritních klíčů. V důsledku toho je datová jednotka GKTP zašifrována a chráněna z hlediska integrity, což zajišťuje, že pouze zamýšlený příjemce s příslušným klíčovým materiálem může přistoupit k skupinovému klíči a ověřit jej. Tento mechanismus zabraňuje odposlechu a manipulaci během distribuce klíčů.

V praxi je GKTP klíčové pro služby, které jsou závislé na efektivní a zabezpečené distribuci klíčů typu jeden-mnoho. Pro MBMS umožňuje bezpečné doručení servisních klíčů pro dešifrování vysílaného obsahu. Pro GCSE usnadňuje distribuci skupinových hovorových klíčů pro důležitou push-to-talk komunikaci. Standardizací tohoto formátu datové jednotky 3GPP zajišťuje interoperabilitu mezi síťovými funkcemi různých dodavatelů a poskytuje škálovatelnou a bezpečnou metodu pro správu skupinových klíčů napříč vyvíjejícími se architekturami služeb 5G.

## K čemu slouží

GKTP bylo vytvořeno, aby řešilo konkrétní problém zabezpečené distribuce kryptografických klíčů více příjemcům – což je běžný požadavek pro skupinově orientované služby jako vysílání/multicast a skupinová komunikace. Před jeho standardizací se pro distribuci skupinových klíčů používaly ad-hoc metody nebo proprietární rozšíření existujících protokolů, což vedlo k problémům s interoperabilitou, bezpečnostním zranitelnostem a zvýšené složitosti nasazení služeb.

Historický kontext je ukotven v rozšíření 3GPP služeb mimo tradiční komunikaci jeden-jeden. Se zavedením [MBMS](/mobilnisite/slovnik/mbms/) a později služeb kritických z hlediska mise vyžadujících [GCSE](/mobilnisite/slovnik/gcse/) vznikl jasný požadavek na standardizovaný, efektivní a zabezpečený mechanismus pro poskytování skupinových klíčů. Existující [GAA](/mobilnisite/slovnik/gaa/) poskytovala vynikající zabezpečení pro distribuci klíčů jeden-jeden (např. pro zabezpečení aplikací), ale postrádala definovaný kontejner pro skupinové klíče. GKTP tuto mezeru zaplnilo poskytnutím přesně specifikované datové jednotky, která se bezproblémově integruje s infrastrukturou GAA.

Řešením tohoto problému GKTP umožňuje komerční a bezpečné zavádění služeb závislých na sdílených tajemstvích. Zmírňuje riziko kompromitace klíče během distribuce, zajišťuje, že klíče obdrží pouze autorizovaní členové skupiny, a poskytuje základ pro zákonné odposlechy a správu životního cyklu klíčů (např. obnovení nebo odvolání klíče). Jeho vytvoření bylo motivováno potřebou dlouhodobě použitelného řešení založeného na standardech, které by mohlo podpořit rostoucí poptávku po zabezpečených skupinových aplikacích v sítích 4G i 5G.

## Klíčové vlastnosti

- Standardizovaný formát datové jednotky pro zapouzdření skupinových klíčů a přidružených metadat
- Integrace s 3GPP Generic Authentication Architecture (GAA) pro zabezpečené doručení
- Podpora šifrování a ochrany integrity klíčového materiálu během přenosu
- Nese podstatné atributy klíčů jako Identifikátor klíče, Skupinový identifikátor a období platnosti
- Navrženo pro použití s různými skupinovými službami včetně MBMS a GCSE
- Umožňuje interoperabilitu mezi funkcemi správy klíčů a cílovými síťovými aplikacemi

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management

---

📖 **Anglický originál a plná specifikace:** [GKTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gktp/)
