---
slug: "mui"
url: "/mobilnisite/slovnik/mui/"
type: "slovnik"
title: "MUI – Mobile User Identifier"
date: 2025-01-01
abbr: "MUI"
fullName: "Mobile User Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mui/"
summary: "Obecný termín pro jakýkoli identifikátor, který jednoznačně rozlišuje mobilního uživatele nebo účastníka v rámci sítě. Jedná se o zastřešující koncept zahrnující různé konkrétní identifikátory, jako j"
---

MUI je obecný zastřešující termín pro jakýkoli identifikátor, například IMSI nebo MSISDN, který jednoznačně rozlišuje mobilního účastníka v rámci sítě pro směrování, zabezpečení a správu.

## Popis

Mobile User Identifier (MUI) je vysoká, koncepční termín používaný ve specifikacích 3GPP pro označení jakéhokoli identifikátoru, který jednoznačně určuje mobilního uživatele nebo účastníka. Není to jediný konkrétní identifikátor s definovaným formátem, ale spíše kategorické označení pro soubor identifikátorů používaných v celém systému. Tyto identifikátory plní odlišné účely v různých doménách: pro správu předplatného v jádru sítě, pro dočasné směrování v rádiové síti a pro uživatelská telefonní čísla.

V doméně správy předplatného jádrové sítě je primárním MUI International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)). IMSI je trvalý, globálně jednoznačný identifikátor uložený na SIM/USIM karty uživatele a v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Je to základní klíč pro autentizaci, autorizaci a účtování účastníka. Z důvodu ochrany soukromí uživatele se jen zřídka přenáší přes rozhraní v čitelné podobě. Pro většinu rutinních procedur na rádiovém rozhraní se používají dočasné identifikátory. Nejběžnější z nich je Temporary Mobile Subscriber Identity (TMSI) v GSM/UMTS nebo Globally Unique Temporary Identity ([GUTI](/mobilnisite/slovnik/guti/)) v LTE/5G. Tyto identifikátory přiděluje obsluhující síť (VLR/[MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/)) pro jednoznačnou identifikaci uživatele v rámci konkrétní lokální oblasti nebo sledovací oblasti, čímž se zabrání častému přenosu trvalého IMSI.

Z pohledu uživatelského zařízení a koncového uživatele je identifikátorem Mobile Station International Subscriber Directory Number ([MSISDN](/mobilnisite/slovnik/msisdn/)) – telefonní číslo používané k uskutečnění hovoru. Síť musí toto MSISDN mapovat na odpovídající IMSI pro směrování a obsluhu služeb. Termín MUI zahrnuje všechny tyto identifikátory (IMSI, TMSI, GUTI, MSISDN) a jejich role. Specifikace (např. 25.211, 25.214 pro fyzickou vrstvu UMTS) používají termín MUI v obecném smyslu při popisu, jak jsou uživatelsky specifická data nebo řídicí zprávy kódována nebo zpracovávány, což naznačuje, že je v daném kontextu použit příslušný dočasný nebo trvalý identifikátor uživatele.

Pochopení MUI jako konceptu je klíčové pro uchopení životního cyklu identity v mobilních sítích: je zavedena trvalá identita předplatného (IMSI); jsou odvozeny dočasné, lokalizované identity (TMSI/GUTI) pro provozní bezpečnost a efektivitu; a veřejná identita (MSISDN) je používána pro směrování hovorů a zpráv. Síťové entity průběžně spravují mapování a překlad mezi těmito různými formami Mobile User Identifier.

## K čemu slouží

Koncept Mobile User Identifier existuje, aby poskytl abstraktní, jednotný způsob odkazování na princip identifikace účastníka v rámci komplexní architektury celulární sítě. Rané mobilní systémy potřebovaly způsob, jak odlišit jednoho účastníka od druhého pro účtování, směrování a zabezpečení. MUI jako obecný termín uznává, že jediný typ identifikátoru je nedostatečný; různé kontexty vyžadují různé identifikátory vyvažující trvalost, soukromí a směrovatelnost.

Řeší problém, jak konzistentně odkazovat na 'uživatele' napříč stovkami specifikací protokolů a procedur, aniž by byl vázán na technický formát konkrétního identifikátoru. Například, když specifikace popisuje krok zpracování kanálu závislý na uživateli, může obecně odkazovat na 'MUI' místo specifikace [IMSI](/mobilnisite/slovnik/imsi/), TMSI nebo [MSISDN](/mobilnisite/slovnik/msisdn/), které se mohou měnit v závislosti na doméně sítě nebo fázi procedury. Tato abstrakce zjednodušuje psaní standardů.

Navíc vývoj od trvalého IMSI k dočasnému TMSI/GUTI byl hnut kritickými potřebami bezpečnosti a soukromí. Přenos trvalého, globálně jednoznačného IMSI vzduchem činí účastníky zranitelnými vůči sledování a zachycení identity. Použití dočasných identifikátorů, které jsou všechny typy MUI, toto riziko zmírňuje. Zastřešující termín MUI pomáhá konceptualizovat tuto hierarchii identit a překlad mezi jejími vrstvami, což je základní funkcí entit správy mobility, jako jsou VLR, MME a AMF.

## Klíčové vlastnosti

- Koncepční zastřešující termín pro všechny identifikátory účastníka.
- Zahrnuje trvalé identity (IMSI), dočasné identity (TMSI, GUTI) a veřejné identity (MSISDN).
- Používá se obecně ve specifikacích pro označení uživatelsky specifického zpracování.
- Základní pro autentizaci, autorizaci a účtování účastníka (AAA).
- Umožňuje soukromí prostřednictvím používání dočasných, často se měnících identifikátorů.
- Vyžaduje mapování a překlad mezi různými typy MUI síťovými uzly.

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [MUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mui/)
