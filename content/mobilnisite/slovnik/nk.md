---
slug: "nk"
url: "/mobilnisite/slovnik/nk/"
type: "slovnik"
title: "NK – No Keypad capability"
date: 2025-01-01
abbr: "NK"
fullName: "No Keypad capability"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/nk/"
summary: "Indikátor schopnosti pro aplikaci UICC/USIM, který signalizuje, že přidružený terminál (mobilní zařízení) nemá fyzickou ani virtuální klávesnici pro vstup od uživatele. Tyto informace využívá UICC k p"
---

NK je indikátor schopnosti UICC/USIM, který signalizuje, že přidružený mobilní terminál nemá klávesnici, což vede UICC k přizpůsobení potlačením nabídkových voleb vyžadujících ruční zadávání.

## Popis

No Keypad (NK) je pole schopností definované v kontextu aplikací UICC (Universal Integrated Circuit Card) a USIM (Universal Subscriber Identity Module) ve specifikacích 3GPP. Je součástí datového objektu Profil terminálu, který UICC přijímá od mobilního zařízení ([ME](/mobilnisite/slovnik/me/)), což je telefon nebo zařízení hostující UICC. Příznak NK explicitně informuje UICC, že ME postrádá jakoukoliv formu klávesnice – ať už fyzických tlačítek nebo softwarové virtuální klávesnice – pro vstup od uživatele. Tato výměna informací o schopnostech je klíčová pro aplikační logiku UICC, protože umožňuje kartě přizpůsobit své uživatelské rozhraní a sekvence příkazů schopnostem hostitelského zařízení.

Z architektonického hlediska je tato schopnost sdělována během inicializační fáze mezi ME a UICC, jak je definováno v TS 31.111 (USIM Application Toolkit). ME odešle UICC příkaz Terminal Profile, který obsahuje bitmapu podporovaných funkcí. Jeden bit v této bitmapě reprezentuje schopnost 'No Keypad'. Když je tento bit nastaven na '1', indikuje absenci klávesnice. Interpret USIM Application Toolkit (USAT) na UICC poté tyto informace použije ke změně svého chování. Například se může rozhodnout nevydávat proaktivní příkazy, které vyžadují vstup od uživatele přes klávesnici, jako jsou příkazy SELECT ITEM s možnostmi uživatelského vstupu, nebo může přizpůsobit struktury nabídek tak, aby byly ovladatelné jinými prostředky, jako jsou soft klávesy nebo dotykové gesta, pokud jsou tyto podporovány.

Klíčovými komponentami jsou mechanismus hlášení schopností ME, datová struktura Profil terminálu standardizovaná v TS 31.111 a logika aplikace USIM, která tento profil zpracovává. Indikátor NK je jednoduchý booleovský příznak, ale má významné důsledky pro model uživatelské interakce. U zařízení bez klávesnic, jako jsou určité IoT moduly, vestavěná zařízení nebo nositelná zařízení, jsou tradiční nabídky řízené USIM vyžadující číselný nebo textový vstup nepraktické nebo nemožné. Díky znalosti stavu NK se může UICC vyvarovat odesílání příkazů, které by selhaly nebo zmátly uživatele, což vede k robustnějšímu a plynulejšímu zážitku.

Úloha NK v ekosystému spočívá v umožnění aplikacím UICC být nezávislé na zařízení, a přitom poskytovat optimalizovaný zážitek. Je to základní část vyjednávání schopností mezi čipovou kartou a terminálem, která zajišťuje, že služby jako nabídky SIM toolkit, služby s přidanou hodnotou a autentizační procedury fungují správně napříč širokým spektrem typů zařízení, od plnohodnotných smartphonů až po zařízení pro komunikaci mezi stroji (M2M) bez klávesnice. To podporuje široké nasazení technologie UICC v internetu věcí (IoT), kde mnoho zařízení nemá tradiční uživatelské rozhraní.

## K čemu slouží

Schopnost NK byla zavedena, aby řešila rostoucí rozmanitost formátů mobilních zařízení, zejména vznik zařízení bez tradičních klávesnic. Rané mobilní telefony měly univerzálně číselné nebo alfanumerické klávesnice a logika aplikací USIM byla navržena za tohoto předpokladu. Příkazy často vyžadovaly vstup od uživatele přes klávesnici. S příchodem nových typů zařízení, jako jsou datové modemy, telemetrické jednotky, nositelná zařízení a zjednodušené IoT senzory, však mnoho zařízení postrádalo jakoukoliv klávesnici. Bez znalosti tohoto omezení by UICC mohlo odesílat příkazy vyžadující vstup z klávesnice, které by selhaly, způsobily chyby nebo vedly ke špatnému uživatelskému zážitku.

Tato schopnost řeší problém nekompatibility schopností zařízení v rozhraní UICC-ME. Umožňuje UICC dynamicky přizpůsobovat své proaktivní chování na základě hlášených funkcí terminálu. Primární motivací bylo zajistit zpětnou kompatibilitu a kontinuitu služeb: jedna UICC karta mohla být použita jak v tradičním telefonu, tak v modemu bez klávesnice, aniž by bylo nutné mít různé verze karty. Pro nasazení IoT a M2M je to obzvláště kritické, protože tato zařízení často fungují bez dozoru a jakýkoliv chybný příkaz z UICC by mohl narušit službu.

Standardizovaná ve vydání 8 jako součást probíhajících vylepšení USIM Application Toolkit odráží NK posun průmyslu směrem k specializovanějším mobilním zařízením. Řešila omezení dřívějších profilů, které explicitně nedefinovaly absenci klávesnice, což vynucovalo řešení nebo omezovalo funkčnost aplikací UICC v nových kategoriích zařízení. Formální definicí této schopnosti umožnilo 3GPP čistší a spolehlivější model interakce, který podporuje expanzi buněčné konektivity do širšího spektra zařízení a případů použití přesahujících osobní komunikaci.

## Klíčové vlastnosti

- Signalizuje UICC absenci fyzické nebo virtuální klávesnice u mobilního zařízení
- Přenáší se jako součást Profilu terminálu v procedurách USIM Application Toolkit
- Umožňuje UICC potlačit nebo přizpůsobit proaktivní příkazy vyžadující ruční vstup od uživatele
- Podporuje nasazení UICC/USIM v zařízeních IoT a M2M bez klávesnice
- Zlepšuje interoperabilitu mezi jednou UICC kartou a různými formáty terminálů
- Předchází chybám a zlepšuje uživatelský zážitek u zařízení bez tradičních vstupních metod

## Definující specifikace

- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification

---

📖 **Anglický originál a plná specifikace:** [NK na 3GPP Explorer](https://3gpp-explorer.com/glossary/nk/)
