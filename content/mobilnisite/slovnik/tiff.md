---
slug: "tiff"
url: "/mobilnisite/slovnik/tiff/"
type: "slovnik"
title: "TIFF – Tagged Image File Format"
date: 2025-01-01
abbr: "TIFF"
fullName: "Tagged Image File Format"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tiff/"
summary: "TIFF je standardizovaný formát souboru pro ukládání rastrové grafiky a obrazových dat, široce používaný pro vysoce kvalitní snímky. V kontextech 3GPP je odkazován ve specifikacích pro službu multimedi"
---

TIFF je standardizovaný rastrový grafický formát souboru podporovaný ve standardech 3GPP pro interoperabilitu ve službě multimediálních zpráv (MMS) a službách Rich Communication Services (RCS).

## Popis

Formát Tagged Image File Format (TIFF) je flexibilní, přizpůsobitelný rastrový formát obrazových souborů původně vyvinutý společností Aldus (nyní Adobe) pro desktop publishing. Není to protokol vynalezený 3GPP, ale je odkazován v rámci technických specifikací 3GPP, zejména těch, které řídí služby multimediálních zpráv a komunikace, jako standardizovaný formát pro výměnu obrazového obsahu. Soubory TIFF používají strukturu založenou na značkách (tagech) k ukládání obrazových dat a metadat, což umožňuje bezztrátovou kompresi (pomocí algoritmů jako LZW nebo Deflate), více vrstev a vysokou barevnou hloubku, což je činí vhodnými pro vysoce věrné fotografie, skenované dokumenty a grafické umění.

V rámci architektury 3GPP je TIFF specifikován jako přípustný nebo doporučený obrazový formát pro službu multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)), jak je definováno ve specifikacích jako 3GPP TS 22.140 a souvisejících specifikacích fáze 3. Když mobilní zařízení nebo server MMS vytváří nebo zpracovává multimediální zprávu, může kódovat obrazovou přílohu ve formátu TIFF, mimo jiné formáty jako [JPEG](/mobilnisite/slovnik/jpeg/) nebo [PNG](/mobilnisite/slovnik/png/). Specifikace 3GPP zajišťují základní interoperabilitu definováním profilových omezení pro použití TIFF, jako jsou podporované kompresní schémata, maximální rozměry nebo barevné prostory, aby bylo zaručeno, že přijímací zařízení mohou obraz správně dekódovat a zobrazit. To je součástí širší práce na standardizaci adaptace obsahu a mediálních kodeků v pracovních skupinách Services and System Aspects 3GPP.

V pozdějších vydáních, zejména s vývojem služeb Rich Communication Services ([RCS](/mobilnisite/slovnik/rcs/)) a zasílání zpráv založených na IP Multimedia Subsystem (IMS), je podpora TIFF zachována jako součást definic typů objektů rich media. Specifikace jako 3GPP TS 26.955 a 26.956, které pokrývají mediální formáty pro konverzační a nekonverzační služby, mohou odkazovat na TIFF jako na formát pro statický obrazový obsah ve scénářích přenosu souborů nebo sdíleného obsahu. Technické zpracování zahrnuje MMS User Agent nebo RCS klienta na zařízení, MMS Center (MMSC) nebo RCS server pro zasílání zpráv a případně funkce mediálního překódování v rámci sítě, pokud je vyžadována konverze formátu pro přizpůsobení schopnostem zařízení. Role TIFF je jako kontejnerový formát, který zachovává kvalitu obrazu, což je cenné pro profesionální nebo archivní obsah sdílený přes mobilní sítě, i za cenu větších velikostí souborů ve srovnání se ztrátovými formáty jako JPEG.

## K čemu slouží

TIFF je zahrnut ve specifikacích 3GPP, aby zajistil širokou interoperabilitu a podporu pro výměnu vysoce kvalitních snímků v mobilních službách zasílání zpráv. Během vývoje [MMS](/mobilnisite/slovnik/mms/) v 3GPP Release 99 a dále byla potřeba standardizovat sadu mediálních formátů, které musí zařízení a sítě podporovat, aby byla zaručena úspěšná doručovatelnost zpráv napříč různými výrobci a operátory. TIFF, jako široce přijímaný, bezlicenční standard v oboru zobrazování, byl přirozeným kandidátem pro bezztrátovou nebo vysoce kvalitní reprezentaci obrazu. Jeho zařazení řešilo problém fragmentace formátů, kdy proprietární obrazové formáty mohly bránit univerzálnímu zobrazování zpráv.

Motivace vychází z touhy učinit z MMS skutečného multimediálního nástupce [SMS](/mobilnisite/slovnik/sms/), schopného přenášet bohatý obsah jako fotografie, diagramy a skenované dokumenty. TIFF se svou podporou více kompresních metod a vysoké bitové hloubky vyhovuje obchodním a profesionálním případům užití, kde je kritická věrnost obrazu, jako je sdílení technických výkresů nebo lékařských snímků. Standardizací jeho použití umožnilo 3GPP konzistentní implementaci napříč koncovými zařízeními a síťovými prvky, čímž zajistilo, že TIFF snímek odeslaný z jednoho zařízení může být spolehlivě dekódován a zobrazen na jiném, s ohledem na schopnosti zařízení a síťové politiky.

Dále, jak se zasílání zpráv vyvíjelo směrem k [RCS](/mobilnisite/slovnik/rcs/) a službám založeným na IMS, udržení podpory pro zavedené formáty jako TIFF poskytlo zpětnou kompatibilitu a kontinuitu služeb. Také to ladí s celoprůmyslovými standardy digitálního zobrazování, usnadňující integraci s netelekomunikačními systémy (např. e-mail, web). Zatímco efektivnější formáty jako [JPEG](/mobilnisite/slovnik/jpeg/) nebo HEIF jsou často preferovány pro typické spotřebitelské fotografie kvůli menším velikostem, TIFF zůstává účelnou volbou pro specifické aplikace vyžadující bezztrátovou kvalitu nebo specifické zachování metadat v rámci ekosystému 3GPP, což demonstruje závazek standardizačního orgánu k komplexní mediální interoperabilitě.

## Klíčové vlastnosti

- Struktura souboru založená na značkách (tagech) pro flexibilní ukládání obrazových dat a metadat
- Podporuje bezztrátové kompresní algoritmy (např. LZW, Deflate) pro dokonalou věrnost obrazu
- Schopnost vysoké barevné hloubky (např. 16 bitů na kanál) a více vrstev
- Odkazován ve specifikacích 3GPP pro MMS a RCS jako interoperabilní formát statického obrazu
- Umožňuje výměnu vysoce kvalitních snímků pro profesionální/obchodní zasílání zpráv
- Poskytuje standardizované profilové formáty pro zajištění kompatibility napříč zařízeními

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [RCS – Return Channel via Satellite](/mobilnisite/slovnik/rcs/)
- [JPEG – Joint Photographic Experts Group](/mobilnisite/slovnik/jpeg/)

## Definující specifikace

- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [TIFF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tiff/)
