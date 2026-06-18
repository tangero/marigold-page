---
slug: "tarr"
url: "/mobilnisite/slovnik/tarr/"
type: "slovnik"
title: "TARR – Test Action Request Receiver"
date: 2025-01-01
abbr: "TARR"
fullName: "Test Action Request Receiver"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tarr/"
summary: "Síťový prvek v systému správy 3GPP (3GPP MS), který přijímá a zpracovává požadavky na testovací akce. Je klíčovou součástí pro automatizované testování a validaci síťových funkcí a služeb, což umožňuj"
---

TARR je síťový prvek v systému správy 3GPP, který přijímá a zpracovává požadavky na testovací akce pro automatizované testování a validaci síťových funkcí a služeb.

## Popis

Příjemce požadavků na testovací akce (Test Action Request Receiver, TARR) je funkční entita definovaná v architektuře systému správy 3GPP, konkrétně pro účely testování sítě a diagnostiky. Funguje jako serverová komponenta, která naslouchá a zpracovává standardizované požadavky na testovací akce. Tyto požadavky jsou typicky generovány dispečerem testovacích akcí (Test Action Dispatcher, [TAD](/mobilnisite/slovnik/tad/)) nebo jinými aplikacemi správy jako součást automatizovaných testovacích sad, postupů správy poruch nebo pracovních postupů validace služeb. TARR je zodpovědný za interpretaci příchozího požadavku, který je formátován podle specifikací 3GPP (např. pomocí protokolů založených na [XML](/mobilnisite/slovnik/xml/)), a následně za provedení odpovídající testovací logiky nebo spuštění příslušných testovacích podnětů na testované síti nebo síťovém prvku.

Architektonicky je TARR součástí operačního podpůrného systému (Operations Support System, [OSS](/mobilnisite/slovnik/oss/)) nebo systému správy sítě (Network Management System, [NMS](/mobilnisite/slovnik/nms/)). Spojuje se s dispečerem testovacích akcí a dalšími funkcemi správy prostřednictvím standardizovaných rozhraní, jako je Itf-N (northern rozhraní) nebo jiných referenčních bodů správy definovaných v rámci 3GPP pro správu a orchestraci (Management and Orchestration, [MANO](/mobilnisite/slovnik/mano/)). TARR může být samostatný server nebo softwarový modul integrovaný do větší platformy pro správu sítě. Jeho implementace zahrnuje robustní parsování zpráv, bezpečnostní autentizaci příchozích požadavků a spolehlivé prováděcí stroje pro provedení požadovaných testů, které mohou sahat od jednoduchých testů spojení (ping) až po složité vícekrokové postupy validace služeb.

Role TARR je klíčová pro umožnění proaktivního a reaktivního zajištění sítě. Operátorům umožňuje automatizovat provádění testovacích případů, snižovat manuální zásahy a umožnit kontinuální validaci výkonu sítě a kvality služeb. Standardizací příjemce pro testovací akce zajišťuje 3GPP interoperabilitu mezi systémy správy a síťovými prvky nebo řízenými testovacími systémy. Fungování TARR je podrobně popsáno ve specifikacích 3GPP, jako je TS 32.321, která definuje koncepty správy testů, a TS 32.326/327, které pokrývají informační model a postupy pro správu testů.

## K čemu slouží

TARR byl zaveden, aby řešil rostoucí složitost sítí 3GPP a potřebu standardizovaného, automatizovaného testování v rámci operací správy sítě. Před jeho standardizací bylo testování a validace síťových funkcí často prováděno pomocí proprietárních, dodavatelsky specifických nástrojů a skriptů, což vedlo k problémům s interoperabilitou a vysokým provozním nákladům v prostředích sítí s více dodavateli. Vytvoření standardizovaného příjemce požadavků na testovací akce umožňuje oddělenou architekturu, kde mohou aplikace pro správu testů odesílat příkazy generickému příjemci, který následně komunikuje s konkrétními síťovými prvky nebo testovacím vybavením.

Tento přístup řeší problém automatizace testování ve velkém měřítku. Umožňuje síťovým operátorům definovat testovací sady a scénáře způsobem nezávislým na dodavateli a provádět je napříč různými síťovými doménami a technologiemi. TARR jako součást systému správy 3GPP podporuje širší cíle samoorganizujících se sítí (Self-Organizing Networks, [SON](/mobilnisite/slovnik/son/)) a automatizovaných operací tím, že poskytuje spolehlivý mechanismus pro spouštění diagnostických akcí, sběr výsledků a ověřování integrity služeb bez manuálního zásahu. Jeho vývoj byl motivován přechodem průmyslu k více softwarově řízeným, agilním síťovým operacím vyžadujícím postupy průběžné integrace a nasazování ([CI](/mobilnisite/slovnik/ci/)/[CD](/mobilnisite/slovnik/cd/)), kde je automatizované testování základní součástí.

## Klíčové vlastnosti

- Standardizované rozhraní pro přijímání požadavků na testovací akce
- Podporuje automatizované provádění síťových diagnostických a validačních testů
- Integruje se s architekturou systému správy 3GPP (OSS/NMS)
- Umožňuje správu a orchestraci testů nezávislou na dodavateli
- Usnadňuje interoperabilitu v síťových prostředích s více dodavateli
- Podporuje testovací scénáře pro proaktivní monitoring i reaktivní správu poruch

## Definující specifikace

- **TS 32.321** (Rel-19) — Test Management IRP: Requirements
- **TS 32.326** (Rel-19) — Test Management IRP Solution Set Definitions
- **TS 32.327** (Rel-9) — Test Management IRP SOAP Solution Set

---

📖 **Anglický originál a plná specifikace:** [TARR na 3GPP Explorer](https://3gpp-explorer.com/glossary/tarr/)
