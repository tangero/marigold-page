---
slug: "hi1"
url: "/mobilnisite/slovnik/hi1/"
type: "slovnik"
title: "HI1 – Handover Interface Port 1 (for Administrative Information)"
date: 2025-01-01
abbr: "HI1"
fullName: "Handover Interface Port 1 (for Administrative Information)"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hi1/"
summary: "HI1 je administrativní port rozhraní předání (HI) používaný pro zákonný odposlech. Přenáší příkazy k odposlechu a administrativní data od orgánu činného v trestním řízení k síťovému operátorovi, čímž"
---

HI1 je administrativní port rozhraní předání (Handover Interface) používaný pro přenos příkazů k zákonnému odposlechu a administrativních dat od orgánu činného v trestním řízení k síťovému operátorovi.

## Popis

Handover Interface Port 1 (HI1) je specifické logické rozhraní v rámci sady rozhraní pro zákonný odposlech Handover Interface ([HI](/mobilnisite/slovnik/hi/)) podle 3GPP. Jak je definováno v TS 33.108, HI1 je vyhrazeno výhradně pro přenos administrativních informací a příkazů k odposlechu. Je to kanál, přes který orgán činný v trestním řízení ([LEA](/mobilnisite/slovnik/lea/)) sděluje svůj zákonný mandát a žádosti zprostředkovací funkci ([MF](/mobilnisite/slovnik/mf/)) telekomunikačního síťového operátora. Na rozdíl od [HI2](/mobilnisite/slovnik/hi2/) a [HI3](/mobilnisite/slovnik/hi3/), které doručují zachycená data, se HI1 používá pro nastavení, řízení a správu samotné odposlechové relace.

Činnost HI1 začíná, když LEA s platným soudním příkazem potřebuje zachytit komunikaci cílového účastníka. Administrativní funkce ([ADF](/mobilnisite/slovnik/adf/)) LEA naformátuje žádost o odposlech podle specifikací HI1. Tato žádost obsahuje klíčová administrativní data, jako je identifikátor cíle (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)), požadovaný rozsah odposlechu (např. zachycení hovorů, SMS, datových relací), podrobnosti o zákonném oprávnění a adresy pro doručení následných dat IRI a CC (tj. kam posílat datové proudy HI2 a HI3). Tato žádost je zabezpečeně přenesena přes rozhraní HI1 k zprostředkovací funkci síťového operátora.

Po přijetí zprostředkovací funkce ověří administrativní žádost a aktivuje odposlech v síti. Nakonfiguruje příslušné síťové uzly (např. MSC, MME, SGW), aby začaly monitorovat cíl a generovat data IRI a CC. Rozhraní HI1 může být také použito pro následnou administrativní komunikaci během odposlechu, jako jsou změny parametrů odposlechu (např. přidání nového identifikátoru cíle), žádosti o aktualizaci stavu nebo příkaz k ukončení odposlechu. Zabezpečený a spolehlivý provoz HI1 je zásadní, protože jde o řídicí kanál, který zahajuje právně citlivý proces. Jeho protokoly zajišťují autentizaci, integritu a důvěrnost všech administrativních příkazů.

## K čemu slouží

HI1 bylo vytvořeno, aby poskytlo standardizovaný a zabezpečený kanál pro administrativní řízení relací zákonného odposlechu. Bez vyhrazeného administrativního rozhraní by aktivace odposlechů závisela na nestandardních, potenciálně nezabezpečených metodách, jako jsou telefonní hovory, papírové dokumenty nebo proprietární elektronické systémy, což by vedlo ke zpožděním, chybám a bezpečnostním rizikům. Jasné oddělení mezi řídicím kanálem (HI1) a datovými doručovacími kanály (HI2/HI3) je také klíčové pro architektonickou přehlednost a bezpečnost.

Jeho účelem je vyřešit problém, jak může LEA spolehlivě, bezpečně a jednoznačně instruovat síťového operátora, aby zahájil, upravil nebo ukončil odposlech konkrétního účastníka. Rozhraní HI1 přenáší zákonný mandát do sítě v digitálním formátu, který může být automaticky zpracován zprostředkovací funkcí, což umožňuje rychlou aktivaci. Tato automatizace je nezbytná pro včasný odposlech v kritických vyšetřováních. Vytvoření HI1 bylo motivováno potřebou efektivního, auditovatelného a interoperabilního procesu, který splňuje zákonné požadavky a zároveň se hladce integruje s provozními systémy síťového operátora.

## Klíčové vlastnosti

- Vyhrazený administrativní port rozhraní předání (Handover Interface - HI)
- Přenáší žádosti o odposlech, aktivační příkazy a řídicí příkazy od LEA k síti
- Nese identifikátory cíle, rozsah odposlechu, data o zákonném oprávnění a doručovací adresy
- Používá se pro aktivaci, změnu, dotaz na stav a ukončení odposlechových relací
- Vyžaduje zabezpečené a autentizované komunikační protokoly
- Umožňuje automatizované zpracování příkazů k odposlechu zprostředkovací funkcí sítě

## Související pojmy

- [HI – Handover Interface](/mobilnisite/slovnik/hi/)
- [HI2 – Handover Interface Port 2](/mobilnisite/slovnik/hi2/)
- [HI3 – Handover Interface Port 3](/mobilnisite/slovnik/hi3/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [HI1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/hi1/)
