---
slug: "pdi"
url: "/mobilnisite/slovnik/pdi/"
type: "slovnik"
title: "PDI – Packet Detection Information"
date: 2025-01-01
abbr: "PDI"
fullName: "Packet Detection Information"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdi/"
summary: "Packet Detection Information (PDI, informace pro detekci paketů) je klíčová komponenta v protokolu Packet Forwarding Control Protocol (PFCP) používaném v 5G a 4G jádrech sítě. Definuje soubor pravidel"
---

PDI je soubor pravidel a informací používaných UPF nebo PGW k identifikaci paketů pro konkrétní datový tok služby, což umožňuje směrování provozu a vynucování politik v protokolu Packet Forwarding Control Protocol.

## Popis

Packet Detection Information (PDI, informace pro detekci paketů) je základní datová struktura v protokolu 3GPP Packet Forwarding Control Protocol ([PFCP](/mobilnisite/slovnik/pfcp/)), specifikovaná primárně v TS 29.244. Používá se při interakci mezi funkcí řídicí roviny ([CP](/mobilnisite/slovnik/cp/)), jako je Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5G nebo řídicí část Packet Gateway ([PGW-C](/mobilnisite/slovnik/pgw-c/)), a funkcí uživatelské roviny ([UP](/mobilnisite/slovnik/up/)), jako je User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) nebo [PGW-U](/mobilnisite/slovnik/pgw-u/). PDI je součástí Packet Detection Rule ([PDR](/mobilnisite/slovnik/pdr/)), což je kompletní pravidlo instruující funkci UP, jak pakety zpracovat. Komponenta PDI konkrétně definuje kritéria pro shodu při identifikaci paketů náležejících určitému datovému toku služby.

PDI obsahuje seznam informačních elementů (IEs), které slouží jako filtry. Ty mohou zahrnovat Zdrojové rozhraní (udávající, zda paket přichází z přístupové nebo jádrové strany sítě), síťové identifikátory jako Zdrojová/Cílová IP adresa a maska podsítě, transportní identifikátory jako Zdrojová/Cílové číslo portu a identifikátory aplikační vrstvy jako ID protokolu (typ další hlavičky). V pokročilejších nasazeních může také zahrnovat pole pro hlubokou inspekci paketů, jako jsou identifikátory aplikací, filtry Service Data Flow (SDF) nebo dokonce vlastní pravidla specifická pro podnik. Když paket dorazí k funkci UP, jeho hlavička a datová část jsou analyzovány a porovnány se všemi aktivními PDI. Pokud je nalezena shoda, přidružené PDR určuje následné akce: přeposlání, zahození, uložení do bufferu, duplikaci nebo aplikaci označení Quality of Service (QoS).

Z architektonického hlediska PDI umožňuje separaci řídicí a uživatelské roviny, což je základním kamenem moderních 5G a vyvinutých 4G jader. Funkce řídicí roviny, disponující plným kontextem politik, vytváří PDI a instaluje je pomocí procedur PFCP Session Establishment nebo Modification. Funkce uživatelské roviny pak tato pravidla aplikuje na liniové rychlosti, což zajišťuje zpracování paketů s nízkou latencí. Úroveň podrobnosti poskytovaná PDI je klíčová pro implementaci řezů sítě, kde různé řezy vyžadují odlišné zacházení s provozem. Tvoří také základ pro detekci provozu v Policy and Charging Control (PCC), což operátorům umožňuje aplikovat specifické sazby účtování, politiky QoS nebo rozhodnutí o blokování na základě detekované aplikace nebo služby.

Během provozu obsahuje jediné PDR jedno PDI, ale může spustit více následných akcí (Forwarding Action Rules, QoS Enforcement Rules, Usage Reporting Rules). Porovnávání podle PDI se typicky provádí v definovaném pořadí priority napříč všemi nainstalovanými PDR. Jeho návrh umožňuje vysokou flexibilitu a škálovatelnost, podporující vše od jednoduchého best-effort internetového provozu po komplexní podnikové VPN služby se specifickými požadavky na zabezpečení a nízkou latenci. Efektivita porovnávání podle PDI přímo ovlivňuje celkový výkon a kapacitu uzlu uživatelské roviny.

## K čemu slouží

Vytvoření Packet Detection Information (PDI) bylo motivováno potřebou vysoce flexibilní, programovatelné a standardizované metody pro detekci a klasifikaci provozu uživatelské roviny v architektuře s oddělenou řídicí a uživatelskou rovinou (CUPS). Před zavedením CUPS byly detekce provozu a vynucování politik těsně integrovány v monolitických síťových prvcích jako GGSN nebo PGW, což ztěžovalo nezávislé škálování uživatelské roviny nebo rychlé zavádění nových služeb. PDI jako součást protokolu PFCP poskytuje čisté, abstrahované rozhraní, pomocí kterého může řídicí rovina instruovat uživatelskou rovinu, jaký provoz má hledat.

Řeší kritický problém obsluhy provozu s ohledem na služby ve vysoce propustném prostředí s nízkou latencí. Bez strukturovaného detekčního mechanismu, jako je PDI, by byla uživatelská rovina omezena na základní směrování založené na IP adresách. PDI umožňuje hlubokou inspekci a klasifikaci paketů na okraji sítě, což je zásadní pro implementaci sofistikovaného Policy and Charging Control (PCC), řezů sítě, odlehčení výpočetního vytížení na hraně sítě nebo rodičovských kontrol. Umožňuje operátorům zpoplatňovat různé kvality služeb a zajišťovat plnění smluv o úrovni služeb (SLA).

Historicky byla detekce provozu vestavěna do proprietárních implementací. Standardizace PDI v rámci PFCP zajistila interoperabilitu mezi funkcemi řídicí a uživatelské roviny od více dodavatelů. To byl klíčový faktor pro virtualizaci síťových funkcí (NFV) a cloud-nativní nasazení, protože umožnilo operátorům pořizovat funkce CP a UP od různých dodavatelů a nasazovat je elasticky. Model PDI, představený v Release 14 spolu s CUPS pro EPC, byl později převzat a vylepšen v Service-Based Architecture (SBA) 5G jádra, čímž potvrdil svou základní roli v moderních paketových jádrech sítě.

## Klíčové vlastnosti

- Definuje standardizovanou sadu kritérií pro shodu paketů pro protokol PFCP
- Podporuje shodu podle více polí včetně zdrojové/cílové IP adresy, portu, protokolu a ID aplikace
- Umožňuje hlubokou inspekci paketů (DPI) pro pokročilou detekci služeb
- Základní prvek pro implementaci pravidel Policy and Charging Control (PCC)
- Umožňuje směrování provozu pro řezy sítě a edge computing
- Poskytuje základ pro spouštění akcí ukládání paketů do bufferu, jejich duplikace a označování QoS v uživatelské rovině

## Související pojmy

- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [PDR – Packet Detection Rule](/mobilnisite/slovnik/pdr/)
- [FAR](/mobilnisite/slovnik/far/)
- [QER – QoS Enforcement Rule](/mobilnisite/slovnik/qer/)
- [URR – Usage Reporting Rule](/mobilnisite/slovnik/urr/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [PDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdi/)
