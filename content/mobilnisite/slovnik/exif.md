---
slug: "exif"
url: "/mobilnisite/slovnik/exif/"
type: "slovnik"
title: "EXIF – Exchangeable Image File Format"
date: 2025-01-01
abbr: "EXIF"
fullName: "Exchangeable Image File Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/exif/"
summary: "Standardní formát pro ukládání metadat (jako nastavení fotoaparátu, GPS poloha, datum/čas) v souborech s obrázky, zejména JPEG. V 3GPP je odkazován pro multimediální zprávy (MMS) a manipulaci s mediál"
---

EXIF je standardní formát pro vkládání metadat, jako jsou nastavení fotoaparátu a poloha, do souborů s obrázky, používaný v 3GPP pro multimediální zprávy k zajištění interoperability.

## Popis

Exchangeable Image File Format (EXIF) je specifikace, nikoliv vynález 3GPP, ale je v rámci norem 3GPP hojně odkazována a využívána pro multimediální služby. Definuje strukturu pro vkládání metadat ve formě tagů do souborů s obrázky, primárně [JPEG](/mobilnisite/slovnik/jpeg/), ale také [TIFF](/mobilnisite/slovnik/tiff/) a některé RAW formáty. Tato metadata poskytují bohatou sadu informací o vzniku snímku. Mezi klíčová ukládaná data patří značka a model fotoaparátu, expoziční čas (rychlost závěrky), clona (f-číslo), hodnota [ISO](/mobilnisite/slovnik/iso/), ohnisková vzdálenost, použití blesku a datum a čas pořízení snímku. Pro mobilní služby je zásadní, že EXIF také podporuje vložení údajů o zeměpisné poloze ([GPS](/mobilnisite/slovnik/gps/) souřadnice), pokud je pořizující zařízení vybaveno GPS.

V ekosystému 3GPP je EXIF upravena specifikacemi TS 26.140 (Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)); Media formats and codecs) a TS 26.141 (MMS; Media formats and codecs). Tyto specifikace samotný EXIF nedefinují, ale nařizují jeho podporu jako kontejneru pro metadata v MMS zprávách. Když mobilní zařízení odešle MMS obsahující JPEG obrázek, přidružená EXIF data jsou často zachována a přenesena. To umožňuje přijímacím zařízením zobrazit nejen obrázek, ale i jeho přidružené informace, což umožňuje funkce jako galerie fotek řazené podle data nebo mapy poloh.

Technicky jsou EXIF data uložena v aplikačních segmentech (Application Segments) JPEG souboru, konkrétně v segmentu APP1. Používá strukturu založenou na tagech, podobnou TIFF. Čtečka souborů (jako aplikace galerie v telefonu nebo MMS klient) tyto segmenty parsuje, aby extrahovala metadata. Specifikace 3GPP zajišťují základní úroveň interoperability definováním, které EXIF tagy by měly být podporovány a jak by s nimi mělo být při adaptaci médií nakládáno. Například, pokud síťový prvek potřebuje překódovat obrázek na menší velikost, měl by být vědom EXIF dat a zacházet s nimi odpovídajícím způsobem – buď je odstranit, zachovat nebo upravit relevantní tagy (jako rozměry obrázku).

Role EXIF v síti je pasivní, ale pro kvalitu služeb zásadní. Je součástí mediální datové části. Síťové prvky jako MMS Interworking Function (MMS-IWF) nebo Multimedia Message Service Centers (MMSC) mohou EXIF data kontrolovat pro účely validace formátu nebo adaptace médií. Standard zajišťuje, že obsah generovaný uživatelem, bohatý na kontext (jako například fotografie s geografickými značkami), může být bezproblémově vyměňován mezi různými zařízeními a sítěmi operátorů při zachování uživatelského zážitku zamýšleného odesílatelem.

## K čemu slouží

EXIF byla přijata a odkazována v rámci norem 3GPP k vyřešení problému ztráty kontextových informací při výměně digitálních obrázků mezi mobilními zařízeními prostřednictvím služeb jako [MMS](/mobilnisite/slovnik/mms/). Před rozšířeným používáním EXIF obsahoval soubor s obrázkem pouze pixelová data. Jakékoli informace o tom, jak, kdy nebo kde byla fotografie pořízena, byly oddělené a během přenosu se snadno ztratily. Účelem vložení EXIF do multimediálních specifikací 3GPP bylo standardizovat přenos těchto metadat, což umožnilo bohatší uživatelské zážitky a služby.

Historický kontext vychází z rozšíření telefonů s fotoaparáty na počátku roku 2000. Jak se MMS stávalo populárním, vznikla potřeba nejen sdílet obrázky, ale také příběh za nimi. EXIF, původně vytvořená Japan Electronic Industries Development Association (JEIDA), poskytovala hotové, průmyslem přijaté řešení. 3GPP ji začlenila, aby se vyhnula znovuvynalézání kola a zajistila kompatibilitu mobilních služeb se širším ekosystémem digitálního zobrazování (např. digitální fotoaparáty, desktopový software). Vyřešila tak omezení 'hloupých' obrazových souborů tím, že je učinila samopopisnými.

Její integrace byla motivována snahou umožnit nové funkce: automatické řazení fotografií podle data, zobrazování fotografií na mapové aplikaci zařízení a poskytování podrobností o snímku fotografickým nadšencům. Pro síťové operátory podpora standardního formátu metadat zjednodušila návrh systémů pro manipulaci s médii a zaručila interoperabilitu, která byla klíčová pro úspěch mezisíťového MMS. Položila základy pro pozdější služby založené na poloze a pokročilejší správu médií na chytrých telefonech.

## Klíčové vlastnosti

- Vkládá parametry snímku fotoaparátu (rychlost závěrky, clona, ISO) přímo do souborů s obrázky
- Ukládá přesné datum, čas a časové pásmo vytvoření obrázku
- Podporuje vložení GPS souřadnic pro geografické značkování (geotagging)
- Používá standardizovanou strukturu tagů pro rozšiřitelnost
- Odkazována v 3GPP specifikacích pro MMS (TS 26.140, 26.141) pro zajištění interoperability
- Umožňuje pokročilou organizaci fotografií a kontextově citlivé aplikace na mobilních zařízeních

## Související pojmy

- [JPEG – Joint Photographic Experts Group](/mobilnisite/slovnik/jpeg/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats

---

📖 **Anglický originál a plná specifikace:** [EXIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/exif/)
