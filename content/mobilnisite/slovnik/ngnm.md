---
slug: "ngnm"
url: "/mobilnisite/slovnik/ngnm/"
type: "slovnik"
title: "NGNM – Next Generation Networks Management"
date: 2025-01-01
abbr: "NGNM"
fullName: "Next Generation Networks Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ngnm/"
summary: "NGNM je komplexní rámec pro správu sítí příští generace včetně 4G a 5G. Poskytuje standardizované principy, požadavky a architektury pro správu sítě, což operátorům umožňuje efektivně spravovat složit"
---

NGNM je komplexní standardizovaný rámec principů, požadavků a architektur pro správu složitých sítí příští generace, jako jsou 4G a 5G, v prostředí více dodavatelů, aby byla zajištěna kvalita služeb a provozní efektivita.

## Popis

Next Generation Networks Management (NGNM) je holistický rámec definovaný organizací 3GPP, který řeší provozní a manažerské výzvy vyvíjejících se mobilních sítí. Není to jediný protokol nebo rozhraní, ale soubor principů, požadavků a architektonických směrnic pokrývajících celý životní cyklus sítě včetně správy poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS). Rámec je detailně popsán v řadě specifikací 3GPP série 32, přičemž TS 32.102 poskytuje základní architekturu a principy správy. Cílem NGNM je vytvořit jednotné prostředí pro správu, které zvládne složitost zavedenou virtualizací síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)), softwarově definovanými sítěmi ([SDN](/mobilnisite/slovnik/sdn/)), síťovým dělením na řezy (network slicing) a konvergencí více přístupových technologií.

Architektonicky je NGNM postaven na hierarchickém a vrstveném modelu. Jeho jádrem je koncept Systému správy ([MS](/mobilnisite/slovnik/ms/)), který komunikuje se spravovanými prvky ([ME](/mobilnisite/slovnik/me/)) nebo síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) prostřednictvím standardizovaných rozhraní. Klíčovým principem je oddělení řídicí roviny správy od uživatelské a řídicí roviny, což umožňuje centralizovanou orchestraci a automatizaci řízenou politikami. Rámec podporuje jak koncepty dědictví z Telekomunikační sítě pro správu ([TMN](/mobilnisite/slovnik/tmn/)), tak moderní přístupy jako je správa řízená modely, kde datové modely (např. YANG) definují strukturu a sémantiku spravovaných zdrojů. To umožňuje automatizovanou konfiguraci, sledování výkonu v reálném čase a operace s uzavřenou smyčkou.

Úlohou NGNM je zajistit, aby mohli operátoři sítí efektivně nasazovat, poskytovat, monitorovat a optimalizovat služby. Definuje služby správy pro konkrétní domény, jako je 5G Core Network (5GC) a Next Generation Radio Access Network (NG-RAN). Například specifikuje, jak spravovat síťové řezy – klíčovou funkci 5G – včetně správy životního cyklu řezu, zajištění výkonu a izolace poruch. Rámec také řeší správu virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) v souladu se standardy [ETSI](/mobilnisite/slovnik/etsi/) NFV, pokrývající oblasti jako zavedení VNF, vytváření instancí, škálování a ukončování. Poskytnutím těchto standardizovaných vzorů NGNM snižuje integrační náklady, usnadňuje interoperabilitu mezi více dodavateli a připravuje cestu pro plně autonomní sítě.

## K čemu slouží

NGNM byl vytvořen, aby řešil rostoucí složitost a provozní náklady spojené se správou mobilních sítí příští generace. Před jeho formalizací byla správa sítě často specifická pro dodavatele, izolovaná a vyžadovala významný podíl ruční práce. Přechod od monolitických síťových prvků založených na hardwaru k virtualizovaným softwarovým funkcím v 4G a 5G přinesl nové výzvy v oblasti správy životního cyklu, dynamického škálování a zajištění služeb. NGNM poskytuje standardizovaný rámec pro správu tohoto nového paradigmatu.

Historický kontext spočívá ve vývoji od jednoduchých systémů správy prvků (EMS) k integrovaným systémům správy sítě (NMS) a nakonec ke komplexní správě služeb napříč celou sítí. Omezení předchozích přístupů zahrnovala proprietární rozhraní, nedostatek možností automatizace a neschopnost vyrovnat se s dynamickou povahou cloud-nativních sítí. NGNM tyto problémy řeší definováním společného jazyka a architektury pro správu. Umožňuje operátorům automatizovat rutinní úlohy, implementovat řízení založené na politikách a získat jednotný pohled na síťové zdroje a služby napříč různými technologiemi a administrativními doménami.

Navíc je NGNM nezbytný pro naplnění obchodních slibů 5G, jako je síťové dělení na řezy (network slicing) a ultra-spolehlivá komunikace s nízkou latencí (URLLC). Bez robustního standardizovaného rámce pro správu by bylo nepraktické vytvářet, monitorovat a garantovat výkon pro jednotlivé síťové řezy. NGNM poskytuje potřebné nástroje pro provoz řezů jako služby, což operátorům umožňuje nabízet přizpůsobené služby podnikovým zákazníkům se specifickými požadavky na QoS při zachování efektivního využití podkladových fyzických zdrojů.

## Klíčové vlastnosti

- Standardizovaná architektura a principy správy pro interoperabilitu více dodavatelů
- Podpora správy životního cyklu virtualizovaných síťových funkcí (VNF/CNF)
- Rámec pro komplexní správu síťových řezů napříč celou sítí včetně vytváření, monitorování a zajištění kvality
- Správa řízená modely a zpřístupnění dat pro automatizaci a operace využívající AI/ML
- Integrace s rámci ETSI NFV MANO (Management and Orchestration)
- Komplexní pokrytí funkcí správy FCAPS (Fault, Configuration, Accounting, Performance, Security)

## Související pojmy

- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [NGNM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngnm/)
