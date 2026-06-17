---
slug: "eit"
url: "/mobilnisite/slovnik/eit/"
type: "slovnik"
title: "EIT – Event Information Table"
date: 2025-01-01
abbr: "EIT"
fullName: "Event Information Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eit/"
summary: "Datová tabulka používaná ve službě Multimedia Broadcast/Multicast Service (MBMS) a její pokročilé verzi (eMBMS) k poskytování plánovacích informací pro vysílací události. Uvádí časování, délku trvání"
---

EIT je datová tabulka používaná v MBMS a eMBMS, která poskytuje plánovací informace, uvádí časování, délku trvání a identifikátory nadcházejících vysílacích událostí, aby umožnila efektivní příjem uživatelským zařízením.

## Popis

Event Information Table (EIT) je klíčová signalizační komponenta ve servisní vrstvě služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) organizace 3GPP a její pokročilé verze (eMBMS). Definována ve specifikaci 26.917 je součástí frameworku pro doručování a přenos souborů založeného na [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/), používaného pro distribuci vysílaného obsahu. EIT je v podstatě strukturovaná datová tabulka, která nese metadata o plánovaných vysílacích událostech nebo relacích. Jejím hlavním účelem je informovat uživatelské zařízení (UE) o tom, jaký obsah bude vysílán, kdy bude dostupný a jak k němu získat přístup, což umožňuje UE efektivně spravovat svůj přijímač a zdroje.

Z architektonického hlediska je EIT generována Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je hlavní síťová entita odpovědná za poskytování a doručování služeb MBMS. Tabulka je poté doručena k uživatelským zařízením přes vysílací přenosový kanál, typicky vložena do File Delivery Table ([FDT](/mobilnisite/slovnik/fdt/)) protokolu File Delivery over Unidirectional Transport (FLUTE). Když má uživatelské zařízení zájem o vysílací službu, nejprve získá servisní průvodce, který může odkazovat na EIT nebo ji obsahovat. UE poté parsuje EIT, aby získalo plán. Tabulka obsahuje záznamy pro jednotlivé události, každý s poli jako event_id, start_time, duration, service_id a content descriptors. To umožňuje UE přesně vědět, kdy aktivovat svůj přijímač pro naladění na správný multicast/broadcast kanál (např. [MCH](/mobilnisite/slovnik/mch/) nebo [MTCH](/mobilnisite/slovnik/mtch/) v LTE) pro příjem konkrétní události, čímž šetří baterii tím, že se vyhne neustálému příjmu.

Jak to funguje, je v zásadě o plánování a objevování. EIT poskytuje časovou osu událostí. Například pro službu mobilní televize by EIT uváděla programový plán. MBMS klientská aplikace v UE používá tuto informaci k prezentaci elektronického programového průvodce ([EPG](/mobilnisite/slovnik/epg/)) uživateli. Když uživatel vybere budoucí program, klient si může na základě start_time z EIT nastavit interní upozornění. Ve stanovený čas UE probudí příslušné protokolové stacky, připojí se k příslušné multicast skupině a začne přijímat FLUTE relaci nesoucí mediální soubory pro danou událost. Tento push-based plánovací mechanismus je efektivní pro vysílání společného obsahu mnoha uživatelům současně, protože minimalizuje potřebu individuálních signalizačních požadavků na síť.

## K čemu slouží

Event Information Table byla vytvořena, aby řešila potřebu efektivního plánování a uživatelského objevování vysílaného a multicastového obsahu v mobilních sítích. Před standardizovanými mechanismy, jako je EIT, by doručování plánovaných vysílacích služeb (jako živá TV nebo aktualizace softwaru) vyžadovalo buď nepřetržitý přenos – což plýtvá síťovými a zařízeními zdroji – nebo složitou signalizaci mimo přenosový pásmo pro individuální upozornění každého zařízení. Žádný z těchto přístupů se neškáluje dobře pro hromadnou distribuci.

EIT, zavedená v kontextu vylepšení eMBMS kolem Release 14, to řeší poskytováním lehkého plánu v přenosovém pásmu, který všechna zařízení ve vysílací oblasti mohou přijmout jednou a používat nezávisle. Umožňuje funkci 'oznámení' pro vysílací služby. To umožňuje uživatelskému zařízení vypnout přijímače, když není vysílán obsah jeho zájmu, což výrazně zlepšuje výdrž baterie u zařízení s podporou vysílání. Dále zlepšuje uživatelský zážitek tím, že umožňuje známé elektronické programové průvodce, čímž činí vysílací služby dostupnějšími a konkurenceschopnými vůči unicastovému streamování. EIT je klíčovým prvkem pro efektivní plánované doručování obsahu přes LTE a 5G broadcast, podporujíc use case jako výstrahy pro veřejnou bezpečnost, pokrytí živých událostí a distribuci softwaru ve velkém měřítku.

## Klíčové vlastnosti

- Poskytuje plánovací informace pro vysílací události MBMS/eMBMS
- Obsahuje identifikátory událostí, časy začátku, délky trvání a přiřazení ke službám
- Doručována v přenosovém pásmu přes vysílací přenosový kanál pomocí protokolů FLUTE/ALC
- Umožňuje uživatelskému zařízení implementovat strategie příjmu šetřící energii
- Podporuje vytváření elektronických programových průvodců (EPG) pro uživatelské aplikace
- Generována Broadcast Multicast Service Center (BM-SC) v jádru sítě

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [EIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/eit/)
