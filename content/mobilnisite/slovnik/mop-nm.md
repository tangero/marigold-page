---
slug: "mop-nm"
url: "/mobilnisite/slovnik/mop-nm/"
type: "slovnik"
title: "MOP-NM – Master Operator Network Manager"
date: 2025-01-01
abbr: "MOP-NM"
fullName: "Master Operator Network Manager"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mop-nm/"
summary: "Centralizovaná entita správce sítě (Network Manager) definovaná pro správu sítí s více dodavateli a technologiemi. Působí jako nadřazený správce, poskytuje integrovaný pohled a kontrolu nad podřízeným"
---

MOP-NM je centralizovaný hlavní (master) správce sítě operátora, který poskytuje integrovaný pohled a kontrolu nad podřízenými doménově specifickými správci v sítích s více dodavateli a technologiemi.

## Popis

Master Operator Network Manager (MOP-NM) je funkční entita specifikovaná v 3GPP TS 32.130, která se nachází na vrcholu hierarchické architektury správy. Je navržena tak, aby poskytovala integrovaný, komplexní pohled a kontrolu nad telekomunikační sítí, která může sestávat z více technologických domén (např. 2G, 3G, 4G, 5G) a zařízení od různých dodavatelů. MOP-NM přímo nespravuje jednotlivé síťové elementy; místo toho spravuje doménové správce (Domain Managers, DMs) nebo správce elementů (Element Managers, EMs), kteří jsou zodpovědní za konkrétní podsítě nebo zařízení určitého dodavatele. Tím vzniká vrstvená struktura správy: MOP-NM na vrcholu, doménoví správci uprostřed a skutečné síťové elementy (Network Elements, NEs) na spodní úrovni.

V provozu nabízí MOP-NM jednotné rozhraní směrem k vyšším systémům (northbound interface, Itf-N) pro Operations Support System ([OSS](/mobilnisite/slovnik/oss/)) nebo Business Support System ([BSS](/mobilnisite/slovnik/bss/)). Agreguje a koreluje informace o správě přijaté od podřízených doménových správců přes rozhraní směrem k nižším systémům (southbound interfaces, často založená na standardizovaných protokolech jako [MOP](/mobilnisite/slovnik/mop/)). Mezi klíčové funkce MOP-NM patří komplexní správa služeb (zajištění služby napříč více doménami), korelace chyb napříč doménami (identifikace hlavní příčiny z alarmů v různých doménách), konsolidované reportování výkonu a nadřazené vynucování politik pro zabezpečení, kvalitu služeb a síťové slicing. Převádí vysoké obchodní nebo servisní požadavky na technické řídicí direktivy, které jsou delegovány příslušným doménovým správcům.

Architektonická role MOP-NM je klíčová pro zjednodušení provozní složitosti moderních heterogenních sítí. Díky abstrakci detailů jednotlivých domén umožňuje síťovým operátorům spravovat celou svou infrastrukturu z jednoho místa. To je zvláště důležité pro dosažení provozní efektivity, automatizaci složitých pracovních postupů zahrnujících více technologií a implementaci pokročilých konceptů, jako je automatizace s uzavřenou smyčkou (closed-loop automation) nebo síťování založené na záměru (intent-based networking). MOP-NM umožňuje holistický přístup k řízení životního cyklu sítě, od plánování a zřizování přes zajištění (assurance) až po optimalizaci, napříč celou sítí operátora.

## K čemu slouží

Koncept MOP-NM byl zaveden, aby vyřešil provozní roztříštěnost způsobenou nasazením více nezávislých systémů správy pro různé síťové technologie (GSM, UMTS, LTE) a zařízení různých dodavatelů. Před jeho definicí čelili operátoři významným výzvám při získávání konsolidovaného pohledu na stav sítě, výkon služeb a zákaznickou zkušenost. Řešení problémů zasahujících více domén bylo manuální a časově náročné, protože technici se museli přihlašovat do samostatných systémů, aby informace poskládali dohromady.

Primárním účelem MOP-NM je umožnit integrovanou správu. Řeší omezení izolovaných doménových správců tím, že působí jako integrátor a orchestrátor. To je hnací silou obchodní potřeby snížit provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)), zlepšit agilitu služeb a zvýšit spokojenost zákazníků rychlejším řešením problémů a proaktivnějším zajištěním služeb. Jak se sítě vyvíjely směrem k 5G a začaly zahrnovat síťový slicing – kde jedna fyzická síť musí podporovat více logických sítí s různými charakteristikami – potřeba centralizovaného, inteligentního správce se stala ještě výraznější. MOP-NM poskytuje architektonický rámec pro správu těchto řezů (slices) komplexně, což zajišťuje, že specifikace SLA pro konkrétní slice jsou dodrženy napříč všemi podkladovými doménami a technologiemi.

## Klíčové vlastnosti

- Hierarchický model správy nadřazený doménovým správcům
- Komplexní správa a zajištění služeb napříč více doménami
- Korelace chyb napříč doménami a analýza hlavní příčiny
- Agregované monitorování výkonu a reportování
- Jednotné rozhraní směrem k vyšším systémům (Itf-N) k OSS/BSS
- Podpora pro správu řízenou politikami a správu životního cyklu síťových řezů (slices)

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements

---

📖 **Anglický originál a plná specifikace:** [MOP-NM na 3GPP Explorer](https://3gpp-explorer.com/glossary/mop-nm/)
