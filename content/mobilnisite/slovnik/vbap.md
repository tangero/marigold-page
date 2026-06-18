---
slug: "vbap"
url: "/mobilnisite/slovnik/vbap/"
type: "slovnik"
title: "VBAP – Vector Base Amplitude Panning"
date: 2025-01-01
abbr: "VBAP"
fullName: "Vector Base Amplitude Panning"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vbap/"
summary: "Technika vykreslování zvuku standardizovaná organizací 3GPP pro imerzivní média, zejména pro virtuální realitu (VR) a video 360°. VBAP vytváří prostorový zvukový zážitek panoramováním signálu zvukovéh"
---

VBAP je technika prostorového vykreslování zvuku standardizovaná organizací 3GPP pro imerzivní média, která vytváří prostorový zvuk panoramováním signálu zvukového zdroje mezi reproduktory nebo virtuálními kanály za účelem reprezentace polohy zvukových objektů.

## Popis

Vector Base Amplitude Panning (VBAP) je metoda pro prostorovou reprodukci zvuku, která umisťuje virtuální zvukové zdroje do dvourozměrného nebo třírozměrného poslechového prostoru. V rámci 3GPP je standardizována jako součást specifikací kodeku a doručování médií pro imerzivní služby, jako je [VR](/mobilnisite/slovnik/vr/) a video 360°. Základní princip VBAP spočívá v reprezentaci vnímaného směru zvukového zdroje pomocí vektoru. Tento zvukový zdroj je následně vykreslen distribucí jeho audio signálu do sady reproduktorů (skutečných nebo virtuálních), které tvoří polygon (pro 2D) nebo polyedr (pro 3D) obklopující vektor směru zdroje.

Technicky VBAP funguje tak, že nejprve definuje rozmístění reproduktorů, například 5.1 surround systém nebo sadu kanálů podobnou Ambisonics. Pro daný zvukový objekt s cílovým směrovým vektorem algoritmus identifikuje dva (2D) nebo tři (3D) reproduktory, jejichž pozice tvoří trojúhelník nebo čtyřstěn obsahující tento vektor. Audio signál objektu je následně amplitudově panoramován, což znamená, že je distribuován pouze do těchto vybraných reproduktorů. Zesílení (amplituda) aplikované na každý reproduktor se vypočítá na základě barycentrických souřadnic vektoru uvnitř vytvořeného polygonu/polyedru. Součet čtverců zesílení je obvykle normalizován, aby byla zachována konstantní hlasitost bez ohledu na polohu. Výsledkem je koherentní fantomový obraz zvukového zdroje v zamýšleném místě pro posluchače.

V architektuře 3GPP pro imerzivní média je VBAP klíčovou součástí audio vykreslovacího modulu. Mediální soubor nebo proud obsahuje zvukové objekty nebo popisy scény s metadaty určujícími jejich polohy v čase. Audio procesor na straně klienta, například implementující standard MPEG-H 3D Audio, na který 3GPP odkazuje, využívá VBAP (nebo podobné techniky) k vykreslení těchto objektů pro konkrétní nastavení přehrávání uživatele, ať už jde o sluchátka s binauračním vykreslováním nebo vícesystémový reproduktorový systém. Jeho úlohou je převést abstraktní polohová audio data na konkrétní signály pro reproduktory, čímž vytvoří přesný a působivý prostorový zvukový obraz odpovídající vizuálnímu obsahu VR nebo 360° videa.

## K čemu slouží

VBAP byl přijat a standardizován v rámci 3GPP, aby řešil potřebu efektivního a kvalitního prostorového vykreslování zvuku v nově vznikajících aplikacích imerzivních médií. Jak virtuální realita ([VR](/mobilnisite/slovnik/vr/)) a video 360° získávaly na popularitě, klíčovou výzvou bylo vytvoření věrohodného sluchového zážitku odpovídajícího vizuální volnosti. Tradiční kanálový zvuk (např. 5.1) je vázán na pevné pozice reproduktorů a nedokáže dynamicky reprezentovat pohybující se objekty. Objektový zvuk, kde jsou zvuky přenášeny jako diskrétní prvky s metadaty, tuto flexibilitu nabízí, ale vyžaduje na straně klienta metodu vykreslování.

Účelem specifikace VBAP bylo poskytnout standardizovanou, výpočetně efektivní a percepčně účinnou metodu pro toto vykreslování. Ve srovnání se složitější syntézou vlnového pole je VBAP jednodušší a vhodný pro spotřebitelská zařízení. Řeší problém, jak namapovat potenciálně velký počet dynamických zvukových objektů na konkrétní, často omezenou konfiguraci přehrávání (od stereofonních sluchátek po domácí kina). Zařazením VBAP do svých mediálních specifikací zajistilo 3GPP, aby imerzivní služby doručované přes mobilní sítě měly definovaný, interoperabilní způsob produkce prostorového zvuku, což je klíčové pro uživatelskou imerzi, realističnost a celkovou kvalitu zážitku ve VR a interaktivních médiích.

## Klíčové vlastnosti

- Technika amplitudového panoramování pro 2D a 3D prostorovou reprodukci zvuku
- Vykresluje zvukové objekty distribucí signálu do vybrané sady reproduktorů tvořících polygon/polyedr
- Používá výpočty založené na vektorech k určení zesílení reproduktorů při zachování konstantní hlasitosti
- Výpočetně efektivní ve srovnání se syntézou vlnového pole, vhodná pro vykreslování v reálném čase na mobilních zařízeních
- Standardizována v rámci 3GPP pro imerzivní mediální služby jako VR a video 360°
- Funguje s objektovými audio formáty, převádí metadata na signály pro reproduktory

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming

---

📖 **Anglický originál a plná specifikace:** [VBAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/vbap/)
