---
slug: "sba"
url: "/mobilnisite/slovnik/sba/"
type: "slovnik"
title: "SBA – Scene-Based Audio (Ambisonics)"
date: 2026-01-01
abbr: "SBA"
fullName: "Scene-Based Audio (Ambisonics)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sba/"
summary: "3D audio formát pro zachycení a reprodukci plného sférického zvukového pole, který umožňuje imerzivní audio zážitky, jako je virtuální realita. Reprezentuje zvuk jako sférické harmonické funkce, nezáv"
---

SBA je 3D audio formát standardizovaný konsorciem 3GPP pro zachycení a reprodukci plného sférického zvukového pole pomocí sférických harmonických funkcí, což umožňuje imerzivní audio pro distribuci přes mobilní sítě.

## Popis

Scene-Based Audio (SBA), konkrétně založené na technice Ambisonics, je plně sférický formát prostorového zvuku, který zachycuje a reprezentuje trojrozměrné zvukové pole. Na rozdíl od kanálového audia (např. 5.1, 7.1.4), které kóduje audio pro konkrétní pozice reproduktorů, nebo objektového audia (např. MPEG-H), které kóduje jednotlivé zvukové objekty s metadaty, SBA kóduje samotné zvukové pole jako sadu komponent sférických harmonických funkcí. Tato matematická reprezentace popisuje tlak a rychlost zvukových vln v bodě prostoru a umožňuje rekonstrukci původního zvukového pole na různých přehrávacích systémech, od sluchátek s binaurálním vykreslením po složité reproduktorové sestavy.

Jádrem SBA je signál B-formátu, který se skládá z alespoň čtyř kanálů: W (všesměrová složka tlaku) a X, Y, Z (tři ortogonální osmičkové složky reprezentující tlakové gradienty). Toto Ambisonics prvního řádu ([FOA](/mobilnisite/slovnik/foa/)) lze rozšířit na Ambisonics vyšších řádů ([HOA](/mobilnisite/slovnik/hoa/)) zahrnutím více komponent sférických harmonických funkcí, což zvyšuje prostorové rozlišení a přesnost rekonstruovaného zvukového pole, zejména pro zvuky ve výšce a přesnější lokalizaci. Standardizace 3GPP se zaměřuje na efektivní kompresi, přenos a vykreslování těchto Ambisonics komponent v rámci mediálních služeb, jako je streamování pro virtuální realitu ([VR](/mobilnisite/slovnik/vr/)), rozšířenou realitu ([AR](/mobilnisite/slovnik/ar/)) a 360stupňové video.

V rámci architektury 3GPP je SBA integrováno do řetězce distribuce médií. Specifikace definují, jak je obsah SBA zapouzdřen v mediálních kontejnerech (jako [ISOBMFF](/mobilnisite/slovnik/isobmff/)), komprimován pomocí audiokodeků (s konkrétním zpracováním pro kanály sférických harmonických funkcí) a popsán v popisech mediální prezentace. Klíčovým aspektem je podpora dynamického vykreslování: bitový proud SBA obsahující koeficienty zvukového pole je doručen na klientské zařízení. Audio vykreslovač zařízení pak použije sadu dekódovacích matic, potenciálně přizpůsobených konkrétní orientaci hlavy uživatele (sledované pomocí head-mounted displejů) a výstupnímu nastavení (sluchátka nebo reproduktory), aby provedl binauralizaci nebo dekódování audia pro imerzivní přehrávání. To umožňuje audio se šesti stupni volnosti (6DoF), kde se posluchač může pohybovat v rámci zvukové scény.

Práce 3GPP na SBA zahrnuje více technických specifikací (TS) pokrývajících kodeky, formáty souborů, systémové protokoly a zabezpečení. Zajišťuje interoperabilitu pro imerzivní audio služby napříč různými sítěmi a zařízeními. Specifikace také řeší metadata pro koordinaci SBA s 360stupňovým videem, což zajišťuje audiovizuální synchronizaci při změně úhlu pohledu uživatele. To činí ze SBA základní technologii pro poskytování nové generace interaktivních mediálních zážitků přes sítě 5G a další.

## K čemu slouží

Scene-Based Audio (Ambisonics) bylo standardizováno konsorciem 3GPP, aby reagovalo na rostoucí trh s imerzivními médii, zejména poháněný virtuální a rozšířenou realitou. Tradiční kanálové audio je vázáno na pevné konfigurace reproduktorů a nemůže se přizpůsobit pohybu hlavy uživatele nebo různým přehrávacím prostředím. Objektové audio poskytuje flexibilitu, ale vyžaduje významná metadata a výpočetní výkon pro vykreslování mnoha objektů. SBA bylo motivováno potřebou formátu, který inherentně popisuje kompletní zvukovou scénu kompaktním způsobem nezávislým na přehrávacím zařízení.

Historickým kontextem je vzestup 360stupňového videa a obsahu [VR](/mobilnisite/slovnik/vr/). Rané VR zážitky často používaly základní binaurální audio nebo jednoduché vícekanálové mixy, které narušovaly imerzi, když uživatel otočil hlavu. Ambisonics, desítky let starý akademický koncept, bylo identifikováno jako vhodné řešení, protože matematicky kóduje zvukové pole. Úlohou 3GPP bylo standardizovat jeho použití v telekomunikačním ekosystému, čímž se řeší problémy efektivní komprese pro přenos přes mobilní sítě s omezenou šířkou pásma a definuje se, jak klienti přijímají a vykreslují audio synchronně s videem.

Řeší klíčová omezení předchozích audio formátů pro imerzivní aplikace. Kanálové audio postrádá přizpůsobivost. Objektové audio se může stát výpočetně složitým pro husté scény. SBA poskytuje optimální řešení: popis scény, který je relativně kompaktní, nezávislý na výstupním nastavení a dokonale vhodný pro binaurální vykreslování se sledováním hlavy, což je zásadní pro VR. Jeho standardizace umožňuje tvůrcům obsahu produkovat jediný audio stream, který funguje na jakémkoli kompatibilním zařízení, od mobilních telefonů se sluchátky po dedikované VR systémy, a tím podporuje interoperabilní ekosystém pro imerzivní mediální služby 3GPP.

## Klíčové vlastnosti

- Kóduje zvukové pole pomocí sférických harmonických funkcí (B-formát)
- Nezávislé na přehrávacím zařízení; podporuje vykreslování do sluchátek, reproduktorových sestav apod.
- Umožňuje audio se šesti stupni volnosti (6DoF) se sledováním hlavy
- Integrováno s distribucí 360stupňového videa v mediálních službách 3GPP
- Podporuje kompresi pomocí standardizovaných audiokodeků (např. s konkrétním mapováním kanálů)
- Definuje metadata pro synchronizaci s vizuálním úhlem pohledu a konfigurací přehrávání

## Související pojmy

- [VR – Virtualized Resource](/mobilnisite/slovnik/vr/)

## Definující specifikace

- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 29.309** (Rel-19) — Nbsp Service Based Interface for GBA BSF
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [SBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sba/)
