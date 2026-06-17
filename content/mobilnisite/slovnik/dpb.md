---
slug: "dpb"
url: "/mobilnisite/slovnik/dpb/"
type: "slovnik"
title: "DPB – Decoded Picture Buffer"
date: 2025-01-01
abbr: "DPB"
fullName: "Decoded Picture Buffer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dpb/"
summary: "Vyrovnávací paměť ve videokodecích, která ukládá dekódované referenční snímky pro použití v mezisnímkové predikci. Je základní součástí standardů video komprese jako H.264/AVC a H.265/HEVC, umožňuje e"
---

DPB je vyrovnávací paměť ve videokodeku, která ukládá dekódované referenční snímky pro mezisnímkovou predikci, což umožňuje efektivní časovou kompresi a zajišťuje správný pořadí přehrávání.

## Popis

Decoded Picture Buffer (DPB) je klíčová komponenta správy paměti v procesech kódování a dekódování videa standardizovaných orgány jako [ITU-T](/mobilnisite/slovnik/itu-t/) a [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) a odkazovaná v 3GPP pro multimediální služby. Její primární funkcí je ukládání dekódovaných obrazů (snímků), které byly rekonstruovány dekodérem. Tyto uložené snímky slouží jako referenční snímky pro dekódování následujících mezisnímkově kódovaných snímků (P-snímků a B-snímků). Mezisnímková predikce spoléhá na odhad pohybu a kompenzaci pohybu, kde jsou bloky v aktuálním snímku predikovány z bloků v dříve dekódovaných referenčních snímcích uložených v DPB. Dekodér používá DPB ke správě dostupnosti a pořadí těchto referenčních snímků.

Architektonicky je DPB spravován modelem Hypothetical Reference Decoder ([HRD](/mobilnisite/slovnik/hrd/)), který definuje pravidla správy vyrovnávací paměti pro zabránění přetečení a podtečení a zajištění konstantní dekódovací rychlosti. DPB má definovanou maximální velikost, specifikovanou v bitovém toku, která omezuje, kolik referenčních snímků může být uloženo současně. Operace dekodéru zahrnují umístění nově dekódovaného snímku do DPB, označování snímků jako 'použité pro referenci' nebo 'nepoužité pro referenci' a odstranění snímků na základě příkazů z bitového toku (jako operace řízení správy paměti) nebo když již nejsou potřeba pro predikci nebo výstup. Výstupní proces, který doručuje snímky k zobrazení, je oddělen od správy referenčních snímků a DPB zajišťuje, že snímky jsou vyvedeny ve správném zobrazovacím pořadí, které se může lišit od dekódovacího pořadí, zejména u B-snímků.

V 3GPP je DPB relevantní ve specifikacích jako TS 26.119 a 26.906, které se zabývají shodou a výkonem multimediálních kodeků pro služby jako Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Správné fungování DPB přímo ovlivňuje kvalitu videa, efektivitu šířky pásma a složitost dekodéru. Pokud je správa DPB chybná, může vést k vizuálním artefaktům, dekódovacím chybám nebo porušení vyrovnávací paměti, které přeruší proces dekódování. Proto specifikace kodeků 3GPP zahrnují omezení a testy k zajištění, že chování DPB je předvídatelné a interoperabilní mezi různými zařízeními a sítěmi, což je nezbytné pro spolehlivé služby video streamování a komunikace.

## K čemu slouží

Decoded Picture Buffer existuje k vyřešení základního problému časové redundance ve video sekvencích. Standardy video komprese dosahují vysokých kompresních poměrů tím, že nepřenášejí opakovaně celé snímky, ale místo toho posílají rozdíly (rezidua) vzhledem k dříve přeneseným referenčním snímkům. DPB poskytuje potřebnou paměť pro uchování těchto referenčních snímků v dekodéru, což umožňuje predikci s kompenzací pohybu. Bez spravované vyrovnávací paměti pro referenční snímky by efektivní mezisnímkové kódování nebylo možné, což by vedlo k drasticky větším velikostem souborů nebo datovým tokům nevhodným pro mobilní sítě.

Historický kontext vychází z vývoje standardů video kódování od [MPEG-2](/mobilnisite/slovnik/mpeg-2/) přes H.264/[AVC](/mobilnisite/slovnik/avc/) až po H.265/HEVC, z nichž každý zaváděl sofistikovanější správu DPB pro podporu funkcí jako více referenčních snímků, adaptivní výběr referenčních snímků a hierarchické kódovací struktury. V mobilních komunikacích je šířka pásma cenným zdrojem a video je dominantním typem provozu. Zařazení parametrů a bodů shody souvisejících s DPB do specifikací 3GPP (např. pro MBMS nebo paketové streamování) zajišťuje, že video služby jsou efektivně a spolehlivě doručovány různorodým zařízením. Řeší to omezení jednodušších modelů vyrovnávací paměti, které nemohly podporovat pokročilé predikční nástroje potřebné pro video vysoké kvality s nízkým datovým tokem, což je zásadní pro uživatelský zážitek na mobilních sítích s omezenou šířkou pásma.

## Klíčové vlastnosti

- Ukládá dekódované referenční snímky pro predikci s kompenzací pohybu
- Spravován podle modelu Hypothetical Reference Decoder (HRD)
- Má definovanou maximální velikost pro omezení paměti dekodéru
- Podporuje označování snímků jako 'použité pro referenci' nebo 'nepoužité pro referenci'
- Umožňuje přeřazení výstupu pro správnou zobrazovací posloupnost (např. pro B-snímky)
- Klíčový pro testování shody video dekodérů ve specifikacích 3GPP pro multimédia

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [HRD – Hypothetical Reference Decoder](/mobilnisite/slovnik/hrd/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [DPB na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpb/)
