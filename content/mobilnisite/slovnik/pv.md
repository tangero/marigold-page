---
slug: "pv"
url: "/mobilnisite/slovnik/pv/"
type: "slovnik"
title: "PV – Parameter Value"
date: 2025-01-01
abbr: "PV"
fullName: "Parameter Value"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pv/"
summary: "Parameter Value (PV) je základní datová struktura používaná při správě sítí 3GPP, konkrétně v rámci specifikací rozhraní Itf-N. Představuje pojmenovaný datový prvek obsahující konkrétní hodnotu, která"
---

PV je základní pojmenovaná datová struktura obsahující konkrétní hodnotu používanou při správě sítí 3GPP ke konfiguraci, monitorování nebo hlášení stavu síťové funkce nebo zdroje.

## Popis

V kontextu telekomunikační správy 3GPP je [Parameter](/mobilnisite/slovnik/parameter/) Value (PV) klíčový konstrukt definovaný v rámci frameworku Interface-N (Itf-N), který standardizuje severovýchodní rozhraní (northbound interface) mezi systémem správy prvků (Element Management System, [EMS](/mobilnisite/slovnik/ems/)) nebo systémem správy sítě (Network Management System, [NMS](/mobilnisite/slovnik/nms/)) a síťovou funkcí (Network Function, [NF](/mobilnisite/slovnik/nf/)). PV je v podstatě pojmenovaná proměnná, která uchovává konkrétní kus dat. Je definována jedinečným názvem (parameter ID) a hodnotou, která odpovídá specifikovanému datovému typu, jako je celé číslo, řetězec, logická hodnota nebo složitější strukturovaný typ. PV se používají k modelování každého spravovatelného aspektu síťového prvku, od podrobností inventáře hardwaru (např. sériové číslo desky) a verzí softwaru až po provozní stav (např. administrative state = unlocked) a čítače výkonu (např. počet ztracených hovorů).

Architektura informací pro správu v 3GPP je často modelována pomocí objektově orientovaného paradigmatu, kde spravované objekty (Managed Objects, [MO](/mobilnisite/slovnik/mo/)) reprezentují fyzické nebo logické zdroje (např. buňku, desku, spojení). Každý spravovaný objekt má atributy a tyto atributy jsou realizovány jako Parameter Values. PV je tedy instancí atributu pro konkrétní instanci spravovaného objektu. Například spravovaný objekt 'Cell' by měl atribut 'cellId' a PV pro tento atribut by obsahovala skutečný identifikátor, např. 'cellId' = 42. Operace správy – jako GET, [SET](/mobilnisite/slovnik/set/), CREATE, DELETE a NOTIFY – se provádějí na těchto spravovaných objektech a jejich součástných PV. Operace GET načte aktuální PV, operace SET modifikuje zapisovatelné PV pro konfiguraci a operace NOTIFY umožňuje síťovému prvku asynchronně odeslat aktualizované PV do systému správy pro hlášení alarmů nebo změn stavu.

Jak PV fungují v praxi, zahrnuje dobře definovaný protokolový zásobník, typicky používající [CORBA](/mobilnisite/slovnik/corba/) nebo v poslední době RESTful [API](/mobilnisite/slovnik/api/), jak je specifikováno v 3GPP TS 32.150 a podrobně popsáno v TS 37.462 pro Itf-N. Systém správy odešle požadavek obsahující cílovou instanci objektu a PV, na které se má operace provést. Agent správy síťového prvku požadavek zpracuje, komunikuje se skutečným zdrojem, aby přečetl nebo upravil odpovídající provozní parametry, a vrátí odpověď obsahující výsledné PV. Tato abstrakce poskytovaná PV je klíčová pro interoperabilitu mezi více dodavateli, protože umožňuje standardnímu systému správy od jednoho dodavatele konfigurovat a monitorovat síťové prvky od jiného dodavatele, pokud oba dodržují standardizovaný informační model a definice PV.

## K čemu slouží

Koncept Parameter Value existuje, aby vyřešil kritický problém standardizované a interoperabilní správy sítě v telekomunikačních prostředích s více dodavateli. Před takovou standardizací každý dodavatel zařízení používal pro svá rozhraní správy proprietární protokoly a datové modely, což nutilo operátory sítí nasazovat samostatné, na dodavateli závislé systémy správy. To vedlo k provozní složitosti, vysokým integračním nákladům a neschopnosti automatizovat end-to-end zřizování služeb napříč heterogenními síťovými doménami. Vytvoření rozhraní Itf-N a formální definice PV v rámci 3GPP bylo motivováno potřebou společného jazyka pro komunikační správu.

PV poskytují atomické stavební kameny pro tento společný jazyk. Řeší omezení nestandardizované reprezentace dat tím, že přesně definují, jaké informace lze vyměňovat, jejich formát a sémantiku. To umožňuje vývoj obecných aplikací pro správu, které mohou provádět funkce správy poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS) na jakémkoli kompatibilním síťovém prvku. Historický kontext spočívá v širších frameworkech telekomunikační správy, jako je TMN (Telecommunications Management Network), které ovlivnily architekturu správy 3GPP. PV uvádějí do praxe informační modely definované ve standardech, mění abstraktní definice na konkrétní data, která lze přenášet přes síť, a tím umožňují automatizovanou, efektivní a spolehlivou správu stále složitějších sítí 3GPP.

## Klíčové vlastnosti

- Atomický datový prvek s definovaným názvem (Parameter ID) a typovanou hodnotou
- Reprezentuje atribut spravovaného objektu (Managed Object) v informačním modelu správy 3GPP
- Používá se ve všech základních operacích správy: GET, SET, CREATE, DELETE, NOTIFY
- Podporuje širokou škálu datových typů včetně primitivních typů a komplexních struktur
- Umožňuje standardizované zřizování konfigurace (provisioning) a monitorování výkonu
- Základ pro hlášení alarmů a změn stavu prostřednictvím asynchronních notifikací

## Související pojmy

- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)

## Definující specifikace

- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [PV na 3GPP Explorer](https://3gpp-explorer.com/glossary/pv/)
