---
slug: "acn"
url: "/mobilnisite/slovnik/acn/"
type: "slovnik"
title: "ACN – Ambisonics Channel Number"
date: 2025-01-01
abbr: "ACN"
fullName: "Ambisonics Channel Number"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/acn/"
summary: "ACN je standardizované schéma uspořádání kanálů pro formáty Ambisonics audia v rámci 3GPP. Definuje specifickou sekvenci pro přenos sférických harmonických složek, což umožňuje konzistentní dekódování"
---

ACN je standardizované schéma uspořádání kanálů pro Ambisonics audio, které definuje sekvenci přenosu sférických harmonických složek za účelem zajištění konzistentního dekódování a interoperability prostorového audia v sítích 3GPP.

## Popis

Ambisonics Channel Number (ACN) je klíčovou součástí standardů 3GPP pro imerzivní audio, konkrétně definovanou v kontextu služeb virtuální reality (VR) a 360stupňových médií. Nejde o síťový protokol nebo architektonický prvek, ale o zásadní konvenci formátování dat aplikovanou na audiokontent. ACN specifikuje standardizované pořadí pro audiokanály, které reprezentují sférickou harmonickou dekompozici zvukového pole v Ambisonics. V Ambisonics je trojrozměrná zvuková scéna matematicky reprezentována pomocí sady sférických harmonických funkcí (např. W, X, Y, Z pro první řád). Schéma ACN diktuje přesnou sekvenci, ve které jsou tyto komponentní kanály přenášeny, ukládány a zpracovávány. Například definuje, že komponenta nultého řádu (omnidirekční) 'W' je kanál 0, komponenta prvního řádu 'Y' je kanál 1, 'Z' je kanál 2 a 'X' je kanál 3, a tak dále pro Ambisonics vyšších řádů ([HOA](/mobilnisite/slovnik/hoa/)). Toto uspořádání je zásadní pro syntaxi bitového toku definovanou ve specifikacích 3GPP, jako je TS 26.118 pro VR audio.

Technická implementace ACN je hluboce integrována do vrstev přenosu médií a kodeků. Když je imerzivní audioscéna zachycena nebo generována pomocí Ambisonics mikrofonů nebo softwaru, audiová data pro každou sférickou harmonickou složku jsou přiřazena specifickému indexu kanálu podle pořadí ACN. Tento uspořádaný vícekanálový audiový signál je poté zakódován pomocí vhodného kodeku, jako je kodek Immersive Voice and Audio Services ([IVAS](/mobilnisite/slovnik/ivas/)) nebo jiné podporované audiokodeky specifikované 3GPP. Zakódovaný bitový tok s kanály v pořadí ACN je paketizován pro přenos přes sítě 5G pomocí protokolů jako RTP/UDP/IP. Příjemné zařízení, jako je VR headset nebo smartphone, dekóduje bitový tok a použije známé pořadí ACN ke správnému mapování každého přijatého kanálu na odpovídající sférickou harmonickou složku ve svém audiovykreslovacím modulu.

Role ACN v síťovém ekosystému je zaručit konzistentní referenční rámec prostorového audia mezi tvůrcem obsahu, síťovým přenosem a přehrávacím zařízením koncového uživatele. Bez standardizovaného schématu jako ACN by různé systémy mohly používat různá pořadí kanálů (např. FuMa uspořádání), což by vedlo ke zkreslenému prostorovému audiu, kde by se zvuky objevovaly na nesprávných místech. Zavedením ACN 3GPP zajišťuje, že jakýkoli kompatibilní enkodér, síťová přenosová cesta a dekodér sdílejí společnou představu o struktuře audiovych dat. Toto je základním požadavkem pro škálovatelné, interoperabilní služby imerzivních médií. Specifikace také definují související parametry, jako je normalizační konvence (SN3D nebo N3D), která se má používat spolu s ACN, čímž se dokončuje jednoznačný popis formátu Ambisonics.

