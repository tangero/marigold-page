---
slug: "cfudb"
url: "/mobilnisite/slovnik/cfudb/"
type: "slovnik"
title: "CFUDB – Communication Forwarding User Determined Busy"
date: 2025-01-01
abbr: "CFUDB"
fullName: "Communication Forwarding User Determined Busy"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cfudb/"
summary: "CFUDB je doplňková služba, která umožňuje uživateli přesměrovat příchozí hovory na jiné číslo, když je uživatel obsazen. Poskytuje personalizovanou správu hovorů tím, že uživatelům umožňuje definovat"
---

CFUDB (přesměrování hovorů při obsazení zvolené uživatelem) je doplňková služba, která umožňuje uživateli přesměrovat příchozí hovory na jiné číslo, když je uživatel obsazen, a tím poskytuje personalizovanou správu hovorů.

## Popis

Communication Forwarding User Determined Busy (CFUDB) je standardizovaná doplňková služba v rámci specifikací 3GPP, která účastníkům umožňuje automaticky přesměrovat příchozí hlasové hovory na předem definovaný alternativní cíl, když je linka účastníka vyhodnocena jako obsazená. Služba funguje v rámci architektury IP Multimedia Subsystem (IMS) a využívá signalizační mechanismy Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) k implementaci logiky přesměrování hovoru. Když pokus o hovor dorazí do obsluhující sítě, síť zkontroluje profil služeb účastníka a jeho aktuální stav; pokud je účastník zapojen do jiného hovoru nebo si ručně nastavil stav jako obsazený, síť automaticky přesměruje příchozí hovor podle nakonfigurovaných pravidel přesměrování účastníka.

Technická implementace CFUDB zahrnuje koordinaci více síťových prvků. Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) ukládá profil služby CFUDB účastníka, včetně stavu aktivace a čísla cíle přesměrování. Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) provádí servisní logiku tím, že zachytává příchozí požadavky SIP INVITE a aplikuje kritéria filtru na základě profilu účastníka. Když jsou splněny podmínky CFUDB, S-CSCF upraví SIP požadavek, aby hovor přesměroval na nakonfigurovanou adresu. Služba interaguje s dalšími komponentami IMS včetně Application Server ([AS](/mobilnisite/slovnik/as/)), který může hostovat dodatečnou servisní logiku, a Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) pro propojení s sítěmi s přepojováním okruhů.

CFUDB funguje na základě konfigurovatelných parametrů, které mohou účastníci upravovat prostřednictvím síťových provozních rozhraní. Mezi tyto parametry patří adresa cíle přesměrování (kterou může být jakékoliv platné telefonní číslo nebo SIP [URI](/mobilnisite/slovnik/uri/)), stav aktivace/deaktivace a pravidla přesměrování založená na čase. Služba podporuje jak bezpodmínečné přesměrování (při detekci stavu obsazeno), tak podmíněné přesměrování založené na dodatečných kritériích, jako je identita volajícího nebo denní doba. Síťoví operátoři implementují CFUDB jako součást své nabídky služeb, typicky ji nabízejí prostřednictvím samoobslužných portálů nebo rozhraní zákaznické podpory.

Z pohledu signalizace využívá CFUDB standardních SIP response kódů k implementaci přesměrování hovoru. Když S-CSCF určí, že má být CFUDB vyvolána, typicky vrátí odpověď třídy SIP 3xx (například 302 Moved Temporarily) s hlavičkou Contact obsahující adresu pro přesměrování. To spustí v zařízení volající strany nový pokus o hovor na nový cíl. Služba zachovává zpětnou kompatibilitu se staršími sítěmi s přepojováním okruhů prostřednictvím příslušných propojovacích funkcí, které překládají mezi signalizací SIP a protokoly [ISUP](/mobilnisite/slovnik/isup/)/BICC používanými v tradičních telefonních sítích.

## K čemu slouží

CFUDB byl vyvinut, aby řešil základní potřebu rozšířených možností správy hovorů v mobilních sítích, zejména s vývojem hlasových služeb od základní telefonie s přepojováním okruhů k pokročilé multimediální komunikaci založené na IP. Před standardizovanými doplňkovými službami, jako je CFUDB, byla funkce přesměrování hovorů často omezena na implementace specifické pro danou síť s různými možnostmi u různých operátorů a regionů. Standardizace CFUDB v rámci 3GPP vytvořila konzistentní, interoperabilní rámec, který účastníkům umožňuje zachovat kontrolu nad svou komunikační dostupností a zároveň zajišťuje kontinuitu služby.

Služba řeší několik praktických problémů v telekomunikacích. Za prvé řeší problém zmeškaných hovorů, když jsou účastníci zapojeni do jiných konverzací, a zajišťuje, že důležité komunikace nejsou ztraceny, ale spíše přesměrovány na alternativní kontakty nebo systémy hlasové pošty. Za druhé poskytuje uživatelům z podnikového prostředí profesionální možnosti obsluhy hovorů, což jim umožňuje udržovat úroveň zákaznického servisu i během špičky volání. Za třetí CFUDB umožňuje efektivnější využití síťových prostředků snížením opakovaných pokusů o volání na obsazené linky a optimalizací směrování hovorů na základě preferencí účastníka.

Historicky CFUDB navazuje na dřívější služby přesměrování hovorů definované ve standardech GSM a pevných sítí, ale rozšiřuje je o signalizaci založenou na IP a bohatší možnosti konfigurace. Integrace do architektury IMS umožňuje CFUDB bezproblémově spolupracovat s dalšími multimediálními službami a podporovat sofistikovanější pravidla přesměrování, než bylo možné v tradičních telefonních sítích. Tento vývoj odráží širší posun odvětví k službám zaměřeným na účastníka, které nabízejí větší personalizaci a kontrolu nad komunikačním zážitkem.

## Klíčové vlastnosti

- Automatické přesměrování hovoru při obsazení linky účastníka
- Konfigurovatelný cíl přesměrování (telefonní číslo nebo SIP URI)
- Integrace s architekturou IMS využívající signalizaci SIP
- Aktivace/deaktivace pod kontrolou účastníka
- Podpora pravidel přesměrování založených na čase a podmínkách
- Propojení se staršími sítěmi s přepojováním okruhů

## Související pojmy

- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 32.275** (Rel-19) — MMTel Charging Specification

---

📖 **Anglický originál a plná specifikace:** [CFUDB na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfudb/)
