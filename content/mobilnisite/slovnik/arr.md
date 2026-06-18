---
slug: "arr"
url: "/mobilnisite/slovnik/arr/"
type: "slovnik"
title: "ARR – Aggregated RUCI Report Request"
date: 2025-01-01
abbr: "ARR"
fullName: "Aggregated RUCI Report Request"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/arr/"
summary: "ARR je mechanismus správy v sítích 3GPP, který vyžádá agregované hlášení o využití zdrojů a řídicích informacích (RUCI) od síťových prvků. Umožňuje efektivní sběr dat o výkonu a využití zdrojů pro mon"
---

ARR je mechanismus správy podle 3GPP, který vyžádá agregované hlášení o využití zdrojů a řídicích informacích (RUCI) od síťových prvků za účelem efektivního monitorování, optimalizace a vynucování politik.

## Popis

Aggregated [RUCI](/mobilnisite/slovnik/ruci/) Report Request (ARR) je standardizovaný postup definovaný v rámci architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) podle 3GPP, konkrétně na referenčních bodech Gx a Gxx. Funguje jako příkaz od Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) směrem k Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) nebo Bearer Binding and Event Reporting Function ([BBERF](/mobilnisite/slovnik/bberf/)). Jeho hlavním účelem je vyžádat konsolidované hlášení obsahující informace o využití zdrojů a řídicí informace (RUCI) z jedné nebo více uživatelských relací či přenosových kanálů (bearerů), namísto generování samostatných hlášení pro každou jednotlivou entitu. Tato agregace je klíčová pro škálovatelnou správu sítě v prostředích s vysokou hustotou relací.

Z architektonického hlediska ARR funguje v rámci PCC, kde PCRF představuje centrální bod pro rozhodování o politikách. Když PCRF potřebuje komplexní data o využití zdrojů – například pro vyhodnocení dopadu změny politiky, provedení analýzy provozu nebo monitorování dodržování Quality of Service (QoS) – odešle příkaz ARR přes rozhraní Gx (k PCEF v [PDN](/mobilnisite/slovnik/pdn/) Gateway) nebo Gxx (k BBERF v Serving Gateway nebo přístupové síti). Žádost specifikuje kritéria agregace, jako je skupina účastníků, konkrétní Access Point Name ([APN](/mobilnisite/slovnik/apn/)), agregát toku služebních dat nebo sada parametrů QoS. Příslušná funkce (PCEF/BBERF) následně shromáždí relevantní RUCI data, která zahrnují metriky jako objem dat (uplink/downlink), doba trvání, využití identifikátoru třídy QoS a spouštěcí události, a zkompiluje je do jediného agregovaného hlášení odeslaného zpět PCRF.

Mechanismus funguje pomocí specifických atribut-hodnota párů ([AVP](/mobilnisite/slovnik/avp/)) v rámci protokolu Diameter používaného na rozhraních Gx/Gxx. Mezi klíčové AVP patří samotný Aggregated-RUCI-Report-Request AVP, který může obsahovat podřízené AVP definující rozsah agregace (např. User-Equipment-Info, APN-Aggregate-Max-Bitrate-DL). Po přijetí příkazu vymáhací funkce identifikuje všechny aktivní relace nebo přenosové kanály odpovídající kritériím, extrahuje požadované parametry RUCI a provede agregaci (např. sečtení celkových objemů dat, výpočet průměrných přenosových rychlostí). Tato agregovaná data jsou následně naformátována do Aggregated-RUCI-Report AVP a přenesena v odpovědní zprávě Diameter. Tento proces snižuje počet jednotlivých transakcí hlášení, čímž šetří signalizační šířku pásma a výpočetní zdroje jak na PCRF, tak na vymáhacích funkcích.

