---
slug: "jfif"
url: "/mobilnisite/slovnik/jfif/"
type: "slovnik"
title: "JFIF – JPEG File Interchange Format"
date: 2025-01-01
abbr: "JFIF"
fullName: "JPEG File Interchange Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jfif/"
summary: "JFIF je standardní formát souboru pro ukládání statických obrázků kódovaných JPEG. V 3GPP je specifikován jako povinný formát pro službu multimediálních zpráv (MMS) a další multimediální aplikace, aby"
---

JFIF je povinný standardní formát souboru pro ukládání statických obrázků kódovaných JPEG v systémech 3GPP, který zajišťuje interoperabilitu pro službu multimediálních zpráv (MMS) a další multimediální aplikace.

## Popis

[JPEG](/mobilnisite/slovnik/jpeg/) File Interchange Format (JFIF) je specifikace, standardizovaná organizací 3GPP, která definuje konkrétní formát souboru pro zapouzdření obrazových dat komprimovaných pomocí základního standardu JPEG (Joint Photographic Experts Group) ([ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 10918-1). V rámci ekosystému 3GPP není JFIF samotným algoritmem komprese obrazu, ale kontejnerem a protokolem pro interoperabilitu. Určuje, jak uspořádat JPEG-komprimovaná obrazová data spolu s nezbytnými metadaty do bajtového proudu, který může být spolehlivě uložen, přenesen a dekódován libovolným kompatibilním zařízením nebo aplikací.

Technicky je soubor JFIF strukturován jako posloupnost značek (markers) a segmentů značek. Začíná značkou Start of Image (SOI), za níž následuje aplikační segment (APP0), který soubor jednoznačně identifikuje jako JFIF a obsahuje klíčové parametry, jako je verze, jednotky pro hustotu pixelů (dots per inch nebo dots per cm) a poměr stran pixelů. Následují volitelná data náhledu. Jádro souboru obsahuje data snímku JPEG, která zahrnují kvantizační tabulky, Huffmanovy tabulky a entropicky kódovaná skenovací data samotného obrazu. Soubor končí značkou End of Image (EOI). Tato přísná struktura zajišťuje, že dekodéry mohou soubor správně analyzovat a extrahovat rozměry obrazu, barevný prostor (obvykle YCbCr) a dekompresní tabulky potřebné k rekonstrukci bitmapy.

V sítích 3GPP je role JFIF primárně na servisní vrstvě, konkrétně pro službu multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)) a další multimediální aplikace definované ve službě paketového streamování (PSS). Specifikace 3GPP vyžadují podporu JFIF jako základního formátu pro statické obrázky, aby byla zaručena end-to-end interoperabilita. Když zařízení odešle MMS obsahující fotografii JPEG, zakóduje ji do formátu JFIF. Klient MMS nebo prohlížeč obrázků přijímacího zařízení rozpozná značku APP0 formátu JFIF a použije vestavěné informace ke správnému dekódování a zobrazení obrazu bez ohledu na výrobce nebo podkladovou síťovou technologii. Tím se inovativní standard komprese JPEG odděluje od praktických požadavků na ukládání souborů a síťovou výměnu, což z digitální fotografie činí všudypřítomnou mobilní službu.

## K čemu slouží

JFIF byl přijat organizací 3GPP k vyřešení kritického problému interoperability v počátcích mobilních multimediálních služeb. Standard [JPEG](/mobilnisite/slovnik/jpeg/) definoval vynikající metodu komprese pro obrazy s plynulými tóny, ale záměrně byl nejednoznačný ohledně způsobu uložení komprimovaných dat do souboru, což vedlo k mnoha proprietárním a nekompatibilním formátům. Vytvořila se tak situace 'Babylonské věže', kdy se obrázek JPEG vytvořený na jednom zařízení nemusel správně zobrazit na jiném.

Zavedení služby [MMS](/mobilnisite/slovnik/mms/) a mobilních internetových služeb ve vydáních 3GPP 5 a 6 si vyžádalo univerzální, lehký obrazový formát. Bez jediného povinného formátu by MMS jako globální služba selhala; obrázky odeslané z telefonu Nokia se nemusely správně zobrazit na telefonu Sony Ericsson. JFIF jako jednoduchý, široce implementovaný de facto standard ze světa stolních počítačů poskytl řešení. Specifikoval minimální, jednoznačnou podmnožinu standardu JPEG pro výměnu, včetně informací o rozlišení a barevném prostoru, které v raných implementacích JPEG často chyběly. Zavedením povinného JFIF zajistila 3GPP, že jakýkoli kompatibilní mobilní telefon může odesílat a přijímat zobrazitelné fotografické obrázky, což byla klíčová schopnost pro úspěch MMS a širší mobilní datové revoluce. Vyřešil tak omezení spočívající v existenci mocného kompresního nástroje (JPEG) bez spolehlivé 'obálky' pro doručení.

## Klíčové vlastnosti

- Definuje standardizovanou strukturu souboru pro základní JPEG-komprimovaná obrazová data
- Obsahuje aplikační segment APP0 pro identifikaci formátu a základní obrazové parametry (verze, hustota pixelů)
- Podporuje vložení rastrového náhledu pro rychlý náhled
- Určuje použití barevného prostoru YCbCr pro barevné obrázky, čímž zajišťuje konzistentní interpretaci barev
- Je povinný dle 3GPP pro MMS a PSS, aby byla zaručena interoperabilita mezi různými dodavateli a sítěmi
- Slouží jako kontejner oddělený od samotného algoritmu komprese JPEG

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [JPEG – Joint Photographic Experts Group](/mobilnisite/slovnik/jpeg/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification

---

📖 **Anglický originál a plná specifikace:** [JFIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/jfif/)
