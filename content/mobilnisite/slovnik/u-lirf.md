---
slug: "u-lirf"
url: "/mobilnisite/slovnik/u-lirf/"
type: "slovnik"
title: "U-LIRF – UTRAN Location Information Relay Function"
date: 2025-01-01
abbr: "U-LIRF"
fullName: "UTRAN Location Information Relay Function"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-lirf/"
summary: "Funkční entita v rámci UTRAN (UMTS Radio Access Network), která přeposílá polohově související informace mezi UE a jádrem sítě pro účely lokalizace. Usnadňuje přenos měřicích dat a pomocných dat potře"
---

U-LIRF je funkční entita UTRAN, která přeposílá polohové informace a data mezi uživatelským zařízením a jádrem sítě za účelem podpory lokalizačních služeb.

## Popis

U-LIRF ([UTRAN](/mobilnisite/slovnik/utran/) Location Information Relay Function) je logická funkce definovaná v architektuře UTRAN, konkrétně spojená s [RNC](/mobilnisite/slovnik/rnc/) (Radio Network Controller). Slouží jako přeposílací a koordinační bod pro informace lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/)) vyměňované mezi mobilním terminálem (UE) a komponentami LCS v jádru sítě. Jejím hlavním úkolem je podpora lokalizačních metod řízením toku polohově souvisejících dat.

Operačně, když lokalizační požadavek vznikne v jádru sítě (např. od [GMLC](/mobilnisite/slovnik/gmlc/) nebo klienta), U-LIRF přijímá lokalizační příkazy nebo pomocná data prostřednictvím rozhraní jádra sítě. Tyto informace pak přeposílá k UE přes rozhraní Uu pomocí příslušných zpráv [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control). Naopak, když UE provádí lokalizační měření (jako jsou [GPS](/mobilnisite/slovnik/gps/) pseudorange data nebo [OTDOA](/mobilnisite/slovnik/otdoa/) měření), U-LIRF je přijímá od UE a přeposílá zpět do entit jádra sítě ke zpracování. Obvykle sama polohu nepočítá, ale zajišťuje transport dat.

Architektonicky je U-LIRF integrována do řídicích funkcí RNC. Rozhraní s jádrem sítě zajišťuje přes rozhraní Iu (konkrétně Iu-PC pro paketově orientovanou lokalizaci nebo Iu-CS pro spojově orientovanou) a s UE přes rádiové rozhraní Uu. Funguje ve spolupráci s dalšími lokalizačními funkcemi UTRAN, jako je [U-LSADF](/mobilnisite/slovnik/u-lsadf/). Klíčové komponenty zahrnují protokoly pro zpracování zpráv LCS dat, koordinaci s protokolem RRC pro komunikaci s UE a interakci s architekturou LCS jádra sítě. Její role je zásadní pro umožnění síťově asistovaných lokalizačních technik v sítích UMTS.

## K čemu slouží

U-LIRF byla vytvořena za účelem standardizace a usnadnění lokalizačních služeb v sítích UMTS. S vývojem mobilních sítí směrem k podpoře nouzových služeb, zákonného odposlechu a komerčních aplikací založených na poloze byla potřeba strukturované metody pro výměnu lokalizačních dat mezi UE a sítí.

Řešila problém, jak efektivně transportovat lokalizační měřicí data a pomocná data přes rádiovou přístupovou síť. Bez vyhrazené přeposílací funkce by bylo nutné polohové informace zpracovávat ad-hoc obecnými funkcemi RNC, což by komplikovalo standardizaci a interoperabilitu. U-LIRF poskytla jasnou funkční definici této přeposílací role, čímž zajistila, že UTRAN může konzistentně podporovat různé lokalizační metody (jako Assisted GPS, Cell-ID nebo OTDOA).

Historicky byla zavedena v Release 12 jako součást vylepšení lokalizačních schopností UTRAN, v souladu se širší architekturou 3GPP LCS. Vyřešila potřebu definované cesty pro tok lokalizačních dat, což umožnilo spolehlivější a efektivnější lokalizační služby v sítích 3G, zejména s rostoucí prevalencí asistované GPS.

## Klíčové vlastnosti

- Přeposílá lokalizační pomocná data z jádra sítě k UE
- Přeposílá lokalizační měření z UE do jádra sítě
- Integrována v rámci RNC v UTRAN
- Podporuje více lokalizačních metod (např. A-GPS, OTDOA)
- Pro komunikaci s UE využívá zprávy RRC
- Rozhraní s jádrem sítě přes Iu-PC a Iu-CS pro LCS

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [U-LSADF – UTRAN Location System Assistance Data Function](/mobilnisite/slovnik/u-lsadf/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-LIRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-lirf/)
