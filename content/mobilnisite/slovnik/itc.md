---
slug: "itc"
url: "/mobilnisite/slovnik/itc/"
type: "slovnik"
title: "ITC – Information Transfer Capability"
date: 2025-01-01
abbr: "ITC"
fullName: "Information Transfer Capability"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/itc/"
summary: "Informační přenosová schopnost (Information Transfer Capability, ITC) je základní koncept v 3GPP, který klasifikuje povahu přenosové služby, jako je řeč, data nebo video. Definuje základní charakteris"
---

ITC je koncept 3GPP, který klasifikuje povahu přenosové služby (bearer service), například řeč nebo data, aby definoval základní charakteristiky pro vyjednávání služby a nastavení přenosového kanálu mezi sítí a uživatelským zařízením.

## Popis

Informační přenosová schopnost (Information Transfer Capability, ITC) je klíčový parametr v rámci servisní architektury 3GPP, definovaný jako atribut přenosové služby. Kategorizuje základní povahu informací, které mají být přeneseny přes síťové spojení. ITC je klíčovým prvkem v popisu přenosové služby (Bearer Service, [BS](/mobilnisite/slovnik/bs/)), který se vyjednává během procedur zřizování hovoru nebo relace, například u GSM okruhově spínaných ([CS](/mobilnisite/slovnik/cs/)) hovorů nebo kontextů [GPRS](/mobilnisite/slovnik/gprs/)/UMTS paketově spínaných (PS). Síť používá ITC spolu s dalšími parametry, jako je třída provozu a atributy QoS, k výběru vhodného rádiového přístupového kanálu, zdrojů transportní sítě a kódovacích schémat pro splnění požadavků služby.

Parametr ITC je explicitně signalizován mezi uživatelským zařízením (UE) a jádrem sítě (CN) jako součást informačního prvku přenosové schopnosti (bearer capability). V jádru sítě, konkrétně v ústředně mobilního spojení ([MSC](/mobilnisite/slovnik/msc/)) pro CS služby a v uzlu podpory GPRS (SGSN) pro PS služby, se ITC používá pro rozhodování o propojování a správu zdrojů. Například ITC označující 'řeč' aktivuje použití kanálu pro přenos (TCH) s plnou nebo poloviční rychlostí v GSM a příslušných hlasových kodeků, zatímco ITC 'neomezené digitální informace' (UDI) pro data povede k alokaci transparentního nebo netransparentního datového kanálu se specifickými protokoly pro opravu chyb.

Mezi klíčové specifikace upravující ITC patří 3GPP TS 21.905 (slovníček), TS 23.910 (který podrobně popisuje strukturu informačního prvku ITC) a TS 29.007 (Obecné požadavky na vzájemné propojení mezi veřejnou pozemní mobilní sítí (PLMN) a digitální sítí s integrovanými službami ([ISDN](/mobilnisite/slovnik/isdn/)) nebo telefonní veřejnou komutovanou sítí (PSTN)). Úlohou ITC je poskytnout jednoznačný, standardizovaný deskriptor, který umožňuje interoperabilitu mezi zařízeními různých výrobců a konzistentní zpracování služeb napříč různými generacemi sítí, od GSM (2G) až po vývoj 5G jader sítí, kde je podporováno propojení se staršími systémy.

## K čemu slouží

Informační přenosová schopnost (ITC) byla vytvořena, aby poskytla standardizovaný, na síti nezávislý způsob popisu základního typu požadované komunikační služby. Před jejím formalizováním v 3GPP mohly proprietární metody popisu typů služeb bránit interoperabilitě mezi zařízeními různých výrobců a mezi různými sítěmi (např. PLMN a [ISDN](/mobilnisite/slovnik/isdn/)). ITC tento problém řeší definováním jasné sady schopností (jako řeč, 3,1 kHz audio, neomezené digitální, omezené digitální, video), kterým mohou rozumět všechny síťové elementy.

Jejím primárním účelem je umožnit přesné vyjednávání služeb a alokaci zdrojů. Když uživatel zahájí hovor nebo datovou relaci, UE signalizuje požadovanou ITC. Síť tyto informace použije k určení nejvhodnější přenosové cesty, včetně výběru kodeků, typů kanálů, šířky pásma a mechanismů pro zpracování chyb. To zajišťuje, že hlasový hovor obdrží nízkolatenční zpracování s kontinuálním bitovým tokem, zatímco faxový přenos nebo modemové datové volání obdrží správnou adaptaci rychlosti a transparentnost. Bez standardizované ITC by síť mohla špatně alokovat zdroje, což by vedlo ke špatné kvalitě služby nebo selhání spojení.

Historicky byla ITC klíčová pro vzájemné propojení mezi sítěmi GSM a pevnými sítěmi, jako je ISDN, jak je definováno v TS 29.007. Poskytovala mapování mezi popisem přenosové služby v mobilní doméně a informačním prvkem přenosové schopnosti ISDN. To umožnilo bezproblémovou kontinuitu služeb a transparentnost funkcí napříč hranicemi sítí. Zatímco její význam poklesl s plně IP povahou 4G a 5G, kde jsou služby popsány identifikátory třídy QoS (QCIs) a 5QIs, koncept ITC zůstává relevantní pro scénáře navázání na starší okruhově spínané sítě ([CSFB](/mobilnisite/slovnik/csfb/)) a pro propojení se segmenty starších sítí.

## Klíčové vlastnosti

- Standardizovaná klasifikace typu služby (např. řeč, UDI, 3,1 kHz audio)
- Klíčový parametr v informačním prvku přenosové schopnosti (BCIE)
- Základní prvek pro výběr síťových zdrojů a přenosového kanálu
- Umožňuje vzájemné propojení mezi PLMN a pevnými sítěmi (ISDN/PSTN)
- Používá se při vyjednávání jak okruhově spínaných (CS), tak paketově spínaných (PS) služeb
- Poskytuje základ pro konfiguraci kodeků a transportních kanálů

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements

---

📖 **Anglický originál a plná specifikace:** [ITC na 3GPP Explorer](https://3gpp-explorer.com/glossary/itc/)
