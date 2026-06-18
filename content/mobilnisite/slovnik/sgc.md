---
slug: "sgc"
url: "/mobilnisite/slovnik/sgc/"
type: "slovnik"
title: "SGC – Service Gap Control"
date: 2025-01-01
abbr: "SGC"
fullName: "Service Gap Control"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sgc/"
summary: "Mechanismus na úrovni NAS, který spravuje periodické servisní přestávky pro UE, umožňující jim dočasně přerušit datové relace za účelem provádění měření na jiných frekvencích nebo RAT. Optimalizuje mo"
---

SGC je mechanismus na úrovni NAS (Non-Access Stratum), který spravuje periodické servisní přestávky pro UE za účelem provádění měření na jiných frekvencích nebo mezi různými RAT. Optimalizuje mobilitu a energetickou účinnost při zachování aktivní relace.

## Popis

Řízení servisní přestávky (Service Gap Control, SGC) je funkce vrstvy Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) zavedená v 5G a dále rozvíjená v pozdějších vydáních, která umožňuje uživatelskému zařízení (UE) dočasně přerušit aktivní datovou relaci pro účely měření. Funguje tak, že definuje 'servisní přestávku' – nakonfigurované časové okno, během kterého síť upustí od plánování uživatelských dat, což umožní UE přeladit svůj rádiový přijímač z obsluhující buňky a provést skenování jiných frekvencí nebo technologií rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)). Parametry SGC, včetně délky přestávky, periodicity a platnosti, jsou vyjednány mezi UE a jádrem sítě prostřednictvím signalizace NAS, konkrétně definovány ve specifikacích 24.301 (EPS NAS) a 24.501 (5GS NAS).

Z architektonického hlediska SGC zahrnuje koordinaci mezi UE a funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5GC, nebo [MME](/mobilnisite/slovnik/mme/) v EPS. UE požaduje vzor servisní přestávky na základě svých schopností a potřeb, jako jsou měření mezi různými frekvencemi nebo RAT pro přípravu převzetí služeb nebo přesunu buňky. Síť vyhodnotí požadavek s ohledem na politiky a dostupnost zdrojů a poté vzor schválí nebo upraví prostřednictvím zprávy NAS, jako je zpráva SERVICE [GAP](/mobilnisite/slovnik/gap/) CONTROL. Během aktivních přestávek může být [RRC](/mobilnisite/slovnik/rrc/) spojení UE zachováno, ale přenos dat v uživatelské rovině je zastaven, čímž je zajištěna zachovaná relace.

Princip fungování: Jakmile je servisní přestávka aktivována, UE využívá intervaly přestávek k provádění měření na cílových buňkách, které mohou být na různých pásmech NR, nosných LTE, nebo dokonce v ne-3GPP sítích. Síť pozastaví plánování dat ve směru downlink a uloží do vyrovnávací paměti příchozí pakety, přičemž přenos obnoví po skončení přestávky. Tento mechanismus se liší od tradičních měřicích přestávek v RRC, protože SGC funguje na vrstvě NAS, což poskytuje větší flexibilitu a delší trvání vhodné pro úlohy na pozadí, jako je skenování sítě pro edge computing nebo úsporu energie.

Klíčové komponenty zahrnují SERVICE GAP TIMER, který definuje délku přestávky, a SERVICE GAP PERIOD, který nastavuje interval opakování. UE hlásí síti využití přestávek a výsledky měření, což umožňuje optimalizovaná rozhodnutí o mobilitě. SGC zvyšuje účinnost tím, že umožňuje měření bez nutnosti navazovat nová RRC spojení nebo způsobovat ukončení relace, což je klíčové pro služby typu 'vždy zapnuto' a zařízení s omezenou kapacitou baterie.

## K čemu slouží

SGC bylo vytvořeno, aby řešilo omezení stávajících mechanismů měřicích přestávek, které byly primárně řízeny [RRC](/mobilnisite/slovnik/rrc/) a často nedostačující pro rozsáhlé skenování mezi [RAT](/mobilnisite/slovnik/rat/) nebo na pozadí. V dřívějších vydáních UE spoléhala na nakonfigurované měřicí přestávky, které byly krátké a časté, což mohlo narušovat služby citlivé na latenci a chyběla koordinace na úrovni NAS. SGC to řeší zavedením přerušení služby založeného na NAS, které je vyjednatelné, a umožňuje tak delší, přizpůsobené přestávky v souladu se schopnostmi UE a síťovými politikami.

Historicky, jak se sítě vyvíjely směrem k 5G a nasazení více RAT (např. koexistence NR-LTE), potřebovala UE efektivní způsoby, jak objevovat a měřit alternativní buňky bez zhoršení uživatelského zážitku. SGC, zavedené ve vydání 15 s 5G, to umožňuje tím, že povoluje naplánované přestávky ve službě, což usnadňuje plynulou přípravu mobility a objevování sítě. Je zvláště užitečné pro režimy úspory energie a scénáře edge computingu, kde UE může potřebovat pravidelně skenovat místní služby.

Motivace vychází z potřeby vyvážit kontinuitu služby s požadavky na měření. Umožněním řízených přestávek SGC snižuje signalizační režii a spotřebu baterie ve srovnání s častými rekonfiguracemi RRC. Podporuje pokročilé funkce, jako je síťové segmentování a nepozemské sítě, kde se intervaly měření mohou výrazně lišit. Nakonec SGC zvyšuje celkový výkon systému tím, že umožňuje proaktivní mobilitu a optimalizaci zdrojů.

## Klíčové vlastnosti

- Vyjednávání vzorů servisních přestávek na úrovni NAS mezi UE a jádrem sítě
- Umožňuje dočasné přerušení uživatelských dat pro měření mezi různými frekvencemi/RAT
- Konfigurovatelné časovače délky přestávky, periodicity a platnosti
- Během přestávek zachovává RRC spojení a kontinuitu relace
- Podporuje úsporu energie a optimalizaci mobility v prostředích s více RAT
- Aplikovatelné pro EPS i 5GS prostřednictvím specifikací 24.301 a 24.501

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification

---

📖 **Anglický originál a plná specifikace:** [SGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgc/)
