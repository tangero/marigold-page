---
slug: "epg"
url: "/mobilnisite/slovnik/epg/"
type: "slovnik"
title: "EPG – Electronic Program Guide"
date: 2025-01-01
abbr: "EPG"
fullName: "Electronic Program Guide"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/epg/"
summary: "Elektronický programový průvodce (EPG) je multimediální služba, která uživatelům poskytuje interaktivní, menu-řízené rozhraní pro prohlížení, vyhledávání a plánování nadcházejícího vysílaného i on-dem"
---

EPG je standardizovaná služba elektronického programového průvodce (Electronic Program Guide) v 3GPP, která poskytuje uživatelům interaktivní rozhraní pro prohlížení, vyhledávání a plánování vysílaného i on-demand obsahu, efektivně distribuovaného přes MBMS.

## Popis

Elektronický programový průvodce (EPG) je komplexní služba metadat, která tvoří uživatelské rozhraní pro objevování a přístup k lineárnímu vysílanému i on-demand multimediálnímu obsahu. Standardizovaný v rámci 3GPP, zejména ve vztahu k distribuci přes službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), poskytuje EPG strukturované informace o dostupných pořadech, včetně názvu, synopse, času začátku/konce, žánru, hodnocení věkové přístupnosti, obsazení a odkazů na související obsah. Je typicky prezentován jako interaktivní mřížka nebo seznam na uživatelském zařízení, umožňující navigaci v čase, kanálech a kategoriích obsahu. Specifikace 3GPP, jako je TS 26.918, definují protokoly a formáty pro efektivní distribuci, aktualizaci a využívání dat EPG, čímž zajišťují interoperabilitu mezi poskytovateli služeb a zařízeními.

Z architektonické perspektivy zahrnuje služba EPG několik komponent. Broadcast Service Center generuje a spravuje metadata EPG, často ve standardizovaném formátu jako XML (např. TV-Anytime). Tato data jsou následně zabalena pro distribuci. V kontextu 3GPP MBMS mohou být data EPG distribuována prostřednictvím samotného vysílacího/multicastového přenosu nebo přes doplňkové unicastové připojení (např. LTE). Při distribuci přes MBMS jsou data efektivně vysílána všem zařízením v oblasti služby pomocí protokolů File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)) v rámci metody MBMS download delivery. Klientská aplikace na zařízení tato data přijímá, parsuje a ukládá do mezipaměti a prezentuje je uživateli. Klient EPG také zvládá aktualizace, protože programové schéma se může měnit, což vyžaduje dynamické mechanismy obnovy.

Funkcionalita EPG přesahuje pouhý výpis. Umožňuje klíčové uživatelské akce, jako je výběr programu pro okamžité sledování, plánování nahrávání pro funkci Digital Video Recorder (DVR), nastavování upozornění a filtrování rodičovské kontroly na základě hodnocení. Pokročilé EPG podporují funkce vyhledávání, personalizovaná doporučení a bezproblémovou integraci se streamovacími nebo stahovacími službami. V konvergované síti může EPG fungovat jako jednotný portál, agregující obsah z tradičního vysílání (např. přes MBMS) i unicastových streamovacích zdrojů (např. přes IMS). Standardizace 3GPP zajišťuje, že tyto funkce mohou být konzistentně implementovány napříč různými sítěmi a zařízeními, což usnadňuje rozsáhlé nasazení vysílacích a multicastových multimediálních služeb.

## K čemu slouží

Elektronický programový průvodce byl vyvinut k řešení základního problému objevování obsahu v prostředí s neustále rostoucím počtem vysílacích kanálů a on-demand nabídek. Před EPG se uživatelé spoléhali na tištěné programy nebo jednoduchý text na obrazovce, které byly statické, neinteraktivní a nemohly držet krok s rostoucím objemem obsahu. Digitalizace televize a konvergence vysílacích a telekomunikačních sítí vytvořila potřebu dynamického, interaktivního a síťově distribuovaného průvodce, který by mohl zlepšit uživatelský zážitek a umožnit nové služby.

Standardizace EPG v 3GPP, zejména od Release 14 dále, byla motivována vývojem [MBMS](/mobilnisite/slovnik/mbms/) do enhanced Multimedia Broadcast Multicast Service (eMBMS) a jeho integrací s LTE a později s 5G broadcastem. Když mobilní sítě získaly schopnost efektivně distribuovat lineární TV a obsah založený na souborech masivním publikům prostřednictvím vysílání, standardizovaná metoda informování uživatelů o dostupném obsahu se stala nezbytnou. Jednotná specifikace EPG zajišťuje, že zařízení přijímající službu MBMS vysílání v jedné síti může prezentovat informace průvodce konzistentním způsobem, bez ohledu na poskytovatele služeb nebo výrobce síťového vybavení.

EPG navíc umožňuje klíčové obchodní modely pro vysílací služby. Umožňuje poskytovatelům služeb propagovat obsah, nabízet prémiové kanály nebo pay-per-view události a shromažďovat analytické údaje o chování uživatelů při prohlížení. Poskytnutím bohatého, interaktivního rozhraní zvyšuje uživatelskou angažovanost a spotřebu obsahu. Standardizace také připravuje cestu pro pokročilé funkce, jako je cílená vkládání reklamy a personalizovaná doporučení obsahu v rámci samotného průvodce, čímž propojuje efektivnost vysílání s interaktivitou ve stylu unicastu. V podstatě EPG transformuje pasivní vysílací médium na interaktivní platformu pro objevování služeb.

## Klíčové vlastnosti

- Distribuuje strukturovaná metadata (název, čas, popis, hodnocení) pro vysílaný i on-demand obsah
- Podporuje distribuci přes efektivní vysílací/multicastové kanály, jako je MBMS využívající FLUTE
- Umožňuje interaktivní uživatelské funkce: prohlížení, vyhledávání, plánování nahrávání, nastavování upozornění
- Umožňuje dynamické aktualizace pro odrážení změn v programu nebo nové dostupnosti obsahu
- Může být integrován se systémy rodičovské kontroly na základě hodnocení obsahu
- Poskytuje jednotné rozhraní pro obsah z vysílacích i unicastových zdrojů

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP

---

📖 **Anglický originál a plná specifikace:** [EPG na 3GPP Explorer](https://3gpp-explorer.com/glossary/epg/)
