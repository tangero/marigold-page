---
slug: "rps"
url: "/mobilnisite/slovnik/rps/"
type: "slovnik"
title: "RPS – Reference Picture Selection"
date: 2025-01-01
abbr: "RPS"
fullName: "Reference Picture Selection"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rps/"
summary: "Funkce pro zvýšení odolnosti proti chybám ve videokódování (jako H.264/AVC a H.265/HEVC), která umožňuje dekodéru použít dříve dekódovaný snímek (nikoli bezprostředního předchůdce) jako referenci pro"
---

RPS je funkce pro zvýšení odolnosti proti chybám ve videokódování, která umožňuje dekodéru použít dříve dekódovaný snímek (nikoli bezprostředního předchůdce) jako referenci pro predikci budoucích snímků, aby byla zachována kvalita na spojích náchylných k chybám.

## Popis

Reference Picture Selection (RPS, výběr referenčního snímku) je pokročilý nástroj pro zvýšení odolnosti proti chybám definovaný ve standardech videokódování, jako je H.264/Advanced Video Coding ([AVC](/mobilnisite/slovnik/avc/)) a H.265/High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)), které jsou podrobně profilovány a odkazovány ve specifikacích 3GPP pro multimediální telefonii a streamovací služby. Jeho primární funkcí je zmírnit dopad ztráty nebo poškození paketů na kvalitu dekódovaného videa při komunikaci v reálném čase. Ve standardním prediktivním videokódování se snímky (P-snímky a B-snímky) kódují vzhledem k jednomu nebo více dříve zakódovaným a dekódovaným 'referenčním' snímkům. Obvykle se používá nejnověji dekódovaný snímek. Pokud je však tento referenční snímek ztracen nebo poškozen, chyba se přenese na všechny následující snímky, které na něm závisí, což způsobí závažné a dlouhotrvající vizuální artefakty.

RPS funguje tak, že poskytuje kodéru a dekodéru spravovaný seznam více referenčních snímků uložených v 'Decoded Picture Buffer' ([DPB](/mobilnisite/slovnik/dpb/)). Kodér může inteligentně vybrat, který snímek v tomto bufferu použít jako referenci pro kódování aktuálního snímku. Klíčové je, že prostřednictvím signalizace v přenášeném datovém toku (v hlavičce slicu) kodér instruuje dekodér, které konkrétní snímky použít pro dekódování aktuálního snímku a které snímky ponechat nebo odstranit z DPB. Pokud síť indikuje ztrátu (např. prostřednictvím Negative Acknowledgment - [NACK](/mobilnisite/slovnik/nack/) v [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/)), může kodér reagovat výběrem referenčního snímku, o kterém je známo, že byl na dekodéru správně přijat, čímž efektivně 'ustoupí' ke staršímu, nepoškozenému snímku. Tím se přeruší řetězec časového šíření chyby.

Z architektonického hlediska RPS zahrnuje koordinaci mezi aplikační vrstvou (videokodér/dekodér) a podkladovým transportem. V kontextu 3GPP se často používá v Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) a Packet-switched Streaming Service ([PSS](/mobilnisite/slovnik/pss/)). Klíčovými komponentami jsou logika správy referenčních snímků videokodeku, DPB a signalizační mechanismus pro předání sady referenčních snímků. Specifikace 3GPP (např. 26.906 pro výkonnost videokodeků) definují profily a úrovně videokodeků, které zahrnují schopnosti RPS, čímž zajišťují interoperabilitu mezi zařízeními. Jeho úlohou je zvýšit robustnost videoslužeb na inherentně proměnlivém a někdy nespolehlivém rádiovém přístupovém síti, což zlepšuje uživatelský zážitek během období ztráty paketů bez nutnosti úplného obnovení intra-snímku, které je náročné na šířku pásma.

## K čemu slouží

RPS byl vyvinut k řešení kritické slabiny prediktivního videokódování pro komunikaci v reálném čase přes paketově přepínané sítě, jako je internet a mobilní sítě. Jádrem problému je časové šíření chyby: jediný ztracený paket obsahující referenční snímek (nebo jeho část) může znehodnotit mnoho sekund videa, protože každý nový snímek se nesprávně dekóduje na základě poškozené reference. To bylo pro konverzační služby, jako jsou videohovory, nepřijatelné.

Historické přístupy k odolnosti proti chybám zahrnovaly časté vysílání Intra-snímků (I-snímků), které jsou nezávislé, ale spotřebovávají výrazně více šířky pásma, což snižuje celkovou kvalitu videa při daném datovém toku. Jiné metody, jako je Forward Error Correction (FEC), přidávají režii. RPS poskytuje efektivnější řešení založené na zpětné vazbě. Byl motivován růstem mobilní videotelefonie a streamování v sítích 3G a 4G, kde se rádiové podmínky mohou rychle měnit. Tím, že umožňuje kodéru přepnout na známou správnou referenční snímek po obdržení hlášení o ztrátě (prostřednictvím RTCP NACK nebo podobně), RPS lokalizuje dopad ztráty. Dekodér zažije okamžité zakolísání nebo mírné snížení kódovací účinnosti (protože starší reference může být méně korelovaná), ale vyhne se katastrofickému, dlouhotrvajícímu rozpadu videa. To z něj činí klíčový prvek pro spolehlivé, vysoce kvalitní videoslužby v systémech 3GPP, který vyvažuje efektivitu využití šířky pásma a robustnost.

## Klíčové vlastnosti

- Spravuje seznam více dekódovaných snímků pro potenciální použití jako predikční reference.
- Umožňuje kodéru vybrat pro kódování referenční snímek jiný než ten nejnovější.
- Explicitně signalizuje vybranou sadu referenčních snímků v hlavičkách sliců videobitstreamu.
- Umožňuje rychlé zotavení ze ztráty paketu přepnutím na starší, bezchybný referenční snímek.
- Snižuje časové šíření chyb bez vysoké režie častých intra-snímků.
- Pro optimální fungování vyžaduje zpětnou vazbu od dekodéru ke kodéru (např. prostřednictvím RTCP NACK).

## Související pojmy

- [AVC – Assured Voice Communication](/mobilnisite/slovnik/avc/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [RPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rps/)
