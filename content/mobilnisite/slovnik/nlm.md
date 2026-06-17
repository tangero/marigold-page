---
slug: "nlm"
url: "/mobilnisite/slovnik/nlm/"
type: "slovnik"
title: "NLM – Network Listen Mode"
date: 2025-01-01
abbr: "NLM"
fullName: "Network Listen Mode"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nlm/"
summary: "Provozní režim pro uživatelské zařízení (UE) nebo základnovou stanici, při kterém pasivně monitoruje a dekóduje downlinkové přenosy okolních buněk. Primárně se používá pro vlastní konfiguraci a optima"
---

NLM je provozní režim, ve kterém uživatelské zařízení (UE) nebo základnová stanice pasivně monitoruje a dekóduje downlinkové přenosy okolních buněk za účelem vlastní konfigurace a optimalizace, například pro automatické zjišťování sousedních vztahů (ANR).

## Popis

Network Listen Mode (NLM) je funkce definovaná ve specifikacích 3GPP, která umožňuje síťovému uzlu (typicky malé buňce, přenosovému uzlu nebo i UE nakonfigurovanému pro tento účel) fungovat jako přijímač a skener rádiového prostředí. V tomto režimu se zařízení naladí na downlinková frekvenční pásma sousedních makro buněk nebo jiných malých buněk a dekóduje jejich vysílací kanály. Primárním cílem je získat kritické rádiové parametry z okolních buněk bez navázání aktivního připojení k nim.

Z architektonického hlediska je NLM implementován ve fyzické vrstvě a nižších vrstvách protokolového zásobníku naslouchající entity. Například v kontextu malých buněk LTE (Home eNodeB), jak je specifikováno v TS 25.967 a TS 36.300, obsahuje malá buňka vyhrazený přijímací řetězec NLM. Tento řetězec provádí úkony shodné s UE: synchronizuje se s potenciálními sousedními buňkami pomocí primárních (PSS) a sekundárních (SSS) synchronizačních signálů, dekóduje fyzický vysílací kanál (PBCH) pro získání hlavního informačního bloku ([MIB](/mobilnisite/slovnik/mib/)) a dále dekóduje bloky systémových informací (SIB) pro získání parametrů, jako je globální identita buňky ([GCI](/mobilnisite/slovnik/gci/)), kód oblasti sledování, podporované frekvence a seznamy sousedních buněk.

Jak to funguje: zahrnuje naplánované nebo spouštěné naslouchací období. Malá buňka (provozující NLM) může dočasně utlumit vlastní přenosy nebo naplánovat mezery ve svém downlinku, aby se vyhnula vlastnímu rušení, zatímco ladí svůj přijímač na cílovou frekvenci. Poté provede procedury hledání buněk a získávání systémových informací. Shromážděná data, zejména GCI a fyzická identita buňky (PCI), jsou nahlášena systému správy malé buňky nebo přímo použita k naplnění její tabulky sousedních vztahů (NRT). Tento proces je klíčovým prvkem pro funkci automatického zjišťování sousedních vztahů ([ANR](/mobilnisite/slovnik/anr/)), která automatizuje jeden z nejnáročnějších úkolů při nasazení a optimalizaci mobilních sítí.

Jeho role v moderních rádiových přístupových sítích (RAN) je klíčová pro samoorganizující se sítě (SON). NLM odstraňuje potřebu ruční konfigurace seznamů sousedních buněk, která je náchylná k chybám a neadaptuje se na změny v síti. Díky autonomnímu objevování sousedů mohou sítě optimalizovat výkon přechodů mezi buňkami (handover), snížit počet přerušených hovorů a zlepšit celkovou robustnost mobility. Je to zvláště kritické pro hustá, heterogenní nasazení s makro buňkami, mikro buňkami a malými buňkami pracujícími na složitých frekvenčních vrstvách, kde je rádiová topologie dynamická a komplexní.

## K čemu slouží

NLM byl vyvinut k řešení významného provozního problému správy vztahů mezi sousedními buňkami v stále složitějších a hustších mobilních sítích. V sítích 2G a raných 3G byly seznamy sousedů ručně konfigurovány síťovými inženýry na základě testů v terénu a předpokládaných map pokrytí. Tento proces byl nákladný, pomalu reagoval na změny (jako jsou nová nasazení lokalit nebo výpadky) a často nebyl optimální, což vedlo k selháním přechodů mezi buňkami a špatným uživatelským zážitkem.

Hnací motivací byl tlak 3GPP směrem k samoorganizujícím se sítím (SON) se zavedením LTE v Release 8. SON si klade za cíl automatizovat konfiguraci, optimalizaci a samoléčení RAN. Základní funkcí SON je automatické zjišťování sousedních vztahů ([ANR](/mobilnisite/slovnik/anr/)), které vyžaduje mechanismus pro buňku, aby objevila své sousedy. NLM tento mechanismus poskytuje. Řeší problém ručního poskytování seznamů sousedů tím, že umožňuje síťovým prvkům přímo poznávat své rádiové prostředí.

Historicky TS 25.967 pro UMTS Home NodeB položilo určité základy, ale NLM se stal klíčovým kamenem pro SON v LTE a později v NR. Řešil omezení čistě ručních metod a dalších technik objevování, které spoléhaly pouze na měření z UE (která vyžadují připojená a reportující UE). NLM umožňuje buňce provádět objevování nezávisle, dokonce ještě předtím, než obslouží jakákoli UE, což zajišťuje její provozuschopnost a optimalizaci od okamžiku zapnutí. Tato schopnost je nezbytná pro plug-and-play nasazení malých buněk a pro efektivní provoz budoucích sítí s řezáním sítě (network slicing) a dynamickými topologiemi.

## Klíčové vlastnosti

- Umožňuje pasivní downlinkové monitorování a dekódování signálů sousedních buněk
- Provádí hledání buněk, synchronizaci a dekódování bloků systémových informací
- Klíčový prvek pro funkci automatického zjišťování sousedních vztahů (ANR)
- Umožňuje autonomní naplňování tabulky sousedních vztahů (NRT)
- Podporuje vlastní konfiguraci a vlastní optimalizaci v SON
- Kritický pro plug-and-play nasazení malých buněk a přenosových uzlů

## Související pojmy

- [ANR – Automatic Neighbour Relationship](/mobilnisite/slovnik/anr/)

## Definující specifikace

- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report

---

📖 **Anglický originál a plná specifikace:** [NLM na 3GPP Explorer](https://3gpp-explorer.com/glossary/nlm/)
