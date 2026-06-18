---
slug: "csid"
url: "/mobilnisite/slovnik/csid/"
type: "slovnik"
title: "CSID – Call Segment Identifier"
date: 2025-01-01
abbr: "CSID"
fullName: "Call Segment Identifier"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/csid/"
summary: "CSID je jedinečný identifikátor pro segment v rámci hovoru nebo relace, který umožňuje podrobnou kontrolu a účtování v sítích IMS/CS. Umožňuje síťovým funkcím rozlišovat a aplikovat politiky na konkré"
---

CSID je jedinečný identifikátor pro segment v rámci hovoru nebo relace, který umožňuje podrobnou kontrolu, účtování a aplikaci politik na konkrétní části komunikace v sítích IMS/CS.

## Popis

Call Segment Identifier (CSID) je základní konstrukt v rámci 3GPP architektur pro účtování a řízení, konkrétně definovaný v kontextu IP Multimedia Subsystem (IMS) a starších okruhově přepínaných ([CS](/mobilnisite/slovnik/cs/)) domén. Slouží jako jedinečný štítek přiřazený samostatnému segmentu hovoru nebo relace. „Segment hovoru“ představuje logickou část end-to-end komunikace, což může být počáteční pokus o hovor, přesměrovaná větev, převedený segment nebo stream účastníka v rámci konference. CSID umožňuje síťovým entitám, zejména Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) a Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)), korelovat účtovací události a aplikovat politiky na tyto jednotlivé segmenty namísto toho, aby byl celý hovor považován za monolitickou entitu.

Architektonicky je CSID generován a spravován síťovými uzly zapojenými do řízení relace, jako je Serving Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) v IMS nebo Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) v CS sítích. Když dojde k události sestavení, změny nebo přesměrování hovoru, tyto řídicí uzly přiřadí novému segmentu nový CSID. Tento identifikátor je pak zahrnut v účtovacích zprávách, jako jsou záznamy Accounting Request ([ACR](/mobilnisite/slovnik/acr/)) v systému offline účtování ([OFCS](/mobilnisite/slovnik/ofcs/)) založeném na protokolu Diameter nebo účtovací události v systému online účtování ([OCS](/mobilnisite/slovnik/ocs/)). Charging Data Function používá CSID spolu s dalšími identifikátory, jako je IMS Charging Identifier (ICID), k sestavení úplného záznamu o účtovacích datech (CDR), který přesně odráží složitou topologii hovoru zahrnujícího více stran nebo služeb.

Role CSID přesahuje pouhou korelaci účtování. Umožňuje pokročilou servisní logiku a vynucování politik. Například ve scénáři přesměrování hovoru může síť aplikovat na počáteční volající větev a na přesměrovanou větev různé tarify na základě jejich příslušných CSID. V případě předplacených služeb může Online Charging System sledovat spotřebu kreditu na segment, což umožňuje podrobnější kontrolu. CSID navíc usnadňuje zpracování chyb a odstraňování problémů tím, že poskytuje jasný sledovatelný identifikátor pro každý segment v signalizační cestě hovoru, což pomáhá při izolaci chyb a zajištění služeb.

## K čemu slouží

CSID byl zaveden, aby řešil omezení starších účtovacích systémů, které se potýkaly se složitými scénáři hovorů běžnými v moderní telekomunikaci. Před jeho standardizací účtovací mechanismy často zacházely s více-segmentovým hovorem (např. zahrnujícím přesměrování, převod nebo konferenci) jako s jedinou událostí. To ztěžovalo přesné přiřazení nákladů, aplikaci diferencovaných tarifů pro různé větve hovoru nebo implementaci politik spravedlivého využití pro konkrétní součásti služby. Nedostatek granularity na úrovni segmentů také komplikoval vyřizování fakturačních sporů a provádění servisní logiky.

Primární motivací pro vytvoření CSID byla podpora sofistikovaných servisních schopností IP Multimedia Subsystem (IMS) a vyvíjejících se okruhově přepínaných sítí. IMS umožnilo bohaté komunikační služby, jako je přesměrování hovoru při nezvednutí, převod hovoru a multimediální konference, které se přirozeně skládají z více propojených segmentů. CSID poskytuje nezbytný technický základ pro nezávislé sledování těchto segmentů. Řeší problém korelace účtování v distribuovaném, multi-operatorním prostředí, kde různé síťové uzly mohou zpracovávat různé segmenty stejného end-to-end hovoru.

Tím, že umožňuje identifikaci na úrovni segmentu, CSID umožňuje operátorům implementovat detailní, přesné a flexibilní účtovací modely. Podporuje obchodní modely, kde na různé části služby platí různé sazby (např. prémiová sazba za konferenční most). Navíc poskytuje granularitu potřebnou pro zákonné odposlechy a monitorování služeb na úrovni segmentu, čímž splňuje regulatorní požadavky. Jeho vznik byl hnán potřebou odvětví po standardizovaném, robustním mechanismu pro zvládání finančních a provozních komplikací, které přinášejí pokročilé telefonní služby.

## Klíčové vlastnosti

- Jednoznačná identifikace jednotlivých segmentů hovoru/relace
- Umožňuje korelaci účtovacích událostí napříč složitými topologiemi hovorů
- Podporuje diferencované účtovací politiky pro jednotlivé větve hovoru
- Usnadňuje přesné generování CDR v systémech offline a online účtování
- Integruje se s účtovacími architekturami sítí IMS a starších CS
- Napomáhá provádění servisní logiky a odstraňování problémů na úrovni segmentu

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [CSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/csid/)
