---
slug: "emsk"
url: "/mobilnisite/slovnik/emsk/"
type: "slovnik"
title: "EMSK – Extended Master Session Key"
date: 2026-01-01
abbr: "EMSK"
fullName: "Extended Master Session Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/emsk/"
summary: "Kryptograficky silný klíč odvozený během procedury 5G Authentication and Key Agreement (AKA). Slouží jako kořenový klíč pro generování dalších klíčů používaných k zabezpečení specifických síťových slu"
---

EMSK je kořenový klíč odvozený během 5G AKA autentizace, ze kterého se generují další klíče pro zabezpečení specifických síťových služeb a aplikačních relací nad rámec přístupu k jádru sítě.

## Popis

Extended Master Session Key (EMSK) je výstupní klíčový materiál generovaný protokolem Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) v systémech 3GPP, konkrétně definovaný od Release 14 pro 5G a vylepšené systémy. Je odvozen spolu s Master Session Key ([MSK](/mobilnisite/slovnik/msk/)) během úspěšného autentizačního procesu mezi uživatelským zařízením (UE) a sítí. Odvození používá stejné kryptografické vstupy jako MSK (jako je sdílené tajemství K, náhodné výzvy a identifikátory sítě), ale aplikuje odlišný štítek (label) Key Derivation Function ([KDF](/mobilnisite/slovnik/kdf/)) pro vytvoření samostatného, nezávislého klíče. EMSK není exportován z instance protokolu AKA; místo toho je uchováván lokálně v entitě, která AKA provedla (typicky v UE a Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) v 5G).

Jak to funguje, je založeno na hierarchii a odvozování klíčů. Po úspěšném 5G AKA nezávisle vypočítají EMSK jak UE, tak AUSF. Tento klíč není nikdy přenášen vzduchem ani do jiných síťových funkcí v surové podobě. Jeho primární role je sloužit jako kořenový klíč pro odvození dalších specifických kryptografických klíčů. Tyto následné klíče jsou generovány aplikací KDF na EMSK spolu s dalšími vazebními parametry (jako je identita služby, identifikátor slicu nebo řetězce specifické pro aplikaci). Tento proces vytváří kryptograficky oddělené klíče pro různé účely, což zajišťuje izolaci klíčů.

Jeho role v síti spočívá v poskytnutí bezpečného základu pro klíčový materiál nad rámec tradičního přístupového zabezpečení. Zatímco klíče odvozené z KAUSF (který je sám odvozen z [CK](/mobilnisite/slovnik/ck/), [IK](/mobilnisite/slovnik/ik/) v 5G AKA) chrání Radio Access Network (RAN) a signalizaci [NAS](/mobilnisite/slovnik/nas/), klíče odvozené z EMSK mohou být použity k zabezpečení relací na aplikační vrstvě, komunikací přes rozhraní založená na službách mezi síťovými funkcemi nebo k poskytnutí autentizace pro specifická síťová dělení (slices). To umožňuje flexibilní a škálovatelný bezpečnostní model pro 5G Service-Based Architecture ([SBA](/mobilnisite/slovnik/sba/)) a podporuje bezpečnostní požadavky síťového dělení tím, že umožňuje generování aplikačních klíčů specifických pro konkrétní slice.

## K čemu slouží

EMSK byl zaveden, aby řešil potřebu standardizovaného, kryptograficky robustního kořenového klíče, který by mohl být použit k zabezpečení služeb a aplikací nad rámec tradičního rozsahu přístupového zabezpečení sítí 3GPP. Před jeho definicí neexistoval v rámci 3GPP standardizovaný mechanismus pro odvozování klíčů na ochranu aplikačních relací nebo komunikací založených na službách, které by spoléhaly na primární AKA proceduru. Tento požadavek se stal kritickým s příchodem 5G a jeho Service-Based Architecture.

Historický kontext je evoluce směrem k síťovému dělení a oddělení síťových funkcí. 5G jádrová síť se svou SBA vyžaduje zabezpečenou komunikaci mezi různými síťovými funkcemi (NFs). Navíc jedno předplatné UE může přistupovat k více izolovaným síťovým řezům (slices), z nichž každý může vyžadovat vlastní sadu bezpečnostních klíčů na aplikační úrovni. EMSK poskytuje společný, důvěryhodný zdroj pro odvozování těchto různorodých klíčů, čímž zajišťuje, že jsou kryptograficky svázány s počáteční uživatelskou autentizací.

Řeší problém škálovatelnosti správy klíčů a jejich izolace pro pokročilé služby. Odvozováním klíčů specifických pro službu z EMSK se systém vyhne složitosti a potenciálnímu riziku provádění samostatných autentizačních protokolů pro každou službu nebo slice. Také zachovává jasné bezpečnostní oddělení; kompromitace klíče odvozeného pro jednu službu (např. klíče specifického pro slice) neohrozí klíče pro přístup k jádru sítě ani klíče odvozené pro jiné služby, protože všechny pocházejí z různých větví stromu odvozování klíčů zakořeněného v EMSK.

## Klíčové vlastnosti

- Odvozen během 5G AKA spolu s MSK
- Uchováván lokálně a nikdy neexportován v surové podobě
- Slouží jako kořenový klíč pro další odvozování klíčů
- Umožňuje generování aplikačních klíčů specifických pro službu a pro síťový slice
- Poskytuje izolaci klíčů mezi různými službami a přístupovou vrstvou jádra sítě
- Základní pro zabezpečení komunikací v 5G Service-Based Architecture

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [MSK – Minimum-shift keying](/mobilnisite/slovnik/msk/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)

## Definující specifikace

- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps

---

📖 **Anglický originál a plná specifikace:** [EMSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/emsk/)
