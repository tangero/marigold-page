---
slug: "tts"
url: "/mobilnisite/slovnik/tts/"
type: "slovnik"
title: "TTS – Text To Speech"
date: 2026-01-01
abbr: "TTS"
fullName: "Text To Speech"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tts/"
summary: "TTS je síťová služba, která převádí psaný text na syntetizovaný mluvený projev. V sítích 3GPP umožňuje aplikace, jako je přečtení textového přepisu hlasové schránky, síťová oznámení pro zrakově postiž"
---

TTS je síťová služba, která převádí psaný text na syntetizovanou řeč, což umožňuje funkce zvyšující dostupnost, jako je přehrávání hlasových zpráv nebo automatické hlasové oznámení v mobilních sítích.

## Popis

Text To Speech (TTS, převod textu na řeč) v architektuře 3GPP je služební schopnost, která transformuje libovolný textový vstup na srozumitelný syntetický řečový výstup. Funguje jako funkce zpracování médií, často umístěná ve funkci Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) nebo na vyhrazeném aplikačním serveru v rámci IP Multimedia Subsystem (IMS) nebo servisní vrstvy. Základní proces zahrnuje několik fází: normalizaci textu (zpracování čísel, zkratek), lingvistickou analýzu (určení výslovnosti, prozodie) a digitální zpracování signálu pro generování zvukové vlny. Služba je typicky vyvolána pomocí protokolu pro řízení služeb, jako je [SIP](/mobilnisite/slovnik/sip/), přičemž textová data jsou doručena ve standardním formátu.

Architektonicky může být TTS zdroj součástí Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)), který je řízen Media Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)) pomocí protokolů jako H.248. Když služba (např. systém interaktivní hlasové odezvy nebo aplikace pro zasílání zpráv) potřebuje vykreslit text jako řeč, signalizuje MRFC, aby alokoval TTS zdroj na MRFP. Aplikační server poté odešle textový řetězec na MRFP, často prostřednictvím [HTTP](/mobilnisite/slovnik/http/) nebo proprietárního rozhraní. TTS engine na MRFP text zpracuje a vygeneruje zvukový proud (např. ve formátu kodeku [AMR](/mobilnisite/slovnik/amr/) nebo [EVS](/mobilnisite/slovnik/evs/)), který je poté přehrán do aktivního hovoru nebo uložen jako zvukový soubor.

Jak to funguje v typickém případě použití: Uživatel zavolá na svou hlasovou schránku. Server hlasové schránky načte textový přepis zprávy (ze služby převodu řeči na text). Namísto přehrání předem nahrané nabídky odešle tento textový řetězec do TTS služby. TTS engine syntetizuje řeč a MRFP tento zvuk přímo streamuje do volajícího UE. To umožňuje dynamická, personalizovaná oznámení bez nutnosti ukládání nespočtu předem nahraných zvukových klipů. Jejím úkolem je oddělit ukládání informací (jako textu) od jejich auditivní prezentace, což umožňuje flexibilní, reálné generování mluveného obsahu pro zvýšení dostupnosti, automatizaci a vylepšení uživatelských rozhraní v telekomunikačních službách.

## K čemu slouží

Technologie TTS byla integrována do standardů 3GPP, aby vyřešila problém poskytování dynamických, personalizovaných auditivních informací bez nutnosti spoléhat se na rozsáhlé knihovny předem nahrané lidské řeči. Před rozšířením TTS služby, jako jsou nabídky hlasové schránky nebo síťová oznámení, vyžadovaly nahrání každého možného hlasového výzvu hercem, což bylo nepružné, nákladné na aktualizaci a nemožné pro vykreslení uživatelských dat, jako jsou jména nebo zůstatky na účtu. Primární motivací bylo zvýšení automatizace služeb a jejich dostupnosti.

Klíčovým hybatelem byla dostupnost pro uživatele se zrakovým postižením, což umožnilo, aby síťové služby (jako čtečky e-mailů nebo zpravodajské služby) byly přístupné prostřednictvím standardního hovoru. Dále umožnila vývoj sofistikovanějších systémů interaktivní hlasové odezvy ([IVR](/mobilnisite/slovnik/ivr/)) a unified messaging. Pro operátory TTS snížila provozní náklady spojené s nahráváním a správou hlasových výzev, zejména u vícejazyčných služeb. Odstranila omezení statického zvuku tím, že poskytla mechanismus pro hlasové podání libovolných textových dat na vyžádání, což se stalo stále důležitějším s nástupem textových aplikací (SMS, e-mail) v mobilních ekosystémech. Její standardizace v 3GPP zajistila interoperabilitu mezi síťovými zařízeními od různých výrobců a umožnila vytvoření konzistentních, spolehlivých hlasových služeb napříč sítěmi.

## Klíčové vlastnosti

- Převádí standardní textové řetězce na syntetizované řečové zvukové proudy
- Často integrována jako zdroj v rámci Media Resource Function (MRF)
- Podporuje více jazyků a hlasových profilů pro lokalizaci
- Řízena pomocí protokolů servisní vrstvy (např. SIP, HTTP) pro dynamické vyvolání
- Výstupní audio ve standardních telekomunikačních kodecích (např. AMR, EVS) pro přímé vložení do hlasových cest
- Umožňuje generování personalizovaných oznámení a výzev v reálném čase

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.916** (Rel-19) — Study on Network of Service Robots with Ambient Intelligence
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer

---

📖 **Anglický originál a plná specifikace:** [TTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tts/)
