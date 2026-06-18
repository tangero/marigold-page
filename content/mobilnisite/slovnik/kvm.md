---
slug: "kvm"
url: "/mobilnisite/slovnik/kvm/"
type: "slovnik"
title: "KVM – K Virtual Machine"
date: 2025-01-01
abbr: "KVM"
fullName: "K Virtual Machine"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/kvm/"
summary: "Prostředí virtuálního stroje definované v 3GPP pro provádění servisní logiky standardizovaným a přenosným způsobem. Poskytuje běhové prostředí pro aplikace a umožňuje síťovým operátorům nasazovat a sp"
---

KVM je standardizované prostředí virtuálního stroje definované 3GPP pro provádění přenosné servisní logiky, které poskytuje běhové prostředí pro aplikace a umožňuje operátorům nasazovat služby nezávisle na hardwaru.

## Popis

K Virtual Machine (KVM) je standardizované prostředí virtuálního stroje specifikované 3GPP, primárně v kontextu architektury Open Service Architecture ([OSA](/mobilnisite/slovnik/osa/)) a servisního prostředí Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)). Je navržen jako bezpečné a přenosné běhové prostředí pro provádění servisní logiky, často psané v platformně nezávislém bajtkódu. Z architektonického hlediska se KVM nachází v rámci prostředí pro provádění služeb, které může být součástí Serveru servisních schopností ([SCS](/mobilnisite/slovnik/scs/)) nebo aplikačního serveru. Rozhraní k síťovým zdrojům zprostředkovává prostřednictvím standardizovaných aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)) poskytovaných rámcem OSA/Parlay, což umožňuje servisní logice bezpečným a řízeným způsobem využívat schopnosti jádra sítě, jako je řízení hovorů, lokalizace uživatele nebo zasílání zpráv.

Z funkční perspektivy KVM funguje tak, že načte a interpretuje zkompilovaný bajtkód reprezentující servisní aplikaci. Poskytuje izolované (sandboxované) běhové prostředí s řízeným přístupem k systémovým zdrojům a síťovým API, čímž zajišťuje, že servisní logika nemůže nepříznivě ovlivnit podkladovou síťovou infrastrukturu. Mezi klíčové komponenty architektury KVM patří verifikátor bajtkódu, který před spuštěním kontroluje kód z hlediska bezpečnosti a shody; interpret nebo překladač za běhu (JIT), který bajtkód provádí; a správce zabezpečení, který vynucuje politiky řízení přístupu k voláním API. Samotný KVM je relativně odlehčený virtuální stroj optimalizovaný pro omezení zdrojů v telekomunikačních prostředích v době jeho specifikace.

Jeho úlohou v síti je oddělení tvorby služeb od implementačních detailů sítě. Poskytnutím standardizované prováděcí platformy umožňuje vývojářům aplikací třetích stran a síťovým operátorům psát služby jednou a nasazovat je na různých zařízeních různých dodavatelů, pokud tato zařízení podporují KVM a související API. To podporuje inovace a rychlejší nasazování služeb. Zatímco KVM představoval raný krok směrem k programovatelnosti sítě, jeho adopce byla nakonec zastíněna modernějšími webovými technologiemi a principy cloud-nativních aplikací, ačkoli jeho koncepty ovlivnily pozdější virtualizační snahy v telekomunikacích.

## K čemu slouží

KVM bylo vytvořeno pro potřeby standardizovaného, bezpečného a přenosného prostředí pro provádění přidané servisní logiky v mobilních sítích. Před jeho zavedením bylo nasazování služeb často pevně svázáno s proprietárními platformami konkrétních dodavatelů síťového vybavení, což vedlo k závislosti na dodavateli, pomalým inovacím služeb a vysokým integračním nákladům. Motivací byla snaha o otevření sítě poskytovatelům aplikací třetích stran, což mělo umožnit bohatší ekosystém služeb nad rámec těch, které poskytoval pouze operátor.

Historický kontext představuje snaha z počátku 21. století o zvýšení inteligence a programovatelnosti sítě, jejímž příkladem jsou iniciativy jako [OSA](/mobilnisite/slovnik/osa/)/Parlay a [CAMEL](/mobilnisite/slovnik/camel/). Tyto rámce definovaly standardizovaná rozhraní k síťovým schopnostem, ale zároveň vyžadovaly standardizovaný způsob hostování a provádění aplikací, které tato rozhraní používají. KVM byla odpovědí na tuto potřebu a poskytla 'běhovou' část této skládačky. Cílem bylo vyřešit problém přenositelnosti a zabezpečení aplikací a zajistit, aby služba napsaná pro síť jednoho operátora mohla teoreticky běžet v síti jiného, pokud obě podporovaly virtuální stroj specifikovaný 3GPP.

KVM a související přístup OSA však narážely na omezení, včetně složitosti a konkurence ze strany internetových modelů poskytování služeb (jako IMS a později webové služby). Tato technologie řešila počáteční problém uzavřené sítě, ale byla nakonec nahrazena agilnějšími a na web orientovanými architekturami. Přesto představovala základní koncept oddělení servisní logiky od síťové infrastruktury, což je princip, který zůstává klíčový pro moderní virtualizaci síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)).

## Klíčové vlastnosti

- Standardizovaný formát bajtkódu pro přenositelnost aplikací
- Izolované (sandboxované) běhové prostředí pro zabezpečení a řízení zdrojů
- Integrace s OSA/Parlay API pro zpřístupnění síťových schopností
- Odlehčený design vhodný pro prostředí telekomunikačních serverů
- Řízený model paměti a provádění pro prevenci pádů systému
- Podpora pro stažení servisní logiky a správu jejího životního cyklu

## Související pojmy

- [OSA – Open Services Architecture](/mobilnisite/slovnik/osa/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [KVM na 3GPP Explorer](https://3gpp-explorer.com/glossary/kvm/)
