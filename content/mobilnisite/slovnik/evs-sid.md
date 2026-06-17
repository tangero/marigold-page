---
slug: "evs-sid"
url: "/mobilnisite/slovnik/evs-sid/"
type: "slovnik"
title: "EVS-SID – Enhanced Voice Services Silence Insertion Descriptor"
date: 2025-01-01
abbr: "EVS-SID"
fullName: "Enhanced Voice Services Silence Insertion Descriptor"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/evs-sid/"
summary: "Specifický deskriptor pro vkládání ticha (SID) používaný v kodeku Enhanced Voice Services (EVS) pro nespojitý přenos (DTX). Poskytuje kompaktní a efektivní reprezentaci ticha a šumu na pozadí během pa"
---

EVS-SID je specifický deskriptor pro vkládání ticha (Silence Insertion Descriptor) používaný kodekem EVS během nespojitého přenosu k efektivní reprezentaci ticha a šumu na pozadí, čímž šetří přenosovou kapacitu při zachování kvality hovoru.

## Popis

EVS-SID (Enhanced Voice Services Silence Insertion Descriptor) je klíčovou součástí systému nespojitého přenosu ([DTX](/mobilnisite/slovnik/dtx/)) a generování komfortního šumu ([CNG](/mobilnisite/slovnik/cng/)) kodeku [EVS](/mobilnisite/slovnik/evs/). Během aktivní řeči kodek EVS kóduje zvukové rámce s vysokou přenosovou rychlostí. Během pauz nebo ticha je však přenos plných rámců neefektivní. Mechanismus DTX tyto neaktivní periody detekuje a přepne se do režimu s nízkou přenosovou rychlostí. V tomto režimu místo odesílání běžných řečových rámců vysílač přenáší speciální rámce SID (Silence Insertion Descriptor). EVS-SID je specifický typ rámce SID optimalizovaný pro parametrický model šumu na pozadí kodeku EVS.

Technicky rámec EVS-SID obsahuje vysoce komprimovaný parametrický popis aktuálního akustického šumu na pozadí. Tento popis typicky zahrnuje parametry spektrální obálky (např. koeficienty lineární predikce nebo energie spektrálních pásem) a případně informace o stacionaritě a úrovni šumu. Rámec je přenášen v pravidelných, prodloužených intervalech (např. každých 160–640 ms) během periody ticha, nikoli v každém 20ms rámci používaném pro aktivní řeč. To drasticky snižuje průměrnou přenosovou rychlost během hovorů s významnými pauzami.

Na přijímací straně dekodér používá parametry z posledního přijatého rámce EVS-SID k syntéze komfortního šumu. Tento syntetizovaný šum odpovídá spektrálním charakteristikám šumu na pozadí na straně vysílače, čímž zabraňuje nepřirozenému „mrtvému tichu“, které by jinak nastalo při zastavení přenosu. Proces zahrnuje generování šumového signálu, tvarování jeho spektra podle přijatých parametrů a úpravu jeho zesílení. Tím je udržováno konzistentní a přirozené akustické pozadí pro posluchače, což je psychologicky důležité pro kvalitu hovoru.

EVS-SID funguje v rámci širší architektury kodeku EVS definované v 3GPP TS 26.445. Jeho specifické formáty paketů a struktury datové části pro rámce SID jsou podrobně popsány v transportních specifikacích kodeku, TS 26.453 (formát RTP payload) a TS 26.454 (souborový formát). Konstrukce EVS-SID je nedílnou součástí vynikajícího výkonu EVS v hlučném prostředí a jeho schopnosti poskytovat vysoce kvalitní hlasové služby při nižších průměrných přenosových rychlostech ve srovnání se staršími kodeky, jako je [AMR-WB](/mobilnisite/slovnik/amr-wb/).

## K čemu slouží

EVS-SID byl vytvořen k řešení specifických potřeb kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)), představeného ve 3GPP Release 13, pro vysoce efektivní nespojitý přenos ([DTX](/mobilnisite/slovnik/dtx/)). Předchozí kodeky jako [AMR](/mobilnisite/slovnik/amr/) a [AMR-WB](/mobilnisite/slovnik/amr-wb/) také používaly rámce SID, ale pokročilý audio model EVS a podpora superširokopásmového a plnopásmového zvuku vyžadovaly sofistikovanější přístup k modelování šumu. Účelem EVS-SID je umožnit významné úspory rádiových zdrojů během hlasových hovorů bez degradace vnímané kvality konverzace.

Historicky rané digitální hlasové systémy bez DTX jednoduše přenášely zakódované ticho, čímž plýtvaly přenosovou kapacitou. Pozdější kodeky zavedly základní DTX s jednoduchými modely šumu, ale syntetizovaný komfortní šum mohl znít uměle nebo nedokázal sledovat měnící se šum na pozadí. Kodek EVS byl navržen pro hlasové služby nové generace (VoLTE, ViLTE, VoNR), které vyžadují jak vysokou kvalitu, tak síťovou efektivitu. EVS-SID řeší problém efektivní reprezentace složitého, časově proměnlivého šumu na pozadí (jako je hovor v kanceláři nebo hluk z ulice) pomocí parametrického popisu s velmi nízkou přenosovou rychlostí, což síti umožňuje přenášet více simultánních hovorů nebo uvolnit kapacitu pro datové služby.

Jeho vytvoření bylo motivováno potřebou rozšířit výhody efektivního DTX do oblastí kvalitního zvuku superširokopásmového a plnopásmového přenosu řeči. Bez přizpůsobeného mechanismu SID by se úspory přenosové kapacity díky DTX ztratily při použití vysoce kvalitních režimů EVS. EVS-SID zajišťuje, že pokročilé schopnosti kodeku nejsou narušeny během pauz v řeči, což činí vysoce kvalitní hlasové služby ekonomicky životaschopnými pro mobilní operátory.

## Klíčové vlastnosti

- Parametrické kódování spektra šumu na pozadí pro přenos s ultranízkou přenosovou rychlostí
- Umožňuje nespojitý přenos (DTX) v kodeku EVS, což drasticky snižuje průměrnou přenosovou rychlost hovoru
- Podporuje generování komfortního šumu (CNG) na přijímací straně, aby se zabránilo „mrtvému tichu“
- Optimalizováno pro superširokopásmové a plnopásmové audio modely EVS
- Definované formáty datové části pro RTP transport (TS 26.453) a ukládání (TS 26.454)
- Nedílná součást robustního výkonu EVS v proměnných akustických prostředích

## Definující specifikace

- **TS 26.453** (Rel-19) — EVS Codec Generic Frame Format for 3G CS Networks
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks

---

📖 **Anglický originál a plná specifikace:** [EVS-SID na 3GPP Explorer](https://3gpp-explorer.com/glossary/evs-sid/)
