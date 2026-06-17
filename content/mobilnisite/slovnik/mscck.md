---
slug: "mscck"
url: "/mobilnisite/slovnik/mscck/"
type: "slovnik"
title: "MSCCK – MBMS Sub-Channel Control Key"
date: 2026-01-01
abbr: "MSCCK"
fullName: "MBMS Sub-Channel Control Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mscck/"
summary: "Bezpečnostní klíč používaný ve službě Multimedia Broadcast Multicast Service (MBMS) k ochraně řídicích informací subkanálu. Zajišťuje integritu a důvěrnost plánovacích a konfiguračních údajů pro vysíl"
---

MSCCK je bezpečnostní klíč používaný v MBMS k ochraně integrity a důvěrnosti řídicích informací subkanálu, jako jsou plánovací a konfigurační údaje, což brání neoprávněnému přístupu a narušení služby.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Sub-Channel Control Key (MSCCK) je kryptografický klíč definovaný v rámci bezpečnostní architektury 3GPP pro službu Multimedia Broadcast Multicast Service (MBMS). Jeho hlavní funkcí je zabezpečit informace řídicí roviny spojené s MBMS subkanály. Služba MBMS může být rozdělena do více subkanálů, z nichž každý může nést odlišný obsah nebo úrovně kvality. Řídicí informace pro tyto subkanály, které zahrnují podrobnosti o plánování, konfigurační parametry a oznámení služeb, jsou přenášeny přes rozhraní vzduchem a musí být chráněny, aby byla zajištěna spolehlivost služby a zabránilo se podvržení nebo útokům typu odepření služby.

MSCCK je odvozen v rámci [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Centre) jako součást hierarchie klíčů MBMS. Je generován z nadřazeného klíče, MBMS Service Key ([MUK](/mobilnisite/slovnik/muk/)), pomocí funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)) se specifickými vstupními parametry, které identifikují službu a řídicí kanál. Tento odvozený klíč je pak použit k výpočtu hodnot ochrany integrity ([MAC](/mobilnisite/slovnik/mac/)) a volitelně k šifrování řídicích zpráv vysílaných na kanálech, jako je [MCCH](/mobilnisite/slovnik/mcch/) (MBMS Control Channel) nebo [MSCH](/mobilnisite/slovnik/msch/) (MBMS Scheduling Channel). Uživatelské zařízení (UE) přijímající službu MBMS musí také odvodit stejný MSCCK pomocí MUK, který si bezpečně opatřilo, což mu umožňuje ověřit integritu a dešifrovat řídicí informace.

Z architektonického hlediska MSCCK funguje v rámci bezpečnostního rámce MBMS definovaného v TS 33.246 a souvisejících specifikacích. Je klíčovým prvkem pro umožnění bezpečného selektivního dešifrování v MBMS. Tím, že existují samostatné klíče pro řídicí a přenosovou rovinu (MSCCK vs. [MTK](/mobilnisite/slovnik/mtk/) - MBMS Traffic Key), může síť poskytovat volně dostupné řídicí informace (chráněné MSCCK), zatímco skutečný mediální obsah zůstává šifrován jiným klíčem. Toto oddělení umožňuje flexibilní modely služeb, například umožňuje uživatelům objevovat a přihlašovat se ke službám prostřednictvím chráněných řídicích kanálů před zakoupením klíče pro samotný obsah. Role MSCCK je tedy zásadní pro bezpečné poskytování služeb, efektivní správu klíčů a robustní ochranu před útoky cílícími na mechanismy objevování služeb a konfigurace ve vysílacích sítích.

## K čemu slouží

MSCCK byl zaveden k řešení konkrétních bezpečnostních zranitelností v řídicí rovině MBMS. Raná nasazení MBMS se zaměřovala na zabezpečení přenosové roviny (samotného video nebo datového proudu) pomocí MTK. Řídicí informace nezbytné pro to, aby UE našlo, přihlásilo se a správně přijímalo službu MBMS, však byly často přenášeny nešifrovaně nebo s nedostatečnou ochranou. To vytvořilo vektor pro útoky, kdy škodliví aktéři mohli vkládat falešné plánovací informace, což způsobovalo, že se UE ladila na nesprávné frekvence nebo časové sloty, což vedlo k narušení služby (odepření služby) nebo vybití baterie.

Vytvoření MSCCK bylo motivováno potřebou holistického bezpečnostního přístupu pro vysílací služby. Řeší problém zajištění autenticity a integrity kritických metadat služby. Bez něj by útočník mohl falšovat oznámení služeb nebo upravovat plánovací parametry, což by podkopalo celý model služby MBMS. MSCCK umožňuje síti kryptograficky propojit řídicí informace s legitimním poskytovatelem služby (BM-SC), což zajišťuje, že UE jednají pouze na základě příkazů z důvěryhodného zdroje. To je zvláště důležité pro komerční služby, včetně mobilní televize a komunikací pro veřejnou bezpečnost, kde je spolehlivé a neporušitelné objevování služeb nezbytné. Jeho zavedení v rámci Rel-13 jako součást vylepšené bezpečnosti MBMS (eMBMS) odráží rostoucí důraz na robustní zabezpečení pro vysílací komponenty podporující 5G, jako je LTE-based 5G Broadcast.

## Klíčové vlastnosti

- Odvozen z MBMS User Key (MUK) pomocí standardizované funkce pro odvozování klíčů (KDF).
- Chrání integritu a volitelně i důvěrnost řídicích zpráv MBMS subkanálu.
- Umožňuje bezpečné objevování služeb a konfiguraci ochranou kanálů jako je MCCH a MSCH.
- Podporuje oddělení bezpečnosti řídicí a přenosové roviny (MSCCK vs. MTK) pro flexibilní modely služeb.
- Nezbytný pro prevenci podvržení a útoků typu odepření služby na řídicí rovině MBMS.
- Specifikován v rámci bezpečnostní architektury MBMS 3GPP v TS 33.246 a souvisejících dokumentech.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MUK – Multicast User Key](/mobilnisite/slovnik/muk/)
- [MTK – MBMS Traffic Key](/mobilnisite/slovnik/mtk/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [MSCH – MBMS point-to-multipoint Scheduling Channel](/mobilnisite/slovnik/msch/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services

---

📖 **Anglický originál a plná specifikace:** [MSCCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/mscck/)
