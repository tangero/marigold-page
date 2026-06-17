---
slug: "isobmff"
url: "/mobilnisite/slovnik/isobmff/"
type: "slovnik"
title: "ISOBMFF – International Organization for Standards, Base Media File Format"
date: 2025-01-01
abbr: "ISOBMFF"
fullName: "International Organization for Standards, Base Media File Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/isobmff/"
summary: "ISOBMFF je standard ISO definující strukturovaný kontejnerový formát pro ukládání a streamování multimediálního obsahu, jako je video a audio. V rámci 3GPP je adaptován pro služby jako DASH a MBMS, co"
---

ISOBMFF je standardizovaný kontejnerový formát ISO, který 3GPP adaptoval pro služby jako DASH a MBMS, aby umožnil efektivní multimediální streamování a vysílání v mobilních sítích.

## Popis

[ISO](/mobilnisite/slovnik/iso/) Base Media File Format (ISOBMFF) je mezinárodní standard (ISO/[IEC](/mobilnisite/slovnik/iec/) 14496-12), který specifikuje strukturovaný, objektově orientovaný kontejnerový formát pro ukládání a přenos časově založeného multimediálního obsahu včetně videa, audia a metadat. V rámci 3GPP slouží ISOBMFF jako základ pro různé mechanismy doručování médií, především pro Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) a Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Formát organizuje mediální data do diskrétních jednotek nazývaných 'boxy' nebo 'atomy', které zapouzdřují různé typy informací, jako jsou mediální vzorky, časování a popisy stop. Tato modulární architektura umožňuje flexibilní kompozici, efektivní streamování a snadné parsování klientskými zařízeními.

V provozu ISOBMFF funguje tak, že segmentuje mediální obsah do sekvence filmových fragmentů, z nichž každý obsahuje jednu nebo více stop (např. samostatné stopy pro video a audio). Každá stopa je složena ze vzorků (např. jednotlivých snímků videa nebo audio paketů) s přidruženými informacemi o časování a synchronizaci. Struktura souboru zahrnuje box 'moov' (movie box), který obsahuje metadata o celé prezentaci, a boxy 'mdat' (media data boxes), které obsahují skutečné mediální vzorky. Pro streamovací aplikace jako DASH je obsah dále rozdělen na segmenty, z nichž každý je samostatný soubor nebo fragment ISOBMFF, což umožňuje klientům adaptivně vyžadovat segmenty na základě síťových podmínek.

Klíčovými komponentami ISOBMFF v kontextech 3GPP jsou Common Media Application Format ([CMAF](/mobilnisite/slovnik/cmaf/)), který profiluje ISOBMFF pro segmentované doručování médií, a podpora šifrování a správy digitálních práv ([DRM](/mobilnisite/slovnik/drm/)) prostřednictvím standardů jako Common Encryption ([CENC](/mobilnisite/slovnik/cenc/)). Rozšiřitelnost formátu umožňuje 3GPP definovat specifické boxy pro funkce jako časovaný text (titulky), značky kapitol a alternativní rychlosti přehrávání. Díky využití ISOBMFF zajišťuje 3GPP interoperabilitu mediálních služeb s širokou škálou zařízení a platforem, podporuje vysoce kvalitní streamování, efektivní využití šířky pásma a robustní obnovu po chybách v mobilním prostředí.

## K čemu slouží

ISOBMFF byl vytvořen, aby poskytl univerzální, flexibilní kontejnerový formát pro multimediální obsah, který řešil fragmentaci a neefektivitu proprietárních formátů v raných dobách digitálních médií. Jeho účelem v rámci 3GPP je umožnit efektivní a adaptivní streamovací služby v mobilních sítích, kde jsou významnou výzvou proměnlivá šířka pásma a různorodost zařízení. Standardizací na ISOBMFF řeší 3GPP problémy související s balením obsahu, škálovatelností doručování a kompatibilitou přehrávání mezi různými výrobci a poskytovateli služeb.

Historicky, před ISOBMFF, se doručování multimédií často spoléhalo na formáty jako AVI nebo MPEG-2 Transport Streamy, které mohly být méně optimalizované pro adaptivní streamování nebo internetové protokoly. Vývoj ISOBMFF, původně součást standardu MPEG-4, poskytl moderní, objektově orientovanou strukturu, která lépe podporuje funkce jako náhodný přístup, editaci a streamování. 3GPP přijalo a rozšířilo ISOBMFF, aby splnilo specifické požadavky mobilních sítí, jako je snížená latence pro živé streamování a efektivní využití vysílacích schopností v MBMS.

Motivací pro integraci ISOBMFF do standardů 3GPP, zejména od vydání 12, byl růst spotřeby videa na mobilních zařízeních a potřeba standardizovaného adaptivního streamování s proměnnou datovou rychlostí. Umožňuje operátorům nasazovat služby jako DASH bez uzamčení do řešení specifických pro dodavatele, čímž snižuje náklady a zlepšuje uživatelský zážitek. Navíc podpora pokročilých funkcí jako šifrování a fragmentované streamování v ISOBMFF koresponduje s cíli 3GPP pro zabezpečené, škálovatelné doručování médií v vyvíjejících se síťových architekturách, jako je 5G.

## Klíčové vlastnosti

- Objektově orientovaný kontejnerový formát využívající boxy/atomy pro strukturovaná data
- Podpora adaptivního streamování prostřednictvím segmentovaných mediálních fragmentů
- Rozšiřitelnost pro specifická rozšíření 3GPP, jako CMAF a DASH
- Integrace se standardy šifrování (např. CENC) pro DRM
- Efektivní ukládání a přenos pomocí filmových fragmentů a stop
- Kompatibilita se širokou škálou kodeků a typů metadat

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [MPEG – Moving Pictures Experts Group](/mobilnisite/slovnik/mpeg/)
- [CMAF – Common Media Application Format](/mobilnisite/slovnik/cmaf/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [ISOBMFF na 3GPP Explorer](https://3gpp-explorer.com/glossary/isobmff/)
