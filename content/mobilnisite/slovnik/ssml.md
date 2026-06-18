---
slug: "ssml"
url: "/mobilnisite/slovnik/ssml/"
type: "slovnik"
title: "SSML – Speech Synthesis Markup Language"
date: 2025-01-01
abbr: "SSML"
fullName: "Speech Synthesis Markup Language"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ssml/"
summary: "SSML je značlovací jazyk založený na XML pro řízení syntézních enginů řeči. Umožňuje aplikacím specifikovat výslovnost, hlasitost, výšku tónu a rychlost syntetizované řeči, čímž umožňuje přirozený a v"
---

SSML je značkovací jazyk založený na XML, používaný v 3GPP zprávových a hlasových službách k řízení syntézy řeči. Umožňuje specifikovat výslovnost, hlasitost, výšku tónu a rychlost pro přirozený a přizpůsobitelný zvukový výstup.

## Popis

Speech Synthesis Markup Language (SSML) je standard konsorcia World Wide Web Consortium ([W3C](/mobilnisite/slovnik/w3c/)), který 3GPP přijalo a profilovalo pro použití v telekomunikačních službách. Jde o jazyk založený na [XML](/mobilnisite/slovnik/xml/), který poskytuje bohatou sadu značek a atributů pro anotaci textového vstupu do systémů syntézy řeči (text-to-speech enginů). Hlavní funkcí SSML je poskytnout poskytovatelům služeb a vývojářům aplikací přesnou kontrolu nad tím, jak je text převeden na mluvený zvuk, což jde daleko za jednoduchou, monotónní konverzi. Značky lze použít k definování fonetické výslovnosti neobvyklých slov, vložení pauz, řízení prozódie (výšky tónu, rychlosti a hlasitosti), specifikaci mluvícího hlasu a dokonce k vložení nahraných zvukových klipů do proudu syntetizované řeči.

V rámci architektur 3GPP je SSML primárně referencováno v kontextu služby Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)) a dalších zprávových enablerů. Například zpráva MMS může obsahovat textové tělo anotované značkami SSML. Když zařízení příjemce nebo síťová služba vykreslí tuto zprávu jako zvuk (např. pro použití hands-free nebo pro přístupnost), značkování SSML instruuje [TTS](/mobilnisite/slovnik/tts/) engine, jak přesně řeč vyprodukovat. Specifikace TS 23.333 definuje, jak jsou dokumenty SSML v systémech 3GPP zapouzdřovány a přenášeny. Jazyk funguje tak, že obaluje textový obsah do elementů jako <speak>, což je kořenový kontejner. Mezi klíčové elementy patří <phoneme> pro poskytnutí fonetické abecední výslovnosti, <break> pro vložení ticha, <prosody> pro úpravu výšky tónu a rychlosti a <voice> pro výběr konkrétní hlasové charakteristiky.

Role SSML v 3GPP spočívá v umožnění přirozenějších, srozumitelnějších a poutavějších audio služeb. Je to klíčový enabler pro unified messaging, kde uživatelé mohou přijímat e-maily nebo textové zprávy předčítané se správnou intonací pro otázky nebo důraz. Také podporuje systémy interaktivní hlasové odpovědi ([IVR](/mobilnisite/slovnik/ivr/)) a služby přístupnosti pro uživatele se zrakovým postižením. Standardizací na společném značkovacím jazyce zajišťuje 3GPP interoperabilitu mezi tvůrci obsahu, síťovými službami a terminálovými TTS enginy, což umožňuje konzistentní uživatelský zážitek bez ohledu na podkladový hardwarový nebo softwarový syntetizátor.

## K čemu slouží

SSML byl vytvořen, aby vyřešil problém robotického, nepřirozeného a často nesrozumitelného výstupu z raných text-to-speech systémů. Jednoduché [TTS](/mobilnisite/slovnik/tts/) enginy vyslovovaly text doslovně, což vedlo k chybné výslovnosti jmen, akronymů a čísel a k naprostému nedostatku výrazových prostředků (pauz, důrazu, změn výšky tónu), které charakterizují lidskou řeč. To omezovalo použitelnost TTS pro kritické aplikace jako jsou zprávy, navigace a zákaznický servis. [W3C](/mobilnisite/slovnik/w3c/) vyvinulo SSML, aby poskytlo dodavatelsky neutrální, platformně nezávislý způsob řízení parametrů syntézy.

Přijetí SSML organizací 3GPP, zejména ve verzi Rel-7, bylo motivováno růstem multimediálního zasílání zpráv a potřebou vylepšených zprávových služeb. Umožnilo síťovým přidaným službám (jako je vykreslování audio zpráv) a schopným koncovým zařízením poskytnout výrazně lepší uživatelský zážitek. Před SSML byl jakýkoli pokus o zlepšení kvality řeči proprietární a neinteroperabilní. SSML poskytlo standardizovanou sadu nástrojů, aby poskytovatelé obsahu zajistili, že jejich zprávy budou přečteny podle záměru, což bylo klíčové pro komerční služby jako audio zpravodajství, hlasem ovládané prohlížení webu a přístupné telekomunikace. Umožnilo to inovace služeb v audio doméně v rámci paketově přepínané servisní architektury.

## Klíčové vlastnosti

- Značkování založené na XML pro anotaci textu instrukcemi pro syntézu řeči
- Kontrola výslovnosti pomocí fonematických abeced (např. IPA, X-SAMPA)
- Přesná kontrola prozódie: výšky tónu, rychlosti řeči a hlasitosti
- Schopnost vkládat specifikované pauzy a přestávky v řeči
- Podpora více hlasů a jazyků v rámci jednoho dokumentu
- Možnost vkládat předem nahrané zvukové soubory do proudu syntetizované řeči

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)
- [IVR – Interactive Voice Response](/mobilnisite/slovnik/ivr/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements

---

📖 **Anglický originál a plná specifikace:** [SSML na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssml/)
