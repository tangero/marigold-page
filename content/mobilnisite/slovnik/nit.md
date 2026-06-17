---
slug: "nit"
url: "/mobilnisite/slovnik/nit/"
type: "slovnik"
title: "NIT – Network Information Table"
date: 2025-01-01
abbr: "NIT"
fullName: "Network Information Table"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nit/"
summary: "Datová struktura definovaná v 3GPP pro vysílání síťových informací k uživatelskému zařízení. Používá se primárně v MBMS k předávání podrobností o službách a síti, což umožňuje efektivní vyhledání a př"
---

NIT je datová struktura definovaná v 3GPP pro vysílání informací o síti a službách k uživatelskému zařízení, primárně v MBMS, která umožňuje efektivní vyhledání a přístup k vysílacím nebo multicastovým službám.

## Popis

Network Information Table (NIT, tabulka síťových informací) je strukturovaná datová tabulka specifikovaná v kontextu služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) v 3GPP. Funguje jako kontejner pro vysílané informace, který je přenášen ze sítě k uživatelskému zařízení (UE) za účelem poskytnutí klíčových podrobností o dostupných službách MBMS a konfiguraci sítě, která je podporuje. NIT je definována ve specifikaci 3GPP TS 26.917, která se zaměřuje na protokoly a kodeky MBMS. Jejím hlavním úkolem je usnadnit vyhledávání služeb, což umožňuje UE efektivně identifikovat a přistupovat k obsahu MBMS bez nutnosti rozsáhlé vyhrazené signalizace nebo unicastových spojení.

Z architektonického hlediska je NIT generována a spravována ve vysílací/multicastové servisní vrstvě sítě, často je spojována s Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) a prvky rádiového přístupového sítě zodpovědnými za přenos MBMS, jako jsou MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) a eNBy/gNBy v LTE a NR. Tabulka je typicky vysílána přes nosič MBMS pomocí protokolů jako [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/) na aplikační vrstvě. Obsahuje soubor deskriptorů a informačních prvků, které popisují atributy služeb, identifikátory sítě a případně další parametry relevantní pro získání služby.

Mezi klíčové komponenty NIT patří identifikátory sítě (jako PLMN ID), informace o servisní oblasti a odkazy na další důležité tabulky nebo streamy, jako je Service Description Table (SDT) nebo INT (IP/[MAC](/mobilnisite/slovnik/mac/) Notification Table). UE přijímá a parsuje NIT, aby pochopilo, jaké služby MBMS jsou na jeho aktuálním místě dostupné, která síť je poskytuje a jak postupovat k přijetí konkrétní služby. Tento mechanismus je pro UE klíčový pro inicializaci příjmu MBMS, protože snižuje spotřebu energie a signalizační režii ve srovnání s průběžným skenováním nebo unicastovými dotazy.

NIT hraje v ekosystému MBMS zásadní roli tím, že odděluje oznamování služeb od vlastního přenosu médií. Funguje jako centralizovaný zdroj informací na síťové úrovni, což umožňuje škálovatelné a efektivní nasazení vysílacích služeb. Pro síťové operátory umožňuje flexibilní definici servisních oblastí a správu síťových zdrojů. Pro koncové uživatele umožňuje bezproblémové vyhledávání a přepínání mezi různými vysílacími službami, což zlepšuje uživatelský zážitek u aplikací jako živé TV, komunikace pro veřejnou bezpečnost nebo bezdrátové aktualizace softwaru.

## K čemu slouží

NIT byla zavedena, aby vyřešila potřebu efektivního, standardizovaného mechanismu pro vyhledávání služeb a distribuci síťových informací ve vysílacích a multicastových službách v sítích 3GPP. Před její standardizací se vyhledávání vysílacích služeb často opíralo o proprietární metody nebo mechanismy mimo přenosovou cestu, což vedlo k problémům s interoperabilitou, zvýšené složitosti UE a vyšší spotřebě energie kvůli neefektivnímu skenování. Vytvoření [MBMS](/mobilnisite/slovnik/mbms/) vyžadovalo jednotný způsob, jak mohou UE rychle identifikovat dostupné služby bez nutnosti navazovat jednotlivá unicastová spojení pro dotazování.

Hlavním problémem, který NIT řeší, je snížení signalizační režie a spotřeby energie UE ve scénářích, kdy více UE v geografické oblasti potřebuje objevit stejnou sadu vysílacích služeb. Vysíláním NIT síť tyto informace poskytne všem UE současně. To je obzvláště kritické pro zařízení s omezenou kapacitou baterie a pro škálování na velký počet uživatelů, jako jsou události na stadionech nebo nouzová varování. NIT také poskytuje strukturovaný rámec, který odděluje informace o topologii sítě od metadat specifických pro službu, což umožňuje flexibilnější návrh sítě a nasazení služeb.

Historicky její zavedení v Release 14 časově souviselo s vylepšeními MBMS založeného na LTE (eMBMS) a zkoumáním vysílacích schopností pro nové případy užití. Poskytla základ pro budoucí evoluce, včetně integrace s multicast-broadcast službami 5G NR. NIT standardizuje informace, které byly dříve fragmentované nebo zpracovávané nekonzistentně, a zajišťuje, že UE od různých výrobců mohou spolehlivě vyhledat a přistupovat ke službám MBMS napříč různými operátorskými sítěmi, čímž podporuje růst ekosystému a interoperabilitu služeb.

## Klíčové vlastnosti

- Vysílá identifikační informace o síti (např. PLMN ID) pro služby MBMS
- Předává definice servisních oblastí a geografický rozsah vysílacích nabídek
- Odkazuje na další klíčové tabulky MBMS, jako je Service Description Table (SDT)
- Umožňuje efektivní vyhledání dostupných multicast/vysílacích služeb zařízením UE
- Snižuje spotřebu energie UE a síťovou signalizační režii
- Podporuje flexibilní konfiguraci sítě a služeb pro operátory

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [NIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/nit/)
