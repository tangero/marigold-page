---
slug: "vq"
url: "/mobilnisite/slovnik/vq/"
type: "slovnik"
title: "VQ – Voice Quality"
date: 2025-01-01
abbr: "VQ"
fullName: "Voice Quality"
category: "QoS"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/vq/"
summary: "Soubor metrik a metodik definovaných 3GPP pro objektivní a subjektivní hodnocení vnímané kvality hovoru z pohledu posluchače. Je klíčový pro operátory sítí při monitorování, odstraňování problémů a op"
---

VQ je soubor metrik a metodik definovaných 3GPP pro objektivní a subjektivní hodnocení vnímané kvality hovoru z pohledu posluchače.

## Popis

Kvalita hlasu (Voice Quality, VQ) v 3GPP označuje technickou charakterizaci a měření sluchového zážitku, který je uživateli doručen během hovoru. Zahrnuje jak subjektivní poslechovou kvalitu (jak ji vnímá člověk), tak objektivní algoritmické predikce této kvality. Hlavní rámec je definován v sérii P.800 od [ITU-T](/mobilnisite/slovnik/itu-t/), kterou 3GPP přijímá a rozšiřuje pro specifické podmínky mobilních sítí. Mezi klíčové objektivní metriky patří Perceptual Evaluation of Speech Quality ([PESQ](/mobilnisite/slovnik/pesq/)), definovaný v ITU-T P.862, a jeho nástupce Perceptual Objective Listening Quality Assessment ([POLQA](/mobilnisite/slovnik/polqa/)), definovaný v ITU-T P.863. Tyto algoritmy analyzují degradovaný řečový signál přijatý na straně posluchače vůči původnímu referenčnímu signálu, aby predikovaly střední hodnotu známky kvality (Mean Opinion Score, [MOS](/mobilnisite/slovnik/mos/)), typicky na škále od 1 (špatná) do 5 (vynikající).

Specifikace 3GPP definují, jak jsou tato měření integrována do síťové architektury. To může zahrnovat aktivní testování, při kterém jsou uskutečňovány testovací hovory se známými referenčními vzorky řeči, nebo pasivní monitorování, při kterém je analyzován živý provoz bez vkládání testovacích signálů. Tato měření mohou provádět síťové prvky jako Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) nebo dedikované sondy. Pro VoLTE a VoNR je monitorování VQ úzce spojeno s IP Multimedia Subsystem (IMS) a vrstvou Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), aby bylo možné korelovat metriky kvality s konkrétními rádiovými podmínkami, předáváním hovoru mezi buňkami (handover) nebo změnami kodeku. Parametry jako typ kodeku (např. [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/)), ztráta paketů, chvění zpoždění (jitter), zpoždění a ozvěna (echo) všechny kriticky ovlivňují vypočtené skóre VQ.

Role VQ je nedílnou součástí správy kvality služeb (Quality of Service, QoS) a kvality uživatelského zážitku (Quality of Experience, QoE). Poskytuje operátorům kvantifikovatelná data pro provedení analýzy hlavní příčiny špatného hlasového výkonu, ať už problém pochází z rádiové přístupové sítě (např. slabé pokrytí, interference), ze základnové sítě (např. zahlcení, překódování) nebo ze samotného zařízení. Definováním standardizovaných měřicích technik a formátů hlášení zajišťuje 3GPP, že hodnocení VQ je konzistentní a srovnatelné napříč různými sítěmi a dodavateli zařízení, což je zásadní pro benchmarkování, ověřování smluv o úrovni služeb (Service Level Agreement, SLA) a řízení průběžné optimalizace sítě.

## K čemu slouží

Standardizace metrik kvality hlasu byla motivována základní potřebou operátorů mobilních sítí objektivně spravovat a garantovat výkon jejich nejkritičtější služby: hlasových hovorů. Jak se sítě vyvíjely od přepojování okruhů (2G/3G) k přepojování paketů (VoLTE a VoNR), přenos se stal zranitelným vůči novým závadám, jako je ztráta IP paketů, proměnlivé zpoždění (jitter) a artefakty překódování. Samotné subjektivní poslechové testy jsou drahé, pomalé a neškálovatelné pro monitorování v rámci celé sítě. Proto byly nezbytné objektivní, automatizované měřicí nástroje, které poskytují přehled o kvalitě služeb v reálném nebo téměř reálném čase.

Historicky byla kvalita hlasu často odvozována z rádiových metrik, jako je síla signálu (RxLev) nebo míra bitových chyb (BER). Ty jsou však nepřímými ukazateli a nezachycují celkový vnímaný zážitek od konce ke konci, na který má vliv celý řetězec od výběru kodeku po síťový jitter. Zavedení standardizovaných metodik VQ v 3GPP, počínaje Rel-8 spolu s ranými pracemi na LTE a IMS, tuto mezeru zaplnilo. Poskytlo společný jazyk a technický základ pro hodnocení výkonu, což operátorům umožnilo proaktivně identifikovat zhoršení, korelovat ho se síťovými událostmi a zavádět nápravná opatření. To bylo klíčové pro úspěšné zavedení a přijetí VoLTE, protože muselo splnit nebo překonat očekávání kvality stanovená tradičním hlasem s přepojováním okruhů.

## Klíčové vlastnosti

- Standardizované objektivní metriky kvality (např. predikce PESQ, POLQA MOS)
- Podpora pro metodologie aktivního testování i pasivního monitorování
- Integrace s IMS a EPC/5GC pro zajištění kvality VoLTE/VoNR
- Korelace skóre kvality hlasu s parametry rádiové a transportní vrstvy
- Definované formáty hlášení a rozhraní pro systémy správy sítě
- Hodnocení širokopásmových a super-širokopásmových řečových kodeků (např. EVS)

## Související pojmy

- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface
- **TS 46.022** (Rel-19) — GSM Half Rate DTX Comfort Noise Specification

---

📖 **Anglický originál a plná specifikace:** [VQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/vq/)
