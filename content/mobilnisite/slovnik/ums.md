---
slug: "ums"
url: "/mobilnisite/slovnik/ums/"
type: "slovnik"
title: "UMS – User plane node Management Service"
date: 2025-01-01
abbr: "UMS"
fullName: "User plane node Management Service"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ums/"
summary: "Služba správy v architektuře 3GPP odpovědná za správu typu Porucha, Konfigurace, Účtování, Výkon a Zabezpečení (FCAPS) pro síťové funkce uživatelské roviny. Poskytuje standardizované operace a rozhran"
---

UMS je služba správy podle 3GPP odpovědná za správu typu FCAPS pro síťové funkce uživatelské roviny, jako je UPF, a poskytuje standardizované operace pro monitorování, konfiguraci a řízení těchto uzlů.

## Popis

Služba správy uzlů uživatelské roviny (UMS) je specifická služba správy definovaná v rámci architektury správy a orchestrace ([MANO](/mobilnisite/slovnik/mano/)) podle 3GPP. Spadá pod skupinu služeb správy síťových zdrojů ([NRM](/mobilnisite/slovnik/nrm/)) a je určena pro správu životního cyklu síťových funkcí, které zpracovávají datový provoz uživatelů, známých jako uzly uživatelské roviny. Primární spravovanou entitou pro UMS v systémech 5G je funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), ale koncept platí i pro analogické entity uživatelské roviny v předchozích generacích, jako je uživatelská rovina brány obslužné sítě ([SGW](/mobilnisite/slovnik/sgw/)) a brány paketové datové sítě ([PGW](/mobilnisite/slovnik/pgw/)) v architektuře Evolved Packet Core (EPC).

Architektonicky je UMS typicky realizována jako soubor schopností v rámci systému správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systému správy prvků ([EMS](/mobilnisite/slovnik/ems/)). Poskytuje rozhraní směrem k vyšším systémům (tzv. northbound), často založená na informačních modelech definovaných 3GPP s využitím [UML](/mobilnisite/slovnik/uml/), pro vyšší orchestrační systémy (jako je orchestrátor virtualizace síťových funkcí – NFVO) nebo pro integrovaný OSS. Služba implementuje standardní oblasti správy FCAPS: správu poruch (pro dohled nad alarmy a obnovu po poruše), správu konfigurace (pro zřizování a aktualizaci parametrů UPF), správu účtování (pro sběr dat o využití), správu výkonu (pro sběr KPI a metrik) a správu zabezpečení (pro řízení přístupu a protokolování bezpečnostních událostí).

Provozně UMS funguje tak, že udržuje instanci spravovaného objektu, která reprezentuje každý uzel uživatelské roviny pod její kontrolou. Prostřednictvím referenčního bodu Itf-N nebo jiných rozhraní správy může přijímat příkazy od operátora nebo orchestrátoru k vytvoření instance, konfiguraci, škálování nebo ukončení UPF. Průběžně sbírá data o výkonu (např. propustnost, zpoždění paketů, ztrátovost paketů) a indikace poruch z uzlu. Tato data jsou následně korelována, analyzována a prezentována, což umožňuje automatizované nebo manuální akce pro zajištění kvality služeb uživatelské roviny a efektivity sítě. Ve virtualizovaném prostředí UMS interaguje se správcem virtualizované infrastruktury (VIM) pro alokaci podkladových výpočetních a úložných zdrojů pro UPF.

## K čemu slouží

UMS byla vytvořena, aby poskytla standardizovanou, abstrahovanou a automatizovanou metodu pro správu kritických komponent uživatelské roviny mobilních sítí. Jak se sítě vyvíjely směrem k plně IP architekturám a později k cloud-nativním, softwarovým nasazením, uzly uživatelské roviny se staly dynamičtějšími a početnějšími. Tradiční přístupy správy prvků specifické pro jednotlivé dodavatele byly neefektivní pro více-dodavatelské sítě a neschopné podporovat rychlé, automatizované operace životního cyklu vyžadované pro síťové řezy a vytváření služeb na vyžádání.

Její specifikace řeší potřebu společného modelu služby správy, který odděluje záměr správy (např. 'zajistit zpoždění pod 10 ms pro řez X') od implementačních detailů UPF specifických pro dodavatele. Definováním UMS umožňuje 3GPP interoperabilitu mezi systémy správy od různých dodavatelů a umožňuje centralizované orchestraci zacházet s funkcemi uživatelské roviny jako se spravovatelnými, skládanými zdroji. To je zvláště důležité pro 5G, kde může být UPF nasazena distribuovaným způsobem (např. na okraji sítě) a její konfigurace (např. kotvy PDU sezení, pravidla směrování provozu) musí být dynamicky upravována na základě mobility uživatelů a požadavků služeb.

## Klíčové vlastnosti

- Správa typu FCAPS pro síťové funkce uživatelské roviny (např. UPF, SGW-U)
- Standardizované rozhraní správy směrem k vyšším systémům (např. založené na informačních modelech 3GPP)
- Správa životního cyklu včetně vytvoření instance, konfigurace, škálování a ukončení
- Monitorování výkonu a sběr KPI uživatelské roviny (propustnost, zpoždění)
- Integrace se správci virtualizované infrastruktury pro alokaci zdrojů
- Podpora automatizované správy v souladu s principy ETSI NFV-MANO

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.539** (Rel-19) — NW-TT Protocol Aspects

---

📖 **Anglický originál a plná specifikace:** [UMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ums/)
