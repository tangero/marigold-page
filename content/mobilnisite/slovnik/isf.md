---
slug: "isf"
url: "/mobilnisite/slovnik/isf/"
type: "slovnik"
title: "ISF – Interworking Selection Function"
date: 2025-01-01
abbr: "ISF"
fullName: "Interworking Selection Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/isf/"
summary: "ISF je logická funkce v rámci IP multimediálního podsystému (IMS), která určuje vhodnou metodu interoperability pro komunikační relaci. Vybírá mezi protokoly SIP-I a SIP-T na základě schopností sítě a"
---

ISF je funkce IMS, která vybírá mezi protokoly SIP-I nebo SIP-T, aby zajistila bezproblémovou interoperabilitu mezi IP multimediální podsystémem a staršími přepojovanými sítěmi.

## Popis

Funkce pro výběr interoperability (ISF) je klíčová součást architektury IP multimediálního podsystému (IMS), speciálně navržená pro správu interoperability mezi sítěmi založenými na IMS a staršími přepojovanými ([CS](/mobilnisite/slovnik/cs/)) sítěmi, jako jsou například sítě používající signalizační systém č. 7 (SS7). Funguje jako logická funkce, typicky implementovaná v rámci síťových entit, jako je funkce řízení mediální brány ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo hraniční řadič relace (SBC). Primární role ISF je analyzovat příchozí požadavek na relaci určený pro CS síť a rozhodnout o optimálním protokolu interoperability, který má být použit.

Když relace pochází od uživatele IMS (používajícího SIP) a cílí na uživatele v CS síti, ISF vyhodnocuje několik parametrů. Mezi ně patří schopnosti cílové sítě (podporované metody interoperability), typ požadované služby (např. hlasové volání, videohovor) a jakákoli provozní pravidla. Na základě této analýzy vybere buď SIP-I (SIP s enkapsulovaným [ISUP](/mobilnisite/slovnik/isup/)) nebo SIP-T (SIP pro telefony). SIP-I se používá, když je třeba zachovat podrobné signalizační informace ISUP od konce ke konci pro pokročilé telefonní služby. SIP-T se často používá pro základní interoperabilitu hlasových hovorů, kde není vyžadována plná transparentnost ISUP.

Funkce pracuje tak, že zachytí požadavek SIP INVITE. Zkoumá hlavičky SIP a tělo protokolu popisu relace (SDP). Může také dotazovat externí databáze nebo funkce pravidel. Jakmile je výběr proveden, ISF dá pokyn přidruženému řadiči mediální brány, aby použil zvolený protokol. MGCF poté provede potřebnou signalizační konverzi, přeloží zprávy SIP do příslušných zpráv ISUP pro CS síť a spravuje odpovídající mediální bránu pro zajištění interoperability hlasové cesty.

Její architektonická role je klíčová ve služební vrstvě IMS. Umožňuje síti IMS fungovat jako moderní nadstavba, která stále může komunikovat s rozsáhlou instalovanou základnou starších telefonních sítí. To umožňuje postupnou migraci na plně IP sítě bez narušení stávajících služeb. ISF zajišťuje, že rozhodnutí o interoperabilitě jsou činěna dynamicky a pro každou relaci zvlášť, což umožňuje flexibilní nasazení služeb a efektivní využití síťových zdrojů.

## K čemu slouží

ISF byla vytvořena k vyřešení složitého problému interoperability mezi novými, plně IP sítěmi IMS a stávající globální infrastrukturou přepojované telefonie. Před IMS byly telekomunikace převážně založeny na [CS](/mobilnisite/slovnik/cs/) technologii se standardizovanou signalizací SS7/[ISUP](/mobilnisite/slovnik/isup/). Zavedení IMS, založeného na SIP, vytvořilo protokolovou mezeru. Jednoduché brány mohly hovory přeložit, ale často nedokázaly zachovat bohaté signalizační informace nezbytné pro pokročilé služby, jako je přesměrování hovoru, volané číslo nebo čekání na hovor přes síťovou hranici.

Raná řešení interoperability byla statická a omezená na služby. Brána mohla být nakonfigurována tak, aby používala pouze SIP-T, který zjednodušuje zprávy ISUP, což mohlo vést ke ztrátě servisních informací. To motivovalo potřebu inteligentní výběrové funkce. ISF umožňuje síťovým operátorům nasadit jediný IMS okrajový prvek, který může dynamicky zvolit nejlepší metodu interoperability na základě konkrétního hovoru a schopností cílové sítě. Tím se zachovává kontinuita služeb a transparentnost funkcí při migraci uživatelů ze starších služeb na služby IMS.

Historicky bylo její vývoj v Release 8 součástí širšího úsilí o standardizaci IMS, aby se IMS stalo životaschopnou náhradou tradičních telefonních sítí a bylo s nimi interoperabilní. Řešilo to omezení přístupů typu 'univerzální řešení' u bran a umožnilo sofistikovanější a na služby bohatší interoperabilitu. To bylo klíčové pro komerční úspěch IMS, protože operátoři potřebovali garantovat, že noví účastníci IMS budou stále moci komunikovat s každým ve staré síti bez degradace služeb.

## Klíčové vlastnosti

- Dynamický výběr protokolu mezi SIP-I a SIP-T na základě analýzy relace
- Vyhodnocení schopností cílové sítě a požadavků služby
- Integrace s funkcí řízení mediální brány (MGCF) pro signalizační konverzi
- Podpora rozhodnutí o interoperabilitě založených na pravidlech operátora
- Zachování transparentnosti služeb přepojované telefonie v IMS
- Umožňuje flexibilní strategii interoperability pro každou relaci zvlášť

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 23.204** (Rel-19) — SMS over generic IP access; Stage 2
- **TS 23.824** (Rel-10) — IP-SM-GW enhancements for CPM-SMS Interworking
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.192** (Rel-19) — AMR-WB Comfort Noise Requirements
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report

---

📖 **Anglický originál a plná specifikace:** [ISF na 3GPP Explorer](https://3gpp-explorer.com/glossary/isf/)
