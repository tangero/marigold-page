---
slug: "meho"
url: "/mobilnisite/slovnik/meho/"
type: "slovnik"
title: "MEHO – Mobile Evaluated Handover"
date: 2025-01-01
abbr: "MEHO"
fullName: "Mobile Evaluated Handover"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/meho/"
summary: "Mechanismus rozhodování o předávání spojení (handover), v němž mobilní stanice (UE) vyhodnocuje měření a může iniciovat nebo ovlivnit proces předání. Zlepšuje správu mobility distribucí rozhodovací in"
---

MEHO je mechanismus rozhodování o předávání spojení (handover), v němž mobilní stanice vyhodnocuje měření a může iniciovat nebo ovlivnit proces předání, aby se zlepšila odezva na měnící se rádiové podmínky.

## Popis

Mobile Evaluated Handover (MEHO) je paradigma řízení předávání spojení (handover) v sítích 3GPP, v němž User Equipment (UE) hraje aktivní, hodnotící roli v procesu rozhodování o předání. Na rozdíl od síťově řízeného předání (NCHO), kde rozhodnutí činí základnová stanice sítě (např. Node B, [eNB](/mobilnisite/slovnik/enb/), gNB) primárně na základě měření z uplinku hlášených UE, MEHO umožňuje UE zpracovávat downlink měření okolních buněk. UE tato měření vyhodnocuje vůči předdefinovaným kritériím nebo prahům, které mohou být konfigurovány sítí pomocí broadcastu nebo vyhrazené signalizace. Na základě tohoto vyhodnocení může UE odeslat hlášení o měření, které nejen obsahuje nezpracovaná data, ale může také zahrnovat doporučení nebo konkrétní žádost o předání spojení k cílové buňce, čímž iniciuje proceduru předání.

Architektura podporující MEHO zahrnuje těsnou interakci mezi vrstvou Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) v UE a funkcemi Radio Resource Management ([RRM](/mobilnisite/slovnik/rrm/)) v síti. Síť poskytuje UE konfiguraci měření, včetně objektů k měření (např. kmitočet nosné, ID buňky), konfigurace hlášení a případně prahů pro hlášení spouštěné událostí (např. Událost [A3](/mobilnisite/slovnik/a3/): Sousední buňka se stane o offset lepší než obsluhující). UE kontinuálně monitoruje obsluhující a sousední buňky, a když jsou splněny nastavené podmínky, aktivuje hlášení o měření. Ačkoli finální povel k předání (handover command) je stále vydáván sítí (zdrojovou buňkou), vyhodnocení a hlášení ze strany UE jsou klíčovými vstupy, které mohou urychlit rozhodnutí, zejména ve scénářích s rychle se měnícími rádiovými podmínkami.

Role MEHO je zásadní pro plynulou mobilitu, zejména v heterogenních sítích (HetNets) a scénářích s vysokou rychlostí. Provedením lokálního vyhodnocení může UE reagovat na zhoršení signálu nebo výskyt lepší buňky rychleji, než kdyby musela čekat, až síť zpracuje všechna uplink měření. Tím se snižuje latence předání a pravděpodobnost spadnutí hovoru. Mechanismus funguje ve spojení s dalšími typy předání a je základním konceptem, který se vyvíjel napříč systémy 3G (UMTS), 4G (LTE) a 5G (NR), kde je nedílnou součástí procedur mobility ve stavu RRC_CONNECTED a zajišťuje kontinuitu služeb při pohybu uživatele.

## K čemu slouží

MEHO bylo zavedeno, aby řešilo omezení čistě síťově orientovaných schémat předání spojení, konkrétně latenci a neefektivitu v dynamických rádiových prostředích. V raných mobilních systémech byla rozhodnutí o předání silně centralizována v rámci síťové infrastruktury, což mohlo vést ke zpožděným reakcím na náhlé změny v rádiových frekvenčních podmínkách mobilního zařízení. To bylo problematické pro rychle se pohybující uživatele nebo v prostředích se složitými interferenčními vzory. MEHO decentralizuje část rozhodovací logiky, využívá přímého a okamžitého vnímání downlink rádiového prostředí ze strany UE, aby poskytlo včasný vstup, čímž zlepšuje úspěšnost předání a celkový uživatelský dojem.

Motivace vychází z potřeby robustnější a responsivnější správy mobility, jak se mobilní technologie vyvíjely pro podporu vyšších přenosových rychlostí a rozmanitějších služeb. Díky možnosti UE vyhodnocovat a hlásit může síť činit informovanější a rychlejší rozhodnutí o předání, šetřit signalizační zdroje a snížit výpočetní zátěž na straně sítě při rutinním vyhodnocování měření. Tento přístup distribuované inteligence se stal stále důležitějším s příchodem technologií 4G LTE a 5G NR, které podporují hustá nasazení a agregaci nosných, což činí rádiové prostředí komplexnějším a potřebu agilní mobility prvořadou.

## Klíčové vlastnosti

- Vyhodnocení a hlášení měření založené na UE
- Podpora hlášení měření spouštěných událostí i periodických
- Snižuje latenci rozhodování o předání ve srovnání s čistě síťově řízenými schématy
- Spolupracuje se síťovým RRM pro finální autorizaci předání
- Konfigurovatelné sítí pomocí signalizace RRC (např. MeasurementConfig)
- Základní pro mobilitu v připojeném stavu (connected-mode) v UMTS, LTE a NR

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MEHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/meho/)
