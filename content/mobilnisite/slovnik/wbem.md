---
slug: "wbem"
url: "/mobilnisite/slovnik/wbem/"
type: "slovnik"
title: "WBEM – Web-Based Enterprise Management"
date: 2025-01-01
abbr: "WBEM"
fullName: "Web-Based Enterprise Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/wbem/"
summary: "WBEM je soubor technologií pro správu a internetové standardy pro sjednocení správy distribuovaných IT prostředí. V 3GPP se používá pro rozhraní správy sítě, umožňující standardizovaný, webový přístup"
---

WBEM je soubor standardů pro správu používaných v 3GPP pro rozhraní správy sítě, umožňující webový přístup k informacím o správě.

## Popis

Web-Based Enterprise Management (WBEM) je komplexní soubor standardů pro správu přijatých 3GPP pro rozhraní správy sítě, zejména v kontextu systémů správy prvků ([EMS](/mobilnisite/slovnik/ems/)) a systémů správy sítě ([NMS](/mobilnisite/slovnik/nms/)). WBEM není původní technologie 3GPP, ale standard [DMTF](/mobilnisite/slovnik/dmtf/) (Distributed Management Task Force), který 3GPP využívá k poskytnutí webového, interoperabilního rámce pro správu síťových prvků. Jádrem WBEM je Common Information Model ([CIM](/mobilnisite/slovnik/cim/)), objektově orientované schéma, které jednotným způsobem popisuje informace o správě, a soubor protokolů jako CIM-XML přes [HTTP](/mobilnisite/slovnik/http/)/[SOAP](/mobilnisite/slovnik/soap/) pro přístup k těmto informacím.

Architektonicky zahrnuje WBEM v 3GPP několik klíčových komponent. Schéma CIM definuje spravované objekty reprezentující síťové zdroje, jako jsou základnové stanice, směrovače nebo softwarové funkce, s vlastnostmi, metodami a asociacemi. CIM Object Manager (CIMOM) funguje jako server, který hostuje úložiště CIM a poskytuje přístup ke spravovaným objektům. Aplikace pro správu (klienti) používají standardní webové protokoly ke komunikaci s CIMOM, typicky prostřednictvím CIM operací zapouzdřených v [XML](/mobilnisite/slovnik/xml/) a přenášených přes HTTP nebo [HTTPS](/mobilnisite/slovnik/https/). To umožňuje vzdálenou správu napříč různými dodavateli a platformami. Ve specifikacích 3GPP je WBEM často specifikován jako protokol pro referenční bod Itf-N (Interface-Northbound), spojující EMS s NMS nebo vyššími systémy provozní podpory (OSS).

Jak WBEM funguje v praxi, zahrnuje model klient-server, kde klient správy odesílá CIM operace jako GetInstance, EnumerateInstances nebo InvokeMethod na server (CIMOM) hostující spravované prvky. Například síťový operátor může použít WBEM klienta k získání výkonnostních metrik ze základnové stanice (reprezentované jako CIM objekt) odesláním požadavku GetInstance pro vlastnosti tohoto objektu. CIMOM zpracuje požadavek, komunikuje se skutečným síťovým prvkem přes proprietární rozhraní a vrátí data ve standardizovaném formátu XML. Podobně lze provádět změny konfigurace úpravou vlastností objektů nebo voláním metod. Použití HTTP/SOAP je příznivé pro firewally a snadnou integraci s webovými technologiemi.

Role WBEM v sítích 3GPP spočívá ve standardizaci rozhraní správy, což snižuje náklady na integraci a umožňuje interoperabilitu mezi více dodavateli. Poskytuje společný jazyk (CIM) pro popis dat správy, což je klíčové pro automatizované zřizování, správu poruch, monitorování výkonu a správu konfigurace. Přijetím WBEM 3GPP zajišťuje, že síťové prvky od různých výrobců mohou být spravovány jednotně prostřednictvím vyšších systémů OSS/BSS. To je zvláště důležité v moderních sítích s virtualizovanými síťovými funkcemi (VNF) a cloud-nativními architekturami, kde je vyžadována dynamická správa. Rozšiřitelnost WBEM umožňuje 3GPP definovat specifické CIM profily pro telekomunikace, jako jsou profily pro 5G síťové řezy nebo správu NFV.

## K čemu slouží

WBEM byl začleněn do standardů 3GPP počínaje Release 4, aby řešil rostoucí složitost a heterogenitu správy telekomunikačních sítí. Před WBEM byla rozhraní správy často proprietární nebo založená na různých protokolech jako SNMP, CMIP nebo CORBA, což vedlo k vysokým nákladům na integraci, nedostatku interoperability a izolovaným systémům správy. Jak se sítě vyvíjely a zahrnovaly zařízení od více dodavatelů a nové služby, se standardizovaný, flexibilní rámec správy stal nezbytným.

Primární problém, který WBEM řeší, je sjednocení informací o správě a operací napříč různými síťovými doménami a dodavateli. Využitím webových standardů (HTTP, XML) a objektově orientovaného informačního modelu (CIM) poskytuje WBEM konzistentní způsob reprezentace a přístupu k datům správy. To umožňuje operátorům vytvářet integrovaná OSS, která mohou spravovat celé sítě z jednoho místa. Pro 3GPP znamenalo přijetí WBEM sladění se standardy IT průmyslu a usnadnění konvergence mezi telekomunikačními a IT postupy správy, což je klíčové pro vznikající technologie jako virtualizace síťových funkcí (NFV) a softwarově definované sítě (SDN).

Dále WBEM podporuje automatizaci a škálovatelnost vyžadovanou pro moderní sítě. Jeho webová povaha umožňuje vzdálenou správu přes IP sítě, což je zásadní pro distribuovaná nasazení. Rozšiřitelné schéma CIM umožňuje 3GPP definovat podrobné modely pro 5G síťové řezy, kvalitu služeb nebo správu účastníků. Historicky odráželo přijetí WBEM v 3GPP posun směrem k otevřenějším, programovatelným rozhraním správy a snížení závislosti na starších protokolech TMN (Telecommunications Management Network). WBEM byl tedy motivován potřebou nákladově efektivní, interoperabilní a budoucím potřebám odolné správy sítě v rozvíjejících se mobilních sítích.

## Klíčové vlastnosti

- Založeno na standardech DMTF (CIM, CIM-XML) pro jednotnou správu
- Používá webové protokoly (HTTP/SOAP) pro firewall-přátelský vzdálený přístup
- Objektově orientované schéma Common Information Model (CIM) pro reprezentaci dat
- Podporuje operace jako Get, Enumerate, Invoke pro úlohy správy
- Umožňuje interoperabilitu mezi více dodavateli prostřednictvím standardizovaných rozhraní
- Rozšiřitelné pro definici specifických 3GPP profilů a objektů správy

## Související pojmy

- [CIM – Common Information Model](/mobilnisite/slovnik/cim/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM

---

📖 **Anglický originál a plná specifikace:** [WBEM na 3GPP Explorer](https://3gpp-explorer.com/glossary/wbem/)
