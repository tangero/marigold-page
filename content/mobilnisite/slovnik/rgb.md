---
slug: "rgb"
url: "/mobilnisite/slovnik/rgb/"
type: "slovnik"
title: "RGB – Red-Green-Blue colour space"
date: 2025-01-01
abbr: "RGB"
fullName: "Red-Green-Blue colour space"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rgb/"
summary: "Barevný model, který reprezentuje barvy jako kombinace složek červeného, zeleného a modrého světla, používaný ve specifikacích 3GPP pro multimediální služby, zejména pro video kódování, zobrazovací te"
---

RGB je barevný model, který reprezentuje barvy jako kombinace složek červeného, zeleného a modrého světla, používaný v 3GPP pro kódování a přenos barev ve video a multimediálních službách.

## Popis

Barevný prostor Red-Green-Blue (RGB) je aditivní barevný model, kde se barvy vytvářejí kombinací různých intenzit červeného, zeleného a modrého světla. Ve specifikacích 3GPP je RGB odkazováno v kontextech souvisejících s multimediálním kódováním, zobrazovacími technologiemi a aplikacemi jako rozšířená realita ([AR](/mobilnisite/slovnik/ar/)) a virtuální realita ([VR](/mobilnisite/slovnik/vr/)). Pro video služby může být RGB použito jako vstupní barevný prostor, který je převeden na YUV (jas a barevnost) pro efektivnější kompresi v kodecích jako H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/). Specifikace detailně popisují matice převodu barevného prostoru, reprezentaci bitové hloubky (typicky 8, 10 nebo 12 bitů na složku) a definice barevného gamutu (jako sRGB nebo [BT](/mobilnisite/slovnik/bt/).2020) pro zajištění konzistentní reprodukce barev na různých zařízeních. V AR aplikacích jsou RGB data ze snímačů kamery zpracována a potenciálně překryta počítačově generovanou grafikou. Standardy 3GPP zajišťují, že RGB barevné informace jsou správně zpracovávány v end-to-end multimediálních řetězcích, od tvorby obsahu přes síťový přenos až po finální zobrazení, při zachování barevné přesnosti a kompatibility napříč různými zařízeními a sítěmi.

## K čemu slouží

Specifikace barevného prostoru RGB v 3GPP řeší potřebu standardizované barevné reprezentace v multimediálních službách poskytovaných přes mobilní sítě. Jak se mobilní zařízení vyvinula pro podporu vysoce kvalitního streamování videa, videohovorů a imerzních [AR](/mobilnisite/slovnik/ar/)/[VR](/mobilnisite/slovnik/vr/) zážitků, stala se konzistentní reprodukce barev klíčovou pro uživatelský zážitek. Různá zařízení (telefony, tablety, AR brýle) a zdroje obsahu mohou používat různé barevné prostory a gamuty; bez standardizace by se barvy mohly jevit vybledlé, přesycené nebo nekonzistentní. 3GPP zahrnuje definice RGB pro zajištění interoperability mezi nástroji pro tvorbu obsahu, síťovými přenosovými protokoly a zobrazovacími zařízeními. Tím se řeší problémy barevného nesouladu v multimediálních aplikacích a umožňují se pokročilé funkce jako video s vysokým dynamickým rozsahem ([HDR](/mobilnisite/slovnik/hdr/)), kde je přesná barevná reprezentace nezbytná. Specifikace poskytují společný referenční bod, který mohou poskytovatelé obsahu, síťoví operátoři a výrobci zařízení používat k zajištění předvídatelných a vysoce kvalitních vizuálních zážitků.

## Klíčové vlastnosti

- Aditivní barevný model kombinující složky červeného, zeleného a modrého světla
- Podpora různých bitových hloubek (8-bit, 10-bit, 12-bit) pro barevnou přesnost
- Definice barevných gamutů jako sRGB a BT.2020 pro různé typy obsahu
- Matice převodu barevného prostoru pro transformaci do/z YUV pro video kódování
- Integrace s video kodeky (HEVC, VVC) pro efektivní kompresi
- Použití v AR/VR pro zpracování dat kamery a překryv grafiky

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [HDR – High Dynamic Range](/mobilnisite/slovnik/hdr/)
- [AR – Application Relation](/mobilnisite/slovnik/ar/)
- [VVC – Versatile Video Coding](/mobilnisite/slovnik/vvc/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [RGB na 3GPP Explorer](https://3gpp-explorer.com/glossary/rgb/)
