---
slug: "sbt"
url: "/mobilnisite/slovnik/sbt/"
type: "slovnik"
title: "SBT – Single Band Testing"
date: 2025-01-01
abbr: "SBT"
fullName: "Single Band Testing"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sbt/"
summary: "Single Band Testing (SBT) je metodika konformního testování definovaná 3GPP pro rádiové základnové stanice. Zahrnuje testování charakteristik vysílače a přijímače základnové stanice pracující v rámci"
---

SBT je metodika konformního testování základnových stanic dle 3GPP, která ověřuje výkon vysílače a přijímače v rámci jediného kmitočtového pásma za účelem zajištění shody se specifikacemi.

## Popis

Single Band Testing (SBT) je základní rámec konformního testování podrobně popsaný ve specifikacích 3GPP, především v TS 37.141 pro rádiový přenos a příjem základnové stanice ([BS](/mobilnisite/slovnik/bs/)) a TS 37.145 pro konformní testování BS. Jedná se o metodiku uplatňovanou během fází schvalování typu a certifikace síťového zařízení, která se specificky zaměřuje na výkon v rádiové frekvenci ([RF](/mobilnisite/slovnik/rf/)) a základního pásma základnové stanice, když je nakonfigurována pro provoz v jediném, definovaném kmitočtovém pásmu. Tento proces není síťovou funkcí, ale důkladným hodnocením v laboratorních podmínkách, jehož cílem je zajistit, že hardware od různých dodavatelů splňuje minimální výkonnostní standardy stanovené 3GPP, a tím umožnit více-dodavatelský ekosystém.

Architektura SBT se točí kolem řízeného testovacího prostředí využívajícího specializované testovací vybavení. Testovaná základnová stanice ([EUT](/mobilnisite/slovnik/eut/)) je připojena k testovacímu systému, který simuluje uživatelské zařízení (UE) a podmínky rádiového kanálu. Testování se provádí izolovaně pro jedno provozní pásmo v daný okamžik. Klíčovými součástmi testovací sestavy jsou vektorový generátor signálu pro vytváření testovacích signálů, vektorový analyzátor signálu pro měření výstupu EUT, emulátory kanálů pro simulaci vícecestného útlumu a Dopplerova jevu a systémový simulátor pro řízení testovacích procedur a protokolových vrstev. Základnová stanice je konfigurována se specifickými testovacími modely a referenčními měřicími kanály ([RMC](/mobilnisite/slovnik/rmc/)) definovanými ve specifikacích.

Testovací procedura v rámci SBT je vyčerpávající a pokrývá dvě hlavní oblasti: charakteristiky vysílače a charakteristiky přijímače. Testy vysílače vyhodnocují parametry jako výstupní výkon, dynamický rozsah regulace výkonu, kmitočtovou chybu, obsazenou šířku pásma, masku emisního spektra, poměr výkonu úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)), nežádoucí emise a kvalitu modulace (velikost chybového vektoru - [EVM](/mobilnisite/slovnik/evm/)). Testy přijímače posuzují citlivost základnové stanice, její dynamický rozsah a schopnost správně demodulovat signály za různých podmínek rušení, včetně selektivity sousedního kanálu ([ACS](/mobilnisite/slovnik/acs/)), blokování a intermodulace. Každý test má ve specifikacích definovány přísné limity pro vyhovění/nevyhovění.

Role SBT v síťovém ekosystému je pro zajištění kvality klíčová. Tím, že 3GPP vyžaduje, aby všechny produkty základnových stanic před uvedením na trh prošly těmito jednopásmovými testy, zajišťuje základní úroveň rádiového výkonu. Tím se zabrání tomu, aby nekvalitní zařízení degradovalo síťové pokrytí, kapacitu a uživatelský zážitek. Je to předpoklad pro pokročilejší testování, jako je vícepásmové testování nebo testování agregace nosných, a tvoří základ spolehlivosti sítě, efektivity využití spektra a v konečném důsledku kvality služeb pro koncového uživatele napříč sítěmi 2G, 3G, 4G a 5G.

## K čemu slouží

Účelem Single Band Testing je stanovit standardizovanou, objektivní a opakovatelnou metodu pro ověření základního rádiového výkonu základnových stanic ve vztahu ke specifikacím 3GPP. Před takovým standardizovaným konformním testováním čelili síťoví operátoři při integraci zařízení od různých výrobců významným rizikům. Nekompatibility a podstandardní [RF](/mobilnisite/slovnik/rf/) výkon mohly vést k přerušeným hovorům, nízké datové propustnosti, nadměrnému rušení a celkové nestabilitě sítě. SBT byl vytvořen, aby tyto problémy vyřešil poskytnutím společného technického měřítka, které musí všichni dodavatelé splnit, a tím zajistil základní interoperabilitu a předvídatelnost výkonu v prostředí s více dodavateli.

Historicky vycházela motivace pro SBT z potřeby otevřít telekomunikační trh mimo jednododavatelské, proprietární sítě. S vývojem standardů, jako jsou GSM a UMTS, požadovali regulátoři a operátoři možnost kombinovat síťové prvky od různých dodavatelů. To vyžadovalo důkladný certifikační proces, který by zaručil, že základnová stanice od Dodavatele A bude bezproblémově fungovat s jádrem sítě od Dodavatele B a koncovými zařízeními od Dodavatele C. SBT řeší fyzickou vrstvu tohoto základu interoperability. Konkrétně řeší omezení ad-hoc nebo dodavatelsky specifického testování, kterému chyběla transparentnost a konzistence, tím, že definuje jednoznačné testovací podmínky, signály a limity.

Dále je SBT motivován potřebou efektivního využití spektra a dodržováním regulatorních požadavků. Rádiové spektrum je vzácný a licencovaný zdroj. Regulační orgány požadují, aby nasazené zařízení nezpůsobovalo škodlivé rušení jiným uživatelům v sousedních pásmech nebo kanálech. Specifikace SBT zahrnují testy nežádoucích emisí a spektrálních masek, které zajišťují, že vysílaný signál základnové stanice zůstává v rámci přidělené šířky pásma. Tím, že SBT řeší problémy závislosti na jediném dodavateli, nejistoty výkonu a nedodržování regulatorních požadavků, se stal nepostradatelnou součástí životního cyklu vývoje a nasazení globální mobilní infrastruktury, umožňující zdravý, konkurenční a spolehlivý růst celulárních sítí.

## Klíčové vlastnosti

- Standardizované konformní testování RF výkonu základnové stanice
- Zaměření na provoz v jediném kmitočtovém pásmu během testu
- Komplexní testování vysílače (výkon, EVM, ACLR, spektrální maska)
- Komplexní testování přijímače (citlivost, ACS, blokování)
- Definované testovací modely a referenční měřicí kanály (RMC)
- Umožňuje více-dodavatelskou interoperabilitu a zajištění kvality sítě

## Související pojmy

- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)
- [TRS – Total Radiated Sensitivity](/mobilnisite/slovnik/trs/)
- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)

## Definující specifikace

- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [SBT na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbt/)
