---
slug: "dmp"
url: "/mobilnisite/slovnik/dmp/"
type: "slovnik"
title: "DMP – Detection Miss Probability"
date: 2025-01-01
abbr: "DMP"
fullName: "Detection Miss Probability"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dmp/"
summary: "Klíčový metrik výkonu ve fyzické vrstvě, zejména pro synchronizační signály a referenční signály, představující pravděpodobnost, že přijímač neúspěšně detekuje vysílaný signál. Je zásadní pro hodnocen"
---

DMP (Detection Miss Probability) je klíčový metrik výkonu představující pravděpodobnost, že přijímač neúspěšně detekuje vysílaný signál, což je zásadní pro hodnocení spolehlivosti buněčného vyhledávání a odhadu kanálu.

## Popis

Detection Miss Probability (DMP) je statistický metrik používaný k hodnocení výkonu detekčních algoritmů na fyzické vrstvě bezdrátových komunikačních systémů, jako jsou LTE a 5G New Radio (NR). Kvantifikuje pravděpodobnost, že přijímač (UE nebo základnová stanice) nezjistí přítomnost konkrétního signálu nebo nesprávně identifikuje jeho parametry, když je tento signál skutečně přítomen. Mezi běžné aplikace patří detekce synchronizačních signálů (např. Primary Synchronization Signal ([PSS](/mobilnisite/slovnik/pss/))/Secondary Synchronization Signal ([SSS](/mobilnisite/slovnik/sss/)) v NR), referenčních signálů (např. Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/))) nebo specifických prvků řídicího kanálu.

Výpočet DMP je neodmyslitelně spojen s řetězcem zpracování signálu v přijímači. Když je signál vysílán s určitým výkonem a strukturou, přijímač vzorkuje rádiový kanál, aplikuje filtrování, korelaci a testování hypotéz. DMP je pravděpodobnost, že navzdory přítomnosti signálu a jeho překročení určitého prahu poměru signál-šum ([SNR](/mobilnisite/slovnik/snr/)) detekční algoritmus přijímače vyústí v 'miss' (tj. neprohlásí detekci). To může být způsobeno zhoršením kvality kanálu (útlum, interference), šumem nebo omezeními v citlivosti a nastavení prahů detekčního algoritmu.

V návrhu systému a standardizaci je DMP klíčovým parametrem pro definování požadavků. Technické specifikace 3GPP (jako řada 38.151 pro požadavky na NR [RF](/mobilnisite/slovnik/rf/)) definují minimální požadavky na výkon přijímačů UE a základnových stanic, často specifikují maximální přípustné hodnoty DMP za definovaných podmínek kanálu (např. Additive White Gaussian Noise ([AWGN](/mobilnisite/slovnik/awgn/)) nebo kanály s útlumem). Například specifikace může stanovit, že pro dané SNR musí být DMP pro detekci [NR-PSS](/mobilnisite/slovnik/nr-pss/) během počátečního buněčného vyhledávání menší než 1 %. Tyto požadavky zajišťují interoperabilitu a základní úroveň pokrytí a spolehlivosti sítě.

DMP hraje zásadní roli v procedurách vyšších vrstev. Nedetekování synchronizačního signálu může oddálit nebo znemožnit připojení k buňce. Nedetekování referenčního signálu specifického pro paprsek může vést k selhání beamformingu a snížení propustnosti. Optimalizace návrhu fyzické vrstvy za účelem minimalizace DMP – prostřednictvím robustního návrhu signálu, pokročilých přijímacích algoritmů (např. vylepšené filtrování, detekce založená na strojovém učení) a dostatečného vysílacího výkonu – je proto zásadní pro dosažení cílů nízké latence a vysoké spolehlivosti v 5G a dalších systémech.

## K čemu slouží

DMP existuje jako základní metrik pro kvantifikaci a standardizaci spolehlivosti detekce signálů na nízké úrovni v hlučných a proměnlivých bezdrátových prostředích. Před jeho formalizací v požadavcích na výkon se návrháři systémů spoléhali na kvalitativní hodnocení nebo jednodušší metriky, jako je bitová chybovost ([BER](/mobilnisite/slovnik/ber/)), které plně nezachycovaly událost 'detekce', klíčovou pro počáteční přístup a řídicí signalizaci. Vznikla potřeba pravděpodobnostního metrika, které přímo souvisí s dostupností systému a přístupovou latencí.

Řeší problém zajištění konzistentního a předvídatelného výkonu sítě na okraji pokrytí nebo v náročných rádiových podmínkách. Stanovením standardizovaných požadavků na DMP zajišťuje 3GPP, že všechna kompatibilní UE a základnové stanice mají minimální detekční schopnost, což je nezbytné pro mobilitu (úspěšnost předávání), objevování buněk v hustých nebo heterogenních sítích a provoz pokročilých funkcí, jako je beamforming v 5G mmWave, kde jsou směrové signály náchylnější k nesprávnému nasměrování a blokaci. Historicky, jak se systémy vyvíjely z LTE na 5G NR s jeho složitou správou paprsků a širšími šířkami pásma, se přesná specifikace a testování DMP staly ještě kritičtějšími pro zaručení výkonnostních zisků slibovaných novými technologiemi fyzické vrstvy.

## Klíčové vlastnosti

- Kvantifikuje pravděpodobnost, že přijímač nezjistí známý vysílaný signál, když je přítomen.
- Klíčové pro definování požadavků na RF konformní testování přijímačů UE a základnových stanic ve specifikacích 3GPP.
- Aplikuje se na kritické signály fyzické vrstvy včetně synchronizačních signálů (PSS/SSS), referenčních signálů (CSI-RS, SRS) a prvků řídicího kanálu.
- Hodnocení se provádí za standardizovaných modelů kanálu (např. AWGN, útlumové profily jako TDL, CDL) a podmínek SNR.
- Přímo ovlivňuje metriky výkonu vyšších vrstev, jako je doba buněčného vyhledávání, míra selhání předávání a doba obnovy po selhání paprsku.
- Používá se v simulacích na úrovni spojení a v návrhu systémů pro optimalizaci návrhu signálu, přijímacích algoritmů a vysílacích parametrů za účelem dosažení robustnosti.

## Definující specifikace

- **TR 36.902** (Rel-9) — SON Use Cases and Solutions for LTE
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology

---

📖 **Anglický originál a plná specifikace:** [DMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dmp/)
