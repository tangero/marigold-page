---
slug: "ic-bwe"
url: "/mobilnisite/slovnik/ic-bwe/"
type: "slovnik"
title: "IC-BWE – Inter-Channel BandWidth Extension"
date: 2025-01-01
abbr: "IC-BWE"
fullName: "Inter-Channel BandWidth Extension"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ic-bwe/"
summary: "Vylepšující funkce kodeku zavedená ve 3GPP Release 18 pro kodek EVS. Uměle rozšiřuje zvukové pásmo úzkopásmových (NB) nebo širokopásmových (WB) řečových signálů, aby poskytla plnější a přirozenější zv"
---

IC-BWE je funkcí kodeku EVS ve 3GPP Release 18, která uměle rozšiřuje zvukové pásmo řečových signálů, aby poskytla plnější a přirozenější zvukovou kvalitu.

## Popis

Inter-Channel BandWidth Extension (IC-BWE, rozšíření pásma mezi kanály) je pokročilá funkce zpracování zvuku standardizovaná pro kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) ve 3GPP. Funguje na principu rozšíření pásma, při kterém přijímač rekonstruuje vysokofrekvenční složky zvukového signálu, které nebyly vysílány kvůli omezením šířky pásma původního kanálu. Klíčový mechanismus spočívá v analýze přijímaného úzkopásmového ([NB](/mobilnisite/slovnik/nb/): 300-3400 Hz) nebo širokopásmového ([WB](/mobilnisite/slovnik/wb/): 50-7000 Hz) signálu za účelem extrakce spektrálních a časových charakteristik. Pomocí sofistikovaných parametrických modelů a technik inspirovaných strojovým učením dekodér předpovídá a syntetizuje chybějící frekvenční obsah, aby rozšířil pásmo až na super-širokopásmové ([SWB](/mobilnisite/slovnik/swb/): 50-14000 Hz) nebo plné pásmo ([FB](/mobilnisite/slovnik/fb/): 20-20000 Hz).

Architektura IC-BWE je vestavěna v dekodéru EVS. Nevyžaduje další bity ve vysílaném bitovém toku; místo toho využívá vedlejší informace odvozené z jádrově kódovaného pásma a aplikuje algoritmus rozšíření pásma. Mezi klíčové komponenty patří modul pro replikaci spektrálního pásma ([SBR](/mobilnisite/slovnik/sbr/)), generátor vysokých frekvencí a postfiltr pro vyhlazení rozšířeného spektra, aby se zabránilo artefaktům. Proces se provádí nezávisle pro každý kanál v nastavení vícekanálového zvuku, což zajišťuje kompatibilitu se stereofonními nebo immersivními hlasovými službami.

Jeho úlohou v síti je zlepšit kvalitu uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)) u hovorů bez zvýšení požadované šířky pásma sítě. Umožňuje poskytovatelům služeb doručovat zvuk vysoké kvality i v případě, že podkladová přenosová síť nebo rádiový spoj jsou omezeny na nižší šířky pásma. Například hovor uskutečněný ze starší NB sítě může být na schopném přijímacím zařízení vnímán jako kvalita SWB. Tato funkce je zvláště cenná pro over-the-top ([OTT](/mobilnisite/slovnik/ott/)) komunikační služby a VoLTE/VoNR, protože zajišťuje konzistentně vysokou zvukovou kvalitu napříč různorodými síťovými podmínkami a možnostmi zařízení.

## K čemu slouží

IC-BWE bylo vytvořeno, aby překlenulo propast mezi možnostmi zvukové kvality moderních zařízení a omezeními starší síťové infrastruktury a kodeků. Zatímco sítě a zařízení se vyvinuly tak, aby podporovala HD Voice (WB) a super-širokopásmový zvuk, mnoho hovorů stále pochází z přechází přes sítě omezené na úzkopásmové přenosy. To má za následek zhoršený, 'plechový' zvukový dojem.

Problém, který řeší, je nekonzistentní a často špatná vnímaná zvuková kvalita v reálných scénářích volání. Tradiční metody vyžadovaly end-to-end podporu širokopásmových kodeků, což nebylo vždy proveditelné. IC-BWE představuje řešení na straně přijímače, které umožňuje zařízení na posledním úseku jednosměrně vylepšit zvuk. Jeho zavedení v Release 18 bylo hnací silou snahy o immersivní komunikační zážitky, včetně rozšířené reality a aplikací metaverse, kde je věrný zvuk zásadní. Řeší omezení předchozích přístupů tím, že poskytuje vylepšení kvality bez jakýchkoli změn na vysílací straně nebo v jádru sítě.

## Klíčové vlastnosti

- Umělé rozšíření zvukového pásma z NB/WB na SWB/FB na straně přijímače
- Funguje bez dodatečné režie v přenosové rychlosti ve vysílaném rámci EVS
- Využívá parametrické modely a techniky replikace spektrálního pásma (SBR)
- Zlepšuje vnímanou zvukovou kvalitu, poskytuje bohatší a přirozenější zvuk
- Funguje nezávisle na každém zvukovém kanálu pro podporu vícekanálového zvuku
- Zpětně kompatibilní; pro užitek vyžaduje implementaci pouze na straně dekodéru

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [IC-BWE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ic-bwe/)
