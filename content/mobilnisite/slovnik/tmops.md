---
slug: "tmops"
url: "/mobilnisite/slovnik/tmops/"
type: "slovnik"
title: "TMOPS – True Million of Operations per Second"
date: 2025-01-01
abbr: "TMOPS"
fullName: "True Million of Operations per Second"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tmops/"
summary: "Metrika měření výkonu používaná k benchmarkování výpočetní kapacity kontroléru základnových stanic GSM (BSC). Kvantifikuje maximální počet standardizovaných operací zpracování hovorů, které BSC zvládn"
---

TMOPS je metrika výkonu, která benchmarkuje výpočetní kapacitu kontroléru základnových stanic GSM (BSC) tím, že kvantifikuje maximální počet standardizovaných operací zpracování hovorů, které je schopen zvládnout za sekundu při definovaném modelu zatížení.

## Popis

True Million of Operations per Second (TMOPS) je specifický, standardizovaný benchmark definovaný v dokumentu 3GPP TS 46.055. Je navržen pro měření a vyjádření kapacity zpracování hovorů kontroléru základnových stanic GSM ([BSC](/mobilnisite/slovnik/bsc/)). BSC je klíčový síťový prvek zodpovědný za správu rádiových zdrojů, řízení předávání hovorů (handover) a sestavování/ukončování hovorů pro více základnových přijímačů/vysílačů ([BTS](/mobilnisite/slovnik/bts/)). Hodnota TMOPS představuje maximální udržitelnou rychlost, při které BSC dokáže provádět definovanou sadu 'operací', které modelují reálné úlohy zpracování hovorů v síti GSM.

Benchmark funguje tak, že testovaný BSC je vystaven simulovanému provoznímu zatížení generovanému testovacím systémem. Toto zatížení je definováno specifickým provozním modelem, který zahrnuje mix typů operací, jako je sestavení hovoru iniciovaného mobilním zařízením ([MO](/mobilnisite/slovnik/mo/)), sestavení hovoru přijatého mobilním zařízením ([MT](/mobilnisite/slovnik/mt/)), předání hovoru uvnitř BSC (intra-BSC handover), předání hovoru mezi BSC (inter-BSC handover), aktualizace polohy a odeslání služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)). Každý z těchto reálných postupů je rozložen na spočitatelný počet standardizovaných 'TMOPS operací'. Test zvyšuje nabízené zatížení, dokud BSC nedosáhne své maximální kapacity, definované jako bod, ve kterém udržuje stanovenou jakost služby (Grade of Service, GoS), typicky úspěšnost sestavení hovoru a prahovou hodnotu zpoždění. Výsledné maximální zatížení, měřené v milionech těchto operací za sekundu, je TMOPS hodnocení.

Z architektonického hlediska se měření zaměřuje na centrální procesorovou jednotku ([CPU](/mobilnisite/slovnik/cpu/)) BSC a efektivitu softwaru při zpracování signalizace řídicí roviny (prostřednictvím rozhraní A a Abis) a správě přidružených databází (jako jsou funkce návštěvnické lokální databáze). Neměří propustnost uživatelských dat. Metrika TMOPS je klíčová pro plánovače sítí, protože jim umožňuje dimenzovat počet BSC potřebných pro cílovou populaci účastníků a provozní profil a porovnávat kapacitu zařízení BSC od různých dodavatelů na jednotném základě pomocí společného, rigorózního benchmarku.

## K čemu slouží

TMOPS byl vytvořen, aby vyřešil problém nejednoznačných a neporovnatelných tvrzení dodavatelů ohledně kapacity a výkonu kontrolérů základnových stanic GSM ([BSC](/mobilnisite/slovnik/bsc/)). Před jeho standardizací používali dodavatelé proprietární metriky nebo obecná tvrzení o počtu podporovaných účastníků nebo pokusů o hovor, což ztěžovalo přesné plánování sítě a spravedlivé porovnávání při pořizování zařízení. Různé vnitřní architektury a rozdíly v softwarové efektivitě znamenaly, že surové hardwarové specifikace (jako taktovací frekvence [CPU](/mobilnisite/slovnik/cpu/)) byly špatným ukazatelem reálné schopnosti zpracování hovorů.

Zavedení TMOPS ve verzi 3GPP Release 8 poskytlo standardizovaný, reprodukovatelný a objektivní benchmark. Tento problém vyřešil definováním přesného provozního modelu a spočitatelné sady operací, které přesně odrážejí výpočetní náročnost zpracování hovorů v GSM. To umožnilo operátorům specifikovat požadované TMOPS hodnocení ve svých výběrových řízeních na zařízení, čímž se zajistilo, že vybrané BSC zvládnou předpokládaný provoz v hodině špičky. Také to motivovalo dodavatele k optimalizaci efektivity svého BSC softwaru, aby dosáhli vyššího TMOPS hodnocení na daném hardwaru, což nakonec vedlo k nákladově efektivnější a kapacitně hustší síťové infrastruktuře. Metrika zůstává relevantní pro rozšiřování a modernizaci sítí GSM.

## Klíčové vlastnosti

- Standardizovaný benchmark definovaný v 3GPP TS 46.055 pro měření kapacity BSC v GSM
- Kvantifikuje kapacitu jako miliony definovaných operací zpracování hovorů za sekundu
- Používá specifický provozní model kombinující sestavování hovorů, předávání hovorů (handover), aktualizace polohy a SMS
- Definuje přesný práh jakosti služby (Grade of Service, GoS) pro určení maximálního udržitelného zatížení
- Poskytuje objektivní základ pro porovnání kapacity zařízení BSC od různých dodavatelů
- Nezbytný pro přesné dimenzování sítě a plánování kapacity v sítích GSM

## Související pojmy

- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [TMOPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmops/)
