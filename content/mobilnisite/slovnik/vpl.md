---
slug: "vpl"
url: "/mobilnisite/slovnik/vpl/"
type: "slovnik"
title: "VPL – Vertical Protection Level"
date: 2025-01-01
abbr: "VPL"
fullName: "Vertical Protection Level"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vpl/"
summary: "Vertical Protection Level (VPL) je klíčová metrika integrity v lokalizačních službách 3GPP, která kvantifikuje nejistotu ve vertikální (výškové) složce vypočtené polohy. Je zásadní pro bezpečnostně kr"
---

VPL je klíčová metrika integrity v lokalizačních službách 3GPP, která kvantifikuje nejistotu ve vertikální (výškové) složce vypočtené polohy.

## Popis

Vertical Protection Level (VPL) je statistická veličina definovaná ve specifikacích 3GPP pro lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/)). Představuje poloměr hranice vertikální chyby, vyjádřený v metrech, uvnitř které se předpokládá, že se s určenou vysokou pravděpodobností (např. 95 % nebo 99 %) nachází skutečná vertikální poloha (výška) uživatelského zařízení (UE). Koncepčně jde o vertikální protějšek Horizontal Protection Level ([HPL](/mobilnisite/slovnik/hpl/)). VPL vypočítává lokalizační systém (např. v Location Management Function nebo v UE pro UE-based positioning) na základě geometrie použitých satelitů nebo základnových stanic, odhadovaných měřicích chyb a požadovaného rizika integrity.

Z architektonického hlediska je výpočet VPL integrován do algoritmů pro odhad polohy. U metod založených na globálních navigačních satelitních systémech ([GNSS](/mobilnisite/slovnik/gnss/)), jako je [A-GNSS](/mobilnisite/slovnik/a-gnss/), bere výpočet v úvahu faktory jako úhly elevace satelitů, poměry signál-šum, odhady ionosférického zpoždění a kvalitu efemeridních dat. Satelity s nižší elevací přispívají k odhadu vertikální polohy větší chybou kvůli geometrii přímé viditelnosti. Výpočet často následuje modely jako z Radio Technical Commission for Maritime Services (RTCM) nebo letecké standardy, upravené pro 3GPP uživatelskou rovinu. Hodnota VPL se typicky poskytuje spolu s odhadnutou vertikální polohou (výškou).

Během provozu, když je podána žádost o polohu (např. pro tísňové volání nebo kontrolu dodržení trasy letu dronu), lokalizační uzel vypočítá nejen 3D polohu (zeměpisná šířka, délka, výška), ale také přidružený VPL. Tato hodnota VPL se pak porovná s předdefinovaným Vertical Alert Limit ([VAL](/mobilnisite/slovnik/val/)), což je maximální povolená vertikální chyba pro danou aplikaci. Pokud VPL překročí VAL, je vypočtená poloha považována za nedostatečně spolehlivou pro zamýšlené použití a může být spuštěno upozornění na narušení integrity. Toto 'monitorování integrity' je klíčovou funkcí pro služby související se záchranou života.

Role VPL je prvořadá pro umožnění vertikálního určování polohy s vysokou integritou pro nové případy užití zaváděné v 5G-Advanced, jako je Urban Air Mobility (UAM) a pokročilé automobilové aplikace. Umožňuje síti a aplikaci kvantitativně posoudit důvěryhodnost výškových informací. To je v mnoha scénářích kritičtější než horizontální nejistota, například při určování, na kterém patře budovy se nachází volající tísňové linky (pro E911), nebo při zajištění, že dron udržuje bezpečnou výšku nad terénem.

## K čemu slouží

VPL byl zaveden, aby řešil rostoucí potřebu vertikálního určování polohy s vysokou integritou v systémech 3GPP, což se stalo naléhavým požadavkem s Release 17 a zkoumáním využití 5G pro drony a vzdušná vozidla. Tradiční lokalizace v celulárních sítích se primárně zaměřovala na 2D (horizontální) polohu pro služby jako navigace a základní určení polohy volajícího tísňové linky. Vertikální složka byla často pouze odhadem s nejasně definovanou přesností a, což je důležitější, bez standardizované míry její spolehlivosti či integrity.

Omezení předchozích přístupů byla významná pro bezpečnostní a regulační aplikace. Například služby tísňového volání (E112) potřebují znát nejen budovu, ale i patro, a nesprávná výška může vést záchranáře na špatné místo s vážnými důsledky. Podobně pro provoz dronů letecké předpisy vyžadují znalost jak polohy, tak důvěry v tuto polohu, aby bylo zajištěno bezpečné odstínění od terénu a překážek. Bez standardizované metriky, jako je VPL, bylo pro aplikace nemožné konzistentně určit, zda je hlásená výška vhodná pro daný účel.

Vytvoření VPL v rámci 3GPP bylo motivováno konvergencí celulárních a přesných lokalizačních technologií a potřebou podporovat kategorie vertikálních služeb. Poskytuje standardizovaný, kvantitativní způsob vyjádření vertikální nejistoty, který je v souladu s koncepty integrity z letectví a dalších bezpečnostně kritických domén. To umožňuje sítím 3GPP splnit přísné regulační požadavky pro nové vertikální aplikace a nabízet důvěryhodné lokalizační služby přesahující pouhé mapování.

## Klíčové vlastnosti

- Statistická hranice pro chybu vertikálního určení polohy pro definovanou úroveň spolehlivosti (např. 95 %)
- Nedílná součást monitorování a upozorňování na narušení integrity polohy
- Vypočítává se na základě geometrie měření, kvality signálu a modelů chyb
- Používá se při porovnání s Vertical Alert Limit (VAL) pro kontrolu shody specifické pro danou aplikaci
- Podporuje jak UE-based, tak network-based lokalizační architektury
- Kritické pro služby související se záchranou života, jako je tísňová lokalizace a navigace dronů

## Související pojmy

- [HPL – Horizontal Protection Level](/mobilnisite/slovnik/hpl/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [VPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/vpl/)
