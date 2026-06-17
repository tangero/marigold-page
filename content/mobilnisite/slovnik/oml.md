---
slug: "oml"
url: "/mobilnisite/slovnik/oml/"
type: "slovnik"
title: "OML – Operations and Maintenance Link"
date: 2025-01-01
abbr: "OML"
fullName: "Operations and Maintenance Link"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oml/"
summary: "Rozhraní pro provoz a údržbu (Operations and Maintenance Link, OML) je standardizované rozhraní v sítích 3GPP používané pro správu a údržbu síťových prvků. Umožňuje přenos provozních, administrativníc"
---

OML je standardizované rozhraní 3GPP pro přenos provozních, administrativních a údržbových dat mezi řídicími systémy a síťovými prvky za účelem realizace správy FCAPS.

## Popis

Rozhraní pro provoz a údržbu (Operations and Maintenance Link, OML) je klíčové řídicí rozhraní definované ve specifikacích 3GPP, primárně v TS 21.905. Slouží jako komunikační cesta mezi systémy podpory provozu ([OSS](/mobilnisite/slovnik/oss/)) nebo systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) a různými síťovými prvky ([NE](/mobilnisite/slovnik/ne/)) v architektuře 3GPP, jako jsou Node B, eNode B, gNB a uzly jádra sítě. OML přenáší informace o provozu, správě a údržbě (OAM), které jsou nezbytné pro každodenní fungování, monitorování a řízení sítě. Podporuje model FCAPS, který zahrnuje správu poruch (hlášení alarmů a diagnostiku), správu konfigurace (aktualizace softwaru, nastavení parametrů), správu účtování (údaje o využití pro fakturaci), správu výkonu (sběr klíčových ukazatelů výkonu neboli [KPI](/mobilnisite/slovnik/kpi/)) a správu zabezpečení (vynucování bezpečnostních politik a auditní záznamy).

Z architektonického hlediska je OML logické rozhraní, které může být implementováno přes různé fyzické a transportní protokoly. Často je realizováno pomocí protokolů založených na IP, se specifickými OAM protokoly, jako je SNMP (Simple Network Management Protocol), rozhraní založená na [CORBA](/mobilnisite/slovnik/corba/) (Common Object Request Broker Architecture) podle definice v rámci 3GPP [IRP](/mobilnisite/slovnik/irp/) (Integration Reference Point), nebo modernější RESTful [API](/mobilnisite/slovnik/api/) a modely NETCONF/YANG v novějších verzích. Rozhraní definuje vztah manažer-agent, kde NMS vystupuje jako manažer iniciující požadavky a síťový prvek implementuje agenta, který na tyto požadavky reaguje a může odesílat asynchronní notifikace (například alarmy).

Klíčové součásti zapojené do OML zahrnují aplikační funkci správy v NMS, modely spravovaných objektů reprezentující zdroje a schopnosti síťového prvku a komunikační protokoly, které je spojují. Úlohou OML je poskytnout standardizovaný, na dodavateli nezávislý prostředek pro síťové operátory, aby mohli integrovat zařízení od různých dodavatelů do jediného soudržného rámce správy. Tímto je vrstva správy sítě oddělena od podkladového hardwaru a implementací specifických pro dodavatele, což je zásadní pro rozsáhlá nasazení mobilních sítí s více dodavateli. Umožňuje centralizovanou provizi, monitorování v reálném čase, automatizované zotavení po poruchách a efektivní plánování kapacity.

## K čemu slouží

OML bylo zavedeno, aby řešilo kritickou potřebu standardizované správy sítě v stále složitějších sítích 3GPP s více dodavateli. Před jeho formální definicí čelili síťoví operátoři významným výzvám při integraci zařízení od různých výrobců, protože každý dodavatel používal proprietární řídicí rozhraní, protokoly a datové modely. To vedlo k vysokým provozním nákladům, složitým integračním projektům a omezené flexibilitě v síťových operacích a nasazování služeb. Vytvoření OML mělo za cíl tyto problémy s interoperabilitou vyřešit.

Jeho vývoj byl motivován přechodem k otevřeným, standardizovaným architekturám v telekomunikacích, hnán potřebou provozní efektivity a snížení závislosti na konkrétním dodavateli. Specifikací společného rozhraní pro provoz a údržbu (OML) umožnilo 3GPP operátorům používat jediný systém správy pro řízení a monitorování všech síťových prvků bez ohledu na dodavatele. Tato standardizace je klíčová pro model správy FCAPS, neboť umožňuje konzistentní detekci poruch, sběr dat o výkonu a vzdálenou konfiguraci v celé síti. Tvořila páteř pro automatizované a efektivní síťové operace, což se stalo ještě důležitějším s růstem sítí v nasazeních 3G, 4G a 5G, zahrnujících tisíce základnových stanic a komplexních funkcí jádra sítě.

## Klíčové vlastnosti

- Standardizované rozhraní pro správu síťových prvků od více dodavatelů
- Podporuje kompletní model správy FCAPS (Fault, Configuration, Accounting, Performance, Security)
- Umožňuje sledování alarmů, izolaci poruch a diagnostické testování
- Usnadňuje správu softwaru a firmwaru, včetně stahování a aktivace
- Poskytuje mechanismy pro sběr a hlášení dat měření výkonu
- Definuje zabezpečenou komunikaci pro přenos řídicích dat a řízení přístupu

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [OML na 3GPP Explorer](https://3gpp-explorer.com/glossary/oml/)
