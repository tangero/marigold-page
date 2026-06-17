---
slug: "eotf"
url: "/mobilnisite/slovnik/eotf/"
type: "slovnik"
title: "EOTF – Electro-Optical Transfer Function"
date: 2025-01-01
abbr: "EOTF"
fullName: "Electro-Optical Transfer Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eotf/"
summary: "Matematická funkce, která definuje vztah mezi hodnotami elektrického signálu ve videosystému a odpovídajícím optickým jasovým výstupem na displeji. Je zásadní pro zajištění přesné reprodukce barev a j"
---

EOTF je matematická funkce, která definuje vztah mezi hodnotami elektrického videosignálu a odpovídajícím optickým jasovým výstupem na displeji.

## Popis

Elektro-optická přenosová funkce (EOTF) je klíčový koncept v kódování videa a obrazu, který mapuje digitální kódové hodnoty (typicky uložené nebo přenášené jako elektrické signály) na absolutní úrovně jasu (optický výstup) na obrazovce displeje. Zjednodušeně řečeno určuje, jak jasný by měl být pixel pro daný číselný vstup. Ve standardech 3GPP je EOTF zásadní pro multimediální služby, zejména ty zahrnující doručování videa s vysokým dynamickým rozsahem ([HDR](/mobilnisite/slovnik/hdr/)) přes mobilní sítě. EOTF je inverzní funkcí k optoelektrické přenosové funkci (OETF), která se používá na straně snímání kamery pro převod světla na elektrické signály.

Z architektonického hlediska se EOTF uplatňuje v řetězci dekódování a vykreslování videa uvnitř uživatelského zařízení (UE). Když UE přijme zakódovaná video data (např. prostřednictvím streamování nebo vysílání), proces dekódování zahrnuje interpretaci jasových a barevných složek. Tyto hodnoty jsou nelineárně zakódovány pro optimalizaci efektivity přenosu a přizpůsobení lidskému vnímání (proces známý jako gama kódování). Konkrétní EOTF, signalizovaná ve videoproudu (např. v parametrech Video Usability Information - VUI), říká zobrazovacímu systému, jak tyto zakódované hodnoty převést zpět na lineární světlo. Mezi běžné standardizované EOTF patří tradiční gama křivka (např. [BT](/mobilnisite/slovnik/bt/).709 pro standardní dynamický rozsah - SDR) a složitější funkce jako Perceptual Quantizer (PQ) definovaná v BT.2100 nebo Hybrid Log-Gamma ([HLG](/mobilnisite/slovnik/hlg/)) pro HDR obsah.

Role EOTF v ekosystému 3GPP je definována v specifikacích jako 26.116 (Multimedia Broadcast/Multicast Service) a 26.118 (Transparent end-to-end packet-switched streaming service). Tyto specifikace zajišťují, že videoslužby doručované přes sítě LTE a 5G mohou přesně přenést tvůrčí záměr týkající se jasu, kontrastu a barev. Mediální přehrávač v UE musí identifikovat EOTF z mediálního kontejneru nebo streamovacího protokolu a správně ji aplikovat pro řízení displeje. To je obzvláště kritické pro HDR obsah, kde nesoulad v EOTF může vést k vybledlým barvám, ztrátě detailů ve stínech nebo nesprávným úrovním jasu. Systém zahrnuje koordinaci mezi kodérem obsahu, streamovacím serverem, mechanismy kvality služby (QoS) sítě pro doručování videa a hardwarovými možnostmi displeje UE.

## K čemu slouží

Standardizace EOTF v rámci 3GPP byla hnací silou rozšíření pokročilých videoslužeb, zejména přijetí videa s vysokým dynamickým rozsahem ([HDR](/mobilnisite/slovnik/hdr/)). Tradiční SDR video používalo jednoduchou gama křivku, ale HDR vyžaduje sofistikovanější přenosovou funkci pro efektivní reprezentaci mnohem širšího rozsahu úrovní jasu (od hlubokých stínů po jasné světelné výšky). Bez standardizované EOTF by mohl být HDR obsah na různých zařízeních zobrazován nesprávně, což by vedlo ke špatnému uživatelskému zážitku a ztrátě tvůrčího záměru.

Hlavním problémem, který EOTF řeší, je přesná reprodukce jasu na různých zobrazovacích technologiích. Zajišťuje, že videostream přenášený na smartphone, tablet nebo připojenou TV se zobrazí s zamýšleným jasem a kontrastem bez ohledu na vlastnosti nativního displeje zařízení. To je zásadní pro poskytovatele služeb nabízejících prémiový obsah jako 4K/HDR streamování, mobilní TV a imerzivní média. Definováním parametrů EOTF v multimediálních specifikacích umožňuje 3GPP interoperabilitu mezi tvorbou obsahu, síťovým doručováním a přehráváním na zařízení, což je nezbytné pro konzistentní kvalitu zážitku u mobilních videoslužeb.

## Klíčové vlastnosti

- Definuje mapování z digitálních kódových hodnot na jas displeje
- Podporuje standardy pro SDR (např. gama BT.709) i HDR (např. PQ, HLG)
- Signalizována uvnitř videoproudů pro správnou interpretaci přijímačem
- Umožňuje přesnou reprodukci barev a jasu na různých displejích
- Kritická pro služby doručování videa s vysokým dynamickým rozsahem (HDR)
- Integrována do specifikací 3GPP pro multimediální streamování a vysílání

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats

---

📖 **Anglický originál a plná specifikace:** [EOTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/eotf/)
