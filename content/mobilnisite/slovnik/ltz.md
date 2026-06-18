---
slug: "ltz"
url: "/mobilnisite/slovnik/ltz/"
type: "slovnik"
title: "LTZ – Local Time Zone"
date: 2025-01-01
abbr: "LTZ"
fullName: "Local Time Zone"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ltz/"
summary: "Místní časové pásmo (LTZ) je parametr správy sítě představující časový posun vůči UTC pro konkrétní geografickou oblast. Používá se pro časové značkování síťových událostí, fakturačních záznamů a služ"
---

LTZ je parametr správy sítě představující časový posun vůči UTC pro konkrétní geografickou oblast, používaný pro časové značkování síťových událostí, fakturačních záznamů a služeb účastníků.

## Popis

Místní časové pásmo (LTZ) ve standardech 3GPP je základní administrativní a provozní parametr, který definuje standardní časový posun vůči koordinovanému světovému času ([UTC](/mobilnisite/slovnik/utc/)) pro danou síť nebo geografický region. Nejde o dynamický protokol, ale o konfigurovaný datový prvek používaný napříč různými síťovými funkcemi a rozhraními. Hodnota LTZ typicky zahrnuje posun v hodinách a minutách (např. +01:00 pro středoevropský čas) a může také zohledňovat pravidla letního času ([DST](/mobilnisite/slovnik/dst/)), ačkoli aplikace DST je často řešena samostatně.

Z architektonického hlediska jsou informace o LTZ zřízeny v rámci síťových prvků, jako je Operations Support System ([OSS](/mobilnisite/slovnik/oss/)), Network Management System ([NMS](/mobilnisite/slovnik/nms/)) a uzly základní sítě, například Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo účtovací systémy. Jsou distribuovány příslušným funkcím, které vyžadují lokalizované časové značky. Například když je funkcí účtovacích dat vygenerován záznam detailu hovoru ([CDR](/mobilnisite/slovnik/cdr/)), síťový prvek použije nakonfigurované LTZ (a případně úpravu pro DST) na interní UTC časovou značku, aby vytvořil místní čas pro záznam. Tím je zajištěno, že fakturační události jsou zaznamenávány v místním čase účastníka.

Parametr funguje jako statická nebo semi-statická konfigurace. Specifikace jako TS 21.905 (Vocabulary for 3GPP Specifications) definují tento termín a jeho kontext. Jeho role je klíčová pro správu sítě, hlášení poruch, měření výkonu a zákonné odposlechy, kde musí být události korelovány v místním čase z právních a provozních důvodů. V kontextech týkajících se účastníka může LTZ ovlivnit prezentaci času na faktuře, plánování časově vázaných služeb nebo fungování funkcí, jako je blokování hovorů v závislosti na denní době.

Ačkoli se zdá jednoduchý, konzistentní konfigurace LTZ je zásadní napříč sítěmi více dodavatelů, aby se předešlo časovým nesrovnalostem v logech a záznamech. Je klíčovou součástí administrativních dat sítě spolu s parametry jako identifikátory sítě a kódy zemí. Zpracování přechodů LTZ (např. pro DST) vyžaduje pečlivé postupy, aby se předešlo duplicitním nebo chybějícím časovým značkám v účtovacích a logovacích systémech.

## K čemu slouží

Koncept místního časového pásma existuje pro řešení problému časové reference v globálně nasazených telekomunikačních sítích. Síťové prvky interně typicky používají pro měření času [UTC](/mobilnisite/slovnik/utc/), aby se předešlo nejednoznačnosti. Téměř všechny provozní, komerční a právní výstupy – jako zákaznické faktury, logy síťových událostí a regulatorní reporty – však musí být prezentovány v místním občanském čase země nebo regionu, kde byla služba spotřebována nebo událost nastala.

Bez standardizovaného parametru LTZ by každý síťový prvek nebo dodavatel mohl převod na místní čas implementovat odlišně, což by vedlo k nekonzistentnostem ve fakturačních záznamech, obtížím při korelaci hlášení poruch napříč systémy správy a potenciálnímu nesplnění předpisů na ochranu spotřebitele, které vyžadují fakturaci v místním čase. Před formální standardizací mohly ad-hoc implementace způsobovat chyby, zejména při změnách letního času nebo v regionech s neobvyklými časovými posuny.

Jeho vytvoření a formální definice ve specifikacích 3GPP bylo motivováno potřebou interoperability a konzistence v řídicích a účtovacích datech napříč mezinárodními síťovými nasazeními. Řeší omezení používání pouze UTC časových značek, které jsou technicky přesné, ale pro zákaznicky orientované dokumenty nejsou uživatelsky přívětivé nebo právně dostačující. Definováním LTZ jako spravovaného parametru 3GPP zajišťuje, že všechny síťové funkce mají konzistentní referenci pro převod interních UTC časových značek na správný místní čas, což je zásadní pro přesné účtování, jasné řešení problémů a splnění jurisdikčních právních požadavků.

## Klíčové vlastnosti

- Definuje standardní časový posun vůči UTC pro geografickou oblast
- Používá se pro lokalizaci časových značek v CDR a logech síťových událostí
- Zřizován jako konfigurační data v OSS/NMS a uzlech základní sítě
- Zajišťuje konzistentní prezentaci času pro účtování a správu
- Klíčový pro regulatorní a provozní shodu
- Může být asociován se sadami pravidel pro letní čas (DST)

## Související pojmy

- [UTC – Coordinated Universal Time](/mobilnisite/slovnik/utc/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [LTZ na 3GPP Explorer](https://3gpp-explorer.com/glossary/ltz/)