Role ARR v síti je primárně provozní a analytická. Podporuje funkce jako optimalizace politik, kde může PCRF upravit účtovací pravidla nebo QoS politiky na základě agregovaných vzorců provozu. Napomáhá plánování kapacit tím, že poskytuje sumarizovanou spotřebu zdrojů napříč skupinami uživatelů nebo síťovými segmenty. Dále zlepšuje odstraňování závad a monitorování výkonu tím, že umožňuje síťovým operátorům vyžádat konsolidované snímky využití zdrojů bez generování nadměrné signalizační zátěže. Logika agregace je typicky časovačem řízená nebo spouštěná událostmi, což zajišťuje generování hlášení v odpovídajících intervalech nebo při dosažení specifických prahových hodnot, a tím vyvažuje aktuálnost s efektivitou.

## K čemu slouží

ARR bylo zavedeno, aby řešilo výzvy škálovatelnosti při sběru dat o využití zdrojů z rychle rostoucího počtu uživatelských relací a přenosových kanálů v sítích 3GPP. Před jeho zavedením monitorování využití zdrojů často vyžadovalo jednotlivé dotazy nebo hlášení pro každou relaci, což vedlo k významné signalizační režii na rozhraních Gx/Gxx a zatížení zpracováním na PCRF a vymáhacích funkcích. Jak se sítě vyvíjely, aby podporovaly vyšší hustotu uživatelů a složitější služby (jako IMS a mobilní širokopásmový přístup), tento model hlášení na úrovni relace se stal neefektivním a mohl ovlivnit výkon sítě, zejména během špičky nebo rozsáhlých auditů politik.

Hlavní problém, který ARR řeší, je snížení signalizačního provozu Diameter spojeného s hlášením o zdrojích. Díky umožnění agregovaných hlášení může jedna transakce žádost-odpověď nahradit desítky nebo stovky jednotlivých transakcí hlášení. To je zvláště cenné pro provozní úkoly, jako je audit dodržování politik napříč skupinou účastníků, monitorování agregované spotřeby šířky pásma pro podnikový APN nebo shromažďování statistik pro optimalizaci sítě. Motivací pro jeho vytvoření byla potřeba efektivnějších schopností správy, provozu a údržby (OAM) v rámci PCC, aby bylo zajištěno, že funkce správy mohou škálovat spolu s uživatelským provozem, aniž by se staly úzkým hrdlem.

Historicky, jak 3GPP Release 6 upevnilo PCC architekturu, byl důraz kladen na umožnění dynamického řízení politik na úrovni každé účastnické relace. Síťoví operátoři však rychle identifikovali potřebu hromadných operací a sumarizovaných pohledů pro efektivní správu. ARR, zavedené v Rel-6, tuto schopnost poskytlo rozšířením stávajících mechanismů hlášení RUCI definovaných v dřívějších specifikacích PCC. Řešilo omezení čistě relací-centrického hlášení a umožnilo systémům správy sítě a samotné PCRF získat holistický pohled na využití zdrojů, což je nezbytné pro správu provozu (traffic engineering), vyrovnání účtování a proaktivní správu kapacit ve vyvíjejících se paketových jádrech sítí.

## Klíčové vlastnosti

- Umožňuje vyžádat konsolidovaná hlášení o využití zdrojů a řídicích informacích (RUCI) z více relací/přenosových kanálů
- Snižuje signalizační režii protokolu Diameter na rozhraních Gx a Gxx ve srovnání s jednotlivým hlášením
- Podporuje flexibilní kritéria agregace (např. podle skupiny účastníků, APN, třídy QoS nebo agregátu toku služebních dat)
- Integruje se s architekturou Policy and Charging Control (PCC) podle 3GPP prostřednictvím příkazů iniciovaných PCRF
- Využívá specifické AVP protokolu Diameter pro definici žádosti a doručení hlášení
- Usnadňuje efektivní monitorování sítě, optimalizaci politik a plánování kapacit

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [RUCI – RAN User Plane Congestion Information](/mobilnisite/slovnik/ruci/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface

---

📖 **Anglický originál a plná specifikace:** [ARR na 3GPP Explorer](https://3gpp-explorer.com/glossary/arr/)
