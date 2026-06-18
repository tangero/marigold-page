---
slug: "esrk"
url: "/mobilnisite/slovnik/esrk/"
type: "slovnik"
title: "ESRK – Emergency Service Routing Key"
date: 2025-01-01
abbr: "ESRK"
fullName: "Emergency Service Routing Key"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/esrk/"
summary: "Klíč používaný v severoamerických systémech pro tísňová volání (E911) pro směrování bezdrátových hovorů ke příslušnému bodu přijímání tísňových volání (PSAP). Identifikuje buňku a sektor, ze kterého h"
---

ESRK je klíč používaný v severoamerických systémech E911 pro směrování bezdrátových tísňových hovorů ke správnému PSAP identifikací zdrojové buňky a sektoru pro počáteční hrubé směrování.

## Popis

Emergency Service Routing Key (ESRK) je klíčový identifikátor definovaný ve specifikaci 3GPP TS 23.167 pro podporu starších severoamerických požadavků E911 Fáze I a Fáze [II](/mobilnisite/slovnik/ii/) v sítích 3GPP. Jedná se o desetimístné číslo, podobné telefonnímu číslu, které je dynamicky přiděleno síťovým Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo jeho nástupcem v IP Multimedia Subsystem (IMS), jako je Emergency [CSCF](/mobilnisite/slovnik/cscf/) ([E-CSCF](/mobilnisite/slovnik/e-cscf/)) ve spolupráci s Gateway Mobile Location Center ([GMLC](/mobilnisite/slovnik/gmlc/)). Když mobilní uživatel zahájí tísňové volání (např. vytočí 911), obsluhující síťový uzel (MSC pro circuit-switched, E-CSCF pro IMS) vyžádá ESRK od lokálního serveru nebo jej vygeneruje na základě zdrojové buňky.

Primární funkcí ESRK je směrování hovoru. Síť použije ESRK k směrování tísňového hovoru telefonní sítí k selektivní ústředně, která pak hovor nasměruje ke konkrétnímu [PSAP](/mobilnisite/slovnik/psap/) odpovědnému za geografickou oblast spojenou s tímto ESRK. Mapování mezi ESRK a PSAP je udržováno v národní nebo regionální databázi pro směrování tísňových služeb (ESRD). V podstatě ESRK kóduje hrubou informaci o poloze – typicky identifikátor buňky a sektoru – což umožňuje, aby se hovor dostal k PSAP ve správné jurisdikci ještě před získáním jakékoli přesné polohy z [GPS](/mobilnisite/slovnik/gps/) nebo odvozené ze sítě.

Jakmile je hovor na PSAP navázán, ESRK plní druhou zásadní funkci: slouží jako klíč pro získání přesnější polohy volajícího a zpětného telefonního čísla. Zařízení PSAP automaticky dotazuje databázi Automatic Location Identification (ALI) pomocí ESRK. Tato databáze ALI byla naplněna GMLC nebo lokálním serverem mobilního operátora přesnými souřadnicemi (pro Fázi II) a mobilním telefonním číslem (MDN) spojeným s tímto konkrétním přidělením ESRK. Tento dvoukrokový proces – směrování pomocí ESRK a následné načtení dat pomocí ESRK – zajišťuje, že se hovor rychle dostane ke správnému dispečerovi a dispečer pak obdrží podrobné informace potřebné pro zásah.

Ve scénáři tísňového volání založeném na IMS může být ESRK použito spolu s [ESQK](/mobilnisite/slovnik/esqk/) nebo jako jeho alternativa, v závislosti na požadavcích rozhraní starší sítě PSAP. Síť musí zajistit, že ESRK je po dobu trvání tísňového hovoru jedinečné a je po uplynutí časového limitu uvolněno pro opětovné použití. Jeho role je zásadní pro interoperabilitu mezi moderními sítěmi 3GPP a stávající infrastrukturou E911 v Severní Americe.

## K čemu slouží

ESRK bylo vyvinuto k řešení zásadní výzvy směrování bezdrátových tísňových hovorů ke správnému PSAP, což byl problém, který u tradičních pevných linek neexistoval, protože telefonní číslo je vázáno na pevnou adresu. V počátcích mobilních sítí se volání 911 z mobilního telefonu mohlo směrovat pouze na výchozí PSAP, často na stanici státní policie, což vyžadovalo ruční přepojení a způsobovalo kritická zpoždění. Nařízení E911 Fáze I vyžadovalo, aby mobilní operátoři poskytli zpětné telefonní číslo a polohu buňky obsluhující hovor.

Mechanismus ESRK byl vytvořen, aby toto nařízení splnil. Poskytuje dynamické, na poloze závislé „pseudočíslo“, které telefonní přepojovací síť může použít pro směrování, stejně jako směruje běžné hovory na základě směrového čísla a ústředny. To umožnilo opětovné využití stávající infrastruktury pro selektivní směrování pevných linek E911 pro bezdrátové hovory bez zásadní přestavby. Systém ESRK vyřešil omezení plynoucí z absence pevné polohy účastníka tím, že svázal směrovací klíč se síťovým prvkem (buňkou), který volajícího právě obsluhuje.

S vývojem E911 do Fáze II, která vyžaduje přesnější polohu (v rozmezí 50–300 metrů), se role ESRK rozšířila. Stalo se nezbytným článkem, který spojil počáteční směrovaný hovor s následně doručenými daty o poloze s vysokou přesností. Jeho pokračující specifikace v normách 3GPP, dokonce i pro sítě založené na IMS, zajišťuje zpětnou kompatibilitu a podporuje postupnou migraci pro tísňové služby. Řeší kritický problém zajištění, aby volání o záchranu života dorazila ke správným místním záchranářům v co nejkratším možném čase, a to s využitím jak nových lokalizačních technologií, tak starších směrovacích databází.

## Klíčové vlastnosti

- Desetimístný číselný klíč dynamicky přidělovaný pro každé tísňové volání, podobný telefonnímu číslu
- Primární funkcí je směrování tísňového hovoru ke správnému PSAP na základě polohy buňky
- Slouží jako klíč pro dotazování databáze PSAP, aby získal přesnou polohu a zpětné telefonní číslo z databáze ALI
- Nezbytné pro splnění regulačních požadavků severoamerických E911 Fáze I a Fáze II
- Umožňuje interoperabilitu mezi sítěmi 3GPP a starší infrastrukturou pro selektivní směrování pevných linek E911
- Často používáno spolu s ESQK v nasazeních IMS pro podporu rozhraní starších i novějších generací PSAP

## Související pojmy

- [ESQK – Emergency Service Query Key](/mobilnisite/slovnik/esqk/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions

---

📖 **Anglický originál a plná specifikace:** [ESRK na 3GPP Explorer](https://3gpp-explorer.com/glossary/esrk/)