V širší mediální architektuře 5G je audio formátované podle ACN typem užitečného zatížení přenášeného protokoly pro doručování médií. Interaguje s dalšími podpůrnými službami 3GPP, jako je Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) pro VR, kde popisy mediální prezentace ([MPD](/mobilnisite/slovnik/mpd/)) mohou signalizovat, že audiostopka používá Ambisonics s uspořádáním ACN. To umožňuje klientským mediálním přehrávačům vybrat a nakonfigurovat příslušný vykreslovací modul. Použití ACN podporuje různé stupně imerze, od základního Ambisonics prvního řádu (4 kanály) po komplexní reprezentace vyšších řádů vyžadující mnohem více kanálů, přičemž všechny následují stejný rozšiřitelný princip uspořádání definovaný indexem ACN.

## K čemu slouží

Vytvoření Ambisonics Channel Number (ACN) v rámci 3GPP bylo motivováno nástupem imerzivních mediálních aplikací, jako je virtuální realita (VR), rozšířená realita ([AR](/mobilnisite/slovnik/ar/)) a video 360 stupňů, jako klíčových případů užití pro sítě 5G. Tyto aplikace vyžadují realistické, trojrozměrné audio, které odpovídá vysoké kvalitě vizuální imerze. Ambisonics bylo identifikováno jako flexibilní, na scénu založený audio formát vhodný pro tyto služby, protože reprezentuje celé zvukové pole nezávislé na konkrétním rozmístění reproduktorů nebo orientaci posluchače. Před standardizací však různé implementace Ambisonics používaly proprietární nebo konfliktní schémata uspořádání kanálů (jako FuMa - Furse-Malham), což vytvářelo závažné problémy s interoperabilitou. Obsah zakódovaný pro jeden systém by produkoval nesprávně prostorizované audio na jiném systému, což bránilo rozvoji jednotného ekosystému.

ACN bylo zavedeno, aby vyřešilo tento zásadní problém interoperability. Jeho účelem je poskytnout jedinou, jednoznačnou a standardizovanou sekvenci pro přenos sférických harmonických složek, které tvoří Ambisonics signál. To umožňuje zařízením od různých výrobců, obsahu od různých producentů a sítím od různých operátorů spolehlivě vyměňovat imerzivní audiokontent. Definováním ACN 3GPP odstranilo hlavní překážku pro široké přijetí služeb imerzivního audia přes mobilní sítě. Umožňuje tvůrcům obsahu vytvořit obsah jednou a mít jej správně přehrán na jakémkoli kompatibilním zařízení, což je zásadní pro služby pro masový trh.

Dále ACN podporuje škálovatelnost vyžadovanou pro budoucí imerzivní zážitky. Ambisonics vyšších řádů ([HOA](/mobilnisite/slovnik/hoa/)) poskytuje přesnější rozlišení prostorového audia, ale vyžaduje mnohem více audiokanálů. Schéma ACN je matematicky definováno tak, aby se přirozeně rozšiřovalo na jakýkoli řád Ambisonics, a poskytuje tak rámec připravený na budoucnost. Tím se řeší omezení starších schémat s pevným řádem a umožňuje mediálním službám 5G vyvíjet se od základního prostorového audia k vysoce detailním zvukovým scenériím bez změny základního standardu pro uspořádání kanálů. Jeho integrace do specifikací 3GPP zajišťuje, že je nativně podporováno mechanismy kvality služeb (QoS) sítě a doručování médií optimalizovanými pro nízkou latenci a vysokou šířku pásma, což je kritické pro imerzivní interakce v reálném čase.

## Klíčové vlastnosti

- Standardizované uspořádání kanálů pro sférické harmonické složky (W, Y, Z, X atd.).
- Zajišťuje interoperabilitu mezi enkodéry, sítěmi a dekodéry pro Ambisonics audio.
- Podporuje škálovatelné Ambisonics vyšších řádů (HOA) prostřednictvím rozšiřitelného indexovacího systému.
- Definováno spolu s normalizačními konvencemi (SN3D/N3D) pro úplnou specifikaci formátu.
- Integrováno do bitových toků audiokodeků 3GPP pro VR (např. IVAS) a transportních protokolů.
- Umožňuje správné prostorové vykreslování na zařízeních VR/AR a přehrávačích videa 360 stupňů.

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System

---

📖 **Anglický originál a plná specifikace:** [ACN na 3GPP Explorer](https://3gpp-explorer.com/glossary/acn/)
