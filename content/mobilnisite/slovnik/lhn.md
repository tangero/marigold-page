---
slug: "lhn"
url: "/mobilnisite/slovnik/lhn/"
type: "slovnik"
title: "LHN – Local Home Network Identifier"
date: 2025-01-01
abbr: "LHN"
fullName: "Local Home Network Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lhn/"
summary: "Identifikátor používaný v LTE a 5G NR k rozlišení konkrétní lokální domácí sítě, jako je rezidenční, podniková nebo neutrální hostitelská síť. Používá se v RAN pro řízení přístupu, správu mobility a a"
---

LHN je identifikátor používaný v LTE a 5G NR k rozlišení konkrétní lokální domácí sítě pro řízení přístupu v RAN, správu mobility a aplikaci politik.

## Popis

Identifikátor lokální domácí sítě (LHN ID) je síťový identifikátor používaný v architektuře rádiové přístupové sítě (RAN) 3GPP, zejména v kontextu malých buněk nasazených v domácnostech nebo podnicích (HeNB, HNG). Slouží jako jedinečný štítek pro konkrétní lokální domácí síť, což je logické seskupení jednoho nebo více Home eNodeB (HeNB) nebo Home gNB patřících do stejné administrativní domény, jako je například konkrétní podnikový kampus, síť rezidenčního účastníka nebo neutrální hostitelská infrastruktura.

Technicky je LHN ID nakonfigurován v Home eNodeB/gNB a je komunikován k jádru sítě ([MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/)) a sousedním makro buňkám během navazování síťových rozhraní a procedur předávání. Je přenášen v RAN Application Part (RANAP) a X2 Application Protocol (X2AP) zprávách. Primární funkcí LHN ID je umožnit RAN a jádru sítě identifikovat „domovskou“ síť UE, když je připojeno přes malou buňku. Tato identifikace je klíčová pro několik provozních procedur.

Pro správu mobility umožňuje LHN ID síti optimalizovat předávání. Například předávání mezi dvěma HeNB sdílejícími stejný LHN ID může být považováno za „intra-LHN“ předávání, potenciálně využívající zjednodušené procedury ve srovnání s předáním do buňky v jiném LHN nebo do makro sítě. Pro řízení přístupu a politiky může jádro sítě použít LHN ID k ověření, zda je UE autorizováno přistupovat k této konkrétní lokální síti. Dále umožňuje aplikaci síťově specifických politik, jako jsou vyhrazená pravidla účtování nebo povolené služby, na základě kontextu lokální sítě. Ve scénářích jako buňky s uzavřenou skupinou účastníků ([CSG](/mobilnisite/slovnik/csg/)) nebo buňky s hybridním přístupem pomáhá LHN ID spravovat hybridní členství a rozdělování zdrojů mezi účastníky domácí sítě a navštěvující makro uživatele.

## K čemu slouží

LHN ID byl zaveden k řešení manažerských a provozních komplikací vznikajících z rozsáhlého nasazení spotřebitelských a podnikových malých buněk (femtobuněk). Raná nasazení femtobuněk postrádala standardizovaný způsob, jak makro síť logicky seskupovala a identifikovala shluky těchto buněk patřících stejnému vlastníkovi nebo lokalitě. To ztěžovalo efektivní správu mobility, koordinované řízení rádiových zdrojů a aplikaci lokalizovaných politik.

Jeho vytvoření bylo motivováno potřebou vylepšené podpory RAN pro lokální IP přístup ([LIPA](/mobilnisite/slovnik/lipa/)) a vytipované přesměrování IP provozu (SIPTO) v lokální síti. Pro efektivní směrování provozu a správu mobility pro UE přistupující k lokálním službám síť vyžadovala jasný identifikátor pro lokální doménu. LHN ID toto poskytl, umožňující funkce jako kontinuita SIPTO během mobility v rámci stejné lokální sítě. Vyřešil omezení spočívající v zacházení s každým HeNB jako s izolovanou entitou, což operátorům umožnilo spravovat skupiny malých buněk jako kohezní lokální síť pro provozní účely a poskytování služeb, čímž se zlepšila jak efektivita sítě, tak uživatelský zážitek z lokalizovaných služeb.

## Klíčové vlastnosti

- Jednoznačně identifikuje logickou doménu lokální domácí sítě
- Nakonfigurován v Home eNodeB/gNB a komunikován přes rozhraní X2 a S1/N2
- Umožňuje optimalizované procedury intra-LHN předávání
- Používá se pro řízení přístupu a autorizaci UE k lokálním sítím
- Podporuje aplikaci politik specifických pro lokální síť (účtování, služby)
- Usnadňuje správu mobility pro kontinuitu LIPA a SIPTO

## Definující specifikace

- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.875** (Rel-13) — Dual Connectivity Extension Requirements

---

📖 **Anglický originál a plná specifikace:** [LHN na 3GPP Explorer](https://3gpp-explorer.com/glossary/lhn/)
